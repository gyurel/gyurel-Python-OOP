from restaurant.project.beverage.beverage import Beverage


class ColdBeverages(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
