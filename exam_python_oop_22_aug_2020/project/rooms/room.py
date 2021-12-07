class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

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
