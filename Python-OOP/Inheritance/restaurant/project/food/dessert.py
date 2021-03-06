# from restaurant.project.food.food import Food
from project.food.food import Food


class Desert(Food):
    def __init__(self, name, price, grams, calories):
        Food.__init__(self, name, price, grams)
        self._calories = calories

    @property
    def calories(self):
        return self._calories