grammar LTLformular;

formula
    : '!' formula                           # not_formula
    | 'G' formula                           # always_formula
    | 'F' formula                           # eventually_formula
    | 'X' formula                           # next_formula
    | formula op = (AndOp | OrOp) formula   # logic_formula
    | formula '->' formula                  # implication_formula
    | formula 'U' formula                   # until_formula
    | logicConstant                         # logic_const
    | Identifier                            # atomic_proposition
    | '(' formula ')'                       # formula_in_parentheses
    ;

logicConstant:
    True_op | False_op
    ;

Identifier
    : [a-z]
    ;

AndOp
    : '/\\'
    ;

OrOp
    : '\\/'
    ;

True_op:
    'true'
    ;

False_op:
    'false'
    ;

WS : [ \t\n\r]+ -> skip ;