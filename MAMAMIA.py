from scipy.integrate import quad

def DIV(a,b):
    return a/b
def fact(a):
    result=a
    while a>1:
        result=result*(a-1)
        a=a-1
    if result==0:
        return 1
    if result<0:
        raise ValueError()
    return result
print("hihiha")
print('tarna')
print('hahaahahahahahah')
import math
def roots(a, b, c):
    delta=b**2-4*a*c
    if math.isclose(delta,0,rel_tol=1e-9):
        return((-b/(2*a)))
    if delta!=0:
        if delta>0:
                d=(-b+delta**(1/2))/(2*a)
                e=(-b-delta**(1/2))/(2*a)
                return(e,d)
        if delta<0:
            return tuple()
def integr(function, lower, upper):
    def f(x):
        return eval(function)
    return quad(f,lower,upper)[0]
print(integr("x+1",2,3))


