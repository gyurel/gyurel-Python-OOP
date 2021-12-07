from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, 2)
        self.room_cost = 15
        self.pension_one = pension_one
        self.pension_two = pension_two
        tv = TV()
        fridge = Fridge()
        stove = Stove()
        self.appliances = [tv, fridge, stove] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)

    def calculate_expenses(self, *args):
        appliances_sum = 0
        children_sum = 0
        for el_list in args:
            for el in el_list:
                if el.__class__.__base__.__name__ == 'Appliance':
                    appliances_sum += el.get_monthly_expense()
                if el.__class__.__name__ == 'Child':
                    children_sum += el.cost * 30

        self.expenses = appliances_sum + children_sum
        return self.expenses
