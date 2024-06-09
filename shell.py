from backend.lexer import *
from backend.parser import *
from backend.interprete import *

# Ejemplo de uso
data = '''
SIGMA x$
x <- 10$
ALPHA_LOOP(x < 20):
    x <- x + 1$
$
x <- x +2$
ELEVATE x$
'''

# Ejecución del lexer y parser
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(data)
print(interpreter.visit(result))