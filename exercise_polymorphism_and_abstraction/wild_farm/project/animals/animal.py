from abc import ABC, abstractmethod


class Animal(ABC):
    FOOD_TYPES = []
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_MULTIPLIER

class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        animal_type = self.__class__.__name__
        animal_name = self.name
        animal_weight = self.weight
        food_eaten = self.food_eaten
        wing_size = self.wing_size
        return f"{animal_type} [{animal_name}, {wing_size}, {animal_weight}, {food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        animal_name = self.name
        animal_weight = self.weight
        food_eaten = self.food_eaten
        living_region = self.living_region
        return f"{animal_type} [{animal_name}, {animal_weight}, {living_region}, {food_eaten}]"
