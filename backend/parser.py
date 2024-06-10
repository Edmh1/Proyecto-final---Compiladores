import ply.yacc as yacc
from .lexer import tokens

# Precedencia de operadores
precedence = (
    ('left', 'LOGICAL_OP_OR'),
    ('left', 'LOGICAL_OP_AND'),
    ('right', 'LOGICAL_OP_NOT'),
    ('left', 'LESS_OP', 'LESS_EQUAL_OP', 'GREATER_OP', 'GREATER_EQUAL_OP', 'EQUAL_OP', 'DIFFERENT_OP'),
    ('left', 'PLUS_OP', 'MINUS_OP'),
    ('left', 'MUL_OP', 'DIV_OP'),
    ('nonassoc', 'LPAREN', 'RPAREN'),
)

# Definición de la gramática
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

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
                 | conditional END_LINE
                 | loop END_LINE
                 | function_declaration END_LINE
                 | return_statement END_LINE
                 | break_statement END_LINE
                 | comment'''
    p[0] = p[1]

def p_expression(p):
    '''expression : binary_expression
                  | unitary_expression
                  | primary_expression'''
    p[0] = p[1]

def p_binary_expression(p):
    '''binary_expression : primary_expression PLUS_OP primary_expression
                         | primary_expression MINUS_OP primary_expression
                         | primary_expression MUL_OP primary_expression
                         | primary_expression DIV_OP primary_expression'''
    p[0] = {
        'type': 'binary_expression',
        'operator': p[2],
        'left': p[1],
        'right': p[3],
        'result': eval(f"{p[1]['value']} {p[2]} {p[3]['value']}")
    }

def p_unitary_expression(p):
    '''unitary_expression : MINUS_OP primary_expression'''
    p[0] = {
        'type': 'unitary_expression',
        'operator': p[1],
        'operand': p[2],
        'result': -p[2]['value']
    }

def p_primary_expression(p):
    '''primary_expression : LPAREN expression RPAREN
                          | term'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : NUMBER_INTEGER
            | NUMBER_FLOAT
            | VARIABLE
            | TRUE
            | FALSE
            | NULL
            | TEXT_STRING
            | TEXT_CHAR'''
    p[0] = {
        'type': 'term',
        'value': p[1]
    }

def p_assignment(p):
    '''assignment : VARIABLE ASSIGNMENT_OP expression'''
    p[0] = {
        'type': 'assignment',
        'variable': p[1],
        'value': p[3]
    }

def p_declaration(p):
    '''declaration : TYPE_BOOLEAN VARIABLE 
                   | TYPE_STRING VARIABLE
                   | TYPE_CHAR VARIABLE
                   | TYPE_INTEGER VARIABLE
                   | TYPE_FLOAT VARIABLE
                   | TYPE_BOOLEAN assignment
                   | TYPE_STRING assignment
                   | TYPE_CHAR assignment
                   | TYPE_INTEGER assignment
                   | TYPE_FLOAT assignment'''
    if isinstance(p[2], dict) and p[2]['type'] == 'assignment':
        p[0] = {
            'type': 'declaration',
            'data_type': p[1],
            'variable': p[2]['variable'],
            'value': p[2]['value']
        }
    else:
        p[0] = {
            'type': 'declaration',
            'data_type': p[1],
            'variable': p[2]
        }

def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list'''
    if len(p) == 7:
        p[0] = {
            'type': 'conditional',
            'condition': p[3],
            'if_body': p[6]
        }
    else:
        p[0] = {
            'type': 'conditional',
            'condition': p[3],
            'if_body': p[6],
            'else_body': p[9]
        }

def p_loop(p):
    '''loop : LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list
            | LOOP2 LPAREN expression SEPARATION expression SEPARATION expression RPAREN STRUCTURE_BODY statement_list'''
    if p[1] == 'ALPHA_LOOP':
        p[0] = {
            'type': 'while_loop',
            'condition': p[3],
            'body': p[6]
        }
    else:
        p[0] = {
            'type': 'for_loop',
            'initialization': p[3],
            'condition': p[5],
            'increment': p[7],
            'body': p[10]
        }

def p_function_declaration(p):
    '''function_declaration : FUNCTION_DECLARATION VARIABLE LPAREN RPAREN STRUCTURE_BODY statement_list'''
    p[0] = {
        'type': 'function_declaration',
        'name': p[2],
        'body': p[6]
    }

def p_return_statement(p):
    '''return_statement : RETURN expression
                        | RETURN'''
    if len(p) == 3:
        p[0] = {
            'type': 'return_statement',
            'value': p[2]
        }
    else:
        p[0] = {
            'type': 'return_statement',
            'value': None
        }

def p_break_statement(p):
    '''break_statement : BREAK'''
    p[0] = {
        'type': 'break_statement'
    }

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = {
        'type': 'comment',
        'value': p[1]
    }

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construcción del parser
parser = yacc.yacc()
