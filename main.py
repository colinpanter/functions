import matplotlib.pyplot as plt
from functions import Variable, FunctionLinear


if __name__ == "__main__":
    x = Variable()
    f = x * x

    f.derivative().derivative().derivative().plot(-4, 4)
