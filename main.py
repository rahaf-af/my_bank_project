from user import User
from account import Account ,SavingAccount

print("\nwelcome!! to our banking system 🏦💰")
user_input = 0
while True :
    try:
        user_input = int(input("\nwhat would you like to do 🤔 ?\n1)Signup  2)Login  3)Exit "))
    except ValueError:
        print("\nwrong choice please try again")

    if user_input == 1:
        fname = input("\nenter your first name: ")
        lname = input("\nenter your last name: ")
        while True :
            password = input("\nenter your password: ")
            if User.password_test(password) :
                print("Your password is strong 💪🏼")
                break
            else:
                print("The password you entered is weak ،\nThe password must consist of characters starting with a capital letter followed by lowercase letters,\n then a special character and finally numbers. Please try again.\nExam@123 ")

        new_user = User(fname, lname, password)
        new_user.signup()
        print(f"\nwe are so happy to have you here {fname} 😊")
        print(f"your id number is {new_user.id}")
        #break
        try:
            user_input2 = int(input("\nwhat would you like to do next 🤔 ?\n1)Create a Checking account  2)Create a Checking account "))
        except ValueError:
            print("\nwrong choice please try again")
        if user_input2 == 1:
            id = new_user.get_user_id()
            new_account= Account(id)
            new_account.create_account(id)
            try:
                user_input3 = int(input("\nwhat would you like to do next 🤔 ?\n1)deposit  2)withdraw  3)Back to the previous list "))
            except ValueError:
                print("\nwrong choice please try again")
            if user_input3 == 1:
                pass
            elif user_input3 == 2:
                pass
            elif user_input3 == 3:
                pass

        elif user_input2 == 2: 
            min_b = input("Please enter your min balance ")
            id = new_user.get_id()
            new_account= SavingAccount(id,min_b)
            new_account.create_account(id)

        elif user_input2 == 3:
            pass
            
            
    elif user_input == 2:
        name =input("entar your name: ")
        u_id=input("enter your id: ")
        User.login(name,u_id)
    
    elif user_input == 3:
        e_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ").upper()
        User.logout(e_choice)
    