from dataclasses import dataclass, field
from typing import List, Optional
import random
import math


@dataclass
class Config:
    width: int = 10
    height: int = 10
    num_food_sources: int = 5
    num_bees: int = 10
    food_range: List[int] = field(default_factory=lambda: [5, 10])
    food_limit: int = 20


@dataclass
class Hive:
    food_bank: int = 0


@dataclass
class EmployedBee:
    food_amount: int = field(init=False)
    current_source: Optional['FoodSource'] = None
    food: int = 0

    def post_init(self):
        self.food_amount = random.randint(1, Config().food_limit)

    def fly(self, source: 'FoodSource') -> None:
        self.current_source = source

    def gather(self) -> None:
        if self.current_source is not None:
            self.food += self.current_source.take_food(self.food_amount)
            self.current_source = None

    def upload_food(self, hive: Hive) -> None:
        hive.food_bank += self.food
        self.food = 0


@dataclass
class FoodSource:
    location: List[int]
    capacity: int = field(init=False)

    def post_init(self):
        self.capacity = random.randint(*Config().food_range)

    def take_food(self, amount: int) -> int:
        taken = min(amount, self.capacity)
        self.capacity -= taken
        return taken

    def quality(self, bees: List[EmployedBee], hive: Hive) -> float:
        dist = math.dist(self.location, hive.location)
        taken_food = sum(bee.food if bee.current_source == self else 0 for bee in bees)
        return (random.random() * taken_food) / dist


@dataclass
class InspectorBee:
    def send_bees(self, sources: List[FoodSource], bees: List[EmployedBee], hive: Hive) -> None:
        sources_quality = [(source, source.quality(bees, hive)) for source in sources]
        sorted_sources = sorted(sources_quality, key=lambda x: x[1], reverse=True)
        for i in range(min(len(sorted_sources), len(bees))):
            bees[i].fly(sorted_sources[i][0])


def main() -> None:
    pairs = random.sample([(i, j) for i in range(Config().width + 1) for j in range(Config().height + 1)], Config().num_food_sources)
    sources = [FoodSource(pair) for pair in pairs]
    bees = [EmployedBee() for _ in range(Config().num_bees)]
    hive = Hive()
    inspector = InspectorBee()

    food_count = sum(source.capacity for source in sources)
    print(food_count)

    while any(source.capacity > 0 for source in sources):
        for bee in bees:
            if bee.current_source is None:
                available_sources = [source for source in sources if source.capacity > 0]
                if available_sources:
                    bee.fly(random.choice(available_sources))
            bee.gather()
            bee.upload_food(hive)
        inspector.send_bees(sources, bees, hive)
        print(hive.food_bank)

    print(hive.food_bank)


if name == 'main':
    main()