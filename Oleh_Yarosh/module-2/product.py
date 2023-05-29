from enum import Enum


class TaskState(Enum):
    Stage = None
    ToDo = 0
    InProgress = 1
    NeedsReview = 2
    ReadyForStage = 3
    ReadyForProd = 4
    Prod = 5


class TaskType(Enum):
    BACKEND = 'Backend'
    FRONTEND = 'Frontend'
    MOBILE = 'Mobile'
    ANY = 'Any'


class Task:
    def __init__(self, name: str, task_type: TaskType):
        self.name = name
        self.type = task_type
        self.state = TaskState.ToDo


class Product:
    def __init__(self, tasks: list[Task]):
        self.tasks = tasks

    def get_task(self, task_type: TaskType) -> Task:
        for task in self.tasks:
            if (task.type == task_type or task_type == TaskType.ANY)\
                    and task.state == TaskState.ToDo:
                task.state = TaskState.InProgress
                return task
        return None