# Generated from LTLformular.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,38,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,20,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,1,1,1,1,1,0,1,0,2,0,2,0,2,1,0,
        10,11,1,0,12,13,44,0,19,1,0,0,0,2,35,1,0,0,0,4,5,6,0,-1,0,5,6,5,
        1,0,0,6,20,3,0,0,10,7,8,5,2,0,0,8,20,3,0,0,9,9,10,5,3,0,0,10,20,
        3,0,0,8,11,12,5,4,0,0,12,20,3,0,0,7,13,20,3,2,1,0,14,20,5,9,0,0,
        15,16,5,7,0,0,16,17,3,0,0,0,17,18,5,8,0,0,18,20,1,0,0,0,19,4,1,0,
        0,0,19,7,1,0,0,0,19,9,1,0,0,0,19,11,1,0,0,0,19,13,1,0,0,0,19,14,
        1,0,0,0,19,15,1,0,0,0,20,32,1,0,0,0,21,22,10,6,0,0,22,23,7,0,0,0,
        23,31,3,0,0,7,24,25,10,5,0,0,25,26,5,5,0,0,26,31,3,0,0,6,27,28,10,
        4,0,0,28,29,5,6,0,0,29,31,3,0,0,5,30,21,1,0,0,0,30,24,1,0,0,0,30,
        27,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,1,1,0,0,
        0,34,32,1,0,0,0,35,36,7,1,0,0,36,3,1,0,0,0,3,19,30,32
    ]

class LTLformularParser ( Parser ):

    grammarFileName = "LTLformular.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'G'", "'F'", "'X'", "'->'", "'U'", 
                     "'('", "')'", "<INVALID>", "'/\\'", "'\\/'", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Identifier", "AndOp", "OrOp", "True_op", 
                      "False_op", "WS" ]

    RULE_formula = 0
    RULE_logicConstant = 1

    ruleNames =  [ "formula", "logicConstant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    Identifier=9
    AndOp=10
    OrOp=11
    True_op=12
    False_op=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LTLformularParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Until_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLformularParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLformularParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil_formula" ):
                listener.enterUntil_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil_formula" ):
                listener.exitUntil_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntil_formula" ):
                return visitor.visitUntil_formula(self)
            else:
                return visitor.visitChildren(self)


    class Formula_in_parenthesesContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLformularParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula_in_parentheses" ):
                listener.enterFormula_in_parentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula_in_parentheses" ):
                listener.exitFormula_in_parentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula_in_parentheses" ):
                return visitor.visitFormula_in_parentheses(self)
            else:
                return visitor.visitChildren(self)


    class Logic_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLformularParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLformularParser.FormulaContext,i)

        def AndOp(self):
            return self.getToken(LTLformularParser.AndOp, 0)
        def OrOp(self):
            return self.getToken(LTLformularParser.OrOp, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_formula" ):
                listener.enterLogic_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_formula" ):
                listener.exitLogic_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_formula" ):
                return visitor.visitLogic_formula(self)
            else:
                return visitor.visitChildren(self)


    class Not_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLformularParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_formula" ):
                listener.enterNot_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_formula" ):
                listener.exitNot_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_formula" ):
                return visitor.visitNot_formula(self)
            else:
                return visitor.visitChildren(self)


    class Eventually_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLformularParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventually_formula" ):
                listener.enterEventually_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventually_formula" ):
                listener.exitEventually_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventually_formula" ):
                return visitor.visitEventually_formula(self)
            else:
                return visitor.visitChildren(self)


    class Logic_constContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicConstant(self):
            return self.getTypedRuleContext(LTLformularParser.LogicConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_const" ):
                listener.enterLogic_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_const" ):
                listener.exitLogic_const(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_const" ):
                return visitor.visitLogic_const(self)
            else:
                return visitor.visitChildren(self)


    class Next_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLformularParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_formula" ):
                listener.enterNext_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_formula" ):
                listener.exitNext_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_formula" ):
                return visitor.visitNext_formula(self)
            else:
                return visitor.visitChildren(self)


    class Always_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLformularParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlways_formula" ):
                listener.enterAlways_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlways_formula" ):
                listener.exitAlways_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlways_formula" ):
                return visitor.visitAlways_formula(self)
            else:
                return visitor.visitChildren(self)


    class Atomic_propositionContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LTLformularParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic_proposition" ):
                listener.enterAtomic_proposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic_proposition" ):
                listener.exitAtomic_proposition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_proposition" ):
                return visitor.visitAtomic_proposition(self)
            else:
                return visitor.visitChildren(self)


    class Implication_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLformularParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLformularParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLformularParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplication_formula" ):
                listener.enterImplication_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplication_formula" ):
                listener.exitImplication_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication_formula" ):
                return visitor.visitImplication_formula(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLformularParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = LTLformularParser.Not_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(LTLformularParser.T__0)
                self.state = 6
                self.formula(10)
                pass
            elif token in [2]:
                localctx = LTLformularParser.Always_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(LTLformularParser.T__1)
                self.state = 8
                self.formula(9)
                pass
            elif token in [3]:
                localctx = LTLformularParser.Eventually_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LTLformularParser.T__2)
                self.state = 10
                self.formula(8)
                pass
            elif token in [4]:
                localctx = LTLformularParser.Next_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(LTLformularParser.T__3)
                self.state = 12
                self.formula(7)
                pass
            elif token in [12, 13]:
                localctx = LTLformularParser.Logic_constContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.logicConstant()
                pass
            elif token in [9]:
                localctx = LTLformularParser.Atomic_propositionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(LTLformularParser.Identifier)
                pass
            elif token in [7]:
                localctx = LTLformularParser.Formula_in_parenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(LTLformularParser.T__6)
                self.state = 16
                self.formula(0)
                self.state = 17
                self.match(LTLformularParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LTLformularParser.Logic_formulaContext(self, LTLformularParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 21
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 22
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 23
                        self.formula(7)
                        pass

                    elif la_ == 2:
                        localctx = LTLformularParser.Implication_formulaContext(self, LTLformularParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 24
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 25
                        self.match(LTLformularParser.T__4)
                        self.state = 26
                        self.formula(6)
                        pass

                    elif la_ == 3:
                        localctx = LTLformularParser.Until_formulaContext(self, LTLformularParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 28
                        self.match(LTLformularParser.T__5)
                        self.state = 29
                        self.formula(5)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def True_op(self):
            return self.getToken(LTLformularParser.True_op, 0)

        def False_op(self):
            return self.getToken(LTLformularParser.False_op, 0)

        def getRuleIndex(self):
            return LTLformularParser.RULE_logicConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicConstant" ):
                listener.enterLogicConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicConstant" ):
                listener.exitLogicConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicConstant" ):
                return visitor.visitLogicConstant(self)
            else:
                return visitor.visitChildren(self)




    def logicConstant(self):

        localctx = LTLformularParser.LogicConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_logicConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




