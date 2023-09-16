class BankAccount:class bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0 :
      self.__account_balance +=amount
      print("the deposit is₹{}. the new balance is₹{}.".format(amount,self.__account_balance))
    else:
      print("the deposit amount is invalid")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -=amount
      print("the withdraw is₹{}. the new balance is₹{}.".format(amount,self.__account_balance))
    else:
      print("the deposit amount is invalid")

  def display_balance(self):
    print("account balance for {} (account #{}: {}".format(
      self.__account_holder_name,self.__account_number,
      self.__account_balance))

account = bankaccount(account_number="6789123349",
                      account_holder_name="annamol",
                      initial_balance=8000.0)

account.display_balance()
account.deposit(800.0)
account.withdraw(200.0)
account.display_balance()class bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0 :
      self.__account_balance +=amount
      print("the deposit is₹{}. the new balance is₹{}.".format(amount,self.__account_balance))
    else:
      print("the deposit amount is invalid")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -=amount
      print("the withdraw is₹{}. the new balance is₹{}.".format(amount,self.__account_balance))
    else:
      print("the deposit amount is invalid")

  def display_balance(self):
    print("account balance for {} (account #{}: {}".format(
      self.__account_holder_name,self.__account_number,
      self.__account_balance))

account = bankaccount(account_number="6789123349",
                      account_holder_name="annamol",
                      initial_balance=8000.0)

account.display_balance()
account.deposit(800.0)
account.withdraw(200.0)
account.display_balance()