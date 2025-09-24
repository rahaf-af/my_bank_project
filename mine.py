from user import User

print("\nwelcome!! to our banking system 🏦💰")
user_input = 0
while True :
    try:
        user_input = int(input("\nwhat would you like to do ?\n 1)Signup  2)Login  3)Exit "))
    except ValueError:
        print("\nwrong choice please try again")

    if user_input == 1:
        fname = input("\nenter your first name: ")
        lname = input("enter your last name: ")
        while True :
            password = input("enter your password: ")
            if User.password_test(password) :
                print("Your password is strong 💪🏼")
                break
            else:
                print("The password you entered is weak. Please try again.")

        new_user = User(fname, lname, password)
        new_user.signup()
        print(f"\nwe are so happy to have you here {fname} 😊")
        print(f"your id number is {new_user.id}")
        break
            
    elif user_input == 2:
        u_id=input("enter your id")
        User.login(u_id)
    
    elif user_input == 3:
        e_choice=input("\nAre you sure you want to exit the program?\n Y)yes N)no ").upper()
        User.logout(e_choice)
    