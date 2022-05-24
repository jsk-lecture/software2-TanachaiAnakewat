def inc(x):
    return x + 1

def double(f):
    return (lambda x : (f(f(x))))

print("double(inc)(0) = {}".format(double(inc)(0)))
print("double(inc)(0) => inc(inc(0)) = (0+1)+1 = 2")
print("(double(double))(inc)(0) = {}".format((double(double))(inc)(0)))
print("(double(double(inc))) => inc(inc(inc(inc(0)))) = (((0+1)+1)+1)+1 = 4")
