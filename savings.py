from bank import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.01):
        # Call the base class initializer
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of ${interest: .2f}. New balance: ${self.balance: .2f}.")

    def __str__(self):
        # base_str = super().__str__
        return f"Balance: ${self.balance:.2f} | Interest Rate: {self.interest_rate * 100:.2f}%"

# ---------------------------------------------------------------------------------------------------------------
# Test Code
# ----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # 1. Create an instance of SavingsAccount
    my_savings = SavingsAccount(owner="John Doe", balance=500.0, interest_rate=0.035)
    print("Initial State:")
    print(my_savings)
    print("-" * 40)

    # 2. Demonstrate inherited deposit and withdraw functionalities
    my_savings.deposit(200.00)
    my_savings.withdraw(50.00)
    print("-" * 40)

    # 3. Call apply_interest() and print the account
    my_savings.apply_interest()
    print("\nFinal State:")
    print(my_savings)

    
 