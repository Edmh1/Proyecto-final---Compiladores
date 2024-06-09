import ply.yacc as yacc
from .lexer import tokens

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"

class Statement(ASTNode):
    pass

class Expression(ASTNode):
    pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"

class BinaryOp(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left}, {self.op}, {self.right})"

class UnaryOp(Expression):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def __repr__(self):
        return f"UnaryOp({self.op}, {self.expr})"

class Assignment(Statement):
    def __init__(self, variable, expr):
        self.variable = variable
        self.expr = expr

    def __repr__(self):
        return f"Assignment({self.variable}, {self.expr})"

class Declaration(Statement):
    def __init__(self, var_type, variable):
        self.var_type = var_type
        self.variable = variable

    def __repr__(self):
        return f"Declaration({self.var_type}, {self.variable})"

class Conditional(Statement):
    def __init__(self, condition, true_body, false_body=None):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body

    def __repr__(self):
        return f"Conditional({self.condition}, {self.true_body}, {self.false_body})"

class Loop(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"Loop({self.condition}, {self.body})"

class FunctionDeclaration(Statement):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __repr__(self):
        return f"FunctionDeclaration({self.name}, {self.body})"

class Return(Statement):
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f"Return({self.value})"

class Break(Statement):
    def __repr__(self):
        return "Break()"

class Comment(Statement):
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f"Comment({self.content})"

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
    '''expression : logical_or_expression'''
    p[0] = p[1]

def p_logical_or_expression(p):
    '''logical_or_expression : logical_or_expression LOGICAL_OP_OR logical_and_expression
                             | logical_and_expression'''
    if len(p) == 4:
        p[0] = BinaryOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_logical_and_expression(p):
    '''logical_and_expression : logical_and_expression LOGICAL_OP_AND equality_expression
                              | equality_expression'''
    if len(p) == 4:
        p[0] = BinaryOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_equality_expression(p):
    '''equality_expression : equality_expression EQUAL_OP relational_expression
                           | equality_expression DIFFERENT_OP relational_expression
                           | relational_expression'''
    if len(p) == 4:
        p[0] = BinaryOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_relational_expression(p):
    '''relational_expression : relational_expression LESS_OP additive_expression
                             | relational_expression LESS_EQUAL_OP additive_expression
                             | relational_expression GREATER_OP additive_expression
                             | relational_expression GREATER_EQUAL_OP additive_expression
                             | additive_expression'''
    if len(p) == 4:
        p[0] = BinaryOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_additive_expression(p):
    '''additive_expression : additive_expression PLUS_OP multiplicative_expression
                           | additive_expression MINUS_OP multiplicative_expression
                           | multiplicative_expression'''
    if len(p) == 4:
        p[0] = BinaryOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_multiplicative_expression(p):
    '''multiplicative_expression : multiplicative_expression MUL_OP unary_expression
                                 | multiplicative_expression DIV_OP unary_expression
                                 | unary_expression'''
    if len(p) == 4:
        p[0] = BinaryOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_unary_expression(p):
    '''unary_expression : LOGICAL_OP_NOT unary_expression
                        | primary_expression'''
    if len(p) == 3:
        p[0] = UnaryOp(p[1], p[2])
    else:
        p[0] = p[1]

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

