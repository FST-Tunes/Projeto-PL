import ply.lex as lex

tokens = ['ID', 'LEX', 'YACC', 'TOKENS', 'IGNORE', 'LITERALS', 'STRING', 'REGEX', 'NUM', 'VALUE', 'OP', 'NL'] 
literals = ['=', '"', '[', ']', ',', '{', '}', ':', '%', '.', '(', ')']

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

def t_NL(t):
    r'(\#.+)?\n([ \n]|(\#.+))*'
    return t

def t_OP(t):
    r'((?:\+|-|\*|/|<|>|!)=?)|=='
    return t

def t_VALUE(t):
    r'\'[^\']+\''
    return t

def t_STRING(t):
    r'f?\"[^"]*\"'
    return t

def t_REGEX(t):
    r'r\'[^\']+\''
    return t

def t_ID(t):
    r'[A-Za-z_]\w*'
    return t

def t_NUM(t):
    r'\d+'
    return t

t_ignore = " \t"

def t_error(t):
    print("Illegal character: " + t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()