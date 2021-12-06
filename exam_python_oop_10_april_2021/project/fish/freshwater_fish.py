from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    __INCREASE_SIZE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)
        self.aquarium_type = 'FreshwaterAquarium'
