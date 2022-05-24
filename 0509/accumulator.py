def make_accumulator(balance):
    class context: # Python2 needs context, https://stackoverflow.com/questions/3190706/nonlocal-keyword-in-python-2-x
        _balance = balance
    def value(val):
        balance = context._balance
        balance += val
        context._balance = balance
        return balance
    return value

a=make_accumulator(5)
b=make_accumulator(10)
print("a=make_accumulator(5)")
print("a(10)={}".format(a(10)))
print("a(10)={}".format(a(10)))
print("b=make_accumulator(10)")
print("b(10)={}".format(b(10)))
print("b(10)={}".format(b(10)))
# def make_withdraw(balance):
#     class context: # Python2 needs context, https://stackoverflow.com/questions/3190706/nonlocal-keyword-in-python-2-x
#         _balance = balance
#     def withdraw(amount):
#         # nonlocal balance on Python3 you can use nonlocal
#         balance = context._balance
#         if amount > balance:
#             return 'Insufficient funds'
#         balance = balance - amount
#         context._balance = balance        # Send back to context for Python2
#         return balance
#     return withdraw