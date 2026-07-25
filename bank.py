# Basic Bank Account Management System
class BankAccount:
    def __init__(self, account_number, account_owner, balance=0):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def get_account_owner(self):
        return self.account_owner

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance+= amount

    def withdraw(self, amount):
        try:
            #amount < 0
            if amount <= self.balance:
                self.balance -= amount
              
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_owner}, Balance: ${self.balance}"

account_number = input("Enter account number: ")
account_owner = input("Enter account owner name: ")
balance = float(input("Enter initial balance: "))

account1= BankAccount(account_number, account_owner, balance)
print(account1.get_balance())

amount=float(input("Enter amount to deposit: "))
account1.deposit(amount)
print(account1.get_balance())

amount=float(input("Enter amount to withdraw: "))
account1.withdraw(amount)
print(account1.get_balance())
