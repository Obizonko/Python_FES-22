import random
from configs import Config
import math


class FoodSource:
    """A class representing a food source.

    Attributes:
        location (tuple): The location of the food source.
        capacity (int): The amount of food in the food source.
    """
    def __init__(self, location):
        """Initializes a FoodSource instance.

                Args:
                    location (tuple): The location of the food source.
        """
        self.location = location
        self.capacity = random.randint(*Config.food_range)

    def take_food(self, amount):
        """Takes a specified amount of food from the food source.

                If the requested amount of food is greater than the remaining capacity
                of the food source, the remaining capacity will be taken instead.

                Args:
                    amount (int): The amount of food to take from the food source.

                Returns:
                    int: The actual amount of food taken from the food source.
        """
        if amount > self.capacity:
            amount = self.capacity
        self.capacity -= amount
        return amount

    def quality(self, bees, hive):
        """Calculates the quality of the food source.

                The quality is determined by the amount of food taken by employed bees
                and the distance between the food source and the hive.

                Args:
                    bees (list): A list of EmployedBee instances.
                    hive (Hive): The Hive instance.

                Returns:
                    float: The quality of the food source.
        """
        dist = distance(self.location, hive.location)
        taken_food = 0
        for bee in bees:
            if bee.previous_source == self:
                taken_food += bee.memorized_food
                bee.reset_memorized_food()

        return (random.random() * taken_food) / dist


def distance(a, b):
    """Calculates the Euclidean distance between two points.

        Args:
            a (tuple): The first point as a tuple of (x, y) coordinates.
            b (tuple): The second point as a tuple of (x, y) coordinates.

        Returns:
            float: The Euclidean distance between the two points.
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
