import math

def absolute(p, star_p):
    return abs(p-star_p)

def relative(p, star_p):
    return abs((p-star_p)/p)

p = [math.pi, math.sqrt(2), math.exp(10), math.factorial(9)]
star_p = [3, 1.414, 22000, math.sqrt(18*math.pi)*pow((9/math.e), 9)]
[print(f"Para p = {p[i]} e *p = {star_p[i]} \
o erro absoluto é {absolute(p[i], star_p[i])} e o erro relativo é {relative(p[i], star_p[i])}") for i in range(4)]