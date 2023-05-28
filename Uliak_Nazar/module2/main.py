import random

import employees
import product


class Owner:
    def create_product(self) -> product.Product:
        # todo: gen random tasks

        return product.Product([
            product.Task('bt-1', product.TaskType.BACKEND),
            product.Task('bt-2', product.TaskType.BACKEND),
            product.Task('bt-3', product.TaskType.BACKEND),
            product.Task('ft-1', product.TaskType.FRONTEND),
            product.Task('ft-2', product.TaskType.FRONTEND),
            product.Task('mt-1', product.TaskType.MOBILE),
            product.Task('mt-2', product.TaskType.MOBILE),
            product.Task('mt-3', product.TaskType.MOBILE)
        ])

    def check(self, _: product.Task) -> bool:
        task_completancy = random.randint(0, 100)
        return task_completancy % 15 != 0


class Team:
    __devs: list[employees.Dev] = list[employees.Dev]()
    __lead: employees.Lead
    __qa: employees.QA
    __devops: employees.DevOps

    __owner: Owner
    __product: product.Product

    def __init__(self, owner: Owner) -> None:
        self.__owner = owner
        self.__product = owner.create_product()
        self.__create_team()

    def run(self):
        backend_devs = [d for d in self.__devs if d.__class__ == employees.BackendDev]
        frontend_devs = [d for d in self.__devs if d.__class__ == employees.FrontendDev]
        mobile_devs = [d for d in self.__devs if d.__class__ == employees.MobileDev]

        is_project_complete = False

        while not is_project_complete:
            todo_backend_tasks = [t for t in self.__product.features if
                                  t.state == product.TaskState.ToDo and t.type == product.TaskType.BACKEND]
            todo_frontend_tasks = [t for t in self.__product.features if
                                   t.state == product.TaskState.ToDo and t.type == product.TaskType.FRONTEND]
            todo_mobile_tasks = [t for t in self.__product.features if
                                 t.state == product.TaskState.ToDo and t.type == product.TaskType.MOBILE]

            self.__assign_tasks_to_devs(todo_backend_tasks, backend_devs)
            self.__assign_tasks_to_devs(todo_frontend_tasks, frontend_devs)
            self.__assign_tasks_to_devs(todo_mobile_tasks, mobile_devs)

            for dev in self.__devs:
                dev.do_task()

            self.__review()
            self.__deploy(product.TaskState.Ready_for_stage)
            self.__test()
            self.__deploy(product.TaskState.Ready_for_prod)
            self.__owner_review()

            # until all tasks are on prod and approved by owner
            is_project_complete = len([t for t in self.__product.features if t.state != product.TaskState.Prod]) == 0

    def __owner_review(self):
        tasks_on_prod = [t for t in self.__product.features if t.state == product.TaskState.Prod]
        for task in tasks_on_prod:
            is_task_approved_by_owner = self.__owner.check(task)

            if not is_task_approved_by_owner:
                print(f'onwer:  {task.name} rejected')
                task.state = product.TaskState.ToDo
            else:
                print(f'owner: {task.name} approved')

    def __review(self):
        tasks_to_review = [t for t in self.__product.features if t.state == product.TaskState.Needs_review]
        for task_to_review in tasks_to_review:
            self.__lead.review(task_to_review)

    def __deploy(self, state: product.TaskState):
        if state != product.TaskState.Ready_for_stage and state != product.TaskState.Ready_for_prod:
            raise ValueError('invalid state')

        tasks_to_deploy = [t for t in self.__product.features if t.state == state]
        if state == product.TaskState.Ready_for_stage:
            for task in tasks_to_deploy:
                self.__devops.deploy_to_stage(task)
        elif state == product.TaskState.Ready_for_prod:
            for task in tasks_to_deploy:
                self.__devops.deploy_to_prod(task)

    def __test(self):
        staged_tasks = [t for t in self.__product.features if t.state == product.TaskState.Stage]
        for staged_task in staged_tasks:
            self.__qa.test(staged_task)

    def __assign_tasks_to_devs(self, tasks: list[product.Task], devs: list[employees.Dev]):
        if len(tasks) >= len(devs):
            for i in range(len(devs)):
                devs[i].assign_task(tasks[i])
        else:
            for i in range(len(tasks)):
                devs[i].assign_task(tasks[i])

    def __create_team(self):
        self.__lead = employees.Lead()
        self.__devops = employees.DevOps()
        self.__qa = employees.QA()

        for _ in range(random.randint(1, 3)): self.__devs.append(employees.BackendDev())
        for _ in range(random.randint(1, 3)): self.__devs.append(employees.FrontendDev())
        for _ in range(random.randint(1, 3)): self.__devs.append(employees.MobileDev())

owr = Owner()
t = Team(owr)

t.run()