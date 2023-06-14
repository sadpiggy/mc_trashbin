# Generated from LTLformular.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LTLformularParser import LTLformularParser
else:
    from LTLformularParser import LTLformularParser

# This class defines a complete listener for a parse tree produced by LTLformularParser.
class LTLformularListener(ParseTreeListener):

    # Enter a parse tree produced by LTLformularParser#until_formula.
    def enterUntil_formula(self, ctx:LTLformularParser.Until_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#until_formula.
    def exitUntil_formula(self, ctx:LTLformularParser.Until_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#formula_in_parentheses.
    def enterFormula_in_parentheses(self, ctx:LTLformularParser.Formula_in_parenthesesContext):
        pass

    # Exit a parse tree produced by LTLformularParser#formula_in_parentheses.
    def exitFormula_in_parentheses(self, ctx:LTLformularParser.Formula_in_parenthesesContext):
        pass


    # Enter a parse tree produced by LTLformularParser#logic_formula.
    def enterLogic_formula(self, ctx:LTLformularParser.Logic_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#logic_formula.
    def exitLogic_formula(self, ctx:LTLformularParser.Logic_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#not_formula.
    def enterNot_formula(self, ctx:LTLformularParser.Not_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#not_formula.
    def exitNot_formula(self, ctx:LTLformularParser.Not_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#eventually_formula.
    def enterEventually_formula(self, ctx:LTLformularParser.Eventually_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#eventually_formula.
    def exitEventually_formula(self, ctx:LTLformularParser.Eventually_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#logic_const.
    def enterLogic_const(self, ctx:LTLformularParser.Logic_constContext):
        pass

    # Exit a parse tree produced by LTLformularParser#logic_const.
    def exitLogic_const(self, ctx:LTLformularParser.Logic_constContext):
        pass


    # Enter a parse tree produced by LTLformularParser#next_formula.
    def enterNext_formula(self, ctx:LTLformularParser.Next_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#next_formula.
    def exitNext_formula(self, ctx:LTLformularParser.Next_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#always_formula.
    def enterAlways_formula(self, ctx:LTLformularParser.Always_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#always_formula.
    def exitAlways_formula(self, ctx:LTLformularParser.Always_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#atomic_proposition.
    def enterAtomic_proposition(self, ctx:LTLformularParser.Atomic_propositionContext):
        pass

    # Exit a parse tree produced by LTLformularParser#atomic_proposition.
    def exitAtomic_proposition(self, ctx:LTLformularParser.Atomic_propositionContext):
        pass


    # Enter a parse tree produced by LTLformularParser#implication_formula.
    def enterImplication_formula(self, ctx:LTLformularParser.Implication_formulaContext):
        pass

    # Exit a parse tree produced by LTLformularParser#implication_formula.
    def exitImplication_formula(self, ctx:LTLformularParser.Implication_formulaContext):
        pass


    # Enter a parse tree produced by LTLformularParser#logicConstant.
    def enterLogicConstant(self, ctx:LTLformularParser.LogicConstantContext):
        pass

    # Exit a parse tree produced by LTLformularParser#logicConstant.
    def exitLogicConstant(self, ctx:LTLformularParser.LogicConstantContext):
        pass



del LTLformularParser