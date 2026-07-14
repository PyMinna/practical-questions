from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car starts....")

class Bike(Vehicle):
    def start(self):
        print("Bike starts....")

v1 = Car()
v2 = Bike()
v1.start()
v2.start()