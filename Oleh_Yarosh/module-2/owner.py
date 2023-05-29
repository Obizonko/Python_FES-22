import random
from product import Product, Task, TaskType, TaskState


class Owner:
    def create_product(self) -> Product:
        tasks = [
            Task('bt-1', TaskType.BACKEND),
            Task('bt-2', TaskType.BACKEND),
            Task('bt-3', TaskType.BACKEND),
            Task('ft-1', TaskType.FRONTEND),
            Task('ft-2', TaskType.FRONTEND),
            Task('mt-1', TaskType.MOBILE),
            Task('mt-2', TaskType.MOBILE),
            Task('mt-3', TaskType.MOBILE)
        ]
        return Product(tasks)

    def check_product(self, product: Product) -> bool:
        for task in product.tasks:
            if task.state not in [TaskState.Stage, TaskState.Prod]:
                return False

        print('Product is ready for Stage')
        return True
