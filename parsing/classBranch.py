from functions import Function, FunctionExp

from .classTree import Tree


FCTS = {
    'exp': FunctionExp
}


class Branch(Tree):
    def __init__(self, fct:str, content:Tree):
        self.fct = fct
        self.content = content
    
    @staticmethod
    def parse(equation:str):
        raise NotImplementedError
    
    def convert(self) -> Function:
        return FCTS[self.fct](self.content.convert())
    
    def __str__(self) -> str:
        return f"{self.fct}({self.content})"
