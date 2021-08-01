import matplotlib.pyplot as plt
from functions import Variable, FunctionLinear, Constant


if __name__ == "__main__":
    x = Variable()
    one = Constant(1)
    f = x - x*x

    f.plot(-2, 2)
