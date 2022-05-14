import ply.lex as lex

tokens = ["ID", "LEX", "YACC", "TOKENS", "IGNORE", "LITERALS", "STRING", "REGEX", "NUM", "P"] 
literals = ['=', '"', '[', ']', ',', '{', '}', ':', '%', '.', '(', ')']

def t_LEX(t):
    r'LEX'
    print(t)
    return t

def t_YACC(t):
    r'YACC'
    print(t)
    return t

def t_TOKENS(t):
    r'tokens'
    print(t)
    return t

def t_IGNORE(t):
    r'ignore'
    print(t)
    return t

def t_LITERALS(t):
    r'literals'
    print(t)
    return t

def t_P(t):
    r'\''
    print(t)
    return t

def t_STRING(t):
    r'f?\"[^"]*\"'
    print(t)
    return t

def t_REGEX(t):
    r'r\'[^\']+\''
    print(t)
    return t

def t_ID(t):
    r'[A-Za-z_]\w*'
    print(t)
    return t

def t_NUM(t):
    r'\d+'
    print(t)
    return t

t_ignore = " \n\t"

def t_error(t):
    print("Illegal character: " + t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()