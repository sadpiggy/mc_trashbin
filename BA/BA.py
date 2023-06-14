from typing import List, Dict, Set, Union, Tuple

from LTL import LTLNode
from utils.powerset import PowerSet

from TS import TS

class State:
    def __init__(self, is_initial: bool = False):
        self.is_initial = is_initial

    def get_is_initial(self) -> bool:
        return self.is_initial

class Symbol:
    pass

class BA:

    delta: Dict[State, Dict[Symbol, Set[State]]] = {}
    states: List[State] = []
    alphabet: List[Symbol] = []
    maded_nonblocking: bool = False
    
    def make_nonblocking(self):
        if self.maded_nonblocking:
            return None
        trap = State()
        self.delta[trap] = {symbol: set([trap]) for symbol in self.alphabet}
        self.states.append(trap)
        for state in self.states:
            for symbol in self.alphabet:
                if symbol not in self.delta[state]:
                    self.delta[state][symbol] = set([trap])
        self.maded_nonblocking = True
        return trap






class GNBA(BA):
    def __init__(
        self,
        phi: LTLNode.LTL_Base_Node,
        LTL2Symbol: Dict[Set[LTLNode.LTL_Base_Node], Symbol],
        set2state: Dict[Set[LTLNode.LTL_Base_Node], State],
        PropLTLs_power_set: PowerSet,
        True_: LTLNode.LTL_Base_Node
    ):
        closure = phi.get_closure(phi, None)
        for propLTL in PropLTLs_power_set.get_universe():
            if propLTL not in closure:
                closure.add(propLTL)
                closure.add(LTLNode.Negation(propLTL))
        has_True = True in closure

        elementary_sets = set()
        closure_power_set = PowerSet(list(closure))
        for B in closure_power_set.get_subsets():
            flag = not has_True or True in B
            for it in closure:
                if isinstance(it, LTLNode.And):
                    phi0 = it.get_children()[0]
                    phi1 = it.get_children()[-1]
                    flag &= (it in B) == (phi0 in B and phi1 in B)
                if it in B:
                    if isinstance(it, LTLNode.Negation):
                        psi = it.get_children()[0]
                        flag &= psi not in B
                    else:
                        for phi_ in B:
                            flag &= not (isinstance(phi_, LTLNode.Negation) and phi_.get_children()[0] == it)
                if isinstance(it, LTLNode.Until):
                    phi0 = it.get_children()[0]
                    phi1 = it.get_children()[-1]
                    if phi1 in B:
                        flag &= it in B
                    if it in B and phi1 not in B:
                        flag &= phi0 in B
                if it not in B:
                    if isinstance(it, LTLNode.Negation):
                        psi = it.get_children()[0]
                        flag &= psi in B
                    else:
                        found = False
                        for phi_ in B:
                            if isinstance(phi_, LTLNode.Negation) and phi_.get_children()[0] == it:
                                found = True
                                break
                        flag &= found
            if flag:
                elementary_sets.add((B))

        self.states = []
        self.delta = {}
        self.F = []

        for B in elementary_sets:
            is_initial = phi in B
            state = State(is_initial)
            set2state[B] = state
            self.states.append(state)
            self.delta[state] = {}

        for psi in closure:
            if isinstance(psi, LTLNode.Until):
                phi1 = psi.get_children()[-1]
                F_psi = set()
                for B in elementary_sets:
                    if psi not in B or phi1 in B:
                        F_psi.add(set2state[(B)])
                self.F.append(F_psi)

        set2symbol = {}
        self.alphabet = []
        print("set2symbol={}".format(set2symbol))
        for s in PropLTLs_power_set.get_subsets():
            symbol = Symbol()
            set2symbol[(s)] = symbol
            self.alphabet.append(symbol)
            LTL2Symbol[(s)] = symbol

        for B in elementary_sets:
            intersection = [psi for psi in PropLTLs_power_set.get_universe() if psi in B]
            A = PropLTLs_power_set.get_subset(intersection)
            for B_prime in elementary_sets:
                flag = True
                for it in closure:
                    if isinstance(it, LTLNode.Next):
                        psi = it.get_children()[0]
                        flag &= (it in B) == (psi in B_prime)
                    if isinstance(it, LTLNode.Until):
                        phi0 = it.get_children()[0]
                        phi1 = it.get_children()[-1]
                        flag &= (it in B) == (phi1 in B_prime or (phi0 in B and it in B_prime))
                if flag:
                    delta_B = self.delta[set2state[(B)]]
                    # print(type(A))
                    symbol = set2symbol[frozenset(A)]
                    state_B_prime = set2state[(B_prime)]
                    if symbol not in delta_B:
                        delta_B[symbol] = set()
                    delta_B[symbol].add(state_B_prime)







    F: List[Set[State]]


class NBA(BA):
    def __init__(self, gnba: GNBA, state2state_index: Dict[State, Tuple[State, int]]):
        self.F: Set[State] = set()
        
        self.alphabet = gnba.alphabet
        k = len(gnba.F)
        states_list = []
        index = {}
        for i in range(len(gnba.states)):
            state_ = gnba.states[i]
            index[state_] = i
            states_list.append([])
            for j in range(k):
                state = State(not j and state_.get_is_initial())
                state2state_index[state] = (state_, j)
                self.delta[state] = {}
                for symbol in self.alphabet:
                    self.delta[state][symbol] = set()
                self.states.append(state)
                states_list[-1].append(state)
        
        if k:
            for i in range(len(gnba.states)):
                if gnba.states[i] in gnba.F[0]:
                    self.F.add(states_list[i][0])
        
        for i in range(len(gnba.states)):
            state = gnba.states[i]
            for symbol, next_states in gnba.delta[state].items():
                next_states_list = []
                for j in range(k):
                    next_states_j_set = set()
                    for next_state in next_states:
                        next_states_j_set.add(states_list[index[next_state]][j])
                    next_states_list.append(next_states_j_set)
                for j in range(k):
                    if state not in gnba.F[j]:
                        self.delta[states_list[i][j]][symbol].update(next_states_list[j])
                    else:
                        self.delta[states_list[i][j]][symbol].update(next_states_list[(j + 1) % k])





def to_string_nba(nba: NBA, state2set: Dict[State, Set[LTLNode.LTL_Base_Node]], state2state: Dict[State, Tuple[State, int]], Symbol2LTL: Dict[Symbol, Set[LTLNode.LTL_Base_Node]]) -> str:
    ret = "NBA starts from here.\n"
    ret += "(Non-blocking)\n" if nba.maded_nonblocking else "(Maybe Blocking)\n"
    ret += "States:\n"
    for state in nba.states:
        ret += "\t{"
        state_, index = state2state[state]
        for phi in state2set[state_]:
            ret += phi.to_string() + ", "
        ret += "} * " + str(index)
        if state.get_is_initial():
            ret += " (initial)"
        ret += ",\n"
    ret += "\nAlphabet:\n"
    for symbol in nba.alphabet:
        ret += "\t{"
        set_ = Symbol2LTL[symbol]
        for phi in set_:
            ret += phi.to_string() + ", "
        ret += "},\n"
    ret += "\nDelta function:\n"
    for state in nba.states:
        for symbol, next_states in nba.delta[state].items():
            for next_state in next_states:
                ret += "\t{"
                state_, index = state2state[state]
                for phi in state2set[state_]:
                    ret += phi.to_string() + ", "
                ret += "} * " + str(index) + " -> {"
                state__, index_ = state2state[next_state]
                for phi in state2set[state__]:
                    ret += phi.to_string() + ", "
                ret += "} * " + str(index_) + " with symbol = {"
                for phi in Symbol2LTL[symbol]:
                    ret += phi.to_string() + ", "
                ret += "},\n"
    ret += "\nF set:\n"
    for state in nba.F:
        state_, index = state2state[state]
        ret += "\t{"
        for phi in state2set[state_]:
            ret += phi.to_string() + ", "
        ret += "} * " + str(index) + ",\n"
    ret += "\nGNBA ends at here."
    return ret

 
def to_string_gnba(
    gnba: GNBA,
    state2set: Dict[State, Set[LTLNode.LTL_Base_Node]],
    Symbol2LTL: Dict[Symbol, Set[LTLNode.LTL_Base_Node]]
) -> str:
    ret = "GNBA starts from here.\n"
    ret += "(Non-blocking)\n" if gnba.maded_nonblocking else "(Maybe Blocking)\n"
    ret += "States:\n"
    for state in gnba.states:
        ret += "\t{"
        set = state2set[state]
        for phi in set:
            ret += phi.to_string() + ", "
        ret += "}"
        if state.get_is_initial():
            ret += " (initial)"
        ret += ",\n"
    ret += "\nAlphabet:\n"
    for symbol in gnba.alphabet:
        ret += "\t{"
        set = Symbol2LTL[symbol]
        for phi in set:
            ret += phi.to_string() + ", "
        ret += "},\n"
    ret += "\nDelta function:\n"
    for state in gnba.states:
        for symbol, next_states in gnba.delta[state].items():
            for next_state in next_states:
                ret += "\t{"
                for phi in state2set[state]:
                    ret += phi.to_string() + ", "
                ret += "} -> {"
                for phi in state2set[next_state]:
                    ret += phi.to_string() + ", "
                ret += "} with symbol = {"
                for phi in Symbol2LTL[symbol]:
                    ret += phi.to_string() + ", "
                ret += "},\n"
    ret += "\nF set family:\n"
    for final_set in gnba.F:
        ret += "\t{\n"
        for state in final_set:
            ret += "\t\t{"
            for phi in state2set[state]:
                ret += phi.to_string() + ", "
            ret += "}\n"
        ret += "\t},\n"
    ret += "\nGNBA ends at here."
    return ret
