import json
class User:
    user_list = []

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.messages = {}
        self.friends = []
        self.logedin = False
        user =  {
            "name" : self.name,
            "password" : self.__password
        }
        self.user_list.append(user)
        

    def changePassword(self, new_password):
        self.__password = new_password

    def _save_account(self) :
        with open('account_management', 'w') as file:
            json.dump(self.user_list, file)

    def login(self, name, password) :
        if name in self.user_list :
            print("Correct Username")
            if password in self.user_list :
                print("Correct Password")
                print("Login Successful")
                self.logedin = True
                return True
            else :
                print("Password not found try again")
                return False
        else :
            print("Username not found please try agian")
            return False

    def logout(self) :
        self.logedin = False
        return "Logout Successful"
    
    def delete_account(self, password) :
        for user in self.user_list :
            if self.user_list[self.name] == password :
                del self
                return True
            else :
                return "Error incorrect password"
            
    def send_message(user, message) :
        with open('messages.json', 'a') as messages:
            new_message = {user : message}
            json.dump(new_message)
    
    def load_message(self, user) :
        with open('messages.json', 'r') as messages:
            for message in messages.load():
                if user == self.name:
                    self.messages.update(message)