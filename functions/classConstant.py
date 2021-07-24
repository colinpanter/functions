from .base.classFunction import Function


class Constant(Function):
    def __init__(self, constant) -> None:
        self.constant = constant
    
    def __call__(self, x: float) -> float:
        return self.constant
    
    def derivative(self):
        return Constant(0)