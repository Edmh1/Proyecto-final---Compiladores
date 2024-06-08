import ply.yacc as yacc
from .lexer import tokens


# Precedencia de operadores 
precedence = (
    ('left', 'PLUS_OP', 'MINUS_OP'),
    ('left', 'MUL_OP', 'DIV_OP'),
    ('left', 'LESS_OP', 'LESS_EQUAL_OP', 'GREATER_OP', 'GREATER_EQUAL_OP', 'EQUAL_OP', 'DIFFERENT_OP'),
    ('left', 'LOGICAL_OP_AND', 'LOGICAL_OP_OR'),
    ('right', 'LOGICAL_OP_NOT'),
)

# Definición de la gramática

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression END_LINE
                 | assignment END_LINE
                 | declaration END_LINE
                 | conditional
                 | loop
                 | function_declaration
                 | return_statement
                 | break_statement
                 | COMMENT'''
    p[0] = p[1]

def p_expression(p):
    '''expression : term
                  | expression PLUS_OP term
                  | expression MINUS_OP term
                  | expression MUL_OP term
                  | expression DIV_OP term
                  | expression LESS_OP expression
                  | expression LESS_EQUAL_OP expression
                  | expression GREATER_OP expression
                  | expression GREATER_EQUAL_OP expression
                  | expression EQUAL_OP expression
                  | expression DIFFERENT_OP expression
                  | LOGICAL_OP_NOT expression
                  | expression LOGICAL_OP_AND expression
                  | expression LOGICAL_OP_OR expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''term : NUMBER_INTEGER
            | NUMBER_FLOAT
            | TEXT_STRING
            | TEXT_CHAR
            | VARIABLE
            | TRUE
            | FALSE
            | NULL'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : VARIABLE ASSIGNMENT_OP expression'''
    p[0] = ('assign', p[1], p[3])

def p_declaration(p):
    '''declaration : TYPE_BOOLEAN assignment
                   | TYPE_STRING assignment
                   | TYPE_CHAR assignment
                   | TYPE_INTEGER assignment
                   | TYPE_FLOAT assignment
                   | TYPE_BOOLEAN VARIABLE 
                   | TYPE_STRING VARIABLE
                   | TYPE_CHAR VARIABLE
                   | TYPE_INTEGER VARIABLE
                   | TYPE_FLOAT VARIABLE'''
    p[0] = ('declare', p[1], p[2])

def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list END_LINE
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list END_LINE'''
    if len(p) == 8:
        p[0] = ('conditional1', p[3], p[6])
    else:
        p[0] = ('conditional2', p[3], p[6], p[9])

def p_loop(p):
    '''loop : LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list END_LINE
            | LOOP2 LPAREN expression SEPARATION expression SEPARATION expression RPAREN STRUCTURE_BODY statement_list END_LINE'''
    if p[1] == 'LOOP1':
        p[0] = ('loop1', p[3], p[6])
    else:
        p[0] = ('loop2', p[3], p[5], p[7], p[10])


def p_function_declaration(p):
    '''function_declaration : FUNCTION_DECLARATION VARIABLE LPAREN RPAREN STRUCTURE_BODY statement_list END_LINE'''
    p[0] = ('function', p[2], p[6])

def p_return_statement(p):
    '''return_statement : RETURN expression END_LINE
                        | RETURN END_LINE'''
    if len(p) == 4:
        p[0] = ('return', p[2])
    else:
        p[0] = ('return', None)

def p_break_statement(p):
    '''break_statement : BREAK END_LINE'''
    p[0] = 'break'

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construcción del parser
parser = yacc.yacc()




