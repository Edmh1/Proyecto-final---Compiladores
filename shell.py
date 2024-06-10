from backend.lexer import *
from backend.parser import *

# Ejemplo de uso
data = '''
SIGMA x <- 5 $
REAL z <- 4.8 $
ALPHA ( x+1 < 15):
    ELEVATE VERUM $
BETA:
    ELEVATE FALSUM $
$
'''

# Ejecución del lexer y parser
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(data)
print(result)
##print(interpreter.visit(result))