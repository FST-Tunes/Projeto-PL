import re
import ply.yacc as yacc
from lexer import tokens, literals 

def p_Program(p):
    "Program : '%' '%' LEX NL Lex '%' '%' YACC NL Yacc '%' '%' NL Main"
    for i in parser.vars.keys():
        if type(parser.vars[i]) == bool and parser.vars[i]:
            print("Warning: Token " + i + " por defenir")
        if type(parser.vars[i]) != bool and parser.vars[i] == 0:
            parser.success = False
            print("Error: Variavel " + i + " por defenir")
            exit(1)

    parser.yacc = p[10] + "\n\n" + p[14]

def p_Lex(p):
    "Lex : Dec Def"
    parser.lex['def'] = p[2]

def p_Dec_Multiple(p):
    "Dec : Dec '%' Dec2"

def p_Dec_Single(p):
    "Dec : '%' Dec2"

def p_Dec2_Tokens(p):
    "Dec2 : TOKENS '=' '[' Items ']' NL"
    appendList(p[4], True)
    parser.lex['tokens'] = "tokens = " + "[" + p[4] + "]"

def p_Dec2_Literals_list(p):
    "Dec2 : LITERALS '=' '[' Items ']' NL"
    appendList(p[4], False)
    parser.lex['literals'] = "literals = " + "[" + p[4] + "]"

def p_Dec2_Literals_str(p):
    "Dec2 : LITERALS '=' STRING NL"
    m = re.findall(r'([^\\"\']|\\[\\\"a-z])', p[3])
    appendList(str(m)[1:][:-1], False)
    parser.lex['literals'] = "literals = " + str(m)

def p_Dec2_Ignore(p):
    "Dec2 : IGNORE '=' STRING NL"
    parser.lex['ignore'] = "t_ignore = " + p[3]

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
    "Def2 : REGEX ID '(' VALUE ',' Func ')' NL"
    funcName = re.match(r'(?:\')(.+)(?:\')',p[4]).group(1)
    if funcName in parser.vars.keys():
        if parser.vars[funcName]:
            parser.vars[funcName] = False
            p[0] = "def t_" + funcName + "(t):\n    " + p[1]
            if p[6] == "pass":
                p[0] += "\n    pass"
            elif p[6] != "":
                p[0] += "\n    t.value = " + p[6] + "\n    return t"
            else:
                p[0] += "\n    return t"
        else:
            parser.success = False
            print("Error: Token " + funcName + " nao pode ser redefenido")
            exit(1)
    else:
        parser.success = False
        print("Error: Token " + funcName + " nao e Token desta gramatica")
        exit(1)

def p_Def2_error(p):
    "Def2 : '.' ID '(' String ',' Func ')' NL"
    p[0] = "def t_error(t):\n    print(" + p[4] + ")\n    " + p[6]

def p_String_str(p):
    "String : STRING"
    p[0] = p[1]

def p_String_args(p):
    "String : '(' StrArgs ')'"
    p[0] = p[2]

def p_StrArgs_list(p):
    "StrArgs : StrArgs OP StrArgs2"
    p[0] = p[1] + " + " + p[3]

def p_StrArgs_single(p):
    "StrArgs : StrArgs2"
    p[0] = p[1]

def p_StrArgs2_func(p):
    "StrArgs2 : Func"
    p[0] = p[1]

def p_StrArgs2_str(p):
    "StrArgs2 : STRING"
    p[0] = p[1]

def p_Func_id(p):
    "Func : ID Exp"
    p[0] = p[1] + p[2]

def p_Func_num(p):
    "Func : NUM"
    p[0] = p[1]

def p_Func_empty(p):
    "Func : "
    p[0] = ""

def p_Exp_list(p):
    "Exp : Exp Exp2"
    p[0] = p[1] + p[2]

def p_Exp_empty(p):
    "Exp : "
    p[0] = ""

def p_Exp2_id(p):
    "Exp2 : '.' ID"
    p[0] = "." + p[2]

def p_Exp2_round(p):
    "Exp2 : '(' Args ')'"
    p[0] = "(" + p[2] + ")"

def p_Exp2_square(p):
    "Exp2 : '[' Args ']'"
    p[0] = "[" + p[2] + "]"

def p_Exp2_curly(p):
    "Exp2 : '{' Args '}'"
    p[0] = "{" + p[2] + "}"

def p_Args_list(p):
    "Args : Args ',' Func"
    p[0] = p[1] + ", " + p[3]

def p_Args_single(p):
    "Args : Func"
    p[0] = p[1]

def p_Args_empty(p):
    "Args : "
    p[0] = ""






def p_Yacc(p):
    "Yacc : Inst"
    p[0] = p[1]

def p_Inst_list(p):
    "Inst : Inst Inst2"
    p[0] = p[1] + "\n\n" + p[2]

def p_Inst_single(p):
    "Inst : Inst2"
    p[0] = p[1]

def p_Inst2(p):
    "Inst2 : ID ':' Logic Inst3"
    numb = 1
    if p[1] in parser.vars:
        p1 = parser.vars[p[1]]
        if type(p1) == int:
            numb = 1 + p1
        else:
            parser.success = False
            print("Error: Variavel " + p[1] + " nao e valida")
            exit(1)
    parser.vars[p[1]] = numb
    p[0] = "def p_" + p[1] + "_" + str(numb) + "(p):\n    \"" + p[1] + " :" + p[3] + "\"" + p[4]

def p_Inst3_returnF(p):
    "Inst3 : '{' Return '}' NL"
    p[0] = "\n    " + p[2]

def p_Inst3_nothing(p):
    "Inst3 : NL"
    p[0] = ""

def p_Return_multLine(p):
    "Return : NL Main"
    p[0] = p[2]

def p_Return_singleLine(p):
    "Return : Main"
    p[0] = p[1]

def p_Logic_list(p):
    "Logic : Logic Logic2"
    p[0] = p[1] + " " + p[2]

def p_Logic_empty(p):
    "Logic : "
    p[0] = ""

def p_Logic2_id(p):
    "Logic2 : ID"
    if p[1] not in parser.vars:
        parser.vars[p[1]] = 0
    p[0] = p[1]

def p_Logic2_value(p):
    "Logic2 : VALUE"
    if p[1] not in parser.vars:
        parser.success = False
        print("Error: Literal " + p[1] + " nao faz parte desta gramatica")
        exit(1)
    else:
        p[0] = p[1]






def p_Main_list(p):
    "Main : Main Main2"
    p[0] = p[1] + p[2]

def p_Main_empty(p):
    "Main : "
    p[0] = ""

def p_Main2_nl(p):
    "Main2 : NL"
    p[0] = p[1]
    
def p_Main2_round(p):
    "Main2 : '(' Main ')'"
    p[0] = "(" + p[2] + ")"
    
def p_Main2_square(p):
    "Main2 : '[' Main ']'"
    p[0] = "[" + p[2] + "]"
    
def p_Main2_curly(p):
    "Main2 : '{' Main '}'"
    p[0] = "{" + p[2] + "}"

def p_Main2_funcDef(p):
    "Main2 : ':'"
    p[0] = p[1]

def p_Main2_op(p):
    "Main2 : OP"
    p[0] = " " + p[1] + " "

def p_Main2_attrib(p):
    "Main2 : '='"
    p[0] = " " + p[1] + " "

def p_Main2_coma(p):
    "Main2 : ','"
    p[0] = p[1] + " "

def p_Main2_p(p):
    "Main2 : VALUE"
    p[0] = p[1]

def p_Main2_id(p):
    "Main2 : MainIdNum"
    p[0] = p[1]

def p_MainIdNum_list(p):
    "MainIdNum : MainIdNum idNum"
    p[0] = p[1] + " " + p[2]

def p_MainIdNum_single(p):
    "MainIdNum : idNum"
    p[0] = p[1]

def p_idNum_num(p):
    "idNum : NUM"
    p[0] = p[1]

def p_idNum_id(p):
    "idNum : ID"
    p[0] = p[1]

def p_Main2_regex(p):
    "Main2 : REGEX"
    p[0] = p[1]

def p_Main2_exp(p):
    "Main2 : '.'"
    p[0] = p[1]

def p_Main2_str(p):
    "Main2 : STRING"
    p[0] = p[1]





def p_error(p):
    print('Erro sintatico: ', p)
    parser.success = False





def appendList(str, content):
    if content:
        g = re.findall(r'(?:\')([^\']+)(?:\')', str)
        for i in g:
            parser.vars[i] = True
    else:
        g = re.findall(r'(\'[^\']+\')', str)
        for i in g:
            parser.vars[i] = False


def writeFile(filename):
    
    lexContent = "import ply.lex as lex\n\n"
    lexContent += parser.lex['tokens'] + "\n" + parser.lex['literals'] + "\n\n"
    lexContent += parser.lex['def'] + "\n\n"
    lexContent += parser.lex['ignore'] + "\n\n"
    lexContent += "lexer = lex.lex()"
    
    newLex = filename + "_lex.py"
    fOutLex = open(newLex, "w", encoding="utf-8")
    fOutLex.write(lexContent)
    fOutLex.close()
    

    yaccContent = "import re\n"
    yaccContent += "import ply.yacc as yacc\n"
    yaccContent += "from " + filename + "_lex import tokens, literals\n\n"
    yaccContent += parser.yacc

    newYacc = filename + "_yacc.py"
    fOutYacc = open(newYacc, "w", encoding="utf-8")
    fOutYacc.write(yaccContent)
    fOutYacc.close()

    return True



# Build the parser
parser = yacc.yacc()
parser.vars = {}
parser.lex = {}
parser.yacc = ""

# Read line from input and parse it
import sys
parser.success = True

filename = sys.argv[1]

try:
    file = open(filename, "r", encoding="utf-8")
except FileNotFoundError:
    print("ERRO! Ficheiro nao existe")
    exit(1)

content = file.read()
parser.parse(content)

if parser.success:
    writeFile(filename[:-5])
else:
    print("Programa com erros... Corrija e tente novamente!")