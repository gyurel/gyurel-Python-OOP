from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        animal_type = self.__class__.__name__
        animal_name = self.name
        animal_weight = self.weight
        food_eaten = self.food_eaten
        wing_size = self.wing_size
        return f"{animal_type} [{animal_name}, {wing_size}, {animal_weight}, {food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        animal_name = self.name
        animal_weight = self.weight
        food_eaten = self.food_eaten
        living_region = self.living_region
        return f"{animal_type} [{animal_name}, {animal_weight}, {living_region}, {food_eaten}]"
