"""Main function that displays the menu and allows for user interface"""

from user import User
import json
main_user = None
with open("account_management", 'r') as f:
    User.user_list = json.load(f)
while True:
    print("========Tuffy Social Media========")
    print("""
Menu
1. Login
2. Create Account
3. Exit""")

    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter username: ")
        password = input("Enter password: ")
        main_user = User(name, password)
        if not main_user.login(name = name, password = password):
            continue
        while True:
            print("""
Menu
1. Send Message
2. View Messages
3. Delete Account
4. Exit""")
            option = input("Select option: ")
            if option == '1':
                message = input("Enter message: ")
                recipient = input("Enter recipient")
                main_user.send_message(message)
            elif option == '2':
                pass
            elif option == '3':
                password = input("Enter password to confirm: ")
                if  main_user.delete_account(password):
                    break
            elif option == '4':
                break
            
    elif choice == '2':
        name = input("Enter username: ")
        password = input("Enter password: ")
        new_user = User(name, password)
        account_created = new_user.create_account()
        if not account_created:
            continue

    elif choice == '3' :
        break
