from typing import Set
a = {}
ret = set()
ret1 = set([1,2,3])
ret.add(frozenset(ret1))
a[frozenset(ret1)] = 1
print(a[frozenset(ret1)])