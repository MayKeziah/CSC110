#account class
class account:
    def __init__(self, Name):
        self.name = Name
        
    def setBalance(self, Balance):
        self.balance = float(Balance)

    def withdraw(self, Amount):
        self.balance = self.balance - Amount

    def deposit(self, amount):
        self.balance = selt.balance + Amount

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def printBalance(self):
        print("Your current balance is: $"+str(round(self.balance, 2)))
        
        
