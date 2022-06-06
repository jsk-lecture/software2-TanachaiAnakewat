data = [2, 3, 4, '*', '+']
stack =[]

for i, d in enumerate(data):
    if type(d) != int:
        data[i] = eval('lambda x, y: x' +d+ 'y')

for d in data:
    if type(d) == int:
        stack.append(d)
    else:
        x = stack.pop()
        y = stack.pop()
        z = d(y, x)
        stack.append(z)

print("answer is {}".format(stack.pop()))