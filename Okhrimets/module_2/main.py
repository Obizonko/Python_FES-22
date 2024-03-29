class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.tasks = []

    def develop_software(self, software):
        print(f"{self.name} is developing {software}.")

    def debug_software(self, software):
        print(f"{self.name} is debugging {software}.")

    def acquire_skill(self, new_skill):
        self.skills.append(new_skill)
        print(f"{self.name} acquired a new skill: {new_skill}.")

    def write_code(self, software):
        print(f"{self.name} is writing code for {software}.")

    def __str__(self):
        return self.name

    def review_code(self, software):
        print(f"{self.name} is reviewing code for {software}.")

    def deploy_software(self, software, environment):
        print(f"{self.name} is deploying {software} to {environment}.")

    def assign_task(self, task):
        self.tasks.append(task)
        print(f"{self.name} has been assigned a new task: {task}.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"{self.name} has completed the task: {task}.")
        else:
            print(f"{self.name} does not have the task: {task}.")

    def get_tasks(self):
        return self.tasks.copy()

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)
        print(f"{self.name} has updated skills: {', '.join(new_skills)}.")


class SoftwareComponent:
    def __init__(self, name):
        self.name = name

    def develop(self, team):
        for member in team:
            if isinstance(member, Developer):
                member.develop_software(self.name)

    def test(self, qa_team):
        for member in qa_team:
            if isinstance(member, QA):
                member.test_software(self.name)


class SoftwareArchitect:
    def __init__(self, name):
        self.name = name

    def design_software(self, software):
        print(f"{self.name} is designing {software}.")

    def __str__(self):
        return self.name

    def review_code(self, software):
        print(f"{self.name} is reviewing code for {software}.")

    def coordinate_team(self, team):
        print(f"{self.name} is coordinating the team: {', '.join(str(member) for member in team)}.")

    def delegate_task(self, task, developer):
        print(f"{self.name} is delegating {task} to {developer}.")
        developer.assign_task(task)

    def provide_feedback(self, developer, feedback):
        print(f"{self.name} is providing feedback to {developer}: {feedback}.")
        developer.review_code(feedback)


class BusinessAnalyst:
    def __init__(self, name):
        self.name = name

    def analyze_requirements(self):
        print(f"{self.name} is analyzing requirements.")

    def __str__(self):
        return self.name

    def prioritize_requirements(self):
        print(f"{self.name} is prioritizing requirements.")

    def coordinate_team(self, team):
        print(f"{self.name} is coordinating the team: {', '.join(str(member) for member in team)}.")

    def document_requirements(self):
        print(f"{self.name} is documenting requirements.")


class TeamLead:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def coordinate_team(self):
        print(f"{self.name} is coordinating the team: {', '.join(str(member) for member in self.team)}.")

    def __str__(self):
        return self.name

    def assign_task(self, developer, task):
        print(f"{self.name} is assigning {task} to {developer}.")

    def review_code(self, software):
        print(f"{self.name} is reviewing code for {software}.")


class QA:
    def __init__(self, name):
        self.name = name

    def test_software(self, software):
        print(f"{self.name} is testing {software}.")

    def __str__(self):
        return self.name

    def write_tests(self, software):
        print(f"{self.name} is writing tests for {software}.")

    def coordinate_team(self, team):
        print(f"{self.name} is coordinating the team: {', '.join(str(member) for member in team)}.")

    def report_bug(self, software, bug):
        print(f"{self.name} is reporting a bug in {software}: {bug}.")


class MobileApp(SoftwareComponent):
    def __init__(self, name, platform):
        super().__init__(name)
        self.platform = platform


class WebApp(SoftwareComponent):
    def __init__(self, name, backend, frontend):
        super().__init__(name)
        self.backend = backend
        self.frontend = frontend


class DatabaseAPI(SoftwareComponent):
    def __init__(self, name):
        super().__init__(name)

    def optimize_queries(self):
        print(f"Optimizing queries for {self.name}.")

    def backup_data(self):
        print(f"Backing up data for {self.name}.")

    def restore_data(self):
        print(f"Restoring data for {self.name}.")

    def create_table(self, table_name):
        print(f"Creating table {table_name} in {self.name}.")

    def delete_table(self, table_name):
        print(f"Deleting table {table_name} from {self.name}.")


class Containerization(SoftwareComponent):
    def __init__(self, name):
        super().__init__(name)

    def build_image(self):
        print(f"Building image for {self.name}.")

    def push_image(self, registry):
        print(f"Pushing image of {self.name} to {registry}.")

    def deploy_container(self, environment):
        print(f"Deploying container for {self.name} to {environment}.")

class Deployment(SoftwareComponent):
    def __init__(self, name):
        super().__init__(name)

    def deploy(self, environment):
        print(f"Deploying {self.name} to {environment}.")

    def rollback(self, environment):
        print(f"Rolling back {self.name} deployment in {environment}.")

    def scale_up(self, environment, instances):
        print(f"Scaling up {self.name} deployment in {environment} to {instances} instances.")

    def scale_down(self, environment, instances):
        print(f"Scaling down {self.name} deployment in {environment} to {instances} instances.")



class SoftwareDevelopmentPipeline:
    def __init__(self):
        self.pipeline = []

    def add_component(self, component):
        self.pipeline.append(component)

    def execute_pipeline(self, team, qa_team):
        for component in self.pipeline:
            print(f"Working on {component.name}:")

            if isinstance(component, (MobileApp, WebApp)):
                architect = next((member for member in team if isinstance(member, SoftwareArchitect)), None)
                if architect:
                    architect.design_software(component.name)

                analyst = next((member for member in team if isinstance(member, BusinessAnalyst)), None)
                if analyst:
                    analyst.analyze_requirements()

            component.develop([member for member in team if isinstance(member, Developer)])
            component.test([member for member in qa_team if isinstance(member, QA)])
            print()


def main():
    # Create Developer objects
    developer1 = Developer("oksana", ["Python", "JavaScript"])
    developer2 = Developer("Karina", ["Java", "C++"])

    # Create other team members
    architect = SoftwareArchitect("Ira")
    analyst = BusinessAnalyst("Eva")
    lead = TeamLead("Sofia", [developer1, developer2])

    # Create software components
    mobile_app = MobileApp("Mobile App", "iOS")
    web_app = WebApp("Web App", "Django", "React")
    database_api = DatabaseAPI("Database API")
    containerization = Containerization("Containerization")
    deployment = Deployment("Deployment")

    # Assign tasks to developers
    lead.assign_task(developer1, "Implement login feature")
    lead.assign_task(developer2, "Write unit tests")

    # Developer performs tasks
    developer1.develop_software(mobile_app)
    developer1.write_code(mobile_app)
    developer2.write_code(web_app)
    developer2.develop_software(web_app)
    developer1.debug_software(mobile_app)
    developer2.acquire_skill("HTML")
    developer1.complete_task("Implement login feature")

    # Architect reviews code
    architect.review_code(mobile_app)
    architect.design_software(web_app)

    # Business Analyst analyzes requirements
    analyst.analyze_requirements()
    analyst.document_requirements()

    # Team Lead coordinates team
    lead.coordinate_team()

    # QA team tests software
    qa1 = QA("mariia")
    qa2 = QA("Emma")
    qa_team = [qa1, qa2]
    web_app.test(qa_team)

    # QA reports bugs
    qa1.report_bug(web_app, "Invalid user input")
    qa2.write_tests(web_app)

    # Database API performs tasks
    database_api.optimize_queries()
    database_api.backup_data()

    # Containerization performs tasks
    containerization.build_image()
    containerization.push_image("Docker Hub")
    containerization.deploy_container("Production")

    # Deployment performs tasks
    deployment.deploy("Production")
    deployment.rollback("Production")
    deployment.scale_up("Staging", 3)
    deployment.scale_down("Staging", 1)


# Call the main function
if __name__ == "__main__":
    main()