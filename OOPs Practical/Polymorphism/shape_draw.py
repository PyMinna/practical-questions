class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing circle.."
    
class Triangle(Shape):
    def draw(self):
        return "Drawing triangle"
    
#polymorphism
def call_shape(call):
    print(call.draw())

c = Circle()
t = Triangle()
call_shape(c)
call_shape(t)