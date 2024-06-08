import ply.lex as lex

# Lista de tokens
tokens = [
    'NUMBER_INTEGER',
    'NUMBER_FLOAT',
    'TEXT_STRING',
    'TEXT_CHAR',
    'VARIABLE',
    'PLUS_OP',
    'MINUS_OP',
    'MUL_OP',
    'DIV_OP',
    'TYPE_BOOLEAN',
    'TYPE_STRING',
    'TYPE_CHAR',
    'TYPE_INTEGER',
    'TYPE_FLOAT',
    'CONDITIONAL1',
    'CONDITIONAL2',
    'LOOP1',
    'LOOP2',
    'BREAK',
    'RETURN',
    'LOGICAL_OP_NOT',
    'LOGICAL_OP_AND',
    'LOGICAL_OP_OR',
    'TRUE',
    'FALSE',
    'NULL',
    'FUNCTION_DECLARATION',
    'ASSIGNMENT_OP',
    'LESS_OP',
    'GREATER_OP',
    'LESS_EQUAL_OP',
    'GREATER_EQUAL_OP',
    'EQUAL_OP',
    'DIFFERENT_OP',
    'LPAREN',
    'RPAREN',
    'SEPARATION',
    'STRUCTURE_BODY',
    'COMMENT',
    'END_LINE'
]

# Ignorar caracteres como espacios, tabulaciones y enters
t_ignore = ' \t'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definiciones de tokens
t_PLUS_OP = r'\+'
t_MINUS_OP = r'-'
t_MUL_OP = r'\*'
t_DIV_OP = r'/'
t_ASSIGNMENT_OP = r'<-'
t_LESS_OP = r'<'
t_LESS_EQUAL_OP = r'<='
t_GREATER_OP = r'>'
t_GREATER_EQUAL_OP = r'>='
t_EQUAL_OP = r'=='
t_DIFFERENT_OP = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEPARATION = r';'
t_STRUCTURE_BODY = r':'
t_END_LINE = r'\$'

# Tipos de datos
def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_NUMBER_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_TEXT_STRING(t):
    r'@[^@]+@'
    t.value = t.value[1:-1]
    return t
def t_TEXT_CHAR(t):
    r'@[^@]{1}@'
    t.value = t.value[1:-1]
    return t
def t_VARIABLE(t):
    r'[a-z][a-z0-9]*'
    return t

# Tipos de variables
def t_TYPE_BOOLEAN(t):
    r'STATUS'
    return t
def t_TYPE_STRING(t):
    r'GIGACHAD'
    return t
def t_TYPE_CHAR(t):
    r'CHAD'
    return t
def t_TYPE_INTEGER(t):
    r'SIGMA'
    return t
def t_TYPE_FLOAT(t):
    r'REAL'
    return t

# Estructuras de control
def t_LOOP1(t):
    r'ALPHA_LOOP'
    return t
def t_LOOP2(t):
    r'BETA_LOOP'
    return t
def t_CONDITIONAL1(t):
    r'ALPHA'
    return t
def t_CONDITIONAL2(t):
    r'BETA'
    return t
def t_BREAK(t):
    r'BYEBYE'
    return t
def t_RETURN(t):
    r'ELEVATE'
    return t

# Operadores lógicos
def t_LOGICAL_OP_NOT(t):
    r'FAKE'
    return t
def t_LOGICAL_OP_AND(t):
    r'MOGGED'
    return t
def t_LOGICAL_OP_OR(t):
    r'GOD'
    return t

# Valores especiales
def t_TRUE(t):
    r'VERUM'
    return t
def t_FALSE(t):
    r'FALSUM'
    return t
def t_NULL(t):
    r'NIHIL'
    return t

# Funciones
def t_FUNCTION_DECLARATION(t):
    r'COMMAND'
    return t

def t_COMMENT(t):
    r'\#[^#]+\#'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
