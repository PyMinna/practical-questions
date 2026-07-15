class Car:
    def start(self):
        return "Car starts.."
    
class Bike:
    def start(self):
        return "Bike starts.."
    
def start_vehicle(vehicle):
    print(vehicle.start())

c = Car()
b = Bike()
start_vehicle(c)
start_vehicle(b)