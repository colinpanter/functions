from .classFunction import Function


class FunctionMul(Function):
    def __init__(self, fct1, fct2) -> None:
        self.fct1 = fct1
        self.fct2 = fct2
    
    def __call__(self, x: float) -> float:
        return self.fct1(x) * self.fct2(x)
    
    def derivative(self):
        return self.fct1.derivative() * self.fct2 + self.fct1 * self.fct2.derivative()
