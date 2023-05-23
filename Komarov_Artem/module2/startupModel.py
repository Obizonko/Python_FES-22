# Base class for all team members
class TeamMember:
    def __init__(self, name):
        self.name = name

    def perform_duty(self):
        pass


# Developer class representing developers with specific skills
class Developer(TeamMember):
    def __init__(self, name, skills):
        super().__init__(name)
        self.skills = skills

    def perform_duty(self):
        print(f"{self.name} is developing software.")


# SoftwareArchitect class representing software architects
class SoftwareArchitect(TeamMember):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is designing software architecture.")


# TeamLead class representing team leads
class TeamLead(TeamMember):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is leading the team.")


# QA class representing quality assurance engineers
class QA(TeamMember):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is performing quality assurance.")


# BusinessAnalyst class representing business analysts
class BusinessAnalyst(TeamMember):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is analyzing the business requirements.")


# Software class representing the general software
class Software:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def develop(self):
        for component in self.components:
            component.perform_duty()


# MobileApp class representing the mobile app component
class MobileApp:
    def __init__(self):
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def remove_developer(self, developer):
        self.developers.remove(developer)

    def perform_duty(self):
        for developer in self.developers:
            developer.perform_duty()


# WebApp class representing the web app component
class WebApp:
    def __init__(self):
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def remove_developer(self, developer):
        self.developers.remove(developer)

    def perform_duty(self):
        for developer in self.developers:
            developer.perform_duty()


# DatabaseAPI class representing the database API component
class DatabaseAPI:
    def __init__(self):
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def remove_developer(self, developer):
        self.developers.remove(developer)

    def perform_duty(self):
        for developer in self.developers:
            developer.perform_duty()


# Containerization class representing the containerization component
class Containerization:
    def __init__(self):
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def remove_developer(self, developer):
        self.developers.remove(developer)

    def perform_duty(self):
        for developer in self.developers:
            developer.perform_duty()


# Deployment class representing the deployment component
class Deployment:
    def __init__(self):
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def remove_developer(self, developer):
        self.developers.remove(developer)

    def perform_duty(self):
        for developer in self.developers:
            developer.perform_duty()


# Usage example
# Create team members
developer1 = Developer("John", ["Python", "JavaScript"])
developer2 = Developer("Alice", ["Java", "C++"])
architect = SoftwareArchitect("Bob")
team_lead = TeamLead("Mike")
qa = QA("Sarah")
business_analyst = BusinessAnalyst("Emily")

# Create software components
mobile_app = MobileApp()
web_app = WebApp()
database_api = DatabaseAPI()
containerization = Containerization()
deployment = Deployment()

# Add developers to software components
mobile_app.add_developer(developer1)
web_app.add_developer(developer1)
web_app.add_developer(developer2)
database_api.add_developer(developer2)
containerization.add_developer(developer1)
deployment.add_developer(developer2)

# Create the software
software = Software()
software.add_component(mobile_app)
software.add_component(web_app)
software.add_component(database_api)
software.add_component(containerization)
software.add_component(deployment)

# Develop the software
software.develop()
