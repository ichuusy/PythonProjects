class Animal(): # Parent class definition
    def __init__(self,name): # Constructor definiton
        self.name = name # Inherited object

    def Speak(): # Polymorphism (Virtual) Method
        pass

class Cat(Animal): # Child class definition
    def __init__(self,name:str):
        super().__init__(name) # Retrieved objects from the parent class.

    def Speak(self): # Changed Speak Method (Override)
        print("Meow")

class Dog(Animal): # Child class definition
    def __init__(self,name:str): # Constructor definiton
        super().__init__(name) # Retrieved objects from the parent class.

    def Speak(self):
        print("Dog")

class Cow(Animal): # Child class definition
    def __init__(self,name:str): # Constructor definiton
        super().__init__(name) # Retrieved objects from the parent class.

    def Speak(self): 
        print("Mow")

cow = Cow("Karabaş").Speak()
dog = Dog("Çerez").Speak()
cat = Cat("Karamel").Speak()