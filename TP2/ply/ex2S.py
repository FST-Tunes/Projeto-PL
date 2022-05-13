import os
from ex2L import tokens,literals
from .ply import yacc

# Pasta -> '[' id Lista ']'
# 
# Lista -> Lista Pasta
#       -> Lista Ficheiro
#       -> Empty
#
# Ficheiro -> '(' nome path ')'


def p_z(p):
    "Z : Pasta"

def p_Pasta(p):
    "Pasta : '[' id Lista ']'"
    os.mkdir(p[2])
    for i in p.parser.itens:
        continuar...

def p_Lista_Pasta(p):
    "Lista : Lista Pasta"


def p_Lista_Ficheiro(p):
    "Lista : Lista Ficheiro"

def p_Lista(p):
    "Lista : "

def p_Ficheiro(p):
    "Ficheiro : '(' id id ')'"
    p.parser.items.append(p[2])



def p_error(p):
    print('erro sintatico: ', p)
    parser.success = False

parser = yacc.yacc()

# Variaveis de estado
parser.items = {}


import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print('frase valida: ', linha) 
    else:
        print('frase invalida....')




