import ply.yacc as yacc
from lexer import tokens, literals 

def p_Program(p):
    "Program : '%' '%' LEX Lex '%' '%' YACC '%' '%' Main"

def p_Lex(p):
    "Lex : Dec Def"

def p_Dec_Multiple(p):
    "Dec : Dec '%' Dec2"

def p_Dec_Single(p):
    "Dec : '%' Dec2"

def p_Dec2_Tokens(p):
    "Dec2 : TOKENS '=' '[' Items ']'"

def p_Dec2_Literals_list(p):
    "Dec2 : LITERALS '=' '[' Items ']'"

def p_Dec2_Literals_str(p):
    "Dec2 : LITERALS '=' String"

def p_Dec2_Ignore(p):
    "Dec2 : IGNORE '=' String"

def p_Items_list(p):
    "Items : Items ',' Items2"

def p_Items_single(p):
    "Items : Items2"

def p_Items2(p):
    "Items2 : P ID P "

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

def p_Main_empty(p):
    "Main : "

def p_Main2_par(p):
    "Main2 : '(' Main ')'"
    
def p_Main2_ret(p):
    "Main2 : '[' Main ']'"
    
def p_Main2_chav(p):
    "Main2 : '{' Main '}'"

def p_Main2_funcDef(p):
    "Main2 : ':'"

def p_Main2_attrib(p):
    "Main2 : '='"

def p_Main2_coma(p):
    "Main2 : ','"

def p_Main2_p(p):
    "Main2 : P"

def p_Main2_id(p):
    "Main2 : ID"

def p_Main2_num(p):
    "Main2 : NUM"

def p_Main2_exp(p):
    "Main2 : '.'"

def p_Main2_str(p):
    "Main2 : STRING"






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
print("\n---------------------   CONTENT  ---------------------\n")
print(content)
print("\n---------------------   TOKENS   ---------------------\n")

codigo = parser.parse(content)

print("\n---------------------   OUTPUT   ---------------------\n")


if parser.success:
    print("Programa estruturalmente correto!")
    print(codigo)
else:
    print("Programa com erros... Corrija e tente novamente!")