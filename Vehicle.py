"""
A basic class using class attributes
"""
class Vehicle:
    """
     attributes of class
    """
    mark_v="Toyota"
    color_v="red"
#Test without instantiation
print(Vehicle.mark_v)
print(Vehicle.color_v)

#Test with instantiation
vehicle_01=Vehicle()
vehicle_02=Vehicle()
print(vehicle_01.mark_v)
print(vehicle_02.mark_v)

#Modify  only class attribute and test, what changed ?
Vehicle.mark_v="Suziki"
print(Vehicle.mark_v)
print(vehicle_01)
print(vehicle_02)

#Modify  only class instantiated and test, what changed ?
vehicle_01.mark_v="Prado"

print(Vehicle.mark_v)
print(vehicle_01.mark_v)
print(vehicle_02.mark_v)

#in conclusion: instantiate attribute only affects itself(the object instanciated)
# while class attribute affects the whole class  [instance and class attributes,...]

#N.B:most of the case, it is recommended to use instanciate attribute for the specifications reasons

#You need create a constructor explicitly to be able initialize instanciate attributes

'''
IMPORTANT POINTS TO REMEMBER

To create a class, we use the keyword:class.

To initialize an instance, we use the __init__ method.

To define an instance attribute, we use self.attribute = value.

To create an instance, we use the class name, followed by parentheses.

To set default attributes when creating an instance, specify the values sent to the __init__ method inside parentheses.
'''