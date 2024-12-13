

#Class given.
class BankAccount:
    #Constructor
  def __init__(self, initial_balance=0):
    self.balance = initial_balance
    
   #Deposit money.
  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount
    
    #Withdraw money.
  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount
###    

my_bank_account= BankAccount(100)

