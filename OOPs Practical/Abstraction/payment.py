from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self,amount):
        print("Paid",amount, "using UPI")

class Card(Payment):
    def pay(self,amount):
        print("Paid", amount, 'using card')

p1 = UPI()
p2 = Card()
p1.pay(700)
p2.pay(1200)
