from Parser import LTLvisitor
from antlr4 import CommonTokenStream,InputStream
from Parser.LTLformularLexer import LTLformularLexer
from Parser.LTLformularParser import LTLformularParser
from utils import powerset
from typing import Dict,Set
from TS import TS
from LTL import LTLNode
from typing import List,Set,Tuple
from BA import BA
import sys

def main():
    # TS
    only_concert_ltl = 0
    ts = TS.TS()
    ts_path = "datas/TS1.txt"
    ltl_path = "datas/LTL2.txt"
    if (len(sys.argv) > 2):
        ts_path = sys.argv[1]
        ltl_path = sys.argv[2]
    ts.generate_ts(ts_path)
    # aps
    Name2Prop: Dict[str, 'TS.Proposition'] = ts.get_Name2Prop()
    Prop2LTL: Dict['TS.Proposition', 'LTLNode.LTL_Base_Node'] = {}
    PropLTLs: list['LTLNode.LTL_Base_Node'] = []# ltls
    for name, prop in Name2Prop.items():
        ltl = LTLNode.Variable(prop)
        PropLTLs.append(ltl)
        Prop2LTL[prop] = ltl
    True_: 'LTLNode.LTL_Base_Node' = LTLNode.LTL_Base_Node()
    
    s0_lines_num = 0
    si_lines_num = 0
    ltl_si = 0
    
    with open(ltl_path, 'r') as file:
        line_num = 0
        # state_index = 0
        # s_lable_index = 0
        for line in file:
            line_num += 1
            if line_num == 1:
                items = line.split()
                s0_lines_num = int(items[0])
                si_lines_num = int(items[1])
                continue
            elif line_num <= 1 + s0_lines_num:
                lexer = LTLformularLexer(InputStream(line))
                stream = CommonTokenStream(lexer)
                parser = LTLformularParser(stream)
                tree = parser.formula()
                # visitor = LTLvisitor.L
                visitor = LTLvisitor.LTLformularVisitorImpl(Name2Prop,Prop2LTL,True_)
                root = visitor.visit(tree)
            else:
                ltl_si = int(line.split()[0])
                lexer = LTLformularLexer(InputStream(line[1:]))
                stream = CommonTokenStream(lexer)
                parser = LTLformularParser(stream)
                tree = parser.formula()
                # visitor = LTLvisitor.L
                visitor = LTLvisitor.LTLformularVisitorImpl(Name2Prop,Prop2LTL,True_)
                root = visitor.visit(tree)
            if only_concert_ltl == 1:
                print(root.to_string())
                continue
            root_ltl: LTLNode.LTL_Base_Node = None
            if isinstance(root, LTLNode.Negation):
                #负负得正
                root_ltl = root.get_children()[0]
            else:
                root_ltl = LTLNode.Negation(root)
                
            
            PropLTLs_powerset = powerset.PowerSet(PropLTLs)
            LTL2Symbol: Dict[Set[LTLNode.LTL_Base_Node], BA.Symbol] = {}
            set2gnba_state: Dict[Set[LTLNode.LTL_Base_Node], BA.State] = {}
            gnba: BA.GNBA = BA.GNBA(root_ltl, LTL2Symbol, set2gnba_state, PropLTLs_powerset, True)
            # print("gnbs_states_len=={}".format(gnba.states.__len__()))
            Symbol2LTL: Dict[BA.Symbol, Set[LTLNode.LTL_Base_Node]] = {}
            for set_symbols, symbol in LTL2Symbol.items():
                Symbol2LTL[symbol] = set_symbols
            gnba_state2set: Dict[BA.State, Set[LTLNode.LTL_Base_Node]] = {}
            for set_symbols, state in set2gnba_state.items():
                gnba_state2set[state] = set_symbols
            # print(BA.to_string_gnba(gnba, gnba_state2set, Symbol2LTL), file=open('output/output.txt','a'))
           
            

            trap: BA.State = gnba.make_nonblocking()
            # print("gnbs_states_len222=={}".format(gnba.states.__len__()))
            gnba_state2set[trap] = {}
            # count = 0
            # for i,_ in gnba_state2set.items():
            #     count += 1
            # print("count=={}".format(count))

            # convert GNBA to NBA
            nba_state2gnba_state: Dict[BA.State, Tuple[BA.State, int]] = {}
            nba: BA.NBA = BA.NBA(gnba, nba_state2gnba_state)
            # print("nba_states_len=={}".format(nba.states.__len__()))
            # print(BA.to_string_nba(nba, gnba_state2set, nba_state2gnba_state, Symbol2LTL), file=open('output/output.txt','a'))
            

            # construction production of TransitionSystem and NBA
            s2s_nba_state: Dict[TS.State, Tuple[TS.State, BA.State]] = {}
            F_props: Set[TS.Proposition] = set()
            
            if ts == None:
                print("TS is None")
            if nba == None:
                print("NBA is None")
            if LTL2Symbol == None:
                print("LTL2Symbol is None")
            if Prop2LTL == None:
                print("Prop2LTL is None")
            if PropLTLs_powerset == None:
                print("PropLTLs_powerset is None")
            if F_props == None:
                print("F_props is None")
            if s2s_nba_state == None:
                print("s2s_nba_state is None")
            
            production: TS.TS = TS.product(ts, nba, LTL2Symbol, Prop2LTL, PropLTLs_powerset, F_props, s2s_nba_state)
            # print(production)
            # print(TS.to_string(production,  s2s_nba_state, nba_state2gnba_state, gnba_state2set), file=open('output/output.txt','a'))
            
            result: bool
            if line_num <= 1 + s0_lines_num:
                result = production.persistence_checking(F_props)
            else:
                src_s: TS.State = ts.get_state(ltl_si)
                s_nba_state2s: Dict[Tuple[TS.State, BA.State], TS.State] = {}
                for s, s_nba_state in s2s_nba_state.items():
                    s_nba_state2s[s_nba_state] = s
                entries: Set[TS.State] = TS.get_entries(src_s, ts, nba, LTL2Symbol, Prop2LTL, PropLTLs_powerset, s_nba_state2s)
                result = production.persistence_checking_entries(F_props, entries)

            if result:
                print(1)
            else:
                print(0)

                
    
    
    # Name2Prop_: Dict[str, 'TS.Proposition'] = {}
    # Prop2LTL_: Dict['TS.Proposition', 'LTLNode.LTL_Base_Node'] = {}
    # True_: 'LTLNode.LTL_Base_Node' = LTLNode.LTL_Base_Node()
    
    # input_str = "(G (F p))"
    # lexer = LTLformularLexer(InputStream(input_str))
    # stream = CommonTokenStream(lexer)
    # parser = LTLformularParser(stream)
    # tree = parser.formula()
    # # visitor = LTLvisitor.L
    # visitor = LTLvisitor.LTLformularVisitorImpl(Name2Prop_,Prop2LTL_,True_)
    # result = visitor.visit(tree)

    


if __name__ == '__main__':
    main()



