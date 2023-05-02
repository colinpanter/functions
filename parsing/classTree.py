from functions import Function


OPS = {
    '^': 1,
    '*': 2,
    '/': 2,
    '+': 3,
    '-': 3
}


class Tree:
    def __init__(self, lhs, rhs, operation):
        self.lhs: Tree = lhs
        self.rhs: Tree = rhs
        self.operation = operation

    @staticmethod
    def parse(equation:str):
        # Remove white spaces
        equation = equation.replace(' ', '')

        # Resolve parenthesese
        while equation[0] == '(' and equation[-1] == ')':
            equation = equation[1:-1]

        # Check if there are operations in the string
        op_pos, val = None, -1
        parentheses = 0
        for i, c in enumerate(equation):
            if c == '(':
                parentheses += 1
            if c == ')':
                parentheses -= 1
            if parentheses == 0 and c in OPS and OPS[c] > val:
                op_pos, val = i, OPS[c]
        
        # The parsing is over if there is no operations left
        if op_pos is None:
            sub_eq = equation.find('(')
            if sub_eq == -1:
                from .classLeaf import Leaf
                return Leaf(equation)
            else:
                from .classBranch import Branch
                return Branch(equation[:sub_eq], Tree.parse(equation[sub_eq:]))

        # Split the string in two (left side and right side of the operation)
        op = equation[op_pos]
        lhs_str = equation[:op_pos]
        rhs_str = equation[op_pos+1:]

        # Parse both halves
        lhs = Tree.parse(lhs_str)
        rhs = Tree.parse(rhs_str)

        return Tree(lhs, rhs, op)

    def convert(self) -> Function:
        l_function = self.lhs.convert()
        r_function = self.rhs.convert()

        match self.operation:
            case '*':
                return l_function * r_function
            case '/':
                return l_function / r_function
            case '+':
                return l_function + r_function
            case '-':
                return l_function - r_function

    def __str__(self) -> str:
        return f"({self.lhs} {self.operation} {self.rhs})"
