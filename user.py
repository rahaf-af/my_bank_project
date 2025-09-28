
import csv
import re
import random
import uuid

user_data = []
class User:
    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.id = uuid.uuid4()

    def get_user_id(self):
        return self.id

    def signup(self):

        if self.first_name!= "" and self.last_name != "" and self.password != "":
          user_data.append([self.id,self.first_name,self.last_name,self.password])  
          #file = os.path.exists("users.csv")
          with open("users.csv", "a" ,newline="") as file:
            writer = csv.writer(file , delimiter=",")
            #writer.writerow(["user_id","first_name","last_name","password","balance_checking","balance_savings"])
            #if os.path.exists("bank.csv"):
            for row in user_data:
                writer.writerow(row)
            #else:
                #writer.writerow(["user_id","first_name","last_name","password","balance_checking","balance_savings"])
                #for row in user_data:
                    #writer.writerow(row)
        return self.id , row ,True
            
    
    def password_test(pwd):
        password_format = '^[A-Z]+[a-z]+[!@#$^%]+[0-8]+$'
        return bool(re.search(password_format, str(pwd)))
    
       
    def login(self,id,pwd1):
        with open ("users.csv", "r") as file:
            reader =csv.DictReader(file)

            for row in reader:
                if row["user_id"] == id:
                    if row["password"] == pwd1:
                        return True ,id
                    else :
                        return False
