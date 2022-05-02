def inc(x):
    return x + 1
def dec(x):
    return x - 1

def plus_a(a, b):
    #print("a = {}, b = {} ".format(a,b))
    if a == 0:
        return b
    else:
        print("plus({},{})=plus_a({},{})+1".format(a,b,a-1,b))
        return inc(plus_a(dec(a), b))

def plus_b(a, b):
    #print("a = {}, b = {} ".format(a,b))
    if a == 0:
        return b
    else:
        print("plus({},{})=plus_b({},{})".format(a,b,a-1,b+1))
        return plus_b(dec(a), inc(b))


print("call plus_a(4, 5))")
print(plus_a(4, 5))
print("plus_a is a iterative function")
print("call plus_b(4, 5))")
print(plus_b(4, 5))
print("plus_b is a recursive function")

