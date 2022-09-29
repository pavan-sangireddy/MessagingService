from src.Models.User import User


class NormalUser(User):
    userId = ""
    def login(self, userId):
        self.userId = userId
        print("NormalUser login")

    def logout(self):
        print("NormalUser logout")

    def createUser(self, newUserId):
        print("NormalUser unauthorised to create user")

    def editUser(self, editUserId):
        print("NormalUser unauthorised to edit user")
