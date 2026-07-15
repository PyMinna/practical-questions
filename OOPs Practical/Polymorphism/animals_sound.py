class Dog:
    def speak(self):
        return "Woof"
    
class Cat:
    def speak(self):
        return "Meow"
    
class Cow:
    def speak(self):
        return "Moo"
    
#polymorphism
object = [Dog(),Cat(), Cow()]

for o in object:
    print(o.speak())
