import numpy as np

from .base.classFunction import Function


class FunctionExp(Function):
    def __init__(self, fct: Function) -> None:
        self.fct = fct
    
    def __call__(self, x: float) -> float:
        return np.exp(self.fct(x))
    
    def derivative(self) -> Function:
        return self.fct.derivative() * FunctionExp(self.fct)
    
    def __str__(self) -> str:
        return f"exp({self.fct})"