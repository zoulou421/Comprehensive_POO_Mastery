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