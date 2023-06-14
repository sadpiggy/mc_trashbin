from antlr4 import CommonTokenStream, InputStream
from typing import Dict
from  TS import TS
from LTL import LTLNode
from LTL.LTLNode import *
from Parser.LTLformularParser import LTLformularParser
from Parser.LTLformularVisitor import LTLformularVisitor
from Parser.LTLformularLexer import LTLformularLexer
from Parser.LTLformularVisitor import LTLformularVisitor

# from LTLformularParser import LTLformularParser
# from LTLformularVisitor import LTLformularVisitor
# from LTLformularLexer import LTLformularLexer
# from LTLformularVisitor import LTLformularVisitor


class LTLformularVisitorImpl(LTLformularVisitor):
    
    def __init__(self, Name2Prop_: Dict[str, 'TS.Proposition'],
                 Prop2LTL_: Dict['TS.Proposition', 'LTLNode.LTL_Base_Node'], True_: 'LTLNode.LTL_Base_Node'):
        self.Name2Prop = Name2Prop_
        self.Prop2LTL = Prop2LTL_
        self.LTL_True = True_
        self.LTL_False = LTLNode.Negation(True_)
    
    
    def visitNot_formula(self, ctx: LTLformularParser.Not_formulaContext):
        child:LTL_Base_Node = (self.visit(ctx.formula()))
        if isinstance(child, LTLNode.Negation):
            return child.get_children()[0]
        else:
            return LTLNode.Negation(child)
        
        # return f'!{child}'

    # G:always
    def visitAlways_formula(self, ctx: LTLformularParser.Always_formulaContext):
        child:LTL_Base_Node = (self.visit(ctx.formula()))
        no_child:LTL_Base_Node = None
        if isinstance(child, LTLNode.Negation):
            no_child = child.get_children()[0]
        else:
            no_child = LTLNode.Negation(child)
        return LTLNode.Negation(LTLNode.Until(self.LTL_True,no_child))

    # F:eventually
    def visitEventually_formula(self, ctx: LTLformularParser.Eventually_formulaContext):
        child = self.visit(ctx.formula())
        return LTLNode.Until(self.LTL_True,child)

    # X:next
    def visitNext_formula(self, ctx: LTLformularParser.Next_formulaContext):
        child = self.visit(ctx.formula())
        return LTLNode.Next(child)
        # return f'X{child}'

    def visitLogic_formula(self, ctx: LTLformularParser.Logic_formulaContext):

        left:LTL_Base_Node = (self.visit(ctx.formula(0)))
        right:LTL_Base_Node = (self.visit(ctx.formula(1)))

        not_left:LTL_Base_Node = None
        not_right:LTL_Base_Node = None
        # op = ctx.op.text
        #负负得正捏
        if isinstance(left, LTLNode.Negation):
            not_left = left.get_children()[0]
        else:
            not_left = LTLNode.Negation(left)
        
        if isinstance(right, LTLNode.Negation):
            not_right = right.get_children()[0]
        else:
            not_right = LTLNode.Negation(right)
        if ctx.AndOp() != None:
            return LTLNode.And(left, right)
        
        else:
            return LTLNode.Negation(LTLNode.And(not_left, not_right))


    def visitImplication_formula(self, ctx: LTLformularParser.Implication_formulaContext):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        not_right:LTL_Base_Node = None
        if isinstance(right, LTLNode.Negation):
            not_right = right.get_children()[0]
        else:
            not_right = LTLNode.Negation(right)
        return LTLNode.Negation(LTLNode.And(left, not_right))
            
        # return f'({left} -> {right})'

    # until
    def visitUntil_formula(self, ctx: LTLformularParser.Until_formulaContext):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return LTLNode.Until(left, right)
        # return f'({left} U {right})'

    def visitLogic_const(self, ctx: LTLformularParser.LogicConstantContext):
        # return ctx.getText()
        if ctx.True_op() != None:
            return self.LTL_True
        else: 
            return self.LTL_False

    def visitAtomic_proposition(self, ctx: LTLformularParser.Atomic_propositionContext):
        # return ctx.getText()
        return self.Prop2LTL[self.Name2Prop[ctx.getText()]]

    def visitFormula_in_parentheses(self, ctx: LTLformularParser.Formula_in_parenthesesContext):
        return self.visit(ctx.formula())

if __name__ == '__main__':
    print("hahah")
