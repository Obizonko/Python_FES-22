import math
import random
from typing import Any

from constants import Constants, PlayGround


class EmployedBee:
    food: int
    current_source: None
    food_amount: int

    def __init__(self):
        self.food_amount = random.randint(1, Constants.food_limit)
        self.current_source = None
        self.food = 0

    def gather(self):
        assert isinstance(self.current_source, object)
        if self.current_source is not None:
            self.food += self.current_source.take_food(self.food_amount)
            self.current_source = None

    def fly(self, source):
        self.current_source = source

    def upload_food(self, hive):
        hive.food_bank += self.food
        self.food = 0


class FoodSource:
    capacity: int

    def __init__(self, location):
        self.location = location
        self.capacity = random.randint(*Constants.food_range)

    def take_food(self, amount):
        if amount > self.capacity:
            amount = self.capacity
        self.capacity -= amount
        return amount

    def quality(self, bees, hive):
        distance = math.sqrt((self.location[0] - hive.location[0]) ** 2 + (self.location[1] - hive.location[1]) ** 2)

        taken_food = sum([bee.food if bee.current_source == self else 0 for bee in bees])
        return (random.random() * taken_food) / distance


class InspectorBee:
    def send_bees(self, sources, bees, hive):
        sources_quality: list[tuple[Any, Any]] = [(source, source.quality(bees, hive))
                                                  for source in sources]
        sorted_sources: list[tuple[Any, Any]] = sorted(
            sources_quality,
            key=lambda x: x[1],
            reverse=True)
        for i in range(min(len(sorted_sources), len(bees))):
            bees[i].fly(sorted_sources[i][0])


def main():
    matrix: list[list[int]] = [[i, j] for i in range(Constants.width + 1)
                               for j in range(Constants.height + 1)]

    pairs: object = random.sample(matrix, Constants.num_food_sources)
    sources = []
    for pair in pairs:
        sources.append(FoodSource(pair))
    bees = [EmployedBee() for _ in range(Constants.num_bees)]
    hive = PlayGround()
    inspector: InspectorBee = InspectorBee()

    food_count: int = 0
    for source in sources:
        food_count += source.capacity
    print(food_count)

    while any([source.capacity > 0 for source in sources]):
        for bee in bees:
            if bee.current_source is None:
                available_sources: list[FoodSource] = [
                    source for source in sources if source.capacity > 0]
                if available_sources:
                    bee.fly(random.choice(available_sources))
            bee.gather()
            bee.upload_food(hive)
        inspector.send_bees(sources, bees, hive)

        print(hive.food_bank)

    print(hive.food_bank)


main()
