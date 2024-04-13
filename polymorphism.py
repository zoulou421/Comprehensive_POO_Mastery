class Vehicle:
    def start_vehicle(self):
        print("The vehicle started")
class Car(Vehicle):
    def ride_car(self):
        print("The car is riding!")
class Flight(Vehicle):
    def fly_airplaine(self):
        print("Flying...")

car =Car()
f= Flight()
print(car.ride_car()) #contrary of the polymorphism philosophy: every object his method
print(f.fly_airplaine()) #none polymor...
