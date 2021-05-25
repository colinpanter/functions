from functions_templates.classFunction import Function
from functions_templates.classVariable import Variable
from functions_templates.classFunctionLinear import FunctionLinear


if __name__ == "__main__":
    x = Variable()
    f = FunctionLinear(x, a=4, b=2)
    print(f(2))
