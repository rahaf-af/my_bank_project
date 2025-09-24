import random
def create_account_num():
    account_num = random.randint(10000,99999)
    return account_num
class Account:
    def __init__ (self, account_user):
        self.account_number = create_account_num()
        self.account_user = account_user
        self.balance = 0
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"The amount you deposit is {amount}, and your new alance is {self.balance} ")
        else:
            print("The value you entered is incorrect.")

    def withdraw(self, amount):
        if amount > 0 :
            self.balance -= amount
            print(f"The amount you withdraw is {amount}, and your new alance is {self.balance} ")
        else:
            print("The value you entered is incorrect.")
class SavingAccount(Account):

    def __init__(self, account_user , min_balance):
        super().__init__(account_user)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance :
            self.balance -= amount
            print(f"Cannot withdraw minimum balance requirements not met")
        else:
            super().withdraw(amount)

