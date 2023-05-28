import product
import random


class Employee:
    pass


class Dev(Employee):
    current_task: product.Task

    def assign_task(self, task: product.Task):
        self.current_task = task

    def do_task(self):
        pass

    def is_task_assigned(self) -> bool:  # todo: make it private
        return self.current_task != None


class BackendDev(Dev):
    def do_task(self):
        if not super().is_task_assigned(): return
        self.current_task.state = product.TaskState.In_progress
        print(f'backend dev: {self.current_task.name} - in progress')
        self.current_task.state = product.TaskState.Needs_review
        print(f'backend dev: {self.current_task.name} - prepared for review')
        self.current_task = None


class MobileDev(Dev):
    def do_task(self):
        if not super().is_task_assigned(): return
        self.current_task.state = product.TaskState.In_progress
        print(f'mobile dev: {self.current_task.name} - in progress')
        self.current_task.state = product.TaskState.Needs_review
        print(f'mobile dev: {self.current_task.name} - prepared for review')
        self.current_task = None


class FrontendDev(Dev):
    def do_task(self):
        if not super().is_task_assigned(): return
        self.current_task.state = product.TaskState.In_progress
        print(f'frontend dev: {self.current_task.name} - in progress')
        self.current_task.state = product.TaskState.Needs_review
        print(f'frontend dev: {self.current_task.name} - prepared for review')
        self.current_task = None


class Lead(Employee):
    def review(self, task: product.Task) -> bool:
        if not self.__is_task_done_properly(task):
            task.state = product.TaskState.ToDo
            print(f'lead: {task.name} failed review')
        else:
            task.state = product.TaskState.Ready_for_stage
            print(f'lead: {task.name} passed review - ready for stage')

    def __is_task_done_properly(self, _: product.Task) -> bool:
        task_completance = random.randint(1, 100)
        return task_completance % 25 != 0


class QA(Employee):
    def test(self, task: product.Task):
        if not self.__is_task_done_properly(task):
            task.state = product.TaskState.ToDo
            print(f'qa: {task.name} failed testing')
        else:
            task.state = product.TaskState.Ready_for_prod
            print(f'qa: {task.name} passed testing - ready for prod')

    def __is_task_done_properly(self, _: product.Task) -> bool:
        task_completance = random.randint(1, 100)
        return task_completance % 20 != 0


class DevOps(Employee):
    def deploy_to_stage(self, task: product.Task):
        task.state = product.TaskState.Stage
        print(f'devops: deployed task {task.name} to stage')

    def deploy_to_prod(self, task: product.Task):
        task.state = product.TaskState.Prod
        print(f'devops: deployed task {task.name} to prod')
