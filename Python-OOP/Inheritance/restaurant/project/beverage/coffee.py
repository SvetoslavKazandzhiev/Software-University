# from restaurant.project.beverage.hot_beverage import HotBeverage
from project.beverage.hot_beverage import HotBeverage


class Coffe(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50
    def __init__(self, name, caffeine):
        HotBeverage.__init__(self, name, Coffe.COFFEE_PRICE, Coffe.COFFEE_MILLILITERS)
        self._caffeine = caffeine

    @property
    def caffeine(self):
        return self._caffeine

# cofee = Coffe("ime", 4, 50,5)
# print(cofee.caffeine)