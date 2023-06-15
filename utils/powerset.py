from typing import List, Set

class PowerSet:
    def __init__(self, universe_):
        self.universe = {}
        self.subsets = {}
        for i, element in enumerate(universe_):
            self.universe[element] = i
        tmp = set()
        self.generate_subsets(tmp, universe_, 0, 0)

    def get_universe(self):
        ret = []
        for element, index in self.universe.items():
            ret.append(element)
        return ret

    def get_subset(self, s):
        v = 0
        for x in s:
            v |= (1 << self.universe[x])
        return self.subsets[v]

    def get_subsets(self):
        ret = []
        for index, subset in self.subsets.items():
            ret.append((subset))
        return ret

    def generate_subsets(self, s, universe_, i, v):
        if i == len(universe_):
            self.subsets[v] = set(s)
            return 
        self.generate_subsets(s, universe_, i + 1, v)
        s.add(universe_[i])
        self.generate_subsets(s, universe_, i + 1, v | (1 << i))
        s.remove(universe_[i])

