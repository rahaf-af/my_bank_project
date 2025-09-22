import sys
import csv

class User:
    def login():
        pass
    def signup():
        pass
    def logout():
        exit_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ")
        exit_choice.upper()
        if exit_choice == "Y":
            print("Goodbye, we hope you come back again. 👋")
            sys.exit()
        elif exit_choice == "N":
            pass
        else:
            ("wrong choice please try again")

print("\nwelcome!! to our banking system 🏦💰")
while True :
    user_input = int(input("\nwhat would you like to do ?\n 1)Login 2)Signup 3)Exit "))
    print(user_input)
    print(type(user_input))
    if user_input == 1:
        pass
            
    elif user_input == 2:
        pass
    
    elif user_input == 3:
        User.logout()

        