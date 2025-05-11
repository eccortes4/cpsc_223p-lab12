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
4. Change Username
5. Change Password
6. Add Friends
7. Show Friends List
8. Logout""")
            option = input("Select option: ")
            if option == '1':
                message = input("Enter message: ")
                recipient = input("Enter recipient: ")
                if not main_user.send_message(recipient, message):
                    print("The user you wish to message does not exist")
            elif option == '2':
                main_user.load_message()
            elif option == '3':
                password = input("Enter password to confirm: ")
                if  main_user.delete_account(password):
                    break
            
            elif option == '4' :
                new_username = input("Enter new username: ")
                main_user.change_username(new_username)
                
            elif option == '5':
                new_password = input("Enter new password: ")
                if not main_user.changePassword(new_password):
                    print("Incorrect Password")
                    continue
            elif option == '6' :
                new_friend = input("Enter the username you want to add as a friend: ")
                if not main_user.add_friend(new_friend):
                    print("The user you wish to add does not exist")

            elif option == '7' :
               print("Friends List: ")
               for friend in main_user.show_friends_list():
                print(friend)

            elif option == '8':
                main_user.logout()
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
