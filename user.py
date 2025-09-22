import sys
import csv
import re


class User:
    def signup(self):
       pass
    def login(self):
        pass
    def logout(exit_choice):
        while True:
            if exit_choice == "Y":
                print("\nGoodbye, we hope you come back again. 👋")
                sys.exit()
            elif exit_choice == "N":
                print("\nOkay we'll take you back to the main menu.")
                break
            else:
                print("\nwrong choice please try again")
                break

print("\nwelcome!! to our banking system 🏦💰")
while True :
    user_input = int(input("\nwhat would you like to do ?\n 1)Login 2)Signup 3)Exit "))
    print(user_input)
    print(type(user_input))
    if user_input == 1:
        fname = input("enter your first name: ")
        lname = input("enter your last name: ")
        password = input("enter your password: ")
            
    elif user_input == 2:
        pass
    
    elif user_input == 3:
        exit_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ").upper()
        User.logout(exit_choice)

        