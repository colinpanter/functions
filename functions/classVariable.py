from .base.classFunction import Function


class Variable(Function):
    def __init__(self) -> None:
        pass
    
    def __call__(self, x: float) -> float:
        return x
    
    def derivative(self) -> Function:
        from .classConstant import Constant
        return Constant(1)
    
    def __str__(self) -> str:
        return "x"
