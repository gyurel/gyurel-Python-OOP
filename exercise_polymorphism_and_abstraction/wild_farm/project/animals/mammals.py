from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_TYPES = ['Vegetable', 'Fruit']
    WEIGHT_MULTIPLIER = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    FOOD_TYPES = ['Meat']
    WEIGHT_MULTIPLIER = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    FOOD_TYPES = ['Vegetable', 'Meat']
    WEIGHT_MULTIPLIER = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    FOOD_TYPES = ['Meat']
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
