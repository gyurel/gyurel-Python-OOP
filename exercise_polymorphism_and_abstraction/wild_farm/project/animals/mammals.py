from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_TYPES = ['Vegetable', 'Fruit']

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.1


class Dog(Mammal):
    FOOD_TYPES = ['Meat']

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.4


class Cat(Mammal):
    FOOD_TYPES = ['Vegetable', 'Meat']

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.3


class Tiger(Mammal):
    FOOD_TYPES = ['Meat']

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity
