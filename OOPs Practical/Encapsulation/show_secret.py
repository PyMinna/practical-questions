class private:
    def __init__(self):
        self.__show_secret = "I'm very intelligent"

    def show_public(self):
        print("this is public")
        self.__show_secret
    
    def get_sec(self):
        return self.__show_secret
p = private()
p.show_public()
print(p.show_public)
print(p.get_sec())