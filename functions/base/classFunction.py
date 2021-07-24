class Function:
    def __init__(self) -> None:
        raise NotImplementedError
    
    def __call__(self, x: float) -> float:
        raise NotImplementedError
    
    def derivative(self):
        raise NotImplementedError
    
    def __add__(self, other):
        from .classFunctionAdd import FunctionAdd
        return FunctionAdd(self, other)
    
    def __mul__(self, other):
        from .classFunctionMul import FunctionMul
        return FunctionMul(self, other)
