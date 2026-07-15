class Animal:
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return 'Lion sound: Ggrr...'
    
class Elephant(Animal):
    def sound(self):
        return 'Elephant sound: Ghaa...'

#polymorphism
sounds = [Lion(),Elephant()]

for s in sounds:
    print(s.sound())