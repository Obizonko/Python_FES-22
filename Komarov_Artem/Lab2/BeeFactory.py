import random
import math

from Komarov_Artem.Lab2.constants import Config, Hive


class EmployedBee:
    def __init__(self, food_amount):
        self.food_amount = food_amount
        self.current_source = None

    def fly(self, source):
        self.current_source = source
        distance = math.sqrt((source[0] ** 2) + (source[1] ** 2))
        return distance

    def gather(self):
        return random.randint(1, self.food_amount)

    def upload_food(self, hive):
        hive.upload_food(self.current_source, self.gather())


class InspectorBee:
    def __init__(self):
        pass

    def evaluate_source(self, source, bees):
        total_food = sum([bee.gather() for bee in bees])
        distance = math.sqrt((source[0] ** 2) + (source[1] ** 2))
        quality = random.random() * total_food / distance
        return quality


class BeeColony:
    def __init__(self):
        self.hive = Hive()
        self.food_sources = []
        self.employed_bees = []
        self.inspector_bee = InspectorBee()

    def generate_food_sources(self):
        coords = [(x, y) for x in range(Config.width) for y in range(Config.height)]
        self.food_sources = random.sample(coords, Config.num_food_sources)
        self.food_sources = [(source, random.randint(*Config.food_amount_range)) for source in self.food_sources]

    def generate_employed_bees(self):
        for i in range(Config.num_employed_bees):
            food_amount = random.randint(1, min([source[1] for source in self.food_sources]))
            self.employed_bees.append(EmployedBee(food_amount))

    def process_sources(self):
        iterations = 0
        while self.food_sources and iterations < 1000:
            for source, food_amount in self.food_sources:
                bees_for_source = random.randint(1, min(Config.max_bees_per_source, len(self.employed_bees)))
                bees = random.sample(self.employed_bees, bees_for_source)
                for bee in bees:
                    distance = bee.fly(source)
                    if distance > 0:
                        bee.upload_food(self.hive)
                self.inspector_bee.evaluate_source(source, bees)
                if self.hive.food_bank.get(source, 0) == food_amount:
                    self.food_sources.remove((source, food_amount))
                elif self.hive.food_bank.get(source, 0) > food_amount:
                    self.hive.food_bank[source] = food_amount
            iterations += 1

    def run(self):
        self.generate_food_sources()
        self.generate_employed_bees()
        for i in range(Config.num_iterations):
            print(f"Iteration {i + 1}:")
            self.process_sources()
            for source, food_amount in self.food_sources:
                print(f"Food source at {source} has {food_amount} units of food.")
            for bee in self.employed_bees:
                print(f"Bee with {bee.food_amount} units of food is at source {bee.current_source}.")
            print("Hive food bank:")
            for source, food_amount in self.hive.food_bank.items():
                print(f"  {source}: {food_amount}")


x = BeeColony()
x.run()