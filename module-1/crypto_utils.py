class Wallet:    
    def __init__(self, owner):
        self.owner = owner
        self.balance = {}

    def deposit(self,token, amount):
        self.balance[token] = self.balance.get(token,0) + amount

    def withdraw(self, token, amount):
        if self.balance.get(token,0) >= amount:
            self.balance[token] -= amount
            return True
        else:
            return False

    def view_balance(self):
        return self.balance