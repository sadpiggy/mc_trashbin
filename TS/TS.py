from BA import BA
from LTL import LTLNode
from utils import powerset

from typing import List, Dict, Set, Tuple

class State:
    def __init__(self,name_="", is_initial_=False):
        self.name = name_
        self.is_initial = is_initial_
    
    
    def set_is_initial(self, is_initial_ = False):
        self.is_initial = is_initial_
    
    def get_is_initial(self):
        return self.is_initial
    
    def set_name(self, name_):
        self.name = name_
    
    def to_string(self):
        return self.name

class Action:
    def __init__(self, name_):
        self.name = name_
    
    def to_string(self):
        return self.name

class Proposition:
    def __init__(self, name_=""):
        self.name = name_
    
    def to_string(self):
        return self.name

class TS:
    def __init__(self):
        self.States: List[State] = []
        self.Acts: List[Action] = []
        self.APs: List[Proposition] = []
        self.trans: Dict[State, Set[Tuple[State, Action]]] = {}
        self.Lables: Dict[State, Set[Proposition]] = {}

        self.num_of_states: int
        self.num_of_trans: int

        self.hava_cycle: bool
        
        self.R: Set[State] = set()
        self.T: Set[State] = set()
        self.I: Set[State] = set()
        # stack
        self.U: List[State] = []
        self.V: List[State] = []
    
    def generate_ts(self,filename="datas\TS1.txt"):
        with open(filename, 'r') as file:
            line_num = 0
            # state_index = 0
            s_lable_index = 0
            for line in file:
                line = line.strip()  # 去除行尾的换行符和空格
                if line:  # 忽略空行
                    items = line.split()  # 按空格分割
                    line_num += 1 # 1base
                    if line_num == 1:#
                        self.num_of_states = int(items[0])
                        self.num_of_trans = int(items[1])
                        
                        for i in range(self.num_of_states):
                            s = State(str(i))
                            self.States.append(s)
                            self.trans[s] = set()
                            self.Lables[s] = set()
                        
                    elif line_num == 2:#输入初始状态
                        for i in range(len(items)):
                            self.States[int(items[i])].set_is_initial(True)
                        
                    elif line_num == 3:#输入act set
                        for i in range(len(items)):
                            act = Action(items[i])
                            self.Acts.append(act)
                    elif line_num == 4:# 输入 atomic proposition set
                        for i in range(len(items)):
                            prop = Proposition(items[i])
                            self.APs.append(prop)
                    elif line_num <= 4 + self.num_of_trans:#trans
                        from_state_index = int(items[0])
                        act_index = int(items[1])
                        to_state_index = int(items[2])
                        self.trans[self.States[from_state_index]].add((self.States[to_state_index],self.Acts[act_index]))
                    else: #输入label
                        for i in range(len(items)):
                            if i == -1:
                                break
                            prop_index = int(items[i])
                            self.Lables[self.States[s_lable_index]].add(self.APs[prop_index])
                        
                        s_lable_index += 1
                    
                    

        

        
    
    def persistence_checking(self, F: Set[Proposition]) -> bool:
        self.cycle_found = False
        for s in self.States:
            if s.get_is_initial():
                self.I.add(s)

        while self.I and not self.cycle_found:
            s = self.I.pop()
            self.reachable_cycle(F, s)

        self.R.clear()
        self.T.clear()
        self.I.clear()
        self.U.clear()
        self.V.clear()

        return not self.cycle_found
    
    
    def persistence_checking_entries(self, F: Set[Proposition], entries: Set[State]) -> bool:
        self.cycle_found = False
        self.I = entries

        while self.I and not self.cycle_found:
            s = self.I.pop()
            self.reachable_cycle(F, s)

        self.R.clear()
        self.T.clear()
        self.I.clear()
        self.U.clear()
        self.V.clear()

        return not self.cycle_found
    
    def get_state(self, sid: int) -> State:
        return self.States[sid]
    
    def get_Name2Prop(self) -> Dict[str, Proposition]:
        return {prop.name: prop for prop in self.APs}

    def reachable_cycle(self, F: Set[Proposition], s: State):
        self.U.append(s)
        self.R.add(s)
        
        if s in self.I:
            self.I.remove(s)

        while True:
            s_prime = self.U[-1]
            found = False
            for t, alpha in self.trans[s_prime]:
                if t not in self.R:
                    self.U.append(t)
                    self.R.add(t)
                    if t in self.I:
                        self.I.remove(t)
                    found = True
                    break

            if not found:
                self.U.pop()
                for l in self.Lables[s_prime]:
                    if l in F:
                        found = True
                        break

                if found:
                    self.cycle_found = self.cycle_check(s_prime)
            
            if not self.U or  self.cycle_found:
                break

    def cycle_check(self, s: State) -> bool:
        inner_cycle_found = False
        self.V.append(s)
        self.T.add(s)

        while True:
            s_prime = self.V[-1]
            for t, alpha in self.trans[s_prime]:
                if s == t:
                    inner_cycle_found = True
                    break

            if inner_cycle_found:
                self.V.append(s)
            else:
                found = False
                for t, alpha in self.trans[s_prime]:
                    if t not in self.T:
                        self.V.append(t)
                        self.T.add(t)
                        found = True
                        break

                if not found:
                    self.V.pop()
            
            if not self.V or inner_cycle_found:
                break

        return inner_cycle_found
    


def get_entries(src_s: State,
                    ts: TS,
                    nba: BA.NBA,
                    LTL2Symbol: Dict[Set[LTLNode.LTL_Base_Node], BA.Symbol],
                    Prop2LTL: Dict[Proposition, LTLNode.LTL_Base_Node],
                    power_set: powerset.PowerSet,
                    sstate2s: Dict[Tuple[State, BA.State], State]) -> Set[State]:
        ret = set()
        for q_prime in nba.states:
            if q_prime.get_is_initial():
                tmp = []
                for prop in ts.Lables[src_s]:
                    tmp.append(Prop2LTL[prop])
                LTL_set = power_set.get_subset(tmp)
                for q in nba.delta[q_prime][LTL2Symbol[frozenset(LTL_set)]]:
                    ret.add(sstate2s[(src_s, q)])
        return ret


# def product(ts: TS, nba, LTL2Symbol, Prop2LTL, power_set, F_Props, s2s_state) -> TS:
#     ret = TS()
    
#     # Copy Act
#     ret.Act = ts.Acts.copy()
    
#     # Initialize states
#     ts_index = {s: i for i, s in enumerate(ts.States)}
#     nba_index = {q: i for i, q in enumerate(nba.states)}
#     states_list = [[] for _ in range(len(ts.States))]
    
#     for s in ts.States:
#         for state in nba.states:
#             state_ = State()
#             state_.set_is_initial(True)
#             s2s_state[state_] = (s, state)
#             ret.trans[state_] = set()
#             ret.States.append(state_)
#             ret.Lables[state_] = set()
#             states_list[ts_index[s]].append(state_)
    
#     # Initialize I
#     for i, s in enumerate(ts.States):
#         if s.get_is_initial():
#             for q_prime in nba.states:
#                 if q_prime.get_is_initial():
#                     tmp = [Prop2LTL[prop] for prop in ts.Lables[s]]
#                     LTL_set = power_set.get_subset(tmp)
#                     for q in nba.delta[q_prime][LTL2Symbol[frozenset(LTL_set)]]:
#                         states_list[i][nba_index[q]].set_is_initial(True)
    
#     # Initialize AP
#     for q in nba.states:
#         prop = Proposition()
#         ret.APs.append(prop)
#         if q in nba.F:
#             F_Props.add(prop)
    
#     # Initialize L
#     for i, s_list in enumerate(states_list):
#         for j, q in enumerate(nba.states):
#             ret.Lables[s_list[j]].add(ret.APs[j])
    
#     # Initialize trans
#     for s in ts.States:
#         s_list = states_list[ts_index[s]]
#         for q in nba.states:
#             sq_state = s_list[nba_index[q]]
#             for t, alpha in ts.trans[s]:
#                 t_list = states_list[ts_index[t]]

#     for q in nba.states:
#         sq_state = s_list[nba_index[q]]
#         for t, alpha in ts.trans[s]:
#             t_list = states_list[ts_index[t]]
#             tmp = [Prop2LTL[prop] for prop in ts.Lables[t]]
#             LTL_set = power_set.get_subset(tmp)
#             for p in nba.delta[q][LTL2Symbol[frozenset(LTL_set)]]:
#                 tp_state = t_list[nba_index[p]]
#                 ret.trans[sq_state].add((tp_state, alpha))
#     return ret


def product(ts, nba, LTL2Symbol, Prop2LTL, power_set, F_Props, s2s_state):
    ret = TS()

    # copy Act
    ret.Acts = ts.Acts

    # initialize states
    ts_index = {}
    nba_index = {}
    for i, state in enumerate(ts.States):
        ts_index[state] = i
    for i, state in enumerate(nba.states):
        nba_index[state] = i
    states_list = []
    for s in ts.States:
        states_list.append([])
        for state in nba.states:
            state_ = State()
            state_.set_is_initial()
            s2s_state[state_] = (s, state)
            ret.trans[state_] = set()
            ret.States.append(state_)
            ret.Lables[state_] = set()
            states_list[-1].append(state_)

    # initialize I
    for i, s in enumerate(ts.States):
        if s.get_is_initial():
            for q_prime in nba.states:
                if q_prime.get_is_initial():
                    tmp = []
                    for prop in ts.Lables[s]:
                        tmp.append(Prop2LTL[prop])
                    LTL_set = power_set.get_subset(tmp)
                    # if LTL2Symbol.get(frozenset(LTL_set)) is not None and nba.delta.get(q_prime) is not None and nba.delta[q_prime].get(LTL2Symbol[frozenset(LTL_set)]) is not None:
                    for q in nba.delta[q_prime][LTL2Symbol[frozenset(LTL_set)]]:
                        states_list[i][nba_index[q]].set_is_initial(True)

    # initialize AP
    for q in nba.states:
        prop = Proposition()
        ret.APs.append(prop)
        if q in nba.F:
            F_Props.add(prop)

    # initialize L
    for s_list in states_list:
        for j, q in enumerate(nba.states):
            ret.Lables[s_list[j]].add(ret.APs[j])

    # initialize trans
    for s in ts.States:
        s_list = states_list[ts_index[s]]
        for q in nba.states:
            sq_state = s_list[nba_index[q]]
            for t, alpha in ts.trans[s]:
                t_list = states_list[ts_index[t]]
                tmp = []
                for prop in ts.Lables[t]:
                    tmp.append(Prop2LTL[prop])
                LTL_set = power_set.get_subset(tmp)
                # if LTL2Symbol.get(frozenset(LTL_set)) is not None and nba.delta.get(q_prime) is not None and nba.delta[q_prime].get(LTL2Symbol[frozenset(LTL_set)]) is not None:
                for p in nba.delta[q][LTL2Symbol[frozenset(LTL_set)]]:
                    ret.trans[sq_state].add((t_list[nba_index[p]], alpha))

    return ret



def to_string(prod:TS, s2sstate, state2state, state2set):
    ret = "TS starts from here.\n"
    ret += "S:\n"
    for s_ in prod.States:
        ret += "\t"
        s, state = s2sstate[s_]
        ret += s.to_string() + " * "
        state_, index = state2state[state]
        ret += "{"
        for phi in state2set[state_]:
            ret += phi.to_string() + ", "
        ret += "} * " + str(index)
        if s_.get_is_initial():
            ret += " (initial)"
        ret += ",\n"
    ret += "\nTransition:\n"
    for s in prod.States:
        for next_s, action in prod.trans[s]:
            ret += "\t"
            s_, state = s2sstate[s]
            ret += s_.to_string() + " * "
            state_, index = state2state[state]
            ret += "{"
            for phi in state2set[state_]:
                ret += phi.to_string() + ", "
            ret += "} * " + str(index) + " -> "
            _s_, _state = s2sstate[next_s]
            ret += _s_.to_string() + " * "
            _state_, _index = state2state[_state]
            ret += "{"
            for phi in state2set[_state_]:
                ret += phi.to_string() + ", "
            ret += "} * " + str(_index) + " with action = " + action.to_string()
            ret += ",\n"
    ret += "\nTS ends at here."
    return ret

