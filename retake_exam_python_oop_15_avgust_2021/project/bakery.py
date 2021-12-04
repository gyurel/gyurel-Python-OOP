from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


def factory_create_food(food_type, name, price):
    if food_type == Bread.__name__:
        return Bread(name, price)
    if food_type == Cake.__name__:
        return Cake(name, price)


def factory_create_drink(drink_type, name, portion, brand):
    if drink_type == Tea.__name__:
        return Tea(name, portion, brand)
    if drink_type == Water.__name__:
        return Water(name, portion, brand)


def factory_create_table(table_type, table_number, capacity):
    if table_type == InsideTable.__name__:
        return InsideTable(table_number, capacity)
    if table_type == OutsideTable.__name__:
        return OutsideTable(table_number, capacity)


class Bakery:
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
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.__class__.__name__ == food_type and food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(factory_create_food(food_type, name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drink in self.drinks_menu:
            if drink.__class__.__name__ == drink_type and drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(factory_create_drink(drink_type, name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(factory_create_table(table_type, table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.is_reserved == False and table.capacity <= number_of_people:
                table.is_reserved = True
                table.number_of_people = number_of_people
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        current_table = None
        food_not_in_menu = []
        for table in self.tables_repository:
            if table.table_number == table_number:
                current_table = table
                break

        if current_table is None:
            return f"Could not find table {table_number}"

        for food_name in args:
            found = False
            for food in self.food_menu:
                if food.name == food_name:
                    # current_table.bill += food.price
                    # current_table.food_orders.append(food)
                    current_table.order_food(food)
                    found = True
                    break
            if not found:
                food_not_in_menu.append(food_name)

        result = f"Table {table_number} ordered:\n"
        result += '\n'.join([x.__repr__() for x in current_table.food_orders])
        result += '\n'
        result += f'{self.name} does not have in the menu:\n'
        result += '\n'.join([x for x in food_not_in_menu])

        return result

    def order_drink(self, table_number: int, *args):
        current_table = None
        drink_not_in_menu = []
        for table in self.tables_repository:
            if table.table_number == table_number:
                current_table = table

        if current_table is None:
            return f"Could not find table {table_number}"

        for drink_name in args:
            found = False
            for drink in self.drinks_menu:
                if drink.name == drink_name:
                    # current_table.bill += drink.price
                    # current_table.drink_orders.append(drink)
                    current_table.order_drink(drink)
                    found = True
                    break
            if not found:
                drink_not_in_menu.append(drink_name)

        result = f"Table {table_number} ordered:\n"
        result += '\n'.join([x.__repr__() for x in current_table.drink_orders])
        result += '\n'
        result += f'{self.name} does not have in the menu:\n'
        result += '\n'.join([x for x in drink_not_in_menu])

        return result

    def leave_table(self, table_number: int):
        current_table = None
        for table in self.tables_repository:
            if table.table_number == table_number:
                current_table = table

        bill = current_table.get_bill()
        self.total_income += bill
        current_table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = '\n'.join([x.free_table_info() for x in self.tables_repository if x.free_table_info() is not None])
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
