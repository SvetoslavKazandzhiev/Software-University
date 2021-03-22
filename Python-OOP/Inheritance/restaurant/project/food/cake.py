# from restaurant.project.food.dessert import Desert
from project.food.dessert import Desert


class Cake(Desert):
    CAKE_GRAMS = 250
    CAKE_CALORIES = 1000
    CAKE_PRICE = 5
    def __init__(self, name):
        Desert.__init__(self, name, Cake.CAKE_PRICE, Cake.CAKE_GRAMS, Cake.CAKE_CALORIES)
