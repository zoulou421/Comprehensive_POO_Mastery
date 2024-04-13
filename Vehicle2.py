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

    def __str__(self):
        return f"Vehicle of marque {self.mark} with maximal speed of {self.speed}

toyo= Vehicle2.toyota()
suzi= Vehicle2.suziki()

print(toyo.price)
print(suzi.price)

Vehicle2.show_number_vehicle()

print(toyo) #print of your class, you don't enough info.That ' s why need to use: static __str__ method
#result of print without __str__: [<__main__.Vehicle2 object at 0x000002DACE28DD90>] as an example.

#let assume an example:
display_vcle=str(toyo) #an alternative way to convert first the return content of __str__ in a variable
# and after you cand display. 2 methods are both useful
print(display_vcle)
