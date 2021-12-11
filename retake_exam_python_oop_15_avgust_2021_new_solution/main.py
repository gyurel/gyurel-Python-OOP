from project.bakery import Bakery


bakery = Bakery('Furnata na Pesho')
[bakery.add_table('InsideTable', x, 4) for x in range(1, 51)]
[bakery.add_table('OutsideTable', x, 4) for x in range(51, 101)]
print(bakery.add_food('Cake', 'Snejanka', 10.0))
print(bakery.add_food('Bread', 'Dobruja', 1.0))
print(bakery.add_drink('Water', 'Devin', 0.3, 'Izvorna'))
print(bakery.add_drink('Tea', 'English', 0.2, 'Jacobs'))
print(bakery.reserve_table(4))
print(bakery.reserve_table(4))
print(bakery.reserve_table(4))
print(bakery.reserve_table(4))
print(bakery.order_food(1, 'Snejanka', 'Dobruja', 'Devin', 'English'))
print(bakery.order_drink(1, 'Snejanka', 'Dobruja', 'Devin', 'English'))
print(bakery.leave_table(1))
print(bakery.get_total_income())
print(bakery.get_free_tables_info())
