class Laptop:
    def price(self):
        pass

class GamingLaptop(Laptop):
    def price(self):
        return "price: 60,000"
    
class BusinessLaptop(Laptop):
    def price(self):
        return "price: 80,000"

#polymorphism
show = [GamingLaptop(),BusinessLaptop()]

for s in show:
    print(s.price())

print("-------------------------------")

def show_price(show):
    print(show.price())

g = GamingLaptop()
b = BusinessLaptop()
show_price(g)
show_price(b)