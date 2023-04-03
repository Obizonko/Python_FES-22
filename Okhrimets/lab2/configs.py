

class Config:
    height = 10
    width = 10
    num_food_sources = 5
    food_amount_range = (10, 50)
    max_bees_per_source = 5
    num_employed_bees = 3
    num_iterations = 10


class Hive:
    def __init__(self):
        self.food_bank = {}

    def upload_food(self, source, food_amount):
        if source in self.food_bank:
            self.food_bank[source] += food_amount
        else:
            self.food_bank[source] = food_amount
