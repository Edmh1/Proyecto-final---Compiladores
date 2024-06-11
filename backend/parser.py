import ply.lex as lex
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
                 | print_statement END_LINE
                 | conditional END_LINE
                 | loop END_LINE
                 | comment
                 | error
                 '''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : VARIABLE ASSIGNMENT_OP expression'''
    variables[p[1]] = p[3]['result']
    p[0] = {'type': 'assignment', 'variable': p[1], 'value': p[3]}

def p_declaration(p):
    '''declaration : type VARIABLE ASSIGNMENT_OP expression
                   | type VARIABLE'''
    
    if len(p) == 5:
        data_type = p[1]['value']
        var_name = p[2]
        value = p[4]['result']
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
            raise TypeError(f"Type mismatch: expected {p[1]} but got {p[4]['result']}")
        variables[var_name] = value
        p[0] = {'type': 'declaration', 'variable': var_name, 'data_type': data_type, 'value': p[4]}

    else:
        data_type = p[1]['value']
        var_name = p[2]
        value = None
        variables[var_name] = value
        p[0] = {'type': 'declaration', 'variable': var_name, 'data_type': data_type, 'value': None}
    
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
    p[0] = {
        'type': 'binary_expression',
        'left': p[1],
        'operator': p[2],
        'right': p[3],
        'result': evaluate_binary_expression(p[1]['result'], p[2], p[3]['result'])
    }

def evaluate_binary_expression(left, operator, right):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        return left / right
    elif operator == '<':
        return left < right
    elif operator == '>':
        return left > right
    elif operator == '<=':
        return left <= right
    elif operator == '>=':
        return left >= right
    elif operator == '==':
        return left == right
    elif operator == '!=':
        return left != right
    elif operator == 'MOGGED':
        return left and right
    elif operator == 'GOD':
        return left or right
    else:
        raise ValueError(f"Unknown operator: {operator}")

def p_unitary_expression(p):
    '''unitary_expression : MINUS_OP expression
                          | LOGICAL_OP_NOT expression'''
    if p[1] == '-':
        result = -p[2]['result']
    elif p[1] == 'FAKE':
        result = not p[2]['result']
    p[0] = {'type': 'unitary_expression', 'result': result}

def p_primary_expression(p):
    '''primary_expression : VARIABLE
                          | NUMBER_INTEGER
                          | NUMBER_FLOAT
                          | TRUE
                          | FALSE
                          | NULL
                          | TEXT_CHAR
                          | TEXT_STRING
                          '''
    if isinstance(p[1], str):
        if p[1] in variables:
            p[0] = {'type': 'term', 'result': variables[p[1]]}
        else:
            p[0] = {'type': 'term', 'result': p[1]}
    else:
        p[0] = {'type': 'term', 'result': p[1]}


def p_print_statement(p):
    '''print_statement : PRINT_DECLARATION LPAREN expression RPAREN'''
    p[0] = {'type': 'sigma_speak', 'value': p[3]}

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = {}

def p_empty(p):
    '''empty : '''
    pass

def p_type(p):
    '''type : TYPE_INTEGER
            | TYPE_FLOAT
            | TYPE_BOOLEAN
            | TYPE_CHAR
            | TYPE_STRING'''
    p[0] = {'type': 'type_value',
            'value': p[1]}

def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list'''
    if len(p) == 10:
        p[0] = {
            'type': 'conditional',
            'condition': p[3],
            'if_body': p[6],
            'else_body': p[9]
        }
    else:
        p[0] = {
            'type': 'conditional',
            'condition': p[3],
            'if_body': p[6]
        }

def p_loop(p):
    '''loop : LOOP STRUCTURE_BODY statement_list UNTIL LPAREN expression RPAREN'''
    p[0] = {
        'type': 'loop',
        'condition': p[6],
        'body': p[3]
    }

def p_error(p):
    if p:
        error_token = lex.LexToken()
        error_token.type = 'ERROR'
        error_token.value = f"Syntax error at '{p.value}', line '{p.lineno}'"
        error_token.lineno = p.lineno
    else:
        error_token = lex.LexToken()
        error_token.type = 'ERROR'
        error_token.value = "Syntax error at EOF"
    return error_token

# Crear el parser
parser = yacc.yacc()

#Evalua
def evaluate_statement(statement):
    global variables
    if statement['type'] == 'assignment':
        variables[statement['variable']] = statement['value']
    elif statement['type'] == 'declaration':
        variables[statement['variable']] = statement['value']
    elif statement['type'] == 'sigma_speak':
        print(statement['value']['result'])
    elif statement['type'] == 'conditional':
        condition = statement['condition']['result']
        if condition:
            for stmt in statement['if_body']:
                evaluate_statement(stmt)
        elif 'else_body' in statement:
            for stmt in statement['else_body']:
                evaluate_statement(stmt)
    elif statement['type'] == 'loop':
        while not statement['condition']['result']:
            for stmt in statement['body']:
                evaluate_statement(stmt)
    else:
        raise ValueError(f"Unknown statement type: {statement['type']}")

#Mostrar ATS
def show_parser(code):
    return parser.parse(code)

