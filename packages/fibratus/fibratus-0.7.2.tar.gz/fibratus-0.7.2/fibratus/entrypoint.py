# Copyright 2015 by Nedim Sabic (RabbitStack)
# http://rabbitstack.github.io
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import atexit
import os
import sys
from datetime import datetime

from kstreamc import KEventStreamCollector
from pykwalify.errors import SchemaError

from fibratus.binding.yar import YaraBinding
from fibratus.errors import BindingError
from fibratus.image_meta import ImageMetaRegistry
from fibratus.output.aggregator import OutputAggregator
from fibratus.output.console import ConsoleOutput
from fibratus.output.elasticsearch import ElasticsearchOutput
from fibratus.output.fs import FsOutput
from fibratus.output.smtp import SmtpOutput
from logbook import Logger, FileHandler, StreamHandler

import fibratus.apidefs.etw as etw
from fibratus.common import DotD as ddict, panic
from fibratus.config import YamlConfig
from fibratus.context_switch import ContextSwitchRegistry
from fibratus.controller import KTraceController, KTraceProps
from fibratus.dll import DllRepository
from fibratus.fs import FsIO
from fibratus.handle import HandleRepository
from fibratus.kevent import KEvent
from fibratus.kevent_types import *
from fibratus.tcpip.tcpip import TcpIpParser
from fibratus.output.amqp import AmqpOutput
from fibratus.registry import HiveParser
from fibratus.thread import ThreadRegistry


class Fibratus(object):

    """Fibratus entrypoint.

    Setup the core components including the kernel
    event stream collector and the tracing controller.
    At this point the system handles are also being
    enumerated.

    """
    def __init__(self, filament, **kwargs):

        self._start = datetime.now()
        try:
            log_path = os.path.join(os.path.expanduser('~'), '.fibratus', 'fibratus.log')
            FileHandler(log_path, mode='w+').push_application()
            StreamHandler(sys.stdout, bubble=True).push_application()
        except PermissionError:
            panic("ERROR - Unable to open log file for writing due to permission error")

        self.logger = Logger(Fibratus.__name__)
        self.logger.info('Starting Fibratus...')

        self._config = YamlConfig()
        self.logger.info('Loading configuration from [%s]' % self._config.config_path)
        try:
            self._config.load()
        except SchemaError as e:
            panic('Invalid configuration file. %s' % e.msg)

        enable_cswitch = kwargs.pop('cswitch', False)

        self.kcontroller = KTraceController()
        self.ktrace_props = KTraceProps()
        self.ktrace_props.enable_kflags(cswitch=enable_cswitch)
        self.ktrace_props.logger_name = etw.KERNEL_LOGGER_NAME

        enum_handles = kwargs.pop('enum_handles', True)

        self.handle_repository = HandleRepository()
        self._handles = []
        # query for handles on the
        # start of the kernel trace
        if enum_handles:
            self.logger.info('Enumerating system handles...')
            self._handles = self.handle_repository.query_handles()
            self.logger.info('%s handles found' % len(self._handles))
            self.handle_repository.free_buffers()

        image_meta_config = self._config.image_meta
        self.image_meta_registry = ImageMetaRegistry(image_meta_config.enabled, image_meta_config.imports,
                                                     image_meta_config.file_info)

        self.thread_registry = ThreadRegistry(self.handle_repository, self._handles,
                                              self.image_meta_registry)

        self.kevt_streamc = KEventStreamCollector(etw.KERNEL_LOGGER_NAME.encode())
        skips = self._config.skips
        image_skips = skips.images if 'images' in skips else []
        if len(image_skips) > 0:
            self.logger.info("Adding skips for images %s" % image_skips)
            for skip in image_skips:
                self.kevt_streamc.add_skip(skip)

        self.kevent = KEvent(self.thread_registry)

        self._output_classes = dict(console=ConsoleOutput,
                                    amqp=AmqpOutput,
                                    smtp=SmtpOutput,
                                    elasticsearch=ElasticsearchOutput,
                                    fs=FsOutput)
        self._outputs = self._construct_outputs()
        self.output_aggregator = OutputAggregator(self._outputs)

        self._binding_classes = dict(yara=YaraBinding)
        self._bindings = self._construct_bindings()

        if filament:
            filament.logger = self.logger
            filament.do_output_accessors(self._outputs)
        self._filament = filament

        self.fsio = FsIO(self.kevent, self._handles)
        self.hive_parser = HiveParser(self.kevent, self.thread_registry)
        self.tcpip_parser = TcpIpParser(self.kevent)
        self.dll_repository = DllRepository(self.kevent)
        self.context_switch_registry = ContextSwitchRegistry(self.thread_registry, self.kevent)

        self.output_kevents = {}
        self.filters_count = 0

    def run(self):

        @atexit.register
        def _exit():
            self.stop_ktrace()

        self.kcontroller.start_ktrace(etw.KERNEL_LOGGER_NAME, self.ktrace_props)

        def on_kstream_open():
            if self._filament is None:
                delta = datetime.now() - self._start
                self.logger.info('Started in %sm:%02ds.%s' % (int(delta.total_seconds() / 60), delta.seconds,
                                                              int(delta.total_seconds() * 1000)))
            else:
                self.logger.info('Running [%s] filament...' % self._filament.name)
        self.kevt_streamc.set_kstream_open_callback(on_kstream_open)
        self._open_kstream()

    def _open_kstream(self):
        try:
            self.kevt_streamc.open_kstream(self._on_next_kevent)
        except Exception as e:
            self.logger.error(e)
        except KeyboardInterrupt:
            self.stop_ktrace()

    def _construct_outputs(self):
        """Instantiates output classes.

        Builds the dictionary with instances
        of the output classes.
        """
        outputs = {}
        output_configs = self._config.outputs
        if not output_configs:
            return outputs
        for output in output_configs:
            name = next(iter(list(output.keys())), None)
            if name and \
                    name in self._output_classes.keys():
                # get the output configuration
                # and instantiate its class
                output_config = output[name]
                self.logger.info("Deploying [%s] output - [%s]"
                                 % (name, {k: v for k, v in output_config.items()
                                           if 'password' not in k}))
                output_class = self._output_classes[name]
                outputs[name] = output_class(**output_config)
        return outputs

    def _construct_bindings(self):
        """Builds binding classes.

        :return: dict: dictionary with instances of the binding classes
        """
        bindings = {}
        binding_configs = self._config.bindings
        if not binding_configs:
            return bindings
        for b in binding_configs:
            name = next(iter(list(b.keys())), None)
            if name and \
                    name in self._binding_classes.keys():
                binding_config = b[name]
                self.logger.info("Starting [%s] binding - [%s]" %
                                 (name, binding_config))
                binding_class = self._binding_classes[name]
                try:
                    binding = binding_class(self._outputs, self.logger,
                                            **binding_config)
                    bindings[name] = binding
                except BindingError as e:
                    self.logger.error("Couldn't start [%s] binding. Reason: %s" %
                                      (name, e))
        return bindings

    def __find_binding(self, name):
        return self._bindings[name] if name in self._bindings else None

    def stop_ktrace(self):
        self.logger.info('Stopping fibratus...')
        if self._filament:
            self._filament.close()
        self.kcontroller.stop_ktrace(self.ktrace_props)
        self.kevt_streamc.close_kstream()

    def add_filters(self, kevent_filters, **kwargs):
        self.kevt_streamc.add_pid_filter(kwargs.pop('pid', None))
        self.kevt_streamc.add_image_filter(kwargs.pop('image', None))
        if len(kevent_filters) > 0:
            self.filters_count = len(kevent_filters)
            # include the basic filters
            # that are essential to the
            # rest of kernel events
            self.kevt_streamc.add_ktuple_filter(ENUM_PROCESS)
            self.kevt_streamc.add_ktuple_filter(ENUM_THREAD)
            self.kevt_streamc.add_ktuple_filter(ENUM_IMAGE)
            self.kevt_streamc.add_ktuple_filter(REG_CREATE_KCB)
            self.kevt_streamc.add_ktuple_filter(REG_DELETE_KCB)

            # these kevents are necessary for consistent state
            # of the trace. If the user doesn't include them
            # in a filter list, then we do the job but set the
            # kernel event type as not eligible for rendering
            if KEvents.CREATE_PROCESS not in kevent_filters:
                self.kevt_streamc.add_ktuple_filter(CREATE_PROCESS)
                self.output_kevents[CREATE_PROCESS] = False
            else:
                self.output_kevents[CREATE_PROCESS] = True

            if KEvents.CREATE_THREAD not in kevent_filters:
                self.kevt_streamc.add_ktuple_filter(CREATE_THREAD)
                self.output_kevents[CREATE_THREAD] = False
            else:
                self.output_kevents[CREATE_THREAD] = True

            if KEvents.TERMINATE_PROCESS not in kevent_filters:
                self.kevt_streamc.add_ktuple_filter(TERMINATE_PROCESS)
                self.output_kevents[TERMINATE_PROCESS] = False
            else:
                self.output_kevents[TERMINATE_PROCESS] = True

            if KEvents.TERMINATE_THREAD not in kevent_filters:
                self.kevt_streamc.add_ktuple_filter(TERMINATE_THREAD)
                self.output_kevents[TERMINATE_THREAD] = False
            else:
                self.output_kevents[TERMINATE_THREAD] = True

            for kevent_filter in kevent_filters:
                ktuple = kname_to_tuple(kevent_filter)
                if isinstance(ktuple, list):
                    for kt in ktuple:
                        self.kevt_streamc.add_ktuple_filter(kt)
                        if kt not in self.output_kevents:
                            self.output_kevents[kt] = True
                else:
                    self.kevt_streamc.add_ktuple_filter(ktuple)
                    if ktuple not in self.output_kevents:
                        self.output_kevents[ktuple] = True

    def _on_next_kevent(self, ktype, cpuid, ts, kparams):
        """Callback which fires when new kernel event arrives.

        This callback is invoked for every new kernel event
        forwarded from the kernel stream collector.

        Parameters
        ----------

        ktype: tuple
            Kernel event type.
        cpuid: int
            Indentifies the CPU core where the event
            has been captured.
        ts: str
            Temporal reference of the kernel event.
        kparams: dict
            Kernel event's parameters.
        """

        # initialize kernel event properties
        self.kevent.ts = ts
        self.kevent.cpuid = cpuid
        self.kevent.name = ktuple_to_name(ktype)
        kparams = ddict(kparams)

        # thread / process kernel events
        if ktype in [CREATE_PROCESS,
                     CREATE_THREAD,
                     ENUM_PROCESS,
                     ENUM_THREAD]:
            self.thread_registry.add_thread(ktype, kparams)
            if ktype in [CREATE_PROCESS, CREATE_THREAD]:
                self.thread_registry.init_thread_kevent(self.kevent,
                                                        ktype,
                                                        kparams)
                # apply yara binding by matching against the process's image path
                if ktype == CREATE_PROCESS:
                    yara_binding = self.__find_binding('yara')
                    pid = int(kparams.process_id, 16)
                    thread = self.thread_registry.get_thread(pid)
                    if thread and yara_binding:
                        yara_binding.run(thread_info=thread,
                                         kevent=self.kevent)
                self._aggregate(ktype)

        elif ktype in [TERMINATE_PROCESS, TERMINATE_THREAD]:
            self.thread_registry.init_thread_kevent(self.kevent,
                                                    ktype,
                                                    kparams)
            self._aggregate(ktype)
            self.thread_registry.remove_thread(ktype, kparams)

        # file system/disk kernel events
        elif ktype in [CREATE_FILE,
                       DELETE_FILE,
                       CLOSE_FILE,
                       READ_FILE,
                       WRITE_FILE,
                       RENAME_FILE,
                       SET_FILE_INFORMATION]:
            self.fsio.parse_fsio(ktype, kparams)
            self._aggregate(ktype)

        # dll kernel events
        elif ktype in [LOAD_IMAGE, ENUM_IMAGE]:
            self.dll_repository.register_dll(kparams)
            if ktype == LOAD_IMAGE:
                self._aggregate(ktype)
        elif ktype == UNLOAD_IMAGE:
            self.dll_repository.unregister_dll(kparams)
            self._aggregate(ktype)
        #
        # # registry kernel events
        elif ktype == REG_CREATE_KCB:
            self.hive_parser.add_kcb(kparams)
        elif ktype == REG_DELETE_KCB:
            self.hive_parser.remove_kcb(kparams.key_handle)

        elif ktype in [REG_CREATE_KEY,
                       REG_DELETE_KEY,
                       REG_OPEN_KEY,
                       REG_QUERY_KEY,
                       REG_SET_VALUE,
                       REG_DELETE_VALUE,
                       REG_QUERY_VALUE]:
            self.hive_parser.parse_hive(ktype, kparams)
            self._aggregate(ktype)

        # network kernel events
        elif ktype in [SEND_SOCKET_TCPV4,
                       SEND_SOCKET_UDPV4,
                       RECV_SOCKET_TCPV4,
                       RECV_SOCKET_UDPV4,
                       ACCEPT_SOCKET_TCPV4,
                       CONNECT_SOCKET_TCPV4,
                       DISCONNECT_SOCKET_TCPV4,
                       RECONNECT_SOCKET_TCPV4]:
            self.tcpip_parser.parse_tcpip(ktype, kparams)
            self._aggregate(ktype)

        # context switch events
        elif ktype == CONTEXT_SWITCH:
            self.context_switch_registry.next_cswitch(cpuid, ts, kparams)
            self._aggregate(ktype)

        if self._filament:
            if ktype not in [ENUM_PROCESS,
                             ENUM_THREAD,
                             ENUM_IMAGE,
                             REG_CREATE_KCB,
                             REG_DELETE_KCB]:
                ok = self.output_kevents[ktype] if ktype in self.output_kevents \
                    else False
                if self.kevent.name and ok:
                    thread = self.kevent.thread
                    kevent = {
                        'params': self.kevent.params,
                        'name': self.kevent.name,
                        'pid': self.kevent.pid,
                        'tid': self.kevent.tid,
                        'timestamp': self.kevent.ts,
                        'cpuid': self.kevent.cpuid,
                        'category': self.kevent.category
                    }
                    if thread:
                        kevent.update({
                            'thread': {
                                'name': thread.name,
                                'exe': thread.exe,
                                'comm': thread.comm,
                                'pid': thread.pid,
                                'ppid': thread.ppid
                            }
                        })
                    self._filament.on_next_kevent(kevent)

    def _aggregate(self, ktype):
        """Aggregates the kernel event to the output sink.

        Parameters
        ----------

        ktype: tuple
            Identifier of the kernel event
        """
        if not self._filament:
            if ktype in self.output_kevents:
                if self.output_kevents[ktype]:
                    self.kevent.inc_kid()
                    self.output_aggregator.aggregate(self.kevent)
            elif self.filters_count == 0:
                self.kevent.inc_kid()
                self.output_aggregator.aggregate(self.kevent)