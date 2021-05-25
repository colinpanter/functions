from .classFunction import Function


class Variable(Function):
    def __init__(self) -> None:
        pass
    
    def __call__(self, x: float) -> float:
        return x
