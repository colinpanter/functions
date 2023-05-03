from .classFunction import Function


class FunctionNeg(Function):
    def __init__(self, fct:Function) -> None:
        self.fct = fct
    
    def __call__(self, x: float) -> float:
        return -self.fct(x)
    
    def derivative(self) -> Function:
        return FunctionNeg(self.fct.derivative())
    
    def __str__(self) -> str:
        return f"-{self.fct}"
