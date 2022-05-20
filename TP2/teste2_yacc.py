import re
import ply.yacc as yacc
from teste2_lex import tokens, literals

def p_exp_1(p):
    "exp : exp '+' fas"
    p[0] = p[1] + p[3]

def p_stat_1(p):
    "stat : VAR '=' exp"
    ts[p[1]] = p[3]
    print("eu comi uma batata")
    if 1 == y.b:
        y.a += y.c


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

def p_error(t):
    print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")



def getval(n):
    if n not in ts:
        print(f"Undefined name '{n}'")
        y.a += y.b
    return ts.get(n, 0)

ts = {}
y = yacc.yacc()
y.a = 1
y.b = 1
y.c = 2
y.parse("3+4*7")
