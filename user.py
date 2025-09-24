import sys
import csv
import re
import random

user_data = []
class User:
    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.id = random.randint(1111,9999)

    def signup(self):
        if self.first_name!= "" or self.last_name != "" or self.password != "":
          user_data.append([self.id,self.first_name,self.last_name,self.password])  
          with open("bank.csv", "a" ,newline="") as file:
            writer = csv.writer(file , delimiter=",")
            writer.writerow(["user_id","first_name","last_name","password","balance_checking","balance_savings"])
            for row in user_data:
                writer.writerow(row)
                return self.id
            
    
    def password_test(pwd):
        password_format = '^[a-z]+[A-Z]+[!@#$^%]+[0-8]+$'
        return bool(re.search(password_format, pwd))
    
       
    def login(self,id):
        with open ("bank.csv", "r") as file:
            reader =csv.DictReader(file)

            for row in reader:
                if row["user_id"] == id:
                    pwd1= input("enter your password")
                    if row["password"] == pwd1:
                        print(f"welcome back {row["first_name"]}")
                    else :
                        print("the password you have intered is not correct")
                        break
            else:
                print("the id you have intered is not correct")


    def logout(self,choice):
        while True:
            if choice == "Y":
                print("\nGoodbye, we hope you come back again. 👋")
                sys.exit()
            elif choice == "N":
                print("\nOkay we'll take you back to the main menu.")
                break
            else:
                print("\nwrong choice please try again")
                break

    