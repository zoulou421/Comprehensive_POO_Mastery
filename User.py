from  dataclasses import dataclass
from typing import ClassVar #for attributes of class when importing [@dataclass]

class User1:
    def __init__(self, first_name:str, last_name:str): #str is optional
        self.first_name=first_name #first_name is repeated 3 times
        self.last_name=last_name  # last_name is repeated 3 times.That's we need [dataclasses].

#let look at the dataclass to improve our class. importing it first as above
@dataclass
class User2:
    first_name:str
    last_name:str ="" #you can affect default value or not.# Default value stands for:optional during the creation
    # attribute of class
    c:ClassVar[int]

    def __post_init__(self): #called after init//if you desire to do some of the action
        self.full_name=f"{self.first_name} {self.last_name}"


#Test of User2
my_name = User2(first_name="Bonevy",last_name="BEBY") #last name is optional. if you take out if it will work.
print(my_name.first_name)
print(my_name.last_name)

print(User2.__dict__) #display all attributes and of class as well

print(my_name.full_name)#test for __post_init__

