import ply.lex as lex

tokens = ["ID", "LEX", "YACC", "TOKENS", "IGNORE", "LITERALS", "STRING", "REGEX", "P", "RETURN", "ERROR"] 
literals = ['=', '"', '[', ']', ',', '(', ')', '{', '}', ':', '%', '.']

def t_LEX(t):
    r'LEX'
    return t

def t_YACC(t):
    r'YACC'
    return t

def t_TOKENS(t):
    r'tokens'
    return t

def t_IGNORE(t):
    r'ignore'
    return t

def t_LITERALS(t):
    r'literals'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_ERROR(t):
    r'error'
    return t

def t_P(t):
    r'\''
    return t

def t_STRING(t):
    r'f?\"[^"]*\"'
    return t

def t_REGEX(t):
    r'r\'[^ ]+\''
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

t_ignore = " \n\t"

def t_error(t):
    print("Illegal character: " + t.value[0])

lexer = lex.lex()