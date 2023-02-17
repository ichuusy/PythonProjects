class Player(): # Class definition
    def __init__(self): # Constructor definition
        self.__name = "" # Data hiding
        self.__hp = "" # Data hiding
        self.__state = "" # Data hiding

    @property
    def Name(self): # Getter
        return self.__name # Returned hid object.
    
    @Name.setter
    def Name(self,name): # Setter
        self.__name = name # Changed hidden object.
    
player10 = Player()
player10.Name = "Player10"
print(player10.Name)