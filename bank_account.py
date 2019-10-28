class BankAccount:
    def __init__(self, int_rate = 0.03, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance *= 1 + self.int_rate
        return self

kobe = BankAccount(0.05, 200)
kobe.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()

monty=BankAccount()
monty.deposit(500).deposit(500).withdraw(200).withdraw(100).yield_interest().display_account_info()