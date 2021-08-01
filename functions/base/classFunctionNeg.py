from .classFunction import Function


class FunctionNeg(Function):
    def __init__(self, fct1) -> None:
        self.fct1 = fct1
    
    def __call__(self, x: float) -> float:
        return -self.fct1(x)
    
    def derivative(self):
        return FunctionNeg(self.fct1.derivative())
