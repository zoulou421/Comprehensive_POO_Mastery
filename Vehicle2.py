"""
This is to show you how to manipulate class methods and their interests:
Very simple to manipulate and easy comparing to the instance methods(because you don't have to
remember of attributes contrary to other one which is to remember of the attributes
"""
class Vehicle2:
    nb_vehicle_created=0
    def __init__(self, mark, speed,price):
        Vehicle2.nb_vehicle_created += 1
        self.mark=mark
        self.speed=speed
        self.price=price

    @classmethod
    def toyota(cls):
        return cls(mark="Toyota",speed=250,price=300000)
    @classmethod
    def suziki(cls):
        return cls(mark="Suziki",speed=250,price=200000)

    #static method
    @staticmethod
    def show_number_vehicle():
        print(f"You have {Vehicle2.nb_vehicle_created} in your garage")

toyo= Vehicle2.toyota()
suzi= Vehicle2.suziki()

print(toyo.price)
print(suzi.price)

Vehicle2.show_number_vehicle()
