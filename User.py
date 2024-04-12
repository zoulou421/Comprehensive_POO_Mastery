from  dataclasses import dataclass
class User1:
    def __init__(self, first_name:str, last_name:str): #str is optional
        self.first_name=first_name #first_name is repeated 3 times
        self.last_name=last_name  # last_name is repeated 3 times.That's we need [dataclasses].

#let look at the dataclass to improve our class. importing it first as above
@dataclass
class User2:
    first_name:str
    last_name:str ="" #you can affect default value or not.Default value stands for:optional during the creation


#Test of User2
name = User2(first_name="Bonevy",last_name="BEBY") #last name is optional
print(name.first_name)
print(name.last_name)