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
    def account_info(self):
        print(f"account_number: {self.account_number}, account user: {self.account_user},balance: {self.balance}$ ")

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

#account1=Account("rahaf")
#account1.deposit(100000)
#account1.deposit(-50)
#account1.withdraw(100)
#account1.account_info()

#account2= SavingAccount("mera",1000000)
#account2.deposit(70000)
#account2.withdraw(1999)
#account2.account_info()