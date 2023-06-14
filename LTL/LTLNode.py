from typing import List, Set
from abc import ABC, abstractmethod
# from TS import TS

class LTL_Base_Node(ABC):
    # @abstractmethod
    def get_children(self) -> List['LTL_Base_Node']:
        return []

    def to_string(self) -> str:
        return "true"

    def get_closure(self, tptr: 'LTL_Base_Node', fptr: 'LTL_Base_Node') -> Set['LTL_Base_Node']:
        ret = {tptr}
        if not isinstance(fptr, Negation):
            ret.add(Negation(tptr))
        for phi in self.get_children():
            tmp = phi.get_closure(phi, tptr)
            ret.update(tmp)
        return ret


class Negation(LTL_Base_Node):
    def __init__(self, phi: 'LTL_Base_Node'):
        self.phi = phi

    def get_children(self) -> List['LTL_Base_Node']:
        return [self.phi]

    def to_string(self) -> str:
        return "!(" + self.phi.to_string() + ")"

    def get_closure(self, tptr: 'LTL_Base_Node', fptr: 'LTL_Base_Node') -> Set['LTL_Base_Node']:
        ret = {tptr}
        for phi in self.get_children():
            tmp = phi.get_closure(phi, tptr)
            ret.update(tmp)
        return ret


class Until(LTL_Base_Node):
    def __init__(self, phi0: 'LTL_Base_Node', phi1: 'LTL_Base_Node'):
        self.phi0 = phi0
        self.phi1 = phi1

    def get_children(self) -> List['LTL_Base_Node']:
        return [self.phi0, self.phi1]

    def to_string(self) -> str:
        return "(" + self.phi0.to_string() + ") U (" + self.phi1.to_string() + ")"


class Next(LTL_Base_Node):
    def __init__(self, phi: 'LTL_Base_Node'):
        self.phi = phi

    def get_children(self) -> List['LTL_Base_Node']:
        return [self.phi]

    def to_string(self) -> str:
        return "X(" + self.phi.to_string() + ")"


class And(LTL_Base_Node):
    def __init__(self, phi0: 'LTL_Base_Node', phi1: 'LTL_Base_Node'):
        self.phi0 = phi0
        self.phi1 = phi1

    def get_children(self) -> List['LTL_Base_Node']:
        return [self.phi0, self.phi1]

    def to_string(self) -> str:
        return "(" + self.phi0.to_string() + ") /\\ (" + self.phi1.to_string() + ")"


class Variable(LTL_Base_Node):
    def __init__(self, p):
        self.p = p

    def get_children(self) -> List['LTL_Base_Node']:
        return []

    def to_string(self) -> str:
        # 这里应该return 什么呢？
        return (self.p.to_string())
    


