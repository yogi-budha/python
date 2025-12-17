# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details. Give the complete code for the BankAccount class.

class BankAccount:
    def __init__(self,accountNum,name,balance):
        self.accountNum = accountNum
        self.name = name
        self.balance = balance
        self.bankFee()
    
    def Deposit(self,amount):
        self.balance = self.balance + amount
    
    def WithDraw(self,amount):
        self.balance = self.balance - amount
    
    def bankFee(self):
        self.balance = self.balance - (self.balance*0.05)
    
    def Display(self):
        print("Account Number: ", self.accountNum)
        print("Account Name: ", self.name)
        print("Account Balance: ", self.balance)
    

cutomer = BankAccount(123456,"Yogesh",100)

cutomer.Deposit(500)
cutomer.Display()
cutomer.WithDraw(400)
cutomer.Display()