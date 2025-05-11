import json
from datetime import datetime
class User:
    user_list = []

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.messages = {}
        self.friends = []
        self.logedin = False
        

    def changePassword(self, new_password):
        check = input("Enter Old Password: ")
        if check != self.__password:
            return False
        self.__password = new_password
        for user in self.user_list:
            if self.name == user['name']:
                user['password'] = self.__password
                with open('account_management', 'w') as file:
                    json.dump(self.user_list, file)
            
        return True
    
    def change_username(self, new_username):
        check = input("Enter Old Usename: ")
        if check != self.name:
            return False
        for user in User.user_list:
            if user['name'] == self.name :
                user['name'] = new_username
                self.name = new_username
                with open('account_management', 'w') as file:
                    json.dump(User.user_list, file)
            
        return True

    def login(self, name, password) :
        for user in self.user_list:
            if name == user['name']:
                if password == user['password']:
                    print("Correct Password")
                    print("Login Successful")
                    self.logedin = True
                    return True
                else :
                    print("Password not found try again")
                    return False
        
        print("Username not found please try agian")
        return False
        


    def logout(self) :
        self.logedin = False
        return "Logout Successful"
    
    def create_account(self):
        for user in self.user_list:
            if self.name == user['name']:
                print("Username is taken")
                return False
            
        print("Account Created")
        new_user =  {
        "name" : self.name,
        "password" : self.__password
        }
        self.user_list.append(new_user)
        with open('account_management', 'w') as file:
            json.dump(self.user_list, file)
            
        return True
    
    def delete_account(self, password) :
        if self.__password == password :
            del_user = {
            "name" : self.name,
            "password" : self.__password
            }
            self.user_list.remove(del_user)
            with open('account_management', 'w') as file:
                json.dump(self.user_list, file)
            del self
            return True
        else :
            print("Incorrect password")
            return False
            
    def send_message(self, user, message) :
        msgs = None
        user_exists = False
        time = datetime.now()
        format = time.strftime("%I:%M %p")
        new_message = {self.name : f'{message} @ {format}'}
        for users in self.user_list:
            if user == users['name']:
                user_exists = True
                break
        if not user_exists:        
            return False
        with open('messages.json', 'r') as messages:
            msgs = json.load(messages)
            if user in msgs:
                msgs[user].append(new_message)
            else:
                msgs[user] = [new_message]
        with open('messages.json', 'w') as messages:
            json.dump(msgs, messages)
        return True
    
    def load_message(self) :
        with open('messages.json', 'r') as messages:
            msgs = json.load(messages)
            my_messages = msgs[self.name]
            for message in my_messages:
                print(f"\n{list(message.keys())[0]}: {list(message.values())[0]}")

    def add_friend(self, name) :
        for user in self.user_list:
            if name == user['name']:
                print("Username found!")
                self.friends.append(name)
                print("Friend successfully added!")
                return True
        
        print("Username not found")
        return False
    
    def show_friends_list(self) :
        return self.friends