import random
from configs import Config, Hive
from employed_bee import EmployedBee
from food_source import FoodSource
from inspector_bee import InspectorBee


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.locations = [[i, j] for i in range(width + 1) for j in range(height + 1)]


class Log:
    def __init__(self):
        self.log = []

    def add_in_log(self, i):
        self.log.append(i)

    def get_log(self):
        return self.log


class Simulation:
    def __init__(self):
        self.log = Log()
        self.grid = Grid(Config.width, Config.height)
        self.food_sources = self._create_food_sources()
        self.bees = self._create_bees()
        self.hive = Hive()
        self.inspector = InspectorBee()

    def _create_food_sources(self):
        pairs = random.sample(self.grid.locations, Config.num_food_sources)
        self.log.add_in_log({"pairs": pairs})
        return [FoodSource(pair) for pair in pairs]

    def _create_bees(self):
        return [EmployedBee(_) for _ in range(Config.num_bees)]

    def run_and_get_log(self):
        self.log.add_in_log({"size of matrix": f'width: {self.grid.width} | height: {self.grid.height}'} )
        self.log.add_in_log({"food sum": sum(source.capacity for source in self.food_sources)})
        while any(source.capacity > 0 for source in self.food_sources):
            for bee in self.bees:
                if bee.current_source is None:
                    available_sources = [source for source in self.food_sources if source.capacity > 0]
                    if available_sources:
                        self.log.add_in_log({'bee direction': bee.fly(random.choice(available_sources))})
                bee.gather()
                bee.upload_food(self.hive)
            self.inspector.send_bees(self.food_sources, self.bees, self.hive)
            self.log.add_in_log({"food in hive": self.hive.food_bank})
        self.log.add_in_log(self.hive.food_bank)
        return self.log.get_log()
