
def fundemo(x):
    def fun1(y):
        ret=x(y)
        print("ret:",ret)
        return ret
    return fun1
@fundemo
def fun2(x):
    return(x*222)
# print(fun2)
print(fun2(2))

