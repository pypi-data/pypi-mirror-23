# Copyright 2016 by Nedim Sabic (RabbitStack)
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


from kstream.includes.python cimport PyTuple_SetItem, Py_BuildValue, PyTuple_New
from cpython.ref cimport PyObject
from kstream.includes.windows cimport UCHAR

cdef inline PyObject* build_ktuple(PyObject* kguid, UCHAR opcode) nogil:
    cdef PyObject* ktuple = PyTuple_New(2)
    cdef PyObject* oco = Py_BuildValue('b', opcode)
    PyTuple_SetItem(ktuple, 0, kguid)
    PyTuple_SetItem(ktuple, 1, oco)
    return ktuple
