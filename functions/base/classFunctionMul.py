from .classFunction import Function
from ..classConstant import Constant


class FunctionMul(Function):
    def __init__(self, fct1:Function, fct2:Function) -> None:
        self.fct1 = fct1
        self.fct2 = fct2

    @staticmethod
    def multiply(lhs:Function, rhs:Function) -> Function:
        if lhs == 0 or rhs == 0:
            return Constant(0)
        elif lhs == 1:
            return rhs
        elif rhs == 1:
            return lhs
        else:
            return FunctionMul(lhs, rhs)
    
    def __call__(self, x:float) -> float:
        return self.fct1(x) * self.fct2(x)
    
    def derivative(self) -> Function:
        return self.fct1.derivative() * self.fct2 + self.fct1 * self.fct2.derivative()
    
    def __str__(self) -> str:
        return f"{self.fct1} * {self.fct2}"
