
class User:
    user_list = {}

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.messages = {}
        self.friends = []
        self.logedin = False

    def changePassword(self, new_password):
        self.__password = new_password


    def login(self, name, password) :
        if self.name in self.user_list :
            print("Correct Username")
            if self.__password in self.user_list :
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

    
    