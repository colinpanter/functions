from .classFunction import Function


class FunctionLinear(Function):
    def __init__(self, fct, *, a=1, b=0) -> None:
        self.fct = fct
        self.a = a
        self.b = b
    
    def __call__(self, x: float) -> float:
        return self.a * self.fct(x) + self.b