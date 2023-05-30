from abc import ABC, abstractmethod

class Developer:
    def __init__(self, name, skills, boos):
        self.name = name
        self.skills = skills
        self.current_tasks = []
        self.boss = boos

    def write_code(self, software):
        print(f"{self.name} is writing code for {software.name}")

    def debug_code(self, software):
        print(f"{self.name} is debugging code for {software.name}")

    def add_tasks(self, tasks):
        for task in tasks:
            self.current_tasks.append(task)

        print(f'{self.name} was given task: {" ".join(tasks)} and started write code')

    def complete_task(self, task):
        self.current_tasks.remove(task)
        print(f'{self.name} was completed task: {task}')
        self.boss.report(task)

    def set_boss(self, software_architect):
        self.boss = software_architect

    def get_boss_name(self):
        return self.boss.name


class SoftwareArchitect:
    def __init__(self, name):
        self.name = name

    def design_system(self):
        print(f"{self.name} is designing the system architecture")

    def review_code(self):
        print(f"{self.name} is reviewing the code")

    def review_task(self, task):
        print(f"{self.name} is reviewing task: {task}")

    def report(self, task):
        self.review_task(task)


class TeamLead:
    def __init__(self, name):
        self.name = name

    def assign_tasks(self, developer, tasks):
        print(f'{self.name} is assigning tasks: {" ".join(tasks)} to developers: {developer.name}')
        developer.add_tasks(tasks)

class QA:
    def __init__(self, name):
        self.name = name

    def test_software(self, software):
        print(f"{self.name} is testing {software}")


class BusinessAnalyst:
    def __init__(self, name):
        self.name = name

    def gather_requirements(self):
        print(f"{self.name} is gathering project requirements")

    def analyze_data(self):
        print(f"{self.name} is analyzing project data")


class Software:
    def __init__(self, name):
        self.name = name

    def develop(self):
        print(f"Developing {self.name} software")

    def deploy(self):
        print(f"Deploying {self.name} software")


class MobileApp(Software):
    def __init__(self, name, platform, db):
        super().__init__(name)
        self.platform = platform
        self.db = db

    def develop(self):
        super().develop()
        print(f"Developing {self.name} for {self.platform} platform with {self.db.name} db")


class WebApp(Software):
    def __init__(self, name, backend, frontend, db):
        super().__init__(name)
        self.backend = backend
        self.frontend = frontend
        self.db = db

    def develop(self):
        super().develop()
        print(f"Developing {self.name} with {self.backend} backend, {self.frontend} frontend and {self.db.name} db")


class DatabaseAPI(Software, ABC):
    def __init__(self, name):
        super().__init__(name)

    def develop(self):
        super().develop()
        print(f"Developing {self.name} database API")

    @abstractmethod
    def create_table(self, name):
        pass

    @abstractmethod
    def delete_table(self, name):
        pass

    @abstractmethod
    def add_data(self, data, table_name):
        pass

    @abstractmethod
    def select_data(self, query):
        pass

    @abstractmethod
    def backup_data(self):
        pass


class MongoDB(DatabaseAPI):
    def __init__(self, name):
        super().__init__(name)

    def create_table(self, name):
        print(f'mongoDB created table {name}')

    def delete_table(self, name):
        print(f'mongoDB deleted table {name}')

    def add_data(self, data, table_name):
        print(f'mongoDB insert data into table {table_name}')

    def select_data(self, query):
        print(f'mongoDB returned query')
        return query

    def backup_data(self):
        print(f'mongoDB made a data backup')

class SQLite(DatabaseAPI):
    def __init__(self, name):
        super().__init__(name)

    def create_table(self, name):
        print(f'SQLite created table {name}')

    def delete_table(self, name):
        print(f'SQLite deleted table {name}')

    def add_data(self, data, table_name):
        print(f'SQLite insert data into table {table_name}')

    def select_data(self, query):
        print(f'SQLite returned query')
        return query

    def backup_data(self):
        print(f'SQLite made a data backup')

class Containerization(Software):
    def __init__(self, name, app):
        super().__init__(name)
        self.app = app

    def develop(self):
        super().develop()
        print(f"Developing {self.name} containerization.")


class Deployment(Software):
    def __init__(self, name, app):
        super().__init__(name)
        self.app = app

    def deploy(self):
        super().deploy()
        print(f"Deploying {self.name} software")

    def rollback(self):
        print("version rolled back")


# сreate instances of the classes
team_lead1 = TeamLead("Lead1")
architect1 = SoftwareArchitect("Architect1")
dev1 = Developer("Dev1", ["JS", "TS", "Node"], architect1)
dev2 = Developer("Dev2", ["JS", "Python", "Django"], architect1)
qa1 = QA("QA1")
business_analyst1 = BusinessAnalyst("BA1")

# give the task
team_lead1.assign_tasks(dev1, ['add feature', 'fix bug'])
architect1.design_system()
team_lead1.assign_tasks(dev2, ['make site'])
qa1.test_software("Mobile App")
dev1.complete_task('fix bug')
business_analyst1.gather_requirements()

# create instances of software components
mongo_db = MongoDB('MongoDB')
sq_lite = SQLite('SQLite3')
mobile_app = MobileApp("SomeMobApp", "Android", sq_lite)
web_app = WebApp("SomeWebApp", "PythonBackend", "JSFrontend", mongo_db)
mob_container = Containerization("MobileContainer", mobile_app)
web_container = Containerization("WebContainer", web_app)
deployment_web = Deployment("WebAppDeployment", web_app)
deployment_mobile = Deployment("MobileDeployment", mob_container)

# develop and deploy software components
mobile_app.develop()
web_app.develop()
mob_container.develop()
web_container.develop()
deployment_web.rollback()
