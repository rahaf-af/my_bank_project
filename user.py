import sys
import csv ,os
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

    def signup(self):
        if self.first_name!= "" and self.last_name != "" and self.password != "":
          user_data.append([self.id,self.first_name,self.last_name,self.password])  
          file = os.path.exists("bank.csv")
          with open("bank.csv", "a" ,newline="") as file:
            writer = csv.writer(file , delimiter=",")
            #writer.writerow(["user_id","first_name","last_name","password","balance_checking","balance_savings"])
            #if os.path.exists("bank.csv"):
            for row in user_data:
                writer.writerow(row)
            #else:
                #writer.writerow(["user_id","first_name","last_name","password","balance_checking","balance_savings"])

        return self.id , row
            
    
    def password_test(pwd):
        password_format = '^[A-Z]+[a-z]+[!@#$^%]+[0-8]+$'
        return bool(re.search(password_format, str(pwd)))
    
       
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


    def logout(choice):
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


#new_user = User("wed","fallatah","12345698")
#print(new_user.signup())

#passwor= User("hajar", "ahmad","Rof@1234" )
#print(passwor.password_test())

#log_to_acc = User("wed","70ef6969-3762-4ea0-9f51-40542bd24d86","12345698")
#print(str(log_to_acc.login))
