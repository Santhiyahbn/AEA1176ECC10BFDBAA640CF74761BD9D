class BankAccount:
  def__init__(self, account_number,account_holder_name, initial_balance=0.0):
  self. __account_number = account_number 
self. __account_holder_name=account_holder_name 
self. __account_balance=initial_balance
def deposit (self, amount):
  if amount>0:
    self. __account_balance+=amount 
print ("Deposit ₹{}.New balance:₹{}.format (amount, self. __account_balance"))
else:
print ("Invalid deposit amount, please deposit a positive amount")
def withdraw(self, amount):
  if amount>0 and amount<=self.__account_balance:
    self__account__balance_=amount 
print ("with drew₹{}.New balance:₹{}".format(amount,self__account=balance))
else: 
print ("Invalid withdrawal amount ot insufficient balance") 
def display_balance (self):