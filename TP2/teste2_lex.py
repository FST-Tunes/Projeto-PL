import ply.lex as lex

tokens = ['VAR', 'NUMBER']
literals = ['+', '-', '/', '*', '=', '(', ')']

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    pass

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()