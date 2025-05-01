
class User:

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.messages = {}
        self.friends = []
    
    def changePassword(self, new_password):
        self.__password = new_password
    
    