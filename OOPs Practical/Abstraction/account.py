from abc import ABC,abstractmethod

class Account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class Saving_Account(Account):
    def calculate_interest(self):
        print("Saving account interest: 7% per year.")

class Current_Account(Account):
    def calculate_interest(self):
        print("Current account interest: No interest.")
       

a = Saving_Account()
b = Current_Account()
a.calculate_interest()
b.calculate_interest()