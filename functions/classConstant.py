from .base.classFunction import Function


class Constant(Function):
    def __init__(self, constant:float) -> None:
        self.constant = constant
    
    def __call__(self, x: float) -> float:
        return self.constant
    
    def derivative(self) -> Function:
        return Constant(0)
    
    def __str__(self) -> str:
        return f"{self.constant}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Constant):
            return self.constant == __value.constant
        elif isinstance(__value, Function):
            return super().__eq__(__value)
        else:
            return self.constant == __value