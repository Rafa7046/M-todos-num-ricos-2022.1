def  limits(p, tol = 0.001):
    return [p - (p*tol), p + (p*tol)]

p = [150, 900, 1500, 90]
tol = 0.001
[print(f"Para p = {p[i]} e tol = {tol} o intervalo máximo aceito é [{(x := limits(p[i]))[0]}, {x[1]}]") for i in range(4)]