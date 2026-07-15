class EnglishGreeting:
    def greet(self):
        return "English greeeting: Hello.."
    
class SpanishGreeting:
    def greet(self):
        return "Spanish greeting: Hola.."
    
#polymorphism
def show_greeting(show):
    print(show.greet())

e = EnglishGreeting()
s = SpanishGreeting()
show_greeting(e)
show_greeting(s)