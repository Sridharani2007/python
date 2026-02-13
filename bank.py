class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)



account = BankAccount("John", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
