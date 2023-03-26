import random
import math
from configs import Config, Hive


class EmployedBee:
    def __init__(self):
        self.food_amount = random.randint(1, Config.food_limit)
        self.current_source = None
        self.food = 0

    def fly(self, source):
        self.current_source = source

    def gather(self):
        if self.current_source is not None:
            self.food += self.current_source.take_food(self.food_amount)
            self.current_source = None

    def upload_food(self, hive):
        hive.food_bank += self.food
        self.food = 0


class FoodSource:
    def __init__(self, location):
        self.location = location
        self.capacity = random.randint(*Config.food_range)

    def take_food(self, amount):
        if amount > self.capacity:
            amount = self.capacity
        self.capacity -= amount
        return amount

    def quality(self, bees, hive):
        dist = distance(self.location, hive.location)
        taken_food = sum([bee.food if bee.current_source ==
                         self else 0 for bee in bees])
        return (random.random() * taken_food) / dist


class InspectorBee:
    def send_bees(self, sources, bees, hive):
        sources_quality = [(source, source.quality(bees, hive))
                           for source in sources]
        sorted_sources = sorted(
            sources_quality,
            key=lambda x: x[1],
            reverse=True)
        for i in range(min(len(sorted_sources), len(bees))):
            bees[i].fly(sorted_sources[i][0])


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def main():
    grid = [[i, j] for i in range(Config.width + 1)
            for j in range(Config.height + 1)]
    pairs = random.sample(grid, Config.num_food_sources)
    sources = [FoodSource(pair) for pair in pairs]
    bees = [EmployedBee() for _ in range(Config.num_bees)]
    hive = Hive()
    inspector = InspectorBee()

    food_count = 0
    for source in sources:
        food_count += source.capacity
    print(food_count)

    while any([source.capacity > 0 for source in sources]):
        for bee in bees:
            if bee.current_source is None:
                available_sources = [
                    source for source in sources if source.capacity > 0]
                if available_sources:
                    bee.fly(random.choice(available_sources))
            bee.gather()
            bee.upload_food(hive)
        inspector.send_bees(sources, bees, hive)
        print(hive.food_bank)

    print(hive.food_bank)


main()
