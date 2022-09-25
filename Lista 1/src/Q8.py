import matplotlib.pyplot as plt
from sympy import *
from Q6 import plot_function
from Q7 import newton_root_aproximations

def plot_root_aproximations(root_aproximations):
    x = root_aproximations[0]
    y = root_aproximations[1]
    plt.scatter(x, y, color = "black")

def plot_graphs(fun, a, b, step, p0, tol, n, file_name):
    plot_function(fun, a, b, step)
    plot_root_aproximations(newton_root_aproximations(fun, p0, tol, n))
    plt.grid(true)
    plt.legend(["Função", "Aproximações da raiz"])
    plt.savefig(f".\Graficos\{file_name}")
    plt.clf()

# def f():
#     x = Symbol('x')
#     return ln(x) - 2**x + x**2
# plot_graphs(fun=f, a=3, b=5, step=0.0001, p0=4, tol=0.0000001, n=1000000, file_name="Letra_d.png")