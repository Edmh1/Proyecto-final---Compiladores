import ply.lex as lex
import ply.yacc as yacc

# Tokens list
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
    'CONDITIONAL',
    'LOOP',
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

# Precedence rules
precedence = (
    ('left', 'LOGICAL_OP_OR'),
    ('left', 'LOGICAL_OP_AND'),
    ('left', 'EQUAL_OP', 'DIFFERENT_OP'),
    ('left', 'LESS_OP', 'LESS_EQUAL_OP', 'GREATER_OP', 'GREATER_EQUAL_OP'),
    ('left', 'PLUS_OP', 'MINUS_OP'),
    ('left', 'MUL_OP', 'DIV_OP'),
    ('right', 'LOGICAL_OP_NOT'),
)

# Grammar rules
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression_statement
                 | declaration_statement
                 | control_structure'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : expression END_LINE'''
    p[0] = ('expression_statement', p[1])

def p_declaration_statement(p):
    '''declaration_statement : VARIABLE ASSIGNMENT_OP expression END_LINE'''
    p[0] = ('declaration_statement', p[1], p[3])

def p_expression(p):
    '''expression : arithmetic_expression
                  | boolean_expression
                  | variable
                  | function_call'''
    p[0] = p[1]

def p_arithmetic_expression(p):
    '''arithmetic_expression : arithmetic_expression PLUS_OP arithmetic_expression
                             | arithmetic_expression MINUS_OP arithmetic_expression
                             | arithmetic_expression MUL_OP arithmetic_expression
                             | arithmetic_expression DIV_OP arithmetic_expression
                             | factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('arithmetic_expression', p[2], p[1], p[3])

def p_boolean_expression(p):
    '''boolean_expression : boolean_expression LOGICAL_OP_AND boolean_expression
                          | boolean_expression LOGICAL_OP_OR boolean_expression
                          | LOGICAL_OP_NOT boolean_expression
                          | comparison'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('not', p[2])
    else:
        p[0] = ('boolean_expression', p[2], p[1], p[3])

def p_comparison(p):
    '''comparison : expression LESS_OP expression
                  | expression GREATER_OP expression
                  | expression LESS_EQUAL_OP expression
                  | expression GREATER_EQUAL_OP expression
                  | expression EQUAL_OP expression
                  | expression DIFFERENT_OP expression'''
    p[0] = ('comparison', p[2], p[1], p[3])

def p_control_structure(p):
    '''control_structure : conditional
                         | loop
                         | BREAK END_LINE
                         | RETURN expression END_LINE'''
    if len(p) == 3:
        p[0] = ('break',)
    elif len(p) == 4:
        p[0] = ('return', p[2])
    else:
        p[0] = p[1]

def p_conditional(p):
    '''conditional : CONDITIONAL LPAREN expression RPAREN STRUCTURE_BODY statement_list END_LINE'''
    p[0] = ('conditional', p[3], p[6])

def p_loop(p):
    '''loop : LOOP LPAREN expression RPAREN STRUCTURE_BODY statement_list END_LINE'''
    p[0] = ('loop', p[3], p[6])

def p_function_call(p):
    '''function_call : FUNCTION_DECLARATION LPAREN argument_list RPAREN'''
    p[0] = ('function_call', p[1], p[3])

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list SEPARATION expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_factor(p):
    '''factor : NUMBER_INTEGER
              | NUMBER_FLOAT
              | TEXT_STRING
              | TEXT_CHAR
              | TRUE
              | FALSE
              | NULL'''
    p[0] = p[1]

def p_variable(p):
    '''variable : VARIABLE'''
    p[0] = ('variable', p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construir el lexer y el parser
lexer = lex.lex()
parser = yacc.yacc()

# Prueba del parser
data = '''
COMMAND print(@Hello@);
a <- 3 + 4 * 5;
ALPHA (a < b) {
    COMMAND print(@World@);
}
'''

# Analizar la entrada
lexer.input(data)
result = parser.parse(data, lexer=lexer)
print(result)
