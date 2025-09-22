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
       
    def login(self):
        pass

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

print("\nwelcome!! to our banking system 🏦💰")
user_input = 0
while True :
    try:
        user_input = int(input("\nwhat would you like to do ?\n 1)Login 2)Signup 3)Exit "))
    except ValueError:
        print("\nwrong choice please try again")

    if user_input == 1:
        fname = input("\nenter your first name: ")
        lname = input("enter your last name: ")
        password = input("enter your password: ")
        new_user =User(fname, lname, password)
        new_user.signup()
        print(f"\nwe are so happy to have you here {fname} 😊")
        print(f"your id number is {new_user.id}")
        break
            
    elif user_input == 2:
        pass
    
    elif user_input == 3:
        e_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ").upper()
        User.logout(e_choice)
    