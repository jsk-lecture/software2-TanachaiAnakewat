import sys
sys.setrecursionlimit(2000)
def inc(n):
    return n + 1

def cube(a):
    return a*a*a

def sum(term,a,next,b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def simpson(f,a,b,n):
    h = float(b-a) / n
    def inc(x): return x+1
    def y(k): return f(a+k*h)
    def kvalue(k):
        if k==0 or k==n:
            return 1*y(k)
        elif k%2==0:
            return 2*y(k)
        elif k%2==1:
            return 4*y(k)
    return (h/3.0)*sum(kvalue,0,inc,n)

def integral(f, a, b, dx):
    return sum(f, a + (dx / 2.0), lambda x: x + dx, b) * dx 

print("simp function")
print("f= cube, a=0, b =1")
print("n=5  , integral = {}".format(simpson(cube, 0, 1, 5)))
print("n=10 , integral = {}".format(simpson(cube, 0, 1, 10)))
print("n=100, integral = {}".format(simpson(cube, 0, 1, 100)))

print("integral function f= cube, a=0, b =1")
print("f= cube, a=0, b =1")
print("dx=0.2 , integral = {}".format(integral(cube, 0, 1, 0.2)))
print("dx=0.1 , integral = {}".format(integral(cube, 0, 1, 0.1)))
print("dx=0.01, integral = {}".format(integral(cube, 0, 1, 0.01)))

