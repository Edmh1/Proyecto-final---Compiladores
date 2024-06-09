import ply.yacc as yacc
from .lexer import tokens

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Statement(ASTNode):
    pass

class Expression(ASTNode):
    pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

class Variable(Expression):
    def __init__(self, name):
        self.name = name

class BinaryOp(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(Expression):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class Assignment(Statement):
    def __init__(self, variable, expr):
        self.variable = variable
        self.expr = expr

class Declaration(Statement):
    def __init__(self, var_type, variable):
        self.var_type = var_type
        self.variable = variable

class Conditional(Statement):
    def __init__(self, condition, true_body, false_body=None):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body

class Loop(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class FunctionDeclaration(Statement):
    def __init__(self, name, body):
        self.name = name
        self.body = body

class Return(Statement):
    def __init__(self, value=None):
        self.value = value

class Break(Statement):
    pass

class Comment(Statement):
    def __init__(self, content):
        self.content = content



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
    p[0] = Program(p[1])

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
    elif len(p) == 3:
        p[0] = UnaryOp(p[1], p[2])
    else:
        p[0] = BinaryOp(p[1], p[2], p[3])

def p_term(p):
    '''term : NUMBER_INTEGER
            | NUMBER_FLOAT
            | TEXT_STRING
            | TEXT_CHAR
            | VARIABLE
            | TRUE
            | FALSE
            | NULL'''
    if isinstance(p[1], int) or isinstance(p[1], float):
        p[0] = Number(p[1])
    elif isinstance(p[1], str):
        if p[1] in ('TRUE', 'FALSE', 'NULL'):
            p[0] = Variable(p[1])
        else:
            p[0] = Variable(p[1])

def p_assignment(p):
    '''assignment : VARIABLE ASSIGNMENT_OP expression'''
    p[0] = Assignment(Variable(p[1]), p[3])

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
    if len(p) == 3 and isinstance(p[2], Assignment):
        p[0] = Declaration(p[1], p[2])
    else:
        p[0] = Declaration(p[1], Variable(p[2]))


def p_conditional(p):
    '''conditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list
                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list'''
    if len(p) == 7:
        p[0] = Conditional(p[3], p[6])
    else:
        p[0] = Conditional(p[3], p[6], p[9])

def p_loop(p):
    '''loop : LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list
            | LOOP2 LPAREN expression SEPARATION expression SEPARATION expression RPAREN STRUCTURE_BODY statement_list'''
    if p[1] == 'ALPHA_LOOP':
        p[0] = Loop(p[3], p[6])
    else:
        p[0] = ('loop2', p[3], p[5], p[7], p[10])

def p_function_declaration(p):
    '''function_declaration : FUNCTION_DECLARATION VARIABLE LPAREN RPAREN STRUCTURE_BODY statement_list'''
    p[0] = FunctionDeclaration(p[2], p[6])

def p_return_statement(p):
    '''return_statement : RETURN expression
                        | RETURN'''
    if len(p) == 3:
        p[0] = Return(p[2])
    else:
        p[0] = Return()

def p_break_statement(p):
    '''break_statement : BREAK'''
    p[0] = Break()

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = Comment(p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construcción del parser
parser = yacc.yacc()




