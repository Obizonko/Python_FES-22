import random
from employees import BackendDev, FrontendDev, MobileDev, Lead, QA, DevOps
from product import TaskState


class Team:
    def __init__(self, owner):
        self.owner = owner
        self.product = owner.create_product()
        self.devs = []
        self.lead = Lead()
        self.qa = QA()
        self.devops = DevOps()

        self.__create_team()

    def run(self):
        days = 0
        while not self.owner.check_product(self.product):
            days += 1
            print(f"\nDay {days}")
            for dev in self.devs:
                dev.assign_task(self.product.get_task(dev.tasks_type))

            for dev in self.devs:
                dev.do_task()

            for task in self.product.tasks:
                if task.state == TaskState.NeedsReview:
                    self.lead.review(task)

            for task in self.product.tasks:
                if task.state == TaskState.ReadyForStage:
                    self.qa.test(task)

            for task in self.product.tasks:
                if task.state == TaskState.ReadyForProd:
                    self.devops.deploy(task)

    def __create_team(self):
        backend_devs_count = random.randint(1, 3)
        frontend_devs_count = random.randint(1, 3)
        mobile_devs_count = random.randint(1, 3)

        for _ in range(backend_devs_count):
            self.devs.append(BackendDev())

        for _ in range(frontend_devs_count):
            self.devs.append(FrontendDev())

        for _ in range(mobile_devs_count):
            self.devs.append(MobileDev())
