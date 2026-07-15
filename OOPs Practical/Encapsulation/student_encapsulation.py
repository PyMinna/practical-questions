class student:
    def __init__(self,mark):
        self.__mark = mark

    def add(self,marks):
        self.__mark += marks

    def get_mark(self):
        return self.__mark
    
m = student(90)
m.add(10)
print(m.get_mark())
