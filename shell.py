from backend.lexer import *
from backend.parser import *

# Ejemplo de uso
data = '''
SIGMA x <- 10$
ALPHA(x < 20):
    x <- x + 1$
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

