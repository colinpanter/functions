from .classFunction import Function


class FunctionAdd(Function):
    def __init__(self, fct1:Function, fct2:Function) -> None:
        self.fct1 = fct1
        self.fct2 = fct2

    @staticmethod
    def add(lhs:Function, rhs:Function) -> Function:
        if lhs == 0:
            return rhs
        elif rhs == 0:
            return lhs
        else:
            return FunctionAdd(lhs, rhs)
    
    def __call__(self, x: float) -> float:
        return self.fct1(x) + self.fct2(x)
    
    def derivative(self) -> Function:
        return self.fct1.derivative() + self.fct2.derivative()
    
    def __str__(self) -> str:
        return f"{self.fct1} + {self.fct2}"
