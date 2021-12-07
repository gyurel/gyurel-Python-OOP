from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        tv = TV()
        self.appliances = [tv]
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
