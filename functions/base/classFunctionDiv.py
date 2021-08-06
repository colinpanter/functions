from .classFunction import Function


class FunctionDiv(Function):
    def __init__(self, fct1, fct2) -> None:
        self.fct1 = fct1
        self.fct2 = fct2
    
    def __call__(self, x: float) -> float:
        try:
            return self.fct1(x) / self.fct2(x)
        except ZeroDivisionError:
            return 0
    
    def derivative(self):
        return (self.fct1.derivative() * self.fct2 - self.fct1 * self.fct2.derivative()) / (self.fct2 * self.fct2)
    
    def __str__(self):
        return f"{str(self.fct1)} / {str(self.fct2)}"
