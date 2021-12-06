from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    __INCREASE_SIZE = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)
        self.aquarium_type = 'SaltwaterAquarium'
