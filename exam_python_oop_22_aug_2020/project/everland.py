class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_cost = 0
        for room in self.rooms:
            total_cost += room.expenses
            total_cost += room.room_cost
        return f"Monthly consumption: {total_cost:.2f}$."

    def pay(self):
        result = []
        for index in range(len(self.rooms)):
            monthly_cost = 0
            room = self.rooms[index]
            monthly_cost += room.expenses
            monthly_cost += room.room_cost
            if room.budget >= monthly_cost:
                room.budget -= monthly_cost
                result.append(f"{room.family_name} paid {monthly_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms[index] = ''
        self.rooms = [x for x in self.rooms if x != '']
        return '\n'.join(result)

    def status(self):
        rooms_strings = []
        all_people = sum([room.members_count for room in self.rooms])
        rooms_strings.append(f"Total population: {all_people}")

        for room in self.rooms:

            rooms_strings.append(f"{room.family_name} with {room.members_count} members. Budget: "
                                 f"{room.budget:.2f}$, Expenses: {room.expenses:.2f}$")

            counter = 1
            for index in range(len(room.children)):
                current_child = room.children[index]
                rooms_strings.append(f"--- Child {counter} monthly cost: {current_child.cost * 30:.2f}$")
                counter += 1

            total_appl_expences = 0
            for appl in room.appliances:
                total_appl_expences += appl.get_monthly_expense()
            rooms_strings.append(f"--- Appliances monthly cost: {total_appl_expences:.2f}$")
        return '\n'.join([x for x in rooms_strings])
