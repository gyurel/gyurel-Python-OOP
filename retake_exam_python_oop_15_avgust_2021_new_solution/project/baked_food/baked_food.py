from abc import ABC, abstractmethod


class BakedFood(ABC):
    __NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"
    __PRICE_ERROR_MESSAGE = "Price cannot be less than or equal to zero!"

    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError(self.__NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(self.__PRICE_ERROR_MESSAGE)
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
