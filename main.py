import matplotlib.pyplot as plt
from functions import Variable, FunctionLinear


if __name__ == "__main__":
    var = Variable()
    f = FunctionLinear(var, b=-5) * FunctionLinear(var, b=5) * var

    x = list(range(-5, 6))
    y = [f(xi) for xi in x]
    plt.plot(x, y)
    plt.show()

    f2 = f.derivative()
    x = list(range(-5, 6))
    y = [f2(xi) for xi in x]
    plt.plot(x, y)
    plt.show()
