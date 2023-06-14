# Generated from LTLformular.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LTLformularParser import LTLformularParser
else:
    from LTLformularParser import LTLformularParser

# This class defines a complete generic visitor for a parse tree produced by LTLformularParser.

class LTLformularVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LTLformularParser#until_formula.
    def visitUntil_formula(self, ctx:LTLformularParser.Until_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#formula_in_parentheses.
    def visitFormula_in_parentheses(self, ctx:LTLformularParser.Formula_in_parenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#logic_formula.
    def visitLogic_formula(self, ctx:LTLformularParser.Logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#not_formula.
    def visitNot_formula(self, ctx:LTLformularParser.Not_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#eventually_formula.
    def visitEventually_formula(self, ctx:LTLformularParser.Eventually_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#logic_const.
    def visitLogic_const(self, ctx:LTLformularParser.Logic_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#next_formula.
    def visitNext_formula(self, ctx:LTLformularParser.Next_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#always_formula.
    def visitAlways_formula(self, ctx:LTLformularParser.Always_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#atomic_proposition.
    def visitAtomic_proposition(self, ctx:LTLformularParser.Atomic_propositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#implication_formula.
    def visitImplication_formula(self, ctx:LTLformularParser.Implication_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLformularParser#logicConstant.
    def visitLogicConstant(self, ctx:LTLformularParser.LogicConstantContext):
        return self.visitChildren(ctx)



del LTLformularParser