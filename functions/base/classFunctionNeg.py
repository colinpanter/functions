from .classFunction import Function


class FunctionNeg(Function):
    def __init__(self, fct) -> None:
        self.fct = fct
    
    def __call__(self, x: float) -> float:
        return -self.fct(x)
    
    def derivative(self):
        return FunctionNeg(self.fct1.derivative())
    
    def __str__(self):
        return f"-{str(self.fct)}"
