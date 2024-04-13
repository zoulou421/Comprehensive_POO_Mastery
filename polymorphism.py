"""
This class is showing you how to use real polymorphism : One method for example is used in other classes
if each object of each class has its own method(s), then polymorphism is not applied
"""
class Vehicle:
    def start_vehicle(self):
        print("The vehicle started")
class Car(Vehicle):
    def start_vehicle(self):
        super().start_vehicle()
        print("The car is riding!")
class Flight(Vehicle):
    def start_vehicle(self):
        super().start_vehicle()
        print("Flying...")

car =Car()
f= Flight()
#print(car.ride_car()) #contrary of the polymorphism philosophy: every object its method
#print(f.fly_airplaine()) #none polymor...

#real polymorphism
print(car.start_vehicle())
print(f.start_vehicle())
