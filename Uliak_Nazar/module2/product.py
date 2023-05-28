from enum import Enum


class TaskType(Enum):
    BACKEND = 0
    FRONTEND = 1
    MOBILE = 2


class TaskState(Enum):
    ToDo = 0
    In_progress = 1
    Needs_review = 2
    Ready_for_stage = 3
    Stage = 4
    Ready_for_prod = 5
    Prod = 6


class Task:
    name: str
    type: TaskType
    state: TaskState

    def __init__(self, name: str, type: TaskType) -> None:
        self.name = name
        self.type = type
        self.state = TaskState.ToDo


class Product:
    features: list[Task]

    def __init__(self, features: list[Task]) -> None:
        self.features = features