class Player:
    __PLAYER_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")

        self.player_exists(value)
        self.__name = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 12:
            raise Exception("The player cannot be under 12 years old!")
        self.__age = value
        
    @property
    def stamina(self):
        return self.__stamina
    
    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
        return False

    @classmethod
    def player_exists(cls, name):
        if name in cls.__PLAYER_NAMES:
            raise Exception(f"Name {name} is already used!")
        else:
            cls.__PLAYER_NAMES.append(name)
