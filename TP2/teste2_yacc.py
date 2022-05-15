import re
import ply.yacc as yacc
from teste2_lex import tokens, literals

def p_stat_1(p):
    "stat : VAR '=' exp"
    ts[t[1]] = t[3]
    print("eu comi uma batata")
    if a in b:
        a += c


def p_stat_2(p):
    "stat : exp"
    print(t[1])

def p_stat_3(p):
    "stat : exp"

def p_exp_1(p):
    "exp : exp '+' exp"
    t[0] = t[1] + t[3]

def p_exp_2(p):
    "exp : exp '-' exp"
    t[0] = t[1] - t[3]

def p_exp_3(p):
    "exp : exp '*' exp"
    t[0] = t[1] * t[3]

def p_exp_4(p):
    "exp : exp '/' exp"
    t[0] = t[1] / t[3]

def p_error(t):
    print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")

def getval(n):
    if n not in ts:
        print(f"Undefined name '{n}'")
        a += b
    return ts.get(n, 0)

y = yacc()
y.parse("3+4*7")