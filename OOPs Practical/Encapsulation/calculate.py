class calculate:
    def __init__(self,addition):
        self.addition = addition

    def add(self,add):
        self.addition += add

class sub_calculate(calculate):
    def show_calculation(self):
        return(self.addition)
        
    
c = sub_calculate(13)
c.add(15)
print(c.show_calculation())

