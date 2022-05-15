import re
import ply.yacc as yacc
from lexer import tokens, literals 

def p_Program(p):
    "Program : '%' '%' LEX Lex '%' '%' YACC Yacc '%' '%' Main"

def p_Lex(p):
    "Lex : Dec Def"
    print(p[1] + "\n\n\n" + p[2])

def p_Dec_Multiple(p):
    "Dec : Dec '%' Dec2"
    p[0] = p[3] + "\n" + p[1] 

def p_Dec_Single(p):
    "Dec : '%' Dec2"
    p[0] = p[2]

def p_Dec2_Tokens(p):
    "Dec2 : TOKENS '=' '[' Items ']'"
    p[0] = "tokens = " + "[" + p[4] + "]"

def p_Dec2_Literals_list(p):
    "Dec2 : LITERALS '=' '[' Items ']'"
    p[0] = "literals = " + "[" + p[4] + "]"

def p_Dec2_Literals_str(p):
    "Dec2 : LITERALS '=' STRING"
    m = re.findall(r'([^\\"\']|\\[\\\"a-z])', p[3])
    p[0] = "literals = " + str(m)

def p_Dec2_Ignore(p):
    "Dec2 : IGNORE '=' STRING"
    p[0] = "t_ignore = " + p[3]

def p_Items_list(p):
    "Items : Items ',' Items2"
    p[0] = p[1] + ", " + p[3]

def p_Items_single(p):
    "Items : Items2"
    p[0] = p[1]

def p_Items2(p):
    "Items2 : VALUE "
    p[0] = p[1]

def p_Def_list(p):
    "Def : Def Def2"
    p[0] = p[1] + "\n\n" + p[2]

def p_Def_single(p):
    "Def : Def2"
    p[0] = p[1]

def p_Def2_newDef(p):
    "Def2 : REGEX ID '(' VALUE ',' Func ')'"
    funcName = re.match(r'(?:\')(.+)(?:\')',p[4])
    p[0] = "def p_" + funcName.group(1) + "(p):\n    " + p[1] + "\n    " + "---FUNC---" # p[5])

def p_Def2_error(p):
    "Def2 : '.' ID '(' STRING ',' Func ')'"
    p[0] = "def p_error(p):\n    print(" + p[4] + ")\n    " + "---FUNC---" # p[5])

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

def p_Exp2_round(p):
    "Exp2 : '(' Args ')'"

def p_Exp2_square(p):
    "Exp2 : '[' Args ']'"

def p_Exp2_curly(p):
    "Exp2 : '{' Args '}'"

def p_Args_list(p):
    "Args : Args ',' Func"

def p_Args_single(p):
    "Args : Func"

def p_Args_empty(p):
    "Args : "






def p_Yacc(p):
    "Yacc : Inst"

def p_Inst_list(p):
    "Inst : Inst Inst2"

def p_Inst_single(p):
    "Inst : Inst2"

def p_Inst2(p):
    "Inst2 : ID ':' Logic '{' Main '}'"

def p_Logic_list(p):
    "Logic : Logic Logic2"

def p_Logic_empty(p):
    "Logic : "

def p_Logic2_id(p):
    "Logic2 : ID"

def p_Logic2_value(p):
    "Logic2 : VALUE"







def p_Main_list(p):
    "Main : Main Main2"

def p_Main_empty(p):
    "Main : "

def p_Main2_round(p):
    "Main2 : '(' Main ')'"
    
def p_Main2_square(p):
    "Main2 : '[' Main ']'"
    
def p_Main2_curly(p):
    "Main2 : '{' Main '}'"

def p_Main2_funcDef(p):
    "Main2 : ':'"

def p_Main2_op(p):
    "Main2 : OP"

def p_Main2_attrib(p):
    "Main2 : '='"

def p_Main2_coma(p):
    "Main2 : ','"

def p_Main2_p(p):
    "Main2 : VALUE"

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