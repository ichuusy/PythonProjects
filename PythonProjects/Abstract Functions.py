from abc import abstractmethod,ABC # Importing modules for abstractmethod

class Market(ABC): # Parent class definition
    def __init__(self): # Constructor definiton
        self.name = "" # Inherited object
        self.employeeNumber = "" # Inherited object

    @abstractmethod # Abstractmethod definition
    def WriteMarketName(self): # Child classes are must necessarily defined this method.
        pass

class Bim(Market): # Child class definiton
    def __init__(self,name,employeeCount): # Constructor definition
        super().__init__() # Retrieved objects from the parent class.
        self.name = name # Inherited self.name object's value changed to name parameter. 
        self.employeeNumber = employeeCount # Inherited self.employeeNumber object's value changed to employeeNumber parameter. 


    def WriteMarketName(self): # Abstractmethod must be defined.
        print(f"Market name : {self.name}, Number of employees : {self.employeeNumber}")

market = Bim("Merkez",4)
market.WriteMarketName()