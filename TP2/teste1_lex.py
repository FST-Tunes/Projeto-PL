import ply.lex as lex

literals = ['(', ')']
tokens = ['START']

def t_START(t):
    r'start'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()