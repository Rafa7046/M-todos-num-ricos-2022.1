from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def plot_function(fun, a, b, step):
    x = Symbol('x')
    x_axis = [value for value in np.arange(a, b, step)]
    y_axis = [N(fun().subs(x, value), 10) for value in np.arange(a, b, step)]
    plt.plot(x_axis, y_axis, color = "red")

# def f():
#     x = Symbol('x')
#     return x**5 - x**4 + 3*x**3 + 80*x**2 + 9845*x + 4856

# plot_function(fun=f, a=0, b=20, step=1)
# plt.show()