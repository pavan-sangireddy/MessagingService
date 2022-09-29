from abc import ABC, abstractmethod

class User(ABC):
    userId = ""
    password=""
    @abstractmethod
    def login(self, userID,password):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def createUser(self, newUserID):
        pass

    @abstractmethod
    def editUser(self, editUserID):
        pass