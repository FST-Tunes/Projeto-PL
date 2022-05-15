import ply.lex as lex

tokens = ['INT', 'STR', 'f_INPUT', 'PRINT', 'id', 'str', 'DECLARATIONS', 'STATEMENTS']
literals = ['(', ')', '=', ',']

def t_DECLARATIONS(t):
    r'declarations'
    return t

def t_STATEMENTS(t):
    r'statements'
    return t

def t_INT(t):
    r'int'
    return t

def t_STR(t):
    r'str'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_f_INPUT(t):
    r'input'
    return t

def t_str(t):
    r'\"[^"]\"'
    return t

def t_id(t):
    r'[a-zA-Z_]\w*'
    return t

def t_error(t):
    print("Caracter ilegal: " + t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()