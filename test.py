from typing import Set
import ctypes
a = set([1,2,3])
ret = set()
ret.add(id(a))
for _id in ret:
    print(_id)
    obj = ctypes.pythonapi.PyObject_FromLong(_id)
    # retrieved_a = ctypes.cast(obj, ctypes.py_object).value
    