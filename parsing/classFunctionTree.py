class FunctionTree:
    def __init__(self, rhs, lhs, operation):
        self.rhs = rhs
        self.lhs = lhs
        self.operation = operation

    @staticmethod
    def parse(string):
        # Check if there are operations in the string
        op = None
        
        # The parsing is over if there is no operations left
        if op is None:
            return string

        # Split the string in two (left side and right side of the operation)
        rhs_str = ""
        lhs_str = ""

        # Parse both halves
        rhs = FunctionTree.parse(rhs_str)
        lhs = FunctionTree.parse(lhs_str)

        return FunctionTree(rhs, lhs, op)
