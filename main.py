"""Main function that displays the menu and allows for user interface"""

from user import User
main_user = None
while True:
    print("========Tuffy Social Media========")
    print("""
Menu
1. Login
2. Create Account""")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter username: ")
        password = input("Enter password: ")
        if name not in User.user_list:
            print("Incorrect username or user does not exist")
            continue
        if password != User.user_list[name]:
            print("Invalid password")
            continue
        main_user = User(name, password)
        main_user.login(name, password)
        while True:
            print("""
Menu
1. Send Message
2. View Messages
3. Delete Account""")
            option = input("Select option: ")
            if option == '1':
                pass
            
    elif choice == '2':
        name = input("Enter username: ")
        password = input("Enter password: ")
        if name in User.user_list:
            print("Username is already taken")
            continue
        new_user = User(name, password)
        new_user._save_account()
        continue
