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
        self.creationـdate = datetime.datetime.now()
    
    
    def get_account_id(self):
        return self.id
    
    def create_account(self,user_id):
        account_data.append([user_id,self.account_id,self.account_type ,self.balance,self.status,self.creationـdate ])
        with open("accounts.csv", "a" ,newline="") as file:
            writer = csv.writer(file , delimiter=",")
            #writer.writerow(["user_id","account_id","account_type","balance","status","Creationـdate"])
            for row in account_data:
                writer.writerow(row)
        print(f"\nYour {self.account_type} account has been created successfully ✨🎉 your account id is: {self.account_id}")
        return row , self.account_id

    def deposit(self,amount,id):
        rows =[]
        Process_data = []
        is_found = False
        if amount > 0 :
            with open("accounts.csv", "r" ,newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["account_id"]== id.strip():
                        #print("am here!!")
                        row["balance"] = str(int(row["balance"])+ amount)
                        self.balance += amount
                        is_found = True
                    rows.append(row)
            if is_found :           
                with open("accounts.csv", "w" ,newline="") as file:
                    writer = csv.DictWriter(file, fieldnames = rows[0].keys())
                    #writer.writerow(["user_id","account_id","account_type","balance","status","Creationـdate"])
                    writer.writeheader()
                    writer.writerows(rows)
                print(f"\n{amount}$ has been deposited successfully ✨🎉 to account number {id} ")
                print(f"your new alance is {self.balance}$ ")
            else:
                print("\nDeposit failed, try again")

    def withdraw(self, amount):
        if amount > 0 :
            self.balance -= amount
            print(f"The amount you withdraw is {amount}, and your new alance is {self.balance} ")
        else:
            print("The value you entered is incorrect.")
    def account_info(self):
        print(f"account_number: {self.user_id},balance: {self.balance}$ ")

class SavingAccount(Account):

    def __init__(self, user_id , min_balance):
        super().__init__(user_id)
        self.account_type = "Saving"
        self.min_balance = min_balance
    
    def create_account(self, user_id):
        return super().create_account(user_id)

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