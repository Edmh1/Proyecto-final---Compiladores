from backend.lexer import *

# Prueba del lexer
data = '''
REAL var <- 3 + 4 * 5$
ALPHA_LOOP (a < b) :
    COMMAND print(@Hello@)$ #hello there#
$
'''
lexer.input(data)
for tok in lexer:
    print(tok)
