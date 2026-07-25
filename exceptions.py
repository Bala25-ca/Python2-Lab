import bank
import exceptions


def InsufficientFundsError(self, withdraw):

     try:
          if amount <= self.balance:
               self.balance -= amount
               print("Withdraw sucess.")
           
     except InsufficientFundsError:
          print("Insufficient funds.") 
               