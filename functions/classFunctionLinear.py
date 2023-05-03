from .base.classFunction import Function


class FunctionLinear(Function):
    def __init__(self, fct:Function, *, a:float=1, b:float=0) -> None:
        self.fct = fct
        self.a = a
        self.b = b
    
    def __call__(self, x: float) -> float:
        return self.a * self.fct(x) + self.b
    
    def derivative(self) -> Function:
        return FunctionLinear(self.fct.derivative(), a=self.a)
    
    def __str__(self) -> str:
        return f"{self.a}*{self.fct} + {self.b}"