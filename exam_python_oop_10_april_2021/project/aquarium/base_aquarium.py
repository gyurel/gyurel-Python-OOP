from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ == "FreshwaterFish" and self.__class__.__name__ == fish.aquarium_type:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        if fish.__class__.__name__ == "SaltwaterFish" and self.__class__.__name__ == fish.aquarium_type:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        for obj in self.fish:
            if obj == fish:
                self.fish.remove(obj)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for obj in self.fish:
            obj.eat()

    def __str__(self):
        fish_name = "none"

        if len(self.fish) > 0:
            fish_name = ' '.join([x.name for x in self.fish])

        decorations_count = len(self.decorations)
        aquarium_comfort = self.calculate_comfort()

        return f"""{self.name}:
Fish: {fish_name}
Decorations: {decorations_count}
Comfort: {aquarium_comfort}"""
