import re
import ply.yacc as yacc
from teste1_lex import tokens, literals

def p_Prog_1(p):
    "Prog : Prog Prog2"
    p[0] = p[1] + "\ngroup " + str(parser.count) + ": " + p[2]
    parser.count += 1


def p_Prog_2(p):
    "Prog :"
    p[0] = ""

def p_Prog2_1(p):
    "Prog2 : '(' Prog3 ')'"
    p[0] = "(" + p[2] + " )"

def p_Prog3_1(p):
    "Prog3 : Prog3 Prog2"
    p[0] = p[1] + " " + p[2]

def p_Prog3_2(p):
    "Prog3 :"
    p[0] = ""

def p_error(p):
    print('Erro Sintático: ', p)
    parser.success = False



parser = yacc.yacc()
parser.count = 0
parser.success = True

import sys
program = sys.stdin.read()
p = parser.parse(program)
if parser.success:
    print("Programa Válido:\n" + p)
else:
    print("Programa Inválido... Corrija e tente novamente")
