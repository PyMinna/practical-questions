class User:
    def __init__(self,username,age,password):
        self.username = username
        self.age = age
        self.__password = password

    def check_password(self,enter_password):
      
        if enter_password == self.__password:
            print("password is correct")
        else:
            print('incorrect,try again')

    def get_password(self):
        return self.__password
    
    
p = User("Minna",18,"pyMinnaa")

p.check_password("pyMinnaa")
p.check_password("Minnaapy")

print(p.get_password())

print(p.username)
print(p.age)