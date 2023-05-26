import random
from typing import Tuple, Any

from HiveModule.helper import ab_distance


class Hive:
    """A hive where bees live and work."""
    def __init__(self):
        self.position = (0, 0)
        self.food_bank = 0
        self.employed_bees = []
        self.inspector_bee = None


class EmployedBee:
    """A bee that works for the hive"""
    def __init__(self, id: int = 0):
        self.id = id
        self.position = (0, 0)
        self.max_food_capacity = random.randint(1, 10)
        self.food_amout = 0
        self.target_food_source = None

    def fly(self, position, food_source=None):
        """
        Move bee to the given position.
        """
        # This function makes the bee fly to the source
        self.position = position
        self.target_food_source = food_source

    def gather(self) -> tuple[int, Any]:
        """
        Gather food from the target food source.
        """
        self.food_amout = min(self.max_food_capacity, self.target_food_source.food_amount)
        self.target_food_source.food_amount -= self.food_amout
        self.target_food_source.taken_food += self.food_amout
        previous_target = self.target_food_source
        self.target_food_source = None
        return self.food_amout, previous_target
            
    def upload_food(self, hive):
        """
        Upload food to the hive.
        """
        hive.food_bank += self.food_amout
        uploaded_food = self.food_amout
        self.food_amout = 0
        return uploaded_food


class InspectorBee:
    """A bee that checks the quality of the honey"""
    def __init__(self):
        pass

    @staticmethod
    def check_honey(source, all_taken_food) -> float:
        """Check the quality of the honey in the source.
        Return a number between 0 and 1, where 0 is the worst and 1 is the best.
        """
        source_quality = round(random.random() * all_taken_food / ab_distance((0, 0), source.position), 3)
        return source_quality
