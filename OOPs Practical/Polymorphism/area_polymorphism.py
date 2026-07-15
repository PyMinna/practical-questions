class Circle:
    def area(self):
        return 3.14 * 6 * 6
    
class Square:
    def area(self):
        return 5 * 5
    
#polymorphism
def show_area(shape):
    print(shape.area())

c = Circle()
s = Square()
show_area(c)
show_area(s)