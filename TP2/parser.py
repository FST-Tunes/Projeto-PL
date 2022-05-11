import ply.yacc as yacc

from lexer import tokens

def p_lang(p):
    "lang : '%''%' LEX Lex '%''%' YACC Yacc"

def p_Lex(p):
    "Lex : Dec Def"

def p_Dec_Multiple(p):
    "Dec : Dec Dec2"

def p_Dec_Single(p):
    "Dec : '%' Dec2"

def p_Dec2_Tokens(p):
    "Dec2 : TOKENS '=' Tokens"

def p_Dec2_Literals(p):
    "Dec2 : LITERALS '=' String"

def p_Dec2_Ignore(p):
    "Dec2 : IGNORE '=' String"

def p_Tokens(p):
    "Tokens : '[' Tokens2 ']'"

def p_Tokens2(p):
    "Tokens2 : Tokens2 ',' Tokens3"

def p_Tokens3(p):
    "Tokens3 : ID "

def p_String(p):
    "String : STRING"


def p_error(p):
    print("Syntax error!")
    p.parser.error = True


parser = yacc.yacc()
parser.symtab = {}
parser.symcount = 0
parser.error = False

parser.ifcount = 0

import sys

filename = sys.argv[1]

f = open(filename, 'r')
content = f.read()

result = parser.parse(content)
print(result)

f.close()
