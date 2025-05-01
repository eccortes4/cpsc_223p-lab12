import json
class User:
    user_list = []

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.messages = {}
        self.friends = []
        self.logedin = False

    def changePassword(self, new_password):
        self.__password = new_password

    def _save_account(self) :
        with open('account_management', 'w') as file:
            json.dump(self.user_list, file)

    def login(self, name, password) :
        if self.name in self.user_list :
            print("Correct Username")
            if self.__password in self.user_list :
                print("Correct Password")
                print("Login Successful")
                user = {
                    name : password
                }
                self.user_list.append(user)
                self.logedin = True
                return True
            else :
                print("Password not found try again")
                return False
        else :
            print("Username not found please try agian")
            return False

    
    