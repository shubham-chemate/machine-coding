from food import Food

class Order:

    def __init__(self, restId, foodId, quantity):
        self.restId = restId
        self.food = Food(foodId, quantity)