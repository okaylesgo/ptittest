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
def roots(a, b, c):
    delta=b**2-4*a*c
    if delta==0:
        return((-b/(2*a)))
    if delta>0:
        d=(-b+delta**(1/2))/(2*a)
        e=(-b-delta**(1/2))/(2*a)
        return(e,d)
    if delta<0:
        return tuple()



