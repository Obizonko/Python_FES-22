import random
from alg_data import AlgData
from bees_colony import EmployedBee, InspectorBee
from food_source import FoodSource, Hive


class Simulation:
    def __init__(self):
        self.matrix = None
        self.food_have_sources = None
        self.bees = None
        self.hive = None
        self.inspector_bee = None

    def _create_grid(self):
        self.matrix = [[i, j] for i in range(AlgData.y + 1)
                       for j in range(AlgData.x + 1)]

    def _create_food_sources(self):
        pairs = random.sample(self.matrix, AlgData.food_sources_amount)
        self.food_have_sources = [FoodSource(pair) for pair in pairs]
        print("source with food:")
        for source in self.food_have_sources:
            print(f'location: {source.location} | amount of food: {source.food_amount}')
    def _create_bees(self):
        self.bees = [EmployedBee(_) for _ in range(AlgData.bees_amount)]
        self.inspector_bee = InspectorBee()

    def _create_hive(self):
        self.hive = Hive()

    def get_source_food_amount(self):
        food_num = 0
        for source in self.food_have_sources:
            food_num += source.food_amount
        return food_num

    def send_bee_to_source(self, bee):
        available_sources = [source for source in self.food_have_sources if source.food_amount > 0]
        bee.fly(random.choice(available_sources)) if available_sources else None

    def _run_cycle(self):
        print("the cycle is working")
        for _ in range(AlgData.iteration_limit):
            print("iteration: ", _)
            for bee in self.bees:
                if bee.current_source is None:
                    self.send_bee_to_source(bee)
                bee.offload_current_food(self.hive)
            self.inspector_bee.direct_bees(self.food_have_sources, self.bees, self.hive)
            print(f'amount the foods in the bank: {self.hive.food_amount}')

    def run_simulation(self):
        s._create_grid()
        s._create_food_sources()
        s._create_bees()
        s._create_hive()
        print(f'amount the available food: {self.get_source_food_amount()}')
        s._run_cycle()


s = Simulation()
s.run_simulation()
