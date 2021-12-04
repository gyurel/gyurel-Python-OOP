from abc import ABC, abstractmethod


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
        self.bill = 0

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food):
        self.bill += baked_food.price
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.bill += drink.price
        self.drink_orders.append(drink)

    def get_bill(self):
        return self.bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
        self.bill = 0

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
