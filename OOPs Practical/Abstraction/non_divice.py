class Divice:
    def boot(self):
        pass

class MyDivice(Divice):
    def boot(self):
        self.__load_os()
        self.__checking_hardware()

    def __load_os(self):
        print("Os loaded...")

    def __checking_hardware(self):
        print("hardware checked..")

d =MyDivice()
d.boot()