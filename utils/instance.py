from typing import TypeVar, List
from io import StringIO

T = TypeVar('T')

def instanceof(base: type, ptr: T) -> bool:
    return isinstance(ptr, base)