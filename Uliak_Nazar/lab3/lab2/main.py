import random
from lab2.cell import Cell
from lab2.parameters import parameters
from lab2.bees import EmployedBee, InspectorBee


class FoodQuality:
    cell: Cell
    quality: float

    def __init__(self, cell: Cell, quality: float) -> None:
        self.cell = cell
        self.quality = quality


class BeeAssignment:
    bee: EmployedBee
    cell: Cell

    def __init__(self, bee: EmployedBee, cell: Cell) -> None:
        self.bee = bee
        self.cell = cell


class Hive:
    __config: parameters

    __food_gathered: float = 0
    __field: list[Cell]
    __picked_cells: list[Cell]
    __cells_quality_table: list[FoodQuality]
    __employed_bees: list[EmployedBee]
    __inspector_bee: InspectorBee

    def __init__(self, config: parameters = parameters()) -> None:
        """
        Initialize hive with config
        :param config: parameters, default parameters()
        """
        self.__config = config

        self.__generate_field(self.__config.FIELD_WIDTH, self.__config.FIELD_HEIGHT)
        self.__generate_bees()

    def run(self) -> list[str]:
        logs = []

        while True:
            bee_assignments: list[BeeAssignment] = self.__assign_bees_to_cells()

            for i in range(len(bee_assignments)):
                assignment: BeeAssignment = bee_assignments[i]

                if assignment.cell is None:
                    logs.append('everything is gathered')
                    return logs

                logs.append(f'picked bee {i}')
                logs.append(f'picked cell ({assignment.cell.x}, {assignment.cell.y}) w val = {assignment.cell.val} and max_load = {assignment.cell.max_load}')

            for i in range(len(bee_assignments)):
                assignment: BeeAssignment = bee_assignments[i]

                try:
                    assignment.bee.fly(assignment.cell)
                    assignment.bee.gather()
                    logs.append(f'bee {i} gathered {assignment.bee.food_gathered} food')
                except ValueError as err:
                    logs.append(f'exception: {err}')

            for i in range(len(bee_assignments)):
                assignment: BeeAssignment = bee_assignments[i]

                food_gathered_by_bee: int = assignment.bee.upload_food()
                self.__food_gathered += food_gathered_by_bee

                food_quality: float = self.__inspector_bee.check_src_quality(food_gathered_by_bee, assignment.cell)
                logs.append(f'quality is {food_quality}')
                self.__set_quality_to_cell(assignment.cell, food_quality)

    def __generate_field(self, width: int, height: int) -> None:
        self.__field = []
        self.__cells_quality_table = []

        for h in range(height):
            for w in range(width):
                self.__field.append(Cell(w, h, random.randint(1, self.__config.EMPLOYED_AGENTS)))

        self.__picked_cells: list = random.sample(self.__field, self.__config.SOURCES)

        for i in range(len(self.__picked_cells)):
            field_cell: Cell = next((cell for cell in self.__field if
                                     cell.x == self.__picked_cells[i].x and cell.y == self.__picked_cells[i].y), None)
            field_cell.val = random.randint(self.__config.MAX_FIELD_CAPACITY / 2, self.__config.MAX_FIELD_CAPACITY)
            self.__cells_quality_table.append(FoodQuality(field_cell, float(0)))

    def __generate_bees(self) -> None:
        self.__employed_bees = []

        for i in range(self.__config.EMPLOYED_AGENTS):
            self.__employed_bees.append(EmployedBee(random.randint(1, self.__config.MAX_FIELD_CAPACITY / 4)))

        self.__inspector_bee = InspectorBee()

    def __assign_bees_to_cells(self) -> list[BeeAssignment]:
        bee_assignments: list[BeeAssignment] = []

        for i in range(len(self.__employed_bees)):
            bee_assignments.append(BeeAssignment(self.__employed_bees[i], self.__pick_cell_to_fly()))

        return bee_assignments

    def __set_quality_to_cell(self, cell: Cell, quality: float) -> None:
        for i in range(0, len(self.__cells_quality_table)):
            if self.__cells_quality_table[i].cell == cell:
                self.__cells_quality_table[i].quality = quality

    def __pick_cell_to_fly(self) -> Cell or None:
        sorted_quality_table = sorted(self.__cells_quality_table, key=lambda x: x.quality, reverse=True)

        for i in range(len(sorted_quality_table)):
            cell: Cell = sorted_quality_table[i].cell

            if cell.val == 0:
                continue

            return cell


if __name__ == '__main__':
    hive: Hive = Hive(parameters())
    hive.run()
