from sympy import *
from Q7 import bissecao_root_aproximations, newton_root_aproximations
from Q8 import plot_graphs

def generate_results(fun, a, b, step, p0, tol, n, file_name):
    value_bissecao = bissecao_root_aproximations(fun, a, b, tol, n)
    value_newton = newton_root_aproximations(fun, p0, tol, n)
    plot_graphs(fun, a, b, step, p0, tol, n, file_name)
    print(f"O valor da raiz utilizando o método da bisseção é {value_bissecao[0][-1]}, e tem os valores de aproximação de {value_bissecao[0]}")
    print("")
    print(f"O valor da raiz utilizando o método da newton é {value_newton[0][-1]}, e tem os valores de aproximação de {value_newton[0]}")
    print("==================================================")


def fa():
    x = Symbol('x')
    return x - 2**(-x)

def fb():
    x = Symbol('x')
    return x + 1 - 2*sin(pi*x)

def fc():
    x = Symbol('x')
    return 2*x*cos(2*x) - (x + 1)**2

def fd():
    x = Symbol('x')
    return ln(x) - 2**x + x**2

a = generate_results(fun=fa, a=0, b=1, step=0.0001, p0=0.5, tol=0.0000001, n=1000000, file_name="Letra_a.png")
b = generate_results(fun=fb, a=0, b=0.5, step=0.0001, p0=0.25, tol=0.0000001, n=1000000, file_name="Letra_b.png")
c = generate_results(fun=fc, a=-3, b=2, step=0.0001, p0=-0.5, tol=0.0000001, n=1000000, file_name="Letra_c.png")
d = generate_results(fun=fd, a=3, b=5, step=0.0001, p0=4, tol=0.0000001, n=1000000, file_name="Letra_d.png")