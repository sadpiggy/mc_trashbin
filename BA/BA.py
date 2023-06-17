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
    
    def __init__(self):
        self.delta: Dict[State, Dict[Symbol, Set[State]]] = {}
        self.states: List[State] = []
        self.alphabet: List[Symbol] = []
        self.NF_flag: bool = False
        # self.NFlag = False


# By introducing a trap state, the Büchi automaton can be transformed into a non-blocking form.
# This additional state takes care of undefined transitions in the original automaton, ensuring complete determinism of the automaton.
    def make_nonblocking(self):
        if self.NF_flag:
            return None
        trap = State()
        self.delta[trap] = {symbol: set([trap]) for symbol in self.alphabet}
        # self.delta[trap] = {}
        self.states.append(trap)
        for state in self.states:
            for symbol in self.alphabet:
                if symbol not in self.delta[state]:
                    self.delta[state][symbol] = set([trap])
        self.NF_flag = True
        return trap





# Construct a GNBA 
class GNBA(BA):
    def __init__(
        self,
        formular: LTLNode.LTL_Base_Node,
        LTL2Symbol: Dict[Set[LTLNode.LTL_Base_Node], Symbol],
        set2state: Dict[Set[LTLNode.LTL_Base_Node], State],
        PropLTLs_power_set: PowerSet,
        True_: LTLNode.LTL_Base_Node
    ):
        super().__init__()
        self.F = []

        closure_set = formular.get_closure(formular, None).copy()
        for propLTL in PropLTLs_power_set.get_universe():
            if propLTL not in closure_set:
                closure_set.add(propLTL)
                closure_set.add(LTLNode.Negation(propLTL))
        has_True = True in closure_set
        # if True in closure_set:
        #     print("no problem")
# Compute elementary sets of closure(formula)
        elementary_sets = []
        closure_power_set = PowerSet(list(closure_set))
        for subset in closure_power_set.get_subsets():
            flag = not has_True or True in subset
            for it in closure_set:
                if not flag:
                    break
                if isinstance(it, LTLNode.And):
                    phi0 = it.get_children()[0]
                    phi1 = it.get_children()[-1]
                    flag &= (it in subset) == (phi0 in subset and phi1 in subset)
                if it in subset:
                    if isinstance(it, LTLNode.Negation):
                        target = it.get_children()[0]
                        flag &= target not in subset
                    else:
                        for phi_ in subset:
                            flag &= (not(isinstance(phi_, LTLNode.Negation)) or phi_.get_children()[0] != it)
                if isinstance(it, LTLNode.Until):
                    phi0 = it.get_children()[0]
                    phi1 = it.get_children()[-1]
                    if phi1 in subset:
                        flag &= it in subset
                    if it in subset and phi1 not in subset:
                        flag &= phi0 in subset
                if it not in subset:
                    if isinstance(it, LTLNode.Negation):
                        target = it.get_children()[0]
                        flag &= target in subset
                    else:
                        found = False
                        for phi_ in subset:
                            if isinstance(phi_, LTLNode.Negation) and phi_.get_children()[0] == it:
                                found = True
                                break
                        flag &= found
                
            if flag:
                elementary_sets.append(subset)
#Initialize states
        for subset in elementary_sets:
            is_initial = formular in subset
            state = State(is_initial)
            set2state[frozenset(subset)] = state
            self.states.append(state)
            self.delta[state] = {}
#Construct accepting conditions Final
        for target in closure_set:
            if isinstance(target, LTLNode.Until):
                phi1 = target.get_children()[-1]
                acceptintStates = set()
                for subset in elementary_sets:
                    if target not in subset or phi1 in subset:
                        acceptintStates.add(set2state[frozenset(subset)])
                self.F.append(acceptintStates)

        # self.alphabet = []
        # print("set2symbol={}".format(set2symbol))
# construct alphabet
        set2symbol = {}
        for s in PropLTLs_power_set.get_subsets():
            symbol = Symbol()
            set2symbol[frozenset(s)] = symbol
            self.alphabet.append(symbol)
            LTL2Symbol[frozenset(s)] = symbol
# construct transition function
        for subset in elementary_sets:
            intersection = [psi for psi in PropLTLs_power_set.get_universe() if psi in subset]
            A = PropLTLs_power_set.get_subset(intersection)
            for subset_prime in elementary_sets:
                flag = True
                for it in closure_set:
                    if not flag:
                        break
                    if isinstance(it, LTLNode.Next):
                        target = it.get_children()[0]
                        flag &= (it in subset) == (target in subset_prime)
                    if isinstance(it, LTLNode.Until):
                        phi0 = it.get_children()[0]
                        phi1 = it.get_children()[-1]
                        flag &= (it in subset) == (phi1 in subset_prime or (phi0 in subset and it in subset_prime))
                if flag:
                    delta_subset = self.delta[set2state[frozenset(subset)]]
                    # print(type(A))
                    symbol = set2symbol[frozenset(A)]
                    state_subset_prime = set2state[frozenset(subset_prime)]
                    if symbol not in delta_subset:
                        delta_subset[symbol] = {state_subset_prime}
                    else:
                        delta_subset[symbol].add(state_subset_prime)






class NBA(BA):
    def __init__(self, gnba: GNBA, state2state_index: Dict[State, Tuple[State, int]]):
        super().__init__()
        self.F: Set[State] = set()
        
        self.alphabet = gnba.alphabet
        num_sets = len(gnba.F)
        states_list = []
        index = {}

        for i in range(len(gnba.states)):
            state_ = gnba.states[i]
            index[state_] = i
            states_list.append([])
            for j in range(num_sets):
                new_state = State(not j and state_.get_is_initial())
                state2state_index[new_state] = (state_, j)
                self.delta[new_state] = {}
                for symbol in self.alphabet:
                    self.delta[new_state][symbol] = set()
                self.states.append(new_state)
                states_list[-1].append(new_state)
        # print("self.states_len={},count=={}".format(len(self.states),count))
        
        if num_sets:
            for i in range(len(gnba.states)):
                if gnba.states[i] in gnba.F[0]:
                    self.F.add(states_list[i][0])
        
        for i in range(len(gnba.states)):
            new_state = gnba.states[i]
            for symbol, next_states in gnba.delta[new_state].items():
                next_states_list = []
                for j in range(num_sets):
                    next_states_set = set()
                    for next_state in next_states:
                        next_states_set.add(states_list[index[next_state]][j])
                    next_states_list.append(next_states_set)
                for j in range(num_sets):
                    if new_state not in gnba.F[j]:
                        self.delta[states_list[i][j]][symbol].update(next_states_list[j])
                    else:
                        self.delta[states_list[i][j]][symbol].update(next_states_list[(j + 1) % num_sets])





def to_string_nba(nba: NBA, state2set: Dict[State, Set[LTLNode.LTL_Base_Node]], state2state: Dict[State, Tuple[State, int]], Symbol2LTL: Dict[Symbol, Set[LTLNode.LTL_Base_Node]]) -> str:
    ret = "NBA starts from here.\n"
    ret += "(Non-blocking)\n" if nba.NF_flag else "(Maybe Blocking)\n"
    ret += "States:\n"
    # print(nba.states.__len__())
    # return
    
    for state in nba.states:
        ret += "\t{"
        # print("state={}".format(state))
        # if not state2state.keys().__contains__(state):
        #     print("not contain")
        #     print(state)
        #     for i in state2state.keys():
        #         print(i)
                
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
    ret += "(Non-blocking)\n" if gnba.NF_flag else "(Maybe Blocking)\n"
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

