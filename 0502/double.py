def inc(x):
    return x + 1

def double(f):
    return (lambda x : (f(f(x))))

print("double(inc)(0) = {}".format(double(inc)(0)))
print("(double(double))(inc)(0) = {}".format((double(double))(inc)(0)))

