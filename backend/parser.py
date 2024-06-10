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
        var_name = p[2]
        value = p[4]['result']
    else:
        data_type = p[1]
        var_name = p[2]
        value = None  # Puede agregar lógica predeterminada para tipos específicos aquí
    
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

    variables[var_name] = value
    p[0] = {'type': 'declaration', 'variable': var_name, 'data_type': data_type, 'value': value}

def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list'''
    if len(p) == 10:
        p[0] = {'type': 'conditional', 'condition': p[3], 'if_body': [stmt for stmt in p[6] if stmt is not None], 'else_body': [stmt for stmt in p[9] if stmt is not None]}
    else:
        p[0] = {'type': 'conditional', 'condition': p[3], 'if_body': [stmt for stmt in p[6] if stmt is not None], 'else_body': []}

def p_loop(p):
    '''loop : LOOP STRUCTURE_BODY statement_list UNTIL LPAREN expression RPAREN'''
    p[0] = {'type': 'loop', 'body': p[3], 'condition': p[6]}

def p_return_statement(p):
    '''return_statement : RETURN expression'''
    raise ReturnStatement(p[2]['result'])

def p_break_statement(p):
    '''break_statement : BREAK'''
    raise BreakStatement()

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = None

def p_empty(p):
    '''empty : '''
    pass

def p_type(p):
    '''type : TYPE_INTEGER
            | TYPE_FLOAT
            | TYPE_BOOLEAN
            | TYPE_CHAR
            | TYPE_STRING'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

def typeError(p):
    raise TypeError(f"Type mismatch: expected {p[1]} but got {p[4]['result']}")

# Crear el parser
parser = yacc.yacc()

# Función para ejecutar el parser
def execute_function(func, local_vars):
    try:
        original_vars = variables.copy()
        variables.update(local_vars)
        for statement in func['body']:
            evaluate_statement(statement)
        return None
    except ReturnStatement as e:
        return e.value
    finally:
        variables.clear()
        variables.update(original_vars)

def evaluate_statement(statement):
    global variables
    if statement['type'] == 'assignment':
        variables[statement['variable']] = statement['value']
    elif statement['type'] == 'declaration':
        variables[statement['variable']] = statement['value']
    elif statement['type'] == 'conditional':
        condition = statement['condition']['result']
        if condition:
            for stmt in statement['if_body']:
                evaluate_statement(stmt)
        elif 'else_body' in statement:
            for stmt in statement['else_body']:
                evaluate_statement(stmt)
    elif statement['type'] == 'loop':
        while not evaluate_expression(statement['condition']):
            try:
                for stmt in statement['body']:
                    evaluate_statement(stmt)
            except BreakStatement:
                break
    elif statement['type'] == 'sigma_speak':
        print(statement['value'])
    elif statement['type'] == 'function_call':
        execute_function(functions[statement['name']], dict(zip([param[1] for param in functions[statement['name']]['params']], statement['arguments'])))
    else:
        raise ValueError(f"Unknown statement type: {statement['type']}")

def evaluate_expression(expression):
    if expression['type'] == 'binary_expression':
        return evaluate_binary_expression(expression['left']['result'], expression['operator'], expression['right']['result'])
    elif expression['type'] == 'unitary_expression':
        if expression['operator'] == '-':
            return -evaluate_expression(expression['expression'])
        elif expression['operator'] == 'FAKE':
            return not evaluate_expression(expression['expression'])
    elif expression['type'] == 'term':
        return expression['result']
    elif expression['type'] == 'function_call':
        return execute_function(functions[expression['name']], dict(zip([param[1] for param in functions[expression['name']]['params']], expression['arguments'])))
    else:
        raise ValueError(f"Unknown expression type: {expression['type']}")

def show_parser(code):
    return parser.parse(code)

# Función principal para ejecutar el parser con el código de entrada
def run_parser(code):
    result = parser.parse(code)
    for statement in result:
        evaluate_statement(statement)
