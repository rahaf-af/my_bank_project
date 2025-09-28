from user import User
from account import Account ,SavingAccount
import sys
while True:
    print("-"*35)
    print("welcome!! to ACM banking system 🏦💰")
    print("-"*35)
    print("\nWhat would you like to do 🤔")
    print("\n[1] Signup 👤")
    print("[2] Login 👤")
    print("[3] Exit ➜🚪")
    try:
        user_input = int(input("\nYour choice: "))
    except ValueError:
        print("\n❌ Wrong choice please try again")
    if user_input == 1:
        fname = input("\nFirst name 👤: ")
        lname = input("\nLast name 👤: ")
        while True :
            password = input("\nPassword 🔐: ")
            if User.password_test(password) :
                print("\nYour password is strong 💪🏼")
                break
            else:
                print("\n⚠️ The password you entered is weak")
                print("\nThe password must consist of characters starting with a capital letter followed by lowercase letters")
                print("\nThen a special character and finally numbers. Please try again.\nExa@1234 ")
                continue
        new_user = User(fname, lname, password)
        new_user.signup()
        print(f"\nWe are so happy to have you here {fname} 😊")
        print(f"\nYour id number is {new_user.id}")
    elif user_input == 2:
        name =input("Name 👤: ")
        u_id=input("Id 🪪 : ")
        pwd= input("Password 🔐: ")
        current_user , useid = User.login(name,u_id,pwd)
        if current_user :
             print(f"\nWelcome back {name} 😊")
    elif user_input == 3:
        e_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ").upper()
        if e_choice == "Y":
            print("\nGoodbye, we hope you come back again. 🤞👋")
            sys.exit()
        elif e_choice == "N":
            print("\nOkay we'll take you back to the main menu.")
            continue
        else:
            print("\n❌ Wrong choice please try again")
            continue
    while True:
        print("\nWhat would you like to do 🤔")
        print("[1] Create a Checking account 💳")
        print("[2] Create a Saving account 💰")
        print("[3] Create a Checking & Saving account 💳💰")
        print("[4] I already have an account 😉")
        print("[5] Back to the previous list 🔙")
        try:
            user_input1 = int(input("\nYour choice: "))
        except ValueError:
            print("\n❌ Wrong choice please try again")
            continue
        if user_input1 == 1:
            u_id = new_user.get_user_id()
            new_account= Account(u_id)
            new_account.create_account(u_id)
        elif user_input1 == 2:
            min_b = input("\nPlease enter your min balance ")
            id = new_user.get_user_id()
            new_account= SavingAccount(id,min_b)
            new_account.create_account(id) 
        elif user_input1 == 3:
            u_id = new_user.get_user_id()
            new_account= Account(u_id)
            new_account.create_account(u_id)
            min_b = input("\nPlease enter your min balance ")
            id = new_user.get_user_id()
            new_account= SavingAccount(id,min_b)
            new_account.create_account(id)

        elif user_input1 == 4:
            pass
        elif user_input1 == 5:
            break
        else:
            print("\n❌ Wrong choice please try again")
            continue
        while True:
            print("\nWhat would you like to do 🤔")
            print("[1] Deposit 💵📥")
            print("[2] Withdraw 💸📤")
            print("[3] Transfer money 🔄💵")
            print("[4] Back to the previous list 🔙")
            try:
                user_input2 = int(input("\nYour choice: "))
            except ValueError:
                print("\n❌ Wrong choice please try again")
                continue
            if user_input2 == 1:
                accountId= input("\nPlease enter the account number you want to deposit money into: ")
                d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                new_account = Account(accountId)
                if new_account.deposit(d_amount,accountId ):
                    print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                    print(f"your new alance is {new_account.balance}$ ")
                else:
                    print("\n⚠️ Deposit failed account not found, try again")
            elif user_input2 == 2:
                accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                new_account= Account(accountId)
                is_withdrawn ,new_balance = new_account.withdraw(w_amount,accountId )
                if is_withdrawn :
                    print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                    print(f"\nYour new balance is {new_account.balance}$ ")
                else:
                    print(f"⚠️ Your current balance is {new_account.balance}$ and you cannot withdraw more than that amount.")
            elif user_input2 == 3:
                firs_accountId = input("Please enter the account ID you want to transfer from: ")
                second_accountId = input("Please enter the account ID you want to transfer to: ")
                transfer_amount = input("Please enter the amount you want to transfer: ")
                new_account  = Account(firs_accountId)
                is_transferred,new_b = new_account.transformation(firs_accountId,second_accountId,transfer_amount)
                if is_transferred :
                    print(f"\n{transfer_amount}$ has been transferred from account number {firs_accountId} to {second_accountId} successfully ✨🎉 ")
                    print(f"\nYour new balance is {new_b}$ ")
                elif transfer_amount > new_account.balance :
                    print(f"\nyour current balance is {new_account.balance}$, which is less than the amount {transfer_amount}$ you want to transfer.")
                else:
                    print(f"\n⚠️ The transfer failed . Please try again.")
                            
            elif user_input2 == 4:
                break
            else:
                print("\n⚠️ Invalid value, try again") 
                continue   