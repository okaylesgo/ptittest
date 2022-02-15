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