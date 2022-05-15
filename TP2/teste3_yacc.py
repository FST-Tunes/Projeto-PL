import re
import ply.yacc as yacc
from teste3_lex import tokens, literals

def p_Program_1(p):
    "Program : DECLARATIONS Declarations STATEMENTS Statements"

def p_Declarations_1(p):
    "Declarations : Declarations Declaration"

def p_Declarations_2(p):
    "Declarations :"

def p_Declaration_1(p):
    "Declaration : Type IdList"

def p_Type_1(p):
    "Type : INT"

def p_Type_2(p):
    "Type : STR"

def p_IdList_1(p):
    "IdList : id"

def p_IdList_2(p):
    "IdList : IdList ',' id"

def p_Statements_1(p):
    "Statements : Statements Statement"

def p_Statements_2(p):
    "Statements : Statement"

def p_Statement_1(p):
    "Statement : Atrib"

def p_Statement_2(p):
    "Statement : Print"

def p_Print_1(p):
    "Print : PRINT '(' PrintArgs ')'"

def p_PrintArgs_1(p):
    "PrintArgs : PrintArgs ',' Arg"

def p_PrintArgs_2(p):
    "PrintArgs : Arg"

def p_Arg_1(p):
    "Arg : str"

def p_Arg_2(p):
    "Arg : Exp"

def p_Atrib_1(p):
    "Atrib : id '=' Exp"

def p_Exp_1(p):
    "Exp : INT '(' Exp ')'"

def p_Exp_2(p):
    "Exp : f_INPUT '(' str ')'"

def p_Exp_3(p):
    "Exp : id"

def p_error(p):
    print('Erro Sintático: ', p)
    parser.success = False


parser = yacc.yacc()


import sys
parser.success = True
program = sys.stdin.read()
parser.parse(program)
if parser.success:
    print("Programa Válido")
else:
    print("Programa Inválido... Corrija e tente novamente")