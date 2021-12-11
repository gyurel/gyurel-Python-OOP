from abc import ABC, abstractmethod


class Drink(ABC):
    __NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"
    __PORTION_ERROR_MESSAGE = "Portion cannot be less than or equal to zero!"
    __BRAND_ERROR_MESSAGE = "Brand cannot be empty string or white space!"

    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError(self.__NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError(self.__PORTION_ERROR_MESSAGE)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value == '' or value == ' ':
            raise ValueError(self.__BRAND_ERROR_MESSAGE)
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
