class make_withdraw:
    def  __init__(self, balance):
        self.balance = balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

kei = make_withdraw(100)
bill = make_withdraw(1000)

print (kei.withdraw(25))
print (bill.withdraw(25))
print (kei.withdraw(25))
print (bill.withdraw(25))
print (kei.withdraw(60))
print (bill.withdraw(60))