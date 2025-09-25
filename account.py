import random
import datetime
import csv

account_data = []
def create_account_num():
    account_num = random.randint(10000,99999)
    return account_num

class Account:
    def __init__ (self, user_id):
        self.account_id = create_account_num()
        self.user_id = user_id
        self.account_type = "Checking"
        self.balance = 0
        self.status = "Active"
        self.Creationـdate = datetime.datetime.now()
    
    def create_account(self):
        account_data.append([self.user_id,self.account_id,self.account_type ,self.balance,self.status,self.Creationـdate ])
        with open("accounts.csv", "a" ,newline="") as file:
            writer = csv.writer(file , delimiter=",")
            writer.writerow(["user_id","account_id","account_type","balance","status","Creationـdate"])
            for row in account_data:
                writer.writerow(row)
        return row

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
        print(f"account_number: {self.account_num},balance: {self.balance}$ ")

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