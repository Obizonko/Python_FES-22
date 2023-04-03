import random
from configs import Config, Hive
from employed_bee import EmployedBee
from food_source import FoodSource
from inspector_bee import InspectorBee


def main():
    grid = [[i, j] for i in range(Config.width + 1)
            for j in range(Config.height + 1)]
    print(grid)
    pairs = random.sample(grid, Config.num_food_sources)
    print(pairs)
    sources = [FoodSource(pair) for pair in pairs]
    bees = [EmployedBee(_) for _ in range(Config.num_bees)]
    hive = Hive()
    inspector = InspectorBee()

    food_count = 0
    for source in sources:
        food_count += source.capacity
    print(food_count)

    while any([source.capacity > 0 for source in sources]):
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


if __name__ == '__main__':
    main()
