import re
import ply.yacc as yacc
from teste2_lex import tokens, literals

def p_exp_1(p):
    "exp : exp '+' fas"
    p[0] = p[1] + p[3]

def p_stat_1(p):
    "stat : VAR '=' exp"
    parser.ts[p[1]] = p[3]
    print("eu comi uma batata")
    if 1 == parser.b:
        parser.a += parser.c


def p_stat_2(p):
    "stat : exp"
    print(p[1])

def p_stat_3(p):
    "stat : exp"

def p_exp_2(p):
    "exp : exp '-' exp"
    p[0] = p[1] - p[3]

def p_exp_3(p):
    "exp : exp '*' exp"
    p[0] = p[1] * p[3]

def p_exp_4(p):
    "exp : exp '/' exp"
    p[0] = p[1] / p[3]

def p_fas_1(p):
    "fas : '-' stat"

def p_error(p):
    print(f"Syntax error at '{p.value}', [{p.lexer.lineno}]")


parser = yacc.yacc()
parser.ts = {}
parser.a = 1
parser.b = {
    'asd':14, 
    1:parser.a, 
}
parser.c = ""
parser.d = "aaa" + parser.c

def getval(n):
    if n not in parser.ts:
        print(f"Undefined name '{n}'")
        parser.a += parser.b
    return parser.ts.get(n, 0)

parser.parse("3+4*7")
