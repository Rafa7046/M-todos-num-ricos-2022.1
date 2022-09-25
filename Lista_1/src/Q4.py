import math

def solve_equation(a=1/3, b=-123/4, c=1/6):
    return [(-b + math.sqrt(pow(b, 2) -4 * a * c)/2*a), -b - math.sqrt(pow(b, 2) -4 * a * c)/2*a]

def solve_sum(start=1, stop=10):
    sum = 0
    for i in range(start, stop):
        sum += ((pow(-1, i)*pow(5, i))/math.factorial(i))
    return sum

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def absolute(p, star_p):
    return abs(p-star_p)

def relative(p, star_p):
    return abs((p-star_p)/p)

def calc(fun):
    fun_trunc3, fun_trunc4 = truncate(fun, 3), truncate(fun, 4)
    fun_round3, fun_round4 = round(fun, 3), round(fun, 4)
    print(f"O valor exato é {fun} seus truncamentos são {fun_trunc3} e {fun_trunc4} e seus arredondamentos {fun_round3} e {fun_round4}.\n")
    print(f"O erro absoluto para o truncamento de 3 dígitos é {absolute(fun, fun_trunc3)} para o de 4 é {absolute(fun, fun_trunc4)},\
 o erro relativo é, para 3 dígitos, {relative(fun, fun_trunc3)} e para 4, {relative(fun, fun_trunc4)}\n")
    print(f"Para o arredondamento o erro absoluto de 3 dígitos é {absolute(fun, fun_round3)} para o de 4 é {absolute(fun, fun_round4)},\
 o erro relativo é, para 3 dígitos, {relative(fun, fun_round3)} e para 4, {relative(fun, fun_round4)}\n")

funcs = [-10*math.pi + 6*math.e - 0.327, solve_equation(), solve_sum()]
for fun in funcs:
    try:
        calc(fun)
    except:
        print(f"A equação tem duas raizes, elas são {fun[0]} e {fun[1]}")
        for x in fun:
            calc(x)
    print("===================================================================================")