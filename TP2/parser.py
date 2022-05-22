import re
import ply.yacc as yacc
from lexer import tokens, literals 

def p_Program(p):
    "Program : IgnoreEnter '%' '%' LEX NL Lex '%' '%' YACC NL Yacc '%' '%' NL Main"
    if 'tokens' not in parser.lex:
        parser.success = False
        print("Error: Lista de Tokens por defenir")
        exit(1)

    for i in parser.vars.keys():
        if type(parser.vars[i]) == bool and parser.vars[i]:
            print("Warning: Token " + i + " por defenir")
        if type(parser.vars[i]) != bool and parser.vars[i] == 0:
            parser.success = False
            print("Error: " + i + " por defenir")
            exit(1)

    if 'errorLex' not in parser.vars:
        print("Warning: O caso de erro para o Lexer nao esta definido")

    if 'errorYacc' not in parser.vars:
        print("Warning: O caso de erro para o Yacc nao esta definido")

    parser.yacc = p[11] + "\n\n" + rmCom(p[15])



def p_IgnoreEnter_enter(p):
    "IgnoreEnter : NL"

def p_IgnoreEnter_nothing(p):
    "IgnoreEnter : "




def p_Lex(p):
    "Lex : Dec Def"
    parser.lex['def'] = p[2]

def p_Dec_Multiple(p):
    "Dec : Dec '%' Dec2"

def p_Dec_Single(p):
    "Dec : '%' Dec2"

def p_Dec2_Tokens(p):
    "Dec2 : TOKENS '=' '[' Items ']' NL"
    if 'tokens' in parser.lex:
        parser.success = False
        print("Error: Variavel tokens ja defenida")
        exit(1)
    else:
        appendList(p[4], True)
        parser.lex['tokens'] = "tokens = " + "[" + p[4] + "]"

def p_Dec2_Literals_list(p):
    "Dec2 : LITERALS '=' '[' Items ']' NL"
    if 'literals' in parser.lex:
        parser.success = False
        print("Error: Variavel literals ja defenida")
        exit(1)
    else:
        appendList(p[4], False)
        parser.lex['literals'] = "literals = " + "[" + p[4] + "]"

def p_Dec2_Literals_str(p):
    "Dec2 : LITERALS '=' STRING NL"
    if 'literals' in parser.lex:
        parser.success = False
        print("Error: Variavel literals ja defenida")
        exit(1)
    else:
        m = re.findall(r'([^\\"\']|\\[\\\"a-z])', p[3])
        appendList(str(m)[1:][:-1], False)
        parser.lex['literals'] = "literals = " + str(m)

def p_Dec2_Ignore(p):
    "Dec2 : IGNORE '=' STRING NL"
    if 'ignore' in parser.lex:
        parser.success = False
        print("Error: Variavel ignore ja defenida")
        exit(1)
    else:
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
        print("Error: Token " + funcName + " nao existe nesta desta gramatica")
        exit(1)

def p_Def2_error(p):
    "Def2 : '.' ID '(' String ',' Func ')' NL"
    if 'errorLex' in parser.vars:
        parser.success = False
        print("Error: Função de erro do lexer apenas pode ser defenida uma unica vez")
        exit(1)
    else:
        parser.vars['errorLex'] = False
        p[0] = "def t_error(t):\n    print(" + p[4] + ")\n    " + p[6]

def p_String_list(p):
    "String : String OP String2"
    if p[2] != '+':
        parser.success = False
    p[0] = p[1] + " + " + p[3]

def p_String_single(p):
    "String : STRING"
    p[0] = p[1]

def p_String2_func(p):
    "String2 : Func"
    p[0] = p[1]

def p_String2_str(p):
    "String2 : STRING"
    p[0] = p[1]

def p_Func_id(p):
    "Func : ID Exp"
    p[0] = p[1] + p[2]

def p_Func_num(p):
    "Func : NUM"
    p[0] = p[1]

def p_Func_str(p):
    "Func : String"
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
    "Yacc : Vars Inst"
    p[0] = p[2] + "\n\n\nparser = yacc.yacc()" + p[1]

def p_Vars_list(p):
    "Vars : Vars Vars2 "
    p[0] = p[1] + p[2]

def p_Vars_empty(p):
    "Vars : "
    p[0] = ""

def p_Vars2(p):
    "Vars2 : '%' ID '=' Vars3 NL"
    p[0] = "\nparser." + p[2] + " = " + p[4]

def p_Vars3_dic(p):
    "Vars3 : '{' Vars4 '}'"
    p[0] = "{" + p[2] + "}"

def p_Vars3_list(p):
    "Vars3 : '[' Vars4 ']'"
    p[0] = "[" + p[2] + "]"

def p_Vars3_func(p):
    "Vars3 : Func"
    if p[1] == "":
        parser.success = False
    p[0] = p[1]

def p_Vars4_multLine(p):
    "Vars4 : NL Main"
    p[0] = p[1] + p[2]

def p_Vars4_singleLine(p):
    "Vars4 : Main"
    p[0] = p[1]

def p_Inst_list(p):
    "Inst : Inst Inst2"
    p[0] = p[1] + "\n\n" + p[2]

def p_Inst_single(p):
    "Inst : Inst2"
    p[0] = p[1]

def p_Inst2_rule(p):
    "Inst2 : ID ':' Logic Inst3"
    numb = 1
    if p[1] in parser.vars:
        if type(parser.vars[p[1]]) == int:
            numb = 1 + parser.vars[p[1]]
        else:
            parser.success = False
            print("Error: Variavel " + p[1] + " nao e valida")
            exit(1)
    parser.vars[p[1]] = numb
    p[0] = "def p_" + p[1] + "_" + str(numb) + "(p):\n    \"" + p[1] + " :" + p[3] + "\"" + p[4]

def p_Inst2_error(p):
    "Inst2 : '.' Inst3"
    if 'errorYacc' in parser.vars:
        parser.success = False
        print("Error: Função de erro do parser apenas pode ser defenida uma unica vez")
        exit(1)
    else:
        parser.vars['errorYacc'] = False
        p[0] = "def p_error(p):" + p[2]

def p_Inst3_returnF(p):
    "Inst3 : '{' IgnoreEnter Main '}' NL"
    p[0] = "\n    " + rmCom(p[3])

def p_Inst3_nothing(p):
    "Inst3 : NL"
    p[0] = ""

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



def rmCom(str):
    r = re.sub(r'\#.*',"",str)
    return r

def appendList(str, content):
    if content:
        g = re.findall(r'(?:\')([^\']+)(?:\')', str)
        for i in g:
            if i not in parser.vars:
                parser.vars[i] = True
            else:
                parser.success = False
                print("Error: Token " + i + " duplicado")
                exit(1)
    else:
        g = re.findall(r'(\'[^\']+\')', str)
        for i in g:
            if i not in parser.vars:
                parser.vars[i] = False
            else:
                parser.success = False
                print("Error: Literal " + i + " duplicado")
                exit(1)


def writeFile(filename):
    
    lexContent = "import ply.lex as lex\n"

    if 'literals' in parser.lex:
        lexContent += "\n" + parser.lex['literals']

    lexContent += "\n" + parser.lex['tokens'] + "\n"
    if 'def' in parser.lex:
        lexContent += "\n" + parser.lex['def']

    if 'ignore' in parser.lex:
        lexContent += "\n\n" + parser.lex['ignore']

    lexContent += "\n\nlexer = lex.lex()"
    
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
parser.success = True


# Read line from input and parse it
import sys

if sys.argv[1] == "-r":
    run = True
    filename = sys.argv[2]
else:
    run = False
    filename = sys.argv[1]


try:
    file = open(filename, "r", encoding="utf-8")
except FileNotFoundError:
    print("ERRO! Ficheiro nao existe")
    exit(1)

content = file.read() + "\n"
parser.parse(content)

if parser.success:
    writeFile(filename[:-5])
    if run: 
        import os
        r = "python3.8 " + filename[:-5] + "_yacc.py"
        os.system(r)
else:
    print("Programa com erros... Corrija e tente novamente!")