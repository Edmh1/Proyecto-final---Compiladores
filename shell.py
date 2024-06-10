from backend.lexer import *
from backend.parser import *

# Ejemplo de uso
data = '''
ELEVATE 1+2$
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