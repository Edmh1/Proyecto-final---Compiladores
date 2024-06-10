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
functions = {}

class ReturnStatement(Exception):
    def __init__(self, value):
        self.value = value

class BreakStatement(Exception):
    pass

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

    # Filtrar declaraciones None
    p[0] = [stmt for stmt in p[0] if stmt is not None]

def p_statement(p):
    '''statement : expression END_LINE
                 | assignment END_LINE
                 | declaration END_LINE
                 | conditional END_LINE
                 | loop END_LINE
                 | return_statement END_LINE
                 | break_statement END_LINE
                 | function_declaration END_LINE
                 | function_call END_LINE
                 | print_statement END_LINE
                 | comment
                 '''
    p[0] = p[1]

def p_function_declaration(p):
    '''function_declaration : type FUNCTION_DECLARATION LPAREN parameter_list RPAREN STRUCTURE_BODY statement_list END_LINE
                            | FUNCTION_DECLARATION LPAREN parameter_list RPAREN STRUCTURE_BODY statement_list END_LINE'''
    if len(p) == 9:
        func_type = p[1]
        func_name = p[2].split()[1]
        func_params = p[4]
        func_body = p[7]
    else:
        func_type = 'void'
        func_name = p[1].split()[1]
        func_params = p[3]
        func_body = p[6]

    functions[func_name] = {'type': func_type, 'params': func_params, 'body': func_body}
    p[0] = {'type': 'function_declaration', 'name': func_name, 'params': func_params, 'body': func_body}

def p_parameter_list(p):
    '''parameter_list : parameter_list SEPARATION parameter
                      | parameter
                      | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_parameter(p):
    '''parameter : type VARIABLE'''
    p[0] = (p[1], p[2])

def p_function_call(p):
    '''function_call : VARIABLE LPAREN argument_list RPAREN'''
    func_name = p[1]
    args = p[3]
    if func_name not in functions:
        raise NameError(f"Function '{func_name}' not defined")
    func = functions[func_name]
    if len(args) != len(func['params']):
        raise TypeError(f"Function '{func_name}' expects {len(func['params'])} arguments, got {len(args)}")
    local_vars = dict(zip([param[1] for param in func['params']], args))
    p[0] = execute_function(func, local_vars)

def p_argument_list(p):
    '''argument_list : argument_list SEPARATION expression
                     | expression
                     | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]['result']]
    elif len(p) == 2:
        p[0] = [p[1]['result']]
    else:
        p[0] = []

def p_print_statement(p):
    '''print_statement : PRINT_DECLARATION LPAREN expression RPAREN'''
    p[0] = {'type': 'sigma_speak', 'value': p[3]['result']}

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
    p[0] = {'type': 'binary_expression', 'result': result}

def p_unitary_expression(p):
    '''unitary_expression : MINUS_OP expression
                          | LOGICAL_OP_NOT expression'''
    if p[1] == '-':
        result = -p[2]['result']
    elif p[1] == 'NOT':
        result = not p[2]['result']
    p[0] = {'type': 'unitary_expression', 'result': result}

def p_primary_expression(p):
    '''primary_expression : VARIABLE
                          | NUMBER_INTEGER
                          | NUMBER_FLOAT
                          | TRUE
                          | FALSE
                          | TEXT_CHAR
                          | TEXT_STRING
                          | function_call'''
    if isinstance(p[1], str):
        if p[1] in variables:
            p[0] = {'type': 'term', 'result': variables[p[1]]}
        else:
            p[0] = {'type': 'term', 'result': p[1]}
    else:
        p[0] = {'type': 'term', 'result': p[1]}

def p_assignment(p):
    '''assignment : VARIABLE ASSIGNMENT_OP expression'''
    variables[p[1]] = p[3]['result']
    p[0] = {'type': 'assignment', 'variable': p[1], 'value': p[3]['result']}

def p_declaration(p):
    '''declaration : type VARIABLE ASSIGNMENT_OP expression
                   | type VARIABLE'''
    
    if len(p) == 5:
        data_type = p[1]
        variable = p[2]
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
            typeError(p)

        variables[variable] = value
        p[0] = {'type': 'declaration', 'data_type': data_type, 'variable': variable, 'value': value}
    else:
        variables[p[2]] = None
        p[0] = {'type': 'declaration', 'data_type': p[2], 'variable': None}

def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list'''
    if len(p) == 7:
        p[0] = {'type': 'conditional', 'condition': p[3], 'if_body': [stmt for stmt in p[6] if stmt is not None]}
    else:
        p[0] = {'type': 'conditional', 'condition': p[3], 'if_body': [stmt for stmt in p[6] if stmt is not None], 'else_body': [stmt for stmt in p[9] if stmt is not None]}

def p_loop(p):
    '''loop : LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list
            | LOOP2 LPAREN assignment SEPARATION expression SEPARATION assignment RPAREN STRUCTURE_BODY statement_list'''
    if p[1] == 'ALPHA_LOOP':
        p[0] = {'type': 'while_loop', 'condition': p[3], 'body': p[6]}
    else:
        p[0] = {'type': 'for_loop', 'initialization': p[3], 'condition': p[5], 'increment': p[7], 'body': p[10]}

def p_return_statement(p):
    '''return_statement : RETURN expression
                        | RETURN'''
    if len(p) == 3:
        p[0] = {'type': 'return', 'value': p[2]['result']}
        raise ReturnStatement(p[2]['result'])
    else:
        p[0] = {'type': 'return', 'value': None}
        raise ReturnStatement(None)

def p_break_statement(p):
    '''break_statement : BREAK'''
    p[0] = {'type': 'break'}
    raise BreakStatement()

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = {'type': 'comment', 'value': p[1]}

def p_type(p):
    '''type : TYPE_INTEGER
            | TYPE_FLOAT
            | TYPE_BOOLEAN
            | TYPE_CHAR
            | TYPE_STRING
            | NULL'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = None

def p_syntax_error(p):
    raise SyntaxError(f"Syntax error at '{p.value}' in '{p.lineno}'")

def typeError(p):
    raise TypeError(f"Type mismatch: expected {p[1]} but got {p[4]['result']}")

################# respuesta final
def evaluate_expression(expression):
    if expression['type'] == 'binary_expression':
        left = evaluate_expression(expression['left'])
        right = evaluate_expression(expression['right'])
        if expression['operator'] == '+':
            return left + right
        elif expression['operator'] == '-':
            return left - right
        elif expression['operator'] == '*':
            return left * right
        elif expression['operator'] == '/':
            return left / right
        elif expression['operator'] == '<':
            return left < right
        elif expression['operator'] == '>':
            return left > right
        elif expression['operator'] == '==':
            return left == right
        elif expression['operator'] == '<=':
            return left <= right
        elif expression['operator'] == '>=':
            return left >= right
        elif expression['operator'] == '!=':
            return left != right
    elif expression['type'] == 'term':
        return expression['result']
    elif expression['type'] == 'variable':
        return variables[expression['name']]
    else:
        raise ValueError(f"Unknown expression type: {expression['type']}")

def execute_statement(stmt):
    if stmt['type'] == 'assignment':
        variables[stmt['variable']] = stmt['value']
    elif stmt['type'] == 'declaration':
        variables[stmt['variable']] = stmt['value']
    elif stmt['type'] == 'sigma_speak':
        print(stmt['value'])
    elif stmt['type'] == 'conditional':
        if stmt['condition']['result']:
            for s in stmt['if_body']:
                execute_statement(s)
        elif 'else_body' in stmt:
            for s in stmt['else_body']:
                execute_statement(s)
    elif stmt['type'] == 'while_loop':
        while evaluate_expression(stmt['condition']):
            for s in stmt['body']:
                execute_statement(s)
            # Re-evaluar la condición del bucle después de cada iteración
            stmt['condition']['result'] = evaluate_expression(stmt['condition'])
    elif stmt['type'] == 'for_loop':
        execute_statement(stmt['initialization'])
        while evaluate_expression(stmt['condition']):
            for s in stmt['body']:
                execute_statement(s)
            execute_statement(stmt['increment'])
            # Re-evaluar la condición del bucle después de cada iteración
            stmt['condition']['result'] = evaluate_expression(stmt['condition'])
    elif stmt['type'] == 'return':
        raise ReturnStatement(stmt['value'])
    elif stmt['type'] == 'break':
        raise BreakStatement()
    elif stmt['type'] == 'function_declaration':
        functions[stmt['name']] = {'params': stmt['params'], 'body': stmt['body']}
    else:
        print(f"Found {stmt} statement!")
        raise ValueError(f"Unknown statement type: {stmt['type']}")

def execute_program(statements):
    for stmt in statements:
        execute_statement(stmt)

def execute_function(func, local_vars):
    global variables
    old_vars = variables
    variables = local_vars
    try:
        for stmt in func['body']:
            execute_statement(stmt)
    except ReturnStatement as r:
        variables = old_vars
        return r.value
    variables = old_vars

# Construcción del parser
parser = yacc.yacc()