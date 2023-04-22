import random
from alg_data import AlgData


class EmployedBee:
    def __init__(self, name):
        self.bee_name = name
        self.food_amount = random.randint(1, AlgData.bee_limit)
        self.taken_food = 0
        self.all_taken_food = 0
        self.current_source = None
        self.previous_source = None

    def get_all_taken_food(self):
        temp = self.all_taken_food
        self.all_taken_food = 0
        return temp

    def fly(self, source):
        self.current_source = source
        if self.previous_source is None:
            self.previous_source = source
        print(self.bee_name, 'is flying to ', source.location)

    def _gather(self):
        self.taken_food += (self.current_source.take_food(self.food_amount) if self.current_source is not None else 0)
        if self.current_source is not None:
            print(f'{self.bee_name} is taking {self.taken_food} food dressers from {self.current_source.location}')
        self.previous_source = self.current_source
        self.current_source = None

    def offload_current_food(self, hive):
        self._gather()
        hive.food_amount += self.taken_food
        self.all_taken_food += self.taken_food
        self.taken_food = 0


class InspectorBee:
    def __init__(self):
        self.priority_sources = None

    def check_sources(self, sources, bees, hive):
        def get_quality(elem):
            return elem[1]

        sources_quality = []
        print("quality of source")
        for source in sources:
            quality = source.get_and_update_quality(bees, hive)
            sources_quality.append((source, quality))
            print(f'location: {source.location} quality: {quality}')
        self.priority_sources = sorted(sources_quality, key=get_quality, reverse=True)

    def direct_bees(self, sources, bees, hive):
        self.check_sources(sources, bees, hive)
        sources_bees = list(zip(self.priority_sources, bees))
        for source, bee in sources_bees[:min(len(sources_bees), len(bees))]:
            bee.fly(source[0])
