import random
from configs import Config


class EmployedBee:
    """
    A module that contains the EmployedBee class

    This module contains the EmployedBee class which represents a bee that gathers food from food sources and
    uploads it to the hive's food bank.

    Attributes:
    None
    """

    def __init__(self, name):
        """
        Initialize the employed bee object.

                Args:
                    name (str): Name of the bee.

                Attributes:
                    name (str): Name of the bee.
                    food_amount (int): Amount of food that the bee can carry during one flight.
                    current_source (FoodSource or None): The food source that the bee is currently gathering food from.
                    previous_source (FoodSource or None): The food source that the bee previously gathered food from.
                    food (int): Amount of food that the bee has currently gathered.
                    memorized_food (int): Total amount of food that the bee has gathered during all flights.
        """
        self.name = name
        self.food_amount = random.randint(1, Config.food_limit)
        self.current_source = None
        self.previous_source = None
        self.food = 0
        self.memorized_food = 0

    def fly(self, source):
        """Move the bee to a food source.

                Args:
                    source (FoodSource): The food source to move the bee to.

        """
        self.current_source = source
        if self.previous_source is None:
            self.previous_source = source
        print(self.name, ' fly to ', source.location)

    def gather(self):
        """Gather food from the current food source that the bee is at.
        """
        if self.current_source is not None:
            self.food += self.current_source.take_food(self.food_amount)
            self.previous_source = self.current_source
            self.current_source = None

    def upload_food(self, hive):
        """Upload the food that the bee has gathered to the hive's food bank.

                Args:
                    hive (Hive): The hive to upload the food to.
        """
        hive.food_bank += self.food
        self.memorized_food += self.food
        self.food = 0

    def reset_memorized_food(self):
        """Reset the amount of food that the bee has gathered in total.
        """
        self.memorized_food = 0
