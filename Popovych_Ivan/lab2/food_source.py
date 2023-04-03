import random
from configs import Config
import math


class FoodSource:
    def __init__(self, location):
        self.location = location
        self.capacity = random.randint(*Config.food_range)

    def take_food(self, amount):
        if amount > self.capacity:
            amount = self.capacity
        self.capacity -= amount
        return amount

    def quality(self, bees, hive):
        dist = distance(self.location, hive.location)
        taken_food = 0
        for bee in bees:
            if bee.previous_source == self:
                taken_food += bee.memorized_food
                bee.reset_memorized_food()

        return (random.random() * taken_food) / dist


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
