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

    def add(self, data):
        self.log.append(data)

    def get(self):
        return self.log


class Simulation:
    def __init__(self):
        self.log = Log()
        self.grid = Grid(Config.width, Config.height)
        self.food_sources = self._create_food_sources()
        self.bees = [EmployedBee(i) for i in range(Config.num_bees)]
        self.hive = Hive()
        self.inspector = InspectorBee()

    def _create_food_sources(self):
        pairs = random.sample(self.grid.locations, Config.num_food_sources)
        self.log.add({"pairs": pairs})
        return [FoodSource(pair) for pair in pairs]

    def run(self):
        self.log.add({"size of matrix": f'width: {self.grid.width} | height: {self.grid.height}'})
        self.log.add({"sum": sum(source.capacity for source in self.food_sources)})
        while any(source.capacity > 0 for source in self.food_sources):
            for bee in self.bees:
                if bee.current_source is None:
                    available_sources = [source for source in self.food_sources if source.capacity > 0]
                    if available_sources:
                        self.log.add({'bee direction': bee.fly(random.choice(available_sources))})
                bee.gather()
                bee.upload_food(self.hive)
            self.inspector.send_bees(self.food_sources, self.bees, self.hive)
            self.log.add({"food in hive": self.hive.food_bank})
        self.log.add(self.hive.food_bank)

    def get_log(self):
        return self.log.get()
