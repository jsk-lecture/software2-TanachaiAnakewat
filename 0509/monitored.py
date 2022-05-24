import math

def make_monitored(f):
    count = 0
    def mf(x):
        nonlocal count
        if x == 'how-many-calls?':
            return count
        elif x == 'reset-count':
            count = 0
            return count
        else:
            count += 1
            return f(x)
    return mf

sqrt = make_monitored(math.sqrt)
print(sqrt)
print("sqrt(9)   = {}".format(sqrt(9)))
print("sqrt(100) = {}".format(sqrt(100)))
print("sqrt called {}".format(sqrt('how-many-calls?')))
sqrt('reset-count')
print("sqrt call reset")
print("sqrt called {}".format(sqrt('reset-count')))
print("sqrt(4) = {}".format(sqrt(4)))
print("sqrt(16) = {}".format(sqrt(16)))
print("sqrt(25) = {}".format(sqrt(25)))
print("sqrt called {}".format(sqrt('how-many-calls?')))