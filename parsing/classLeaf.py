from functions import Function, Variable, Constant

from .classTree import Tree


class Leaf(Tree):
    def __init__(self, content:str):
        self.content = content
    
    @staticmethod
    def parse(equation:str):
        return Leaf(equation)
    
    def convert(self) -> Function:
        if self.content == 'x':
            return Variable()
        else:
            return Constant(float(self.content))
    
    def __str__(self) -> str:
        return self.content
