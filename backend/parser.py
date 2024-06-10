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

# Diccionario de variables
variables = {}

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
                 | return_statement END_LINE
                 | break_statement END_LINE
                 | comment
                 '''
    p[0] = p[1]

def p_expression(p):
    '''expression : binary_expression
                  | unitary_expression
                  | primary_expression
                  '''
    p[0] = p[1]

def p_binary_expression(p):
    '''binary_expression : expression PLUS_OP expression
                         | expression MINUS_OP expression
                         | expression MUL_OP expression
                         | expression DIV_OP expression
                         | expression LESS_OP expression
                         | expression GREATER_OP expression
                         | expression LESS_EQUAL_OP expression
                         | expression GREATER_EQUAL_OP expression
                         | expression EQUAL_OP expression
                         | expression DIFFERENT_OP expression
                         | expression LOGICAL_OP_AND expression
                         | expression LOGICAL_OP_OR expression'''
    left_value = p[1]['result']
    right_value = p[3]['result']
    if p[2] == '+':
        result = left_value + right_value
    elif p[2] == '-':
        result = left_value - right_value
    elif p[2] == '*':
        result = left_value * right_value
    elif p[2] == '/':
        result = left_value / right_value
    elif p[2] == '<':
        result = left_value < right_value
    elif p[2] == '>':
        result = left_value > right_value
    elif p[2] == '<=':
        result = left_value <= right_value
    elif p[2] == '>=':
        result = left_value >= right_value
    elif p[2] == '==':
        result = left_value == right_value
    elif p[2] == '!=':
        result = left_value != right_value
    elif p[2] == 'MOGGED':
        result = left_value and right_value
    elif p[2] == 'GOD':
        result = left_value or right_value

    p[0] = {'type': 'binary_expression', 'operator': p[2], 'left': p[1], 'right': p[3], 'result': result}

def p_unitary_expression(p):
    '''unitary_expression : MINUS_OP expression
                          | LOGICAL_OP_NOT expression'''
    if p[1] == '-':
        result = -p[2]['result']
    elif p[1] == 'FAKE':
        result = not p[2]['result']
    p[0] = {'type': 'unitary_expression', 'operator': p[1], 'operand': p[2], 'result': result}

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
    if isinstance(p[1], int) or isinstance(p[1], float):
        p[0] = {'type': 'term', 'result': p[1]}
    elif isinstance(p[1], str) and p[1] in variables:
        p[0] = {'type': 'term', 'result': variables[p[1]]}
    elif p[1] == 'VERUM':
        p[0] = {'type': 'term', 'result': True}
    elif p[1] == 'FALSUM':
        p[0] = {'type': 'term', 'result': False}
    elif p[1] == 'NIHIL':
        p[0] = {'type': 'term', 'result': None}
    else:
        p[0] = {'type': 'term', 'result': p[1]}

def p_assignment(p):
    '''assignment : VARIABLE ASSIGNMENT_OP expression'''
    variables[p[1]] = p[3]['result']
    p[0] = {'type': 'assignment', 'variable': p[1], 'value': p[3]['result']}

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
        data_type = p[1]
        value = p[2]['value']
        variable = p[2]['variable']

        if data_type == 'SIGMA' and isinstance(value, int):
            pass
        elif data_type == 'REAL' and isinstance(value, float):
            pass
        elif data_type == 'STATUS' and value in ['VERUM', 'FALSUM']:
            pass
        elif data_type == 'CHAD' and isinstance(value, str) and len(value) == 1:
            pass
        elif data_type == 'GIGACHAD' and isinstance(value, str):
            pass
        else:
            typeError(p)

        variables[variable] = value
        p[0] = {'type': 'declaration', 'data_type': data_type, 'variable': variable, 'value': value}
    else:
        variables[p[2]] = None
        p[0] = {'type': 'declaration', 'data_type': p[1], 'variable': p[2]}

def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list 
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list'''
    if len(p) == 7:
        if p[3]['result']:
            for stmt in p[6]:
                execute_statement(stmt)
        p[0] = {'type': 'conditional', 'condition': p[3], 'if_body': p[6]}
    else:
        if p[3]['result']:
            for stmt in p[6]:
                execute_statement(stmt)
        else:
            for stmt in p[9]:
                execute_statement(stmt)
        p[0] = {'type': 'conditional', 'condition': p[3], 'if_body': p[6], 'else_body': p[9]}

def p_loop(p):
    '''loop : LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list 
            | LOOP2 LPAREN assignment SEPARATION expression SEPARATION assignment RPAREN STRUCTURE_BODY statement_list'''
    if p[1] == 'ALPHA_LOOP':
        while p[3]['result']:
            for stmt in p[6]:
                execute_statement(stmt)
        p[0] = {'type': 'while_loop', 'condition': p[3], 'body': p[6]}
    else:
        initialization = p[3]['result']
        condition = p[5]['result']
        increment = p[7]['result']
        while condition:
            for stmt in p[10]:
                execute_statement(stmt)
            execute_statement(increment)
        p[0] = {'type': 'for_loop', 'initialization': p[3], 'condition': p[5], 'increment': p[7], 'body': p[10]}

def p_return_statement(p):
    '''return_statement : RETURN expression
                        | RETURN'''
    if len(p) == 3:
        p[0] = {'type': 'return', 'value': p[2]['result']}
    else:
        p[0] = {'type': 'return', 'value': None}

def p_break_statement(p):
    '''break_statement : BREAK'''
    p[0] = {'type': 'break'}

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = {'type': 'comment', 'value': p[1]}

def p_syntax_error(p):
    raise SyntaxError(f"Syntax error at '{p.value}' in '{p.lineno}'")

def typeError(p):
    raise TypeError(f"Type mismatch: expected {p[1]} but got {p[2]['value']}")

# Construcción del parser
parser = yacc.yacc()

def execute_statement(statement):
    if statement['type'] == 'assignment':
        variables[statement['variable']] = statement['value']
    elif statement['type'] == 'declaration':
        variables[statement['variable']] = statement['value']
    elif statement['type'] == 'conditional':
        if 'if_body' in statement:
            for stmt in statement['if_body']:
                execute_statement(stmt)
        elif 'else_body' in statement:
            for stmt in statement['else_body']:
                execute_statement(stmt)
    elif statement['type'] == 'loop':
        if 'while_loop' == statement['type']:
            while statement['condition']['result']:
                for stmt in statement['body']:
                    execute_statement(stmt)
        elif 'for_loop' == statement['type']:
            initialization = statement['initialization']
            condition = statement['condition']
            increment = statement['increment']
            while condition['result']:
                for stmt in statement['body']:
                    execute_statement(stmt)
                execute_statement(increment)
