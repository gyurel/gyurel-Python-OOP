# from appliances.appliance import Appliance
# from appliances.laptop import Laptop
# from appliances.stove import Stove
# from appliances.tv import TV
# from everland import Everland
# from people.child import Child
# from rooms.alone_old import AloneOld
# from rooms.alone_young import AloneYoung
# from rooms.old_couple import OldCouple
# from rooms.room import Room
# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
#
# new_cild = Child(10, 1, 5, 9, 8, 5, 8)
# laptop = Laptop()
# tv = TV()
# stove = Stove()
# child1 = Child(1, 1, 1, 1, 1, 1)
# child2 = Child(1, 1, 1, 1, 1, 1)
# child3 = Child(1, 1, 1, 1, 1, 1)
# child4 = Child(1, 1, 1, 1, 1, 1)
# room1 = Room('Familia', 10, 4)
# list_aplliances = [laptop, tv, stove]
# list_children = [child1, child2, child3, child4]
# print(new_cild.toys_cost)
# print(new_cild.food_cost)
# print(new_cild.cost)
# print(new_cild.__class__.__name__)
# print(isinstance(laptop, Appliance))
# print(laptop.__class__.__base__.__name__)
# room1.calculate_expenses(list_aplliances, list_children)
# print(room1.expenses)
# alone_room = AloneOld('Petrovi', 650)
# alone_room.pension -= 10
# print(alone_room.pension)
# print(alone_room.budget)
# alone_young = AloneYoung('Mitkovi', 700)
# print(alone_young.family_name)
# old_couple = OldCouple('Tenevi', 500, 900)
# print(old_couple.family_name)
# print(old_couple.budget)
# print(old_couple.pension_one)
# print(old_couple.pension_two)
# print(old_couple.expenses)
# young_couple = YoungCouple('Gogovi', 900, 700)
# print(young_couple.family_name)
# print(young_couple.budget)
# print(young_couple.salary_one)
# print(young_couple.salary_two)
# print(young_couple.expenses)
# young_couple_with_children = YoungCoupleWithChildren('Shemizovi', 500, 200, child1, child2, child3, child4)
# print(young_couple_with_children.family_name)
# print(young_couple_with_children.budget)
# print(young_couple_with_children.salary_one)
# print(young_couple_with_children.salary_two)
# print(young_couple_with_children.children)
# print(young_couple_with_children.expenses)
# print(young_couple.room_cost)
# everland = Everland()
# everland.add_room(alone_room)
# everland.add_room(alone_young)
# everland.add_room(old_couple)
# everland.add_room(young_couple)
# everland.add_room(young_couple_with_children)
# print(everland.rooms)
# print(everland.pay())
# print(everland.rooms)
from rooms.alone_old import AloneOld
from rooms.old_couple import OldCouple
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()

def test_one():
    alone_old = AloneOld("Johnsons", 205)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(alone_old)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
