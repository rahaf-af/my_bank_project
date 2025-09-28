from user import User
from account import Account ,SavingAccount
import sys
print("-"*40)
print("welcome!! to ACM banking system 🏦💰")
print("-"*40)
while True :
    try:
        user_input = int(input("\nwhat would you like to do 🤔 ?\n1)Signup  2)Login  3)Exit "))
    except ValueError:
        print("\n⚠️ wrong choice please try again")

    if user_input == 1:
        fname = input("\nenter your first name: ")
        lname = input("\nenter your last name: ")
        while True :
            password = input("\nenter your password: ")
            if User.password_test(password) :
                print("\nYour password is strong 💪🏼")
                break
            else:
                print("\n⚠️ The password you entered is weak")
                print("\nThe password must consist of characters starting with a capital letter followed by lowercase letters")
                print("\n then a special character and finally numbers. Please try again.\nExam@123 ")

        new_user = User(fname, lname, password)
        new_user.signup()
        print(f"\nwe are so happy to have you here {fname} 😊")
        print(f"\nyour id number is {new_user.id}")
        #break
        while True:
            try:
                user_input2 = int(input("\nwhat would you like to do next 🤔 ?\n1)Create a Checking account  2)Create a Saving account  3)Back to the previous list "))
            except ValueError:
                print("\⚠️ Invalid value, try again")
                continue
            if user_input2 == 1:
                u_id = new_user.get_user_id()
                new_account= Account(u_id)
                new_account.create_account(u_id)
                while True:
                    try:
                        user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Transfer money 4)Back to the previous list "))
                    except ValueError:
                        print("\n⚠️ wrong choice please try again")
                    if user_input3 == 1:
                        accountId= input("\nPlease enter the account number you want to deposit money into: ")
                        d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                        #userid = new_user.get_user_id()
                        new_account = Account(accountId)
                        if new_account.deposit(d_amount,accountId ):
                            print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                            print(f"your new alance is {new_account.balance}$ ")
                        else:
                            print("\n⚠️ Deposit failed account not found, try again")
                    elif user_input3 == 2:
                        accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                        w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                        new_account= Account(accountId)
                        is_withdrawn ,new_balance = new_account.withdraw(w_amount,accountId )
                        if is_withdrawn :
                            print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                            print(f"\nYour new balance is {new_account.balance}$ ")
                        else:
                            print(f"⚠️ Your current balance is {new_account.balance}$ and you cannot withdraw more than that amount.")

                    elif user_input3 == 3:
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
                            
                    elif user_input3 == 4:
                        break
                    else:
                        print("\n⚠️ Invalid value, try again") 
                        continue   

            elif user_input2 == 2: 
                min_b = input("\nPlease enter your min balance ")
                id = new_user.get_user_id()
                new_account= SavingAccount(id,min_b)
                new_account.create_account(id)
                u_id = new_user.get_user_id()
                new_account= Account(u_id)
                new_account.create_account(u_id)
                while True:
                    try:
                        user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Transfer money 4)Back to the previous list "))
                    except ValueError:
                        print("\n⚠️ wrong choice please try again")
                    if user_input3 == 1:
                        accountId= input("\nPlease enter the account number you want to deposit money into: ")
                        d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                        #userid = new_user.get_user_id()
                        new_account = Account(accountId)
                        if new_account.deposit(d_amount,accountId ):
                            print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                            print(f"your new alance is {new_account.balance}$ ")
                        else:
                            print("\n⚠️ Deposit failed account not found, try again")
                    elif user_input3 == 2:
                        accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                        w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                        new_account= Account(accountId)
                        is_withdrawn ,new_balance = new_account.withdraw(w_amount,accountId )
                        if is_withdrawn :
                            print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                            print(f"\nYour new balance is {new_account.balance}$ ")
                        else:
                            print(f"\n⚠️ Your current balance is {new_account.balance}$ and you cannot withdraw more than that amount.")

                    elif user_input3 == 3:
                        firs_accountId = input("Please enter the account ID you want to transfer from: ")
                        second_accountId = input("Please enter the account ID you want to transfer to: ")
                        transfer_amount = input("Please enter the amount you want to transfer: ")
                        new_account  = Account(firs_accountId)
                        is_transferred,new_b = new_account.transformation(firs_accountId,second_accountId,transfer_amount)
                        if is_transferred :
                            print(f"\n{transfer_amount}$ has been transferred from account number {firs_accountId} to {second_accountId} successfully ✨🎉 ")
                            print(f"\nYour new balance is {new_b}$ ")
                        elif transfer_amount > new_account.balance :
                            print(f"\n⚠️ your current balance is {new_account.balance}$, which is less than the amount {transfer_amount}$ you want to transfer.")
                        else:
                            print(f"\n⚠️ The transfer failed . Please try again.")
                            
                    elif user_input3 == 4:
                        break
                    else:
                        print("\n⚠️ Invalid value, try again") 
                        continue
            elif user_input2 == 3:
                break
            else:
                print("⚠️ Invalid value, try again") 
         
    elif user_input == 2:
        name =input("entar your name: ")
        u_id=input("enter your id: ")
        pwd= input("enter your password: ")
        current_user , useid = User.login(name,u_id,pwd)
        if current_user :
            print(f"\nwelcome back {name} 😊")
            while True:
                try:
                    user_input2 = int(input("\nwhat would you like to do next 🤔 ?\n1)Create a Checking account  2)Create a Saving account  3)I already have an account  4)Back to the previous list "))
                except ValueError:
                    print("\n⚠️ Invalid value, try again")
                    continue
                if user_input2 == 1:
                    u_id = current_user.get_user_id()
                    current_user= Account(u_id)
                    current_user.create_account(u_id)
                    while True:
                        try:
                            user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Transfer money 4)Back to the previous list "))
                        except ValueError:
                            print("\n⚠️ wrong choice please try again")
                        if user_input3 == 1:
                            accountId= input("\nPlease enter the account number you want to deposit money into: ")
                            d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                            #userid = new_user.get_user_id()
                            current_user = Account(accountId)
                            if current_user.deposit(d_amount,accountId ):
                                print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                                print(f"your new balance is {current_user.balance}$ ")
                            else:
                                print("\n⚠️ Deposit failed account not found, try again")
                        elif user_input3 == 2:
                            accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                            w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                            current_user= Account(accountId)
                            is_withdrawn ,new_balance = current_user.withdraw(w_amount,accountId )
                            if is_withdrawn :
                                print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                                print(f"\nYour new balance is {current_user.balance}$ ")
                            else:
                                print(f"\n⚠️ Your current balance is {current_user.balance}$ and you cannot withdraw more than that amount.")

                        elif user_input3 == 3:
                            firs_accountId = input("Please enter the account ID you want to transfer from: ")
                            second_accountId = input("Please enter the account ID you want to transfer to: ")
                            transfer_amount = input("Please enter the amount you want to transfer: ")
                            current_user  = Account(firs_accountId)
                            is_transferred,new_b = current_user.transformation(firs_accountId,second_accountId,transfer_amount)
                            if is_transferred :
                                print(f"\n{transfer_amount}$ has been transferred from account number {firs_accountId} to {second_accountId} successfully ✨🎉 ")
                                print(f"\nYour new balance is {new_b}$ ")
                            elif transfer_amount > current_user.balance :
                                print(f"\n⚠️ your current balance is {current_user.balance}$, which is less than the amount {transfer_amount}$ you want to transfer.")
                            else:
                                print(f"\n⚠️ The transfer failed . Please try again.")
                                
                        elif user_input3 == 4:
                            break
                        else:
                            print("\n⚠️ Invalid value, try again") 
                            continue   

                elif user_input2 == 2: 
                    min_b = input("\nPlease enter your min balance ")
                    id = new_user.get_user_id()
                    current_user= SavingAccount(id,min_b)
                    current_user.create_account(id)
                    u_id = new_user.get_user_id()
                    current_user= Account(u_id)
                    current_user.create_account(u_id)
                    while True:
                        try:
                            user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Transfer money 4)Back to the previous list "))
                        except ValueError:
                            print("\n⚠️ wrong choice please try again")
                        if user_input3 == 1:
                            accountId= input("\nPlease enter the account number you want to deposit money into: ")
                            d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                            #userid = new_user.get_user_id()
                            current_user = Account(accountId)
                            if current_user.deposit(d_amount,accountId ):
                                print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                                print(f"your new alance is {current_user.balance}$ ")
                            else:
                                print("\n⚠️ Deposit failed account not found, try again")
                        elif user_input3 == 2:
                            accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                            w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                            current_user= Account(accountId)
                            is_withdrawn ,new_balance = current_user.withdraw(w_amount,accountId )
                            if is_withdrawn :
                                print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                                print(f"\nYour new balance is {current_user.balance}$ ")
                            else:
                                print(f"\n⚠️ Your current balance is {current_user.balance}$ and you cannot withdraw more than that amount.")

                        elif user_input3 == 3:
                            firs_accountId = input("Please enter the account ID you want to transfer from: ")
                            second_accountId = input("Please enter the account ID you want to transfer to: ")
                            transfer_amount = input("Please enter the amount you want to transfer: ")
                            current_user  = Account(firs_accountId)
                            is_transferred,new_b = current_user.transformation(firs_accountId,second_accountId,transfer_amount)
                            if is_transferred:
                                print(f"\n{transfer_amount}$ has been transferred from account number {firs_accountId} to {second_accountId} successfully ✨🎉 ")
                                print(f"\nYour new balance is {new_b}$ ")
                            elif transfer_amount > current_user.balance :
                                print(f"\nyour current balance is {current_user.balance}$, which is less than the amount {transfer_amount}$ you want to transfer.")
                            else:
                                print(f"\n⚠️ The transfer failed . Please try again.")
                                
                        elif user_input3 == 4:
                            break
                        else:
                            print("\n⚠️ Invalid value, try again") 
                            continue
                elif user_input2 == 3:
                    while True:
                        try:
                            user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Transfer money 4)Back to the previous list "))
                        except ValueError:
                            print("\n⚠️ wrong choice please try again")
                        if user_input3 == 1:
                            accountId= input("\nPlease enter the account number you want to deposit money into: ")
                            d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                            #userid = new_user.get_user_id()
                            current_user = Account(accountId)
                            if current_user.deposit(d_amount,accountId ):
                                print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                                print(f"your new alance is {current_user.balance}$ ")
                            else:
                                print("\n⚠️ Deposit failed account not found, try again")
                        elif user_input3 == 2:
                            accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                            w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                            current_user= Account(accountId)
                            is_withdrawn ,new_balance = current_user.withdraw(w_amount,accountId )
                            if is_withdrawn :
                                print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                                print(f"\nYour new balance is {current_user.balance}$ ")
                            else:
                                print(f"⚠️ Your current balance is {current_user.balance}$ and you cannot withdraw more than that amount.")

                        elif user_input3 == 3:
                            firs_accountId = input("Please enter the account ID you want to transfer from: ")
                            second_accountId = input("Please enter the account ID you want to transfer to: ")
                            transfer_amount = input("Please enter the amount you want to transfer: ")
                            current_user  = Account(firs_accountId)
                            is_transferred,new_b = current_user.transformation(firs_accountId,second_accountId,transfer_amount)
                            if is_transferred:
                                print(f"\n{transfer_amount}$ has been transferred from account number {firs_accountId} to {second_accountId} successfully ✨🎉 ")
                                print(f"\nYour new balance is {new_b}$ ")
                            elif transfer_amount > current_user.balance :
                                print(f"\n⚠️ your current balance is {current_user.balance}$, which is less than the amount {transfer_amount}$ you want to transfer.")
                            else:
                                print(f"\n⚠️ The transfer failed . Please try again.")
                                
                        elif user_input3 == 4:
                            break
                        else:
                            print("\n⚠️ Invalid value, try again") 
                            continue   

                elif user_input2 == 2: 
                    min_b = input("\nPlease enter your min balance ")
                    id = current_user.get_user_id()
                    current_user= SavingAccount(id,min_b)
                    current_user.create_account(id)
                    u_id = new_user.get_user_id()
                    current_user= Account(u_id)
                    current_user.create_account(u_id)
                    while True:
                        try:
                            user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Transfer money 4)Back to the previous list "))
                        except ValueError:
                            print("\n⚠️ wrong choice please try again")
                        if user_input3 == 1:
                            accountId= input("\nPlease enter the account number you want to deposit money into: ")
                            d_amount = int(input("\nNow enter the amount of money you want to deposit: "))
                            #userid = new_user.get_user_id()
                            current_user = Account(accountId)
                            if current_user.deposit(d_amount,accountId ):
                                print(f"\n{d_amount}$ has been deposited successfully ✨🎉 to account number {accountId}")
                                print(f"your new alance is {current_user.balance}$ ")
                            else:
                                print("\n⚠️ Deposit failed account not found, try again")
                        elif user_input3 == 2:
                            accountId= input("\nPlease enter the account number you want to withdraw money from: ")
                            w_amount = int(input("\nNow enter the amount of money you want to withdraw: "))
                            current_user= Account(accountId)
                            is_withdrawn ,new_balance = current_user.withdraw(w_amount,accountId )
                            if is_withdrawn :
                                print(f"\n{w_amount}$ has been withdrawn successfully ✨🎉 from account number {accountId}")
                                print(f"\nYour new balance is {current_user.balance}$ ")
                            else:
                                print(f"\n⚠️ Your current balance is {current_user.balance}$ and you cannot withdraw more than that amount.")

                        elif user_input3 == 3:
                            firs_accountId = input("Please enter the account ID you want to transfer from: ")
                            second_accountId = input("Please enter the account ID you want to transfer to: ")
                            transfer_amount = input("Please enter the amount you want to transfer: ")
                            current_user  = Account(firs_accountId)
                            is_transferred,new_b = current_user.transformation(firs_accountId,second_accountId,transfer_amount)
                            if is_transferred :
                                print(f"\n{transfer_amount}$ has been transferred from account number {firs_accountId} to {second_accountId} successfully ✨🎉 ")
                                print(f"\nYour new balance is {new_b}$ ")
                            elif transfer_amount > current_user.balance :
                                print(f"\n⚠️ your current balance is {current_user.balance}$, which is less than the amount {transfer_amount}$ you want to transfer.")
                            else:
                                print(f"\n⚠️ The transfer failed . Please try again.")
                        elif user_input3 == 4:
                            break
                        else:
                            print("\n⚠️ Invalid value, try again") 
                            continue 
                else:
                    print("\n⚠️ Invalid value, try again") 
                
        else:
            print( "\n⚠️ The information you entered is incorrect. Please try again.")
    
    elif user_input == 3:
        e_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ").upper()
        if e_choice == "Y":
                print("\nGoodbye, we hope you come back again. 🤞👋")
                sys.exit()
        elif e_choice == "N":
                print("\nokay we'll take you back to the main menu.")
                break
        else:
                print("\n⚠️ wrong choice please try again")
                pass
    