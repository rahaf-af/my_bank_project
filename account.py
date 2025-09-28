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
        self.overdraft_times = 0
        self.overdraft_limit = 200
        self.creationـdate = datetime.datetime.now()
        with open("accounts.csv", "r" ,newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_id"] == self.account_id:
                    self.balance = int(row["balance"])

    def get_account_id(self):
        return self.id
    
    def create_account(self,user_id):
        account_data.append([user_id,self.account_id,self.account_type ,self.balance,self.status,self.creationـdate,self.overdraft_times ])
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
        if int(amount) > 0 :
            with open("accounts.csv", "r" ,newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["account_id"]== id.strip():
                        row["balance"] = str(int(row["balance"])+ int(amount))
                        self.balance += int(amount)
                        is_found = True
                    rows.append(row)
            if is_found :           
                with open("accounts.csv", "w" ,newline="") as file:
                    writer = csv.DictWriter(file, fieldnames = rows[0].keys())
                    #writer.writerow(["user_id","account_id","account_type","balance","status","Creationـdate"])
                    writer.writeheader()
                    writer.writerows(rows)
                return True , self.balance
            else:
                return False

    def withdraw(self, amount,id):
        rows =[]
        Process_data = []
        is_found = False
        with open("accounts.csv", "r" ,newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["account_id"]== id.strip():
                        self.balance =  int(row["balance"])
                        if int(amount) <= 0 or int(amount) > int(self.balance) :
                            return False ,self.balance
                        self.balance -= int(amount)
                        row["balance"] = str(self.balance)
                        is_found = True
                    rows.append(row)
        if is_found :           
            with open("accounts.csv", "w" ,newline="") as file:
                writer = csv.DictWriter(file, fieldnames = rows[0].keys())
                #writer.writerow(["user_id","account_id","account_type","balance","status","Creationـdate"])
                writer.writeheader()
                writer.writerows(rows)
                return True , self.balance
                
        else:
            return False , self.balance
        
    def overdraf(self, amount,id):
        overdraf_fee = 35
        self.overdraft_limit = 200
        rows =[]
        is_done = False
        if amount <= (self.balance + overdraf_fee ):
            with open("accounts.csv", "r" ,newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["account_id"]== id.strip():
                            self.balance =  int(row["balance"])
                            user_res=input("The fee for the overdraf process is $35\n This value will be deducted from your account in addition to the value of the overdrawn balance\n Do you want to continue? Y)Yes N)No ").upper()
                            if user_res == "Y":
                                self.balance -= (int(amount)+ overdraf_fee)
                                row["balance"] = str(self.balance)
                                self.overdraft_times +=1
                                is_done = True
                            else:
                                print("Try withdrawing again when your balance increases.")
                        rows.append(row)
            if is_done:           
                with open("accounts.csv", "w" ,newline="") as file:
                    writer = csv.DictWriter(file, fieldnames = rows[0].keys())
                    #writer.writerow(["user_id","account_id","account_type","balance","status","Creationـdate"])
                    writer.writeheader()
                    writer.writerows(rows)
                    return True , self.balance
                    
            else:
                return False , self.balance



    def transformation (self,account1,account2,t_amount):
        Process_data = []
        is_withdraw , new_balance = self.withdraw(t_amount,account1)
        if is_withdraw :
            if self.deposit(t_amount,account2):
                return True, new_balance
            else:
                return False
        else:
            return False
        
            
    #def account_info(self):
        #print(f"account_number: {self.user_id},balance: {self.balance}$ ")

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
