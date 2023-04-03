import random
from configs import Config


class EmployedBee:
    def __init__(self, name):
        self.name = name
        self.food_amount = random.randint(1, Config.food_limit)
        self.current_source = None
        self.previous_source = None
        self.food = 0
        self.memorized_food = 0

    def fly(self, source):
        self.current_source = source
        if self.previous_source is None:
            self.previous_source = source
        print(self.name, ' fly to ', source.location)

    def gather(self):
        if self.current_source is not None:
            self.food += self.current_source.take_food(self.food_amount)
            self.previous_source = self.current_source
            self.current_source = None

    def upload_food(self, hive):
        hive.food_bank += self.food
        self.memorized_food += self.food
        self.food = 0

    def reset_memorized_food(self):
        self.memorized_food = 0
