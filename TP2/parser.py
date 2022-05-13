import ply.yacc as yacc
from lexer import tokens, literals 

def p_Program(p):
    "Program : '%' '%' LEX Lex '%' '%' YACC Yacc"

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

def p_Def2_return(p):
    "Def2 : REGEX RETURN '(' P ID P ','  ')'"

def p_Def2_error(p):
    "Def2 : '.' ERROR '(' ')'"

def p_Def_list(p):
    "Def : Def Def2"

def p_Def_single(p):
    "Def : Def2"




def p_Yacc(p):
    "Yacc : "



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