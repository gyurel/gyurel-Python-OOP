from abc import ABC, abstractmethod


class Astronaut(ABC):
    BREATHE = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.BREATHE

    def increase_oxygen(self, amount):
        self.oxygen += amount
