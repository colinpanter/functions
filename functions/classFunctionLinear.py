from .base.classFunction import Function


class FunctionLinear(Function):
    def __init__(self, fct, *, a=1, b=0) -> None:
        self.fct = fct
        self.a = a
        self.b = b
    
    def __call__(self, x: float) -> float:
        return self.a * self.fct(x) + self.b
    
    def derivative(self):
        return FunctionLinear(self.fct.derivative(), a=self.a)
    
    def __str__(self):
        return f"{self.a}*{str(self.fct)} + {str(self.b)}"