from lib2to3.pgen2 import literals
from tkinter.tix import TCL_WINDOW_EVENTS
from .ply import lex

literals = ['[',']','(',')']
tokens = ['id']

t_FIM = r'[a-zA-Z]\w*'
t_id = r'\"[^"]+\"'

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


