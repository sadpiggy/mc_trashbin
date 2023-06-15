from typing import Set
import ctypes

class pig:
    def __init__(self,ear_):
        self.ear = ear_
index = pig(0)
a = {}
a[index] = 1
print(a[index])
index.ear = 8
print(a[index])