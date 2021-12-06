from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


def fish_factory(fish_type, fish_name, fish_species, price):
    if fish_type == 'FreshwaterFish':
        return FreshwaterFish(fish_name, fish_species, price)
    if fish_type == 'SaltwaterFish':
        return SaltwaterFish(fish_name, fish_species, price)


def find_current_obj(obj_name, iterable):
    for obj in iterable:
        if obj.name == obj_name:
            return obj


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == FreshwaterAquarium.__name__:
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        if aquarium_type == SaltwaterAquarium.__name__:
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == Ornament.__name__:
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."

        if decoration_type == Plant.__name__:
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        current_aquarium = find_current_obj(aquarium_name, self.aquariums)

        current_decoration = self.decorations_repository.find_by_type(decoration_type)
        if not current_decoration == 'None':
            current_aquarium.add_decoration(current_decoration)
            self.decorations_repository.remove(current_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if not fish_type == 'FreshwaterFish' and not fish_type == 'SaltwaterFish':
            return f"There isn't a fish of type {fish_type}."

        current_fish = fish_factory(fish_type, fish_name, fish_species, price)
        current_aquarium = find_current_obj(aquarium_name, self.aquariums)

        if current_aquarium.__class__.__name__ == current_fish.aquarium_type:
            return current_aquarium.add_fish(current_fish)
        else:
            return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        current_aquarium = find_current_obj(aquarium_name, self.aquariums)

        current_aquarium.feed()
        fish_fed = len(current_aquarium.fish)

        return f"Fish fed: {fish_fed}"

    def calculate_value(self, aquarium_name: str):
        current_aquarium = find_current_obj(aquarium_name, self.aquariums)

        value_of_aquarium = sum([f.price for f in current_aquarium.fish]) \
            + sum([d.price for d in current_aquarium.decorations])

        return f"The value of Aquarium {aquarium_name} is {value_of_aquarium:.2f}."

    def report(self):

        aquarium_info = '\n'.join([str(aqua) for aqua in self.aquariums])

        return aquarium_info
