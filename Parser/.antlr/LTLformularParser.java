// Generated from /home/srb/wky/model/bighw/Parser/LTLformular.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LTLformularParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, Identifier=9, 
		AndOp=10, OrOp=11, True_op=12, False_op=13, WS=14;
	public static final int
		RULE_formula = 0, RULE_logicConstant = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"formula", "logicConstant"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'!'", "'G'", "'F'", "'X'", "'->'", "'U'", "'('", "')'", null, 
			"'/\\'", "'\\/'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "Identifier", "AndOp", 
			"OrOp", "True_op", "False_op", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LTLformular.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LTLformularParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class FormulaContext extends ParserRuleContext {
		public FormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formula; }
	 
		public FormulaContext() { }
		public void copyFrom(FormulaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Until_formulaContext extends FormulaContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public Until_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Formula_in_parenthesesContext extends FormulaContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public Formula_in_parenthesesContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Logic_formulaContext extends FormulaContext {
		public Token op;
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public TerminalNode AndOp() { return getToken(LTLformularParser.AndOp, 0); }
		public TerminalNode OrOp() { return getToken(LTLformularParser.OrOp, 0); }
		public Logic_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Not_formulaContext extends FormulaContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public Not_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Eventually_formulaContext extends FormulaContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public Eventually_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Logic_constContext extends FormulaContext {
		public LogicConstantContext logicConstant() {
			return getRuleContext(LogicConstantContext.class,0);
		}
		public Logic_constContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Next_formulaContext extends FormulaContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public Next_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Always_formulaContext extends FormulaContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public Always_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Atomic_propositionContext extends FormulaContext {
		public TerminalNode Identifier() { return getToken(LTLformularParser.Identifier, 0); }
		public Atomic_propositionContext(FormulaContext ctx) { copyFrom(ctx); }
	}
	public static class Implication_formulaContext extends FormulaContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public Implication_formulaContext(FormulaContext ctx) { copyFrom(ctx); }
	}

	public final FormulaContext formula() throws RecognitionException {
		return formula(0);
	}

	private FormulaContext formula(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		FormulaContext _localctx = new FormulaContext(_ctx, _parentState);
		FormulaContext _prevctx = _localctx;
		int _startState = 0;
		enterRecursionRule(_localctx, 0, RULE_formula, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				{
				_localctx = new Not_formulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(5);
				match(T__0);
				setState(6);
				formula(10);
				}
				break;
			case T__1:
				{
				_localctx = new Always_formulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(7);
				match(T__1);
				setState(8);
				formula(9);
				}
				break;
			case T__2:
				{
				_localctx = new Eventually_formulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(9);
				match(T__2);
				setState(10);
				formula(8);
				}
				break;
			case T__3:
				{
				_localctx = new Next_formulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(11);
				match(T__3);
				setState(12);
				formula(7);
				}
				break;
			case True_op:
			case False_op:
				{
				_localctx = new Logic_constContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(13);
				logicConstant();
				}
				break;
			case Identifier:
				{
				_localctx = new Atomic_propositionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(14);
				match(Identifier);
				}
				break;
			case T__6:
				{
				_localctx = new Formula_in_parenthesesContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(15);
				match(T__6);
				setState(16);
				formula(0);
				setState(17);
				match(T__7);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(32);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(30);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new Logic_formulaContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(21);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(22);
						((Logic_formulaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AndOp || _la==OrOp) ) {
							((Logic_formulaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(23);
						formula(7);
						}
						break;
					case 2:
						{
						_localctx = new Implication_formulaContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(24);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(25);
						match(T__4);
						setState(26);
						formula(6);
						}
						break;
					case 3:
						{
						_localctx = new Until_formulaContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(27);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(28);
						match(T__5);
						setState(29);
						formula(5);
						}
						break;
					}
					} 
				}
				setState(34);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LogicConstantContext extends ParserRuleContext {
		public TerminalNode True_op() { return getToken(LTLformularParser.True_op, 0); }
		public TerminalNode False_op() { return getToken(LTLformularParser.False_op, 0); }
		public LogicConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicConstant; }
	}

	public final LogicConstantContext logicConstant() throws RecognitionException {
		LogicConstantContext _localctx = new LogicConstantContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_logicConstant);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_la = _input.LA(1);
			if ( !(_la==True_op || _la==False_op) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 0:
			return formula_sempred((FormulaContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean formula_sempred(FormulaContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20(\4\2\t\2\4\3\t"+
		"\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\26"+
		"\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\3\3"+
		"\3\3\3\2\3\2\4\2\4\2\4\3\2\f\r\3\2\16\17\2.\2\25\3\2\2\2\4%\3\2\2\2\6"+
		"\7\b\2\1\2\7\b\7\3\2\2\b\26\5\2\2\f\t\n\7\4\2\2\n\26\5\2\2\13\13\f\7\5"+
		"\2\2\f\26\5\2\2\n\r\16\7\6\2\2\16\26\5\2\2\t\17\26\5\4\3\2\20\26\7\13"+
		"\2\2\21\22\7\t\2\2\22\23\5\2\2\2\23\24\7\n\2\2\24\26\3\2\2\2\25\6\3\2"+
		"\2\2\25\t\3\2\2\2\25\13\3\2\2\2\25\r\3\2\2\2\25\17\3\2\2\2\25\20\3\2\2"+
		"\2\25\21\3\2\2\2\26\"\3\2\2\2\27\30\f\b\2\2\30\31\t\2\2\2\31!\5\2\2\t"+
		"\32\33\f\7\2\2\33\34\7\7\2\2\34!\5\2\2\b\35\36\f\6\2\2\36\37\7\b\2\2\37"+
		"!\5\2\2\7 \27\3\2\2\2 \32\3\2\2\2 \35\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#"+
		"\3\2\2\2#\3\3\2\2\2$\"\3\2\2\2%&\t\3\2\2&\5\3\2\2\2\5\25 \"";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}