from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


def create_food(food_type, name, price):
    if food_type == "Bread":
        return Bread(name, price)
    if food_type == "Cake":
        return Cake(name, price)


def create_drink(drink_type: str, name: str, portion: float, brand: str):
    if drink_type == "Tea":
        return Tea(name, portion, brand)
    if drink_type == "Water":
        return Water(name, portion, brand)


def create_table(table_type: str, table_number: int, capacity: int):
    if table_type == "InsideTable":
        return InsideTable(table_number, capacity)
    if table_type == "OutsideTable":
        return OutsideTable(table_number, capacity)


class Bakery:
    __NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError(self.__NAME_ERROR_MESSAGE)
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for x in self.food_menu:
            if x.name == name and x.__class__.__name__ == food_type:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(create_food(food_type, name, price))

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for x in self.drinks_menu:
            if x.name == name and x.__class__.__name__ == drink_type:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(create_drink(drink_type, name, portion, brand))

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for x in self.tables_repository:
            if x.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(create_table(table_type, table_number, capacity))

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for x in self.tables_repository:
            if x.capacity >= number_of_people and not x.is_reserved:
                x.number_of_people = number_of_people
                x.is_reserved = True
                return f"Table {x.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        current_table = None
        food_not_in_menu = []
        ordered_food = []
        string_list = []

        for x in self.tables_repository:
            if x.table_number == table_number:
                current_table = x

        if current_table is None:
            return f"Could not find table {table_number}"

        for f_name in args:
            ordered = False
            for food in self.food_menu:
                if food.name == f_name:
                    current_table.order_food(food)
                    ordered_food.append(food)
                    ordered = True
            if not ordered:
                food_not_in_menu.append(f_name)

        string_list.append(f"Table {table_number} ordered:")
        for x in ordered_food:
            string_list.append(repr(x))
        string_list.append(f"{self.name} does not have in the menu:")
        for x in food_not_in_menu:
            string_list.append(x)
        return '\n'.join([x for x in string_list])

    def order_drink(self, table_number: int, *args):
        current_table = None
        drink_not_in_menu = []
        ordered_drinks = []
        string_list = []

        for x in self.tables_repository:
            if x.table_number == table_number:
                current_table = x

        if current_table is None:
            return f"Could not find table {table_number}"

        for d_name in args:
            ordered = False
            for drink in self.drinks_menu:
                if drink.name == d_name:
                    current_table.order_drink(drink)
                    ordered_drinks.append(drink)
                    ordered = True
            if not ordered:
                drink_not_in_menu.append(d_name)

        string_list.append(f"Table {table_number} ordered:")
        for x in ordered_drinks:
            string_list.append(repr(x))

        string_list.append(f"{self.name} does not have in the menu:")

        for x in drink_not_in_menu:
            string_list.append(x)

        return '\n'.join([x for x in string_list])

    def leave_table(self, table_number: int):
        current_table = None

        for x in self.tables_repository:
            if x.table_number == table_number:
                current_table = x

        bill = current_table.get_bill()
        self.total_income += bill
        current_table.clear()

        return f""""Table: {table_number}
Bill: {bill:.2f}"""

    def get_free_tables_info(self):
        return '\n'.join([x.free_table_info() for x in self.tables_repository if not x.is_reserved])

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
