from project.animals.animal import Bird


class Owl(Bird):
    FOOD_TYPES = ['Meat']

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.25


class Hen(Bird):
    FOOD_TYPES = ['Vegetable', 'Fruit', 'Meat']

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if food.__class__.__name__ not in self.FOOD_TYPES:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35
