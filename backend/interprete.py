from .parser import *

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def visit(self, node):
        if isinstance(node, list):
            return self.visit_list(node)
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{node.__class__.__name__} method')

    def visit_list(self, nodes):
        for node in nodes:
            result = self.visit(node)
            if result is not None:  # If a return statement is found, propagate it
                return result

    def visit_Program(self, node):
        return self.visit(node.statements)

    def visit_Number(self, node):
        return node.value

    def visit_Variable(self, node):
        return self.variables.get(node.name, None)

    def visit_BinaryOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.op
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '<':
            return left < right
        elif op == '<=':
            return left <= right
        elif op == '>':
            return left > right
        elif op == '>=':
            return left >= right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == 'MOGGED':
            return left and right
        elif op == 'GOD':
            return left or right
        elif op == 'FAKE':
            return not self.visit(node.right)

    def visit_Assignment(self, node):
        value = self.visit(node.expr)
        self.variables[node.variable.name] = value

    def visit_Declaration(self, node):
        if isinstance(node.variable, Assignment):
            self.visit(node.variable)
        else:
            self.variables[node.variable.name] = None

    def visit_Conditional(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.visit(node.true_body)
        elif node.false_body:
            return self.visit(node.false_body)

    def visit_Loop(self, node):
        while self.visit(node.condition):
            result = self.visit(node.body)
            if result is not None:
                return result

    def visit_FunctionDeclaration(self, node):
        self.functions[node.name] = node

    def visit_Return(self, node):
        if node.value is not None:
            return self.visit(node.value)
        else:
            return None

    #def visit_Break(self, node):
     #   raise BreakException()

    def visit_Comment(self, node):
        pass


interpreter = Interpreter()

