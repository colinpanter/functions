class Function:
    simplify = True

    def __init__(self) -> None:
        raise NotImplementedError
    
    def __call__(self, x: float) -> float:
        raise NotImplementedError
    
    def __str__(self) -> str:
        raise NotImplementedError
    
    def derivative(self) -> "Function":
        raise NotImplementedError
    
    def plot(self, start, end, n=100) -> None:
        import matplotlib.pyplot as plt

        x = [start + i/n * (end - start) for i in range(n + 1)]
        y = [self(xi) for xi in x]

        plt.plot(x, y)
        plt.show()

    def __neg__(self) -> "Function":
        from .classFunctionNeg import FunctionNeg
        return FunctionNeg(self)

    def __add__(self, other) -> "Function":
        from .classFunctionAdd import FunctionAdd
        return FunctionAdd.add(self, other)

    def __sub__(self, other) -> "Function":
        return self + (-other)
    
    def __mul__(self, other) -> "Function":
        from .classFunctionMul import FunctionMul
        return FunctionMul.multiply(self, other)
    
    def __truediv__(self, other) -> "Function":
        from .classFunctionDiv import FunctionDiv
        return FunctionDiv.divide(self, other)
