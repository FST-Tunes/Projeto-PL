import ply.yacc as yacc
from lexer import tokens, literals 

def p_Program(p):
    "Program : '%' '%' LEX Lex '%' '%' YACC Yacc '%' '%' Main"

def p_Lex(p):
    "Lex : Dec Def"

def p_Dec_Multiple(p):
    "Dec : Dec '%' Dec2"

def p_Dec_Single(p):
    "Dec : '%' Dec2"

def p_Dec2_Tokens(p):
    "Dec2 : TOKENS '=' '[' Tokens ']'"

def p_Dec2_Literals(p):
    "Dec2 : LITERALS '=' String"

def p_Dec2_Ignore(p):
    "Dec2 : IGNORE '=' String"

def p_Tokens_list(p):
    "Tokens : Tokens ',' Tokens2"

def p_Tokens_single(p):
    "Tokens : Tokens2"

def p_Tokens2(p):
    "Tokens2 : P ID P "

def p_String(p):
    "String : STRING"

def p_Def_list(p):
    "Def : Def Def2"

def p_Def_single(p):
    "Def : Def2"

def p_Def2_newDef(p):
    "Def2 : REGEX ID '(' P ID P ',' Func ')'"

def p_Def2_error(p):
    "Def2 : '.' ID '(' STRING ',' Func ')'"


def p_Func_id(p):
    "Func : ID Exp"

def p_Func_num(p):
    "Func : NUM"

def p_Exp_list(p):
    "Exp : Exp Exp2"

def p_Exp_empty(p):
    "Exp : "

def p_Exp2_id(p):
    "Exp2 : '.' ID"

def p_Exp2_par(p):
    "Exp2 : '(' Args ')'"

def p_Args_list(p):
    "Args : Args ',' Func"

def p_Args_single(p):
    "Args : Func"

def p_Args_empty(p):
    "Args : "






def p_Yacc(p):
    "Yacc : "

def p_Main_list(p):
    "Main : Main Main2"

def p_Main_single(p):
    "Main : Main2"

def p_Main2(p):
    "Main2 : "



def p_error(p):
    print('Erro sintatico: ', p)
    parser.success = False




# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
import sys
parser.success = True

filename = sys.argv[1]

f = open(filename, 'r')
content = f.read()
print(content)

codigo = parser.parse(content)


if parser.success:
    print("Programa estruturalmente correto!")
    print(codigo)
else:
    print("Programa com erros... Corrija e tente novamente!")