import random
from abc import ABC, abstractmethod
from product import TaskState, TaskType


class Employee(ABC):
    pass


class Dev(Employee):
    def __init__(self):
        self.current_task = None
        self.tasks_type = TaskType.ANY

    def assign_task(self, task):
        self.current_task = task

    @abstractmethod
    def do_task(self):
        pass

    def is_task_assigned(self) -> bool:
        return self.current_task is not None


class BackendDev(Dev):
    def __init__(self):
        super().__init__()
        self.tasks_type = TaskType.BACKEND

    def do_task(self):
        if not self.is_task_assigned():
            return

        task = self.current_task
        task.state = TaskState.InProgress
        print(f'Backend Dev: {task.name} - In Progress')
        task.state = TaskState.NeedsReview
        print(f'Backend Dev: {task.name} - Prepared for Review')
        self.current_task = None


class FrontendDev(Dev):
    def __init__(self):
        super().__init__()
        self.tasks_type = TaskType.FRONTEND

    def do_task(self):
        if not self.is_task_assigned():
            return

        task = self.current_task
        task.state = TaskState.InProgress
        print(f'Frontend Dev: {task.name} - In Progress')
        task.state = TaskState.NeedsReview
        print(f'Frontend Dev: {task.name} - Prepared for Review')
        self.current_task = None


class MobileDev(Dev):
    def __init__(self):
        super().__init__()
        self.tasks_type = TaskType.MOBILE

    def do_task(self):
        if not self.is_task_assigned():
            return

        task = self.current_task
        task.state = TaskState.InProgress
        print(f'Mobile Dev: {task.name} - In Progress')
        task.state = TaskState.NeedsReview
        print(f'Mobile Dev: {task.name} - Prepared for Review')
        self.current_task = None


class Lead(Employee):
    def __init__(self):
        self.current_task = None

    def review(self, task):
        if not self.__is_task_done_properly(task):
            task.state = TaskState.ToDo
            print(f'Lead: {task.name} failed review')
        else:
            task.state = TaskState.ReadyForStage
            print(f'Lead: {task.name} passed review - Ready for Stage')

    def __is_task_done_properly(self, task):
        if task.state != TaskState.NeedsReview:
            return False

        task_completeness = random.randint(1, 100)
        return task_completeness % (100 // 50) == 0


class QA(Employee):
    def test(self, task):
        if not self.__is_task_done_properly(task):
            task.state = TaskState.ToDo
            print(f'QA: {task.name} failed testing')
        else:
            task.state = TaskState.ReadyForProd
            print(f'QA: {task.name} passed testing - Ready for Prod')

    def __is_task_done_properly(self, task):
        if task.state != TaskState.ReadyForStage:
            return False

        task_completeness = random.randint(1, 100)
        return task_completeness % (100 // 25) == 0


class DevOps(Employee):
    def __deploy_to_stage(self, task):
        task.state = TaskState.Stage
        print(f'DevOps: deployed task {task.name} to stage')

    def __deploy_to_prod(self, task):
        task.state = TaskState.Prod
        print(f'DevOps: deployed task {task.name} to prod')

    def deploy(self, task):
        decision = random.randint(1, 100) % (100 // 50) == 0
        if decision:
            self.__deploy_to_stage(task)
        else:
            self.__deploy_to_prod(task)