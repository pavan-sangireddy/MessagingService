from src.Helper.helperClasses import getUserProfileFromUserID
from src.Models.NormalUser import NormalUser
from src.Models.User import User


class AdminUser(User):
    userId = ""
    def login(self, userID):
        self.userId = userID
        print("AdminUser login")

    def logout(self):
        print("AdminUser logout")
        #has code for end session.

    def createUser(self, newUserID):
        newUser = NormalUser()
        print("AdminUser created new User", newUserID)
        return newUser

    def editUser(self, editUserID):
        user = getUserProfileFromUserID(editUserID)
        print("AdminUser editUser", editUserID)