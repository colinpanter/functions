from .classFunction import Function


class FunctionDiv(Function):
    def __init__(self, fct1:Function, fct2:Function) -> None:
        self.fct1 = fct1
        self.fct2 = fct2
    
    @staticmethod
    def divide(lhs:Function, rhs:Function) -> Function:
        if rhs == 1:
            return lhs
        else:
            return FunctionDiv(lhs, rhs)
    
    def __call__(self, x: float) -> float:
        try:
            return self.fct1(x) / self.fct2(x)
        except ZeroDivisionError:
            return 0
    
    def derivative(self) -> "Function":
        return (self.fct1.derivative() * self.fct2 - self.fct1 * self.fct2.derivative()) / (self.fct2 * self.fct2)
    
    def __str__(self) -> str:
        return f"{self.fct1} / {self.fct2}"
