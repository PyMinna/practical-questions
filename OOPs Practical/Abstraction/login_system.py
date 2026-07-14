from abc import ABC,abstractmethod

class Login_system(ABC):
    def login(self):
        pass

class Check_login(Login_system):
    def login(self):
            self.__verify_user()
            self.__check_password()

    def __verify_user(self):
         print("user verified..")

    def __check_password(self):
         print("password checked..")

l = Check_login()
l.login()