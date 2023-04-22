import random
from alg_data import AlgData
import numpy as np


def calculate_distance(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.linalg.norm(a - b)


class Hive:
    def __init__(self):
        self.location = (0, 0)
        self.food_amount = 0


class FoodSource:
    def __init__(self, location):
        self.location = location
        self.food_amount = random.randint(*AlgData.food_random_distance)

    def _update_quality(self, bees):
        temp = 0
        for bee in bees:
            if bee.previous_source == self:
                temp += bee.get_all_taken_food()
        return temp

    def take_food(self, amount):
        taken_amount = amount if amount <= self.food_amount else self.food_amount
        self.food_amount -= taken_amount
        return taken_amount

    def get_and_update_quality(self, bees, hive):
        distance = calculate_distance(self.location, hive.location)
        taken_food = self._update_quality(bees)
        return (random.random() * taken_food) / distance
