class Function:
    def __init__(self) -> None:
        raise NotImplementedError
    
    def __call__(self, x: float) -> float:
        raise NotImplementedError
    
    def derivative(self):
        raise NotImplementedError
    
    def plot(self, start, end, n=100) -> None:
        import matplotlib.pyplot as plt

        x = [start + i/n * (end - start) for i in range(n + 1)]
        y = [self(xi) for xi in x]

        plt.plot(x, y)
        plt.show()
    
    def __add__(self, other):
        from .classFunctionAdd import FunctionAdd
        return FunctionAdd(self, other)
    
    def __mul__(self, other):
        from .classFunctionMul import FunctionMul
        return FunctionMul(self, other)
