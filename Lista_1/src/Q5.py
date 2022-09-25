from sympy import *

def bissecao(fun, a, b, tol, n):
    a = N(a, 10)
    b = N(b, 10)
    x = Symbol('x')
    i = 1
    fa = N(fun().subs(x, a), 10)
    while i <= n:
        p = N(a + (b-a)/2, 10)
        fp = N(fun().subs(x, p), 10)
        if fp == 0 or (b-a)/2 < tol:
            return N(p, 10)
        i += 1
        if  (fa * fp) > 0:
            a = p
            fa = fp
        else:
            b = p

def newton(fun, p0, tol, n):
    x = Symbol('x')
    i = 1
    while i <= n:
        p = N(p0 - (fun()/diff(fun(), x)).subs(x, p0), 10)
        if Abs((p - p0)/p) < tol:
            return p
        i += 1
        p0 = p
    raise Exception("Atingiu o limite máximo de iterações")
        
# def f():
#     x = Symbol('x')
#     return x**5 - x**4 + 3*x**3 + 80*x**2 + 9845*x + 4856

# print(bissecao(fun=f, a=-5, b=5, tol=0.00001, n=10000))
# print(newton(fun=f, p0=pi/4, tol=0.00001, n=10000))