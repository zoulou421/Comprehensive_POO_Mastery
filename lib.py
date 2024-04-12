#external module
import json
import logging
import os


#internal module
from constants import DATA_DIR

LOGGER = logging.getLogger()
class MyList(list):
    def __init__(self, name):
        self.name=name
    def addElementToList(self,element):
        if not isinstance(element,str):
            raise ValueError("You can only add strings!")
        if element in self:
            LOGGER.error(f"{element} is already in the list")
            return False
        self.append(element)
        return True
    def removeElementInList(self,element):
        if element in self:
            self.remove(element)
            return True
        return False
    def showListElement(self):
        print(f"My list of {self.name} :")
        for element in self:
            print(f" -{element}")
    def saveListElement(self):
        myPath = os.path.join(DATA_DIR, f"{self.name}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        with open(myPath, "w") as f:
            json.dump(self, f, indent=4)
        return True

if __name__=="__main__":
    myList=MyList("Shopping")
    myList.addElementToList("Avocado")
    #myList.removeElementInList("Apples")
    myList.addElementToList("Potatoes")
    myList.addElementToList("Bananas")
    #myList.addElementToList(0)
    '''result = myList.addElementToList("Apples")
    if result:
        pass # output element on UI for example
    '''
    print(myList)
    print(myList.showListElement())

    myList.showListElement()
    myList.saveListElement()


