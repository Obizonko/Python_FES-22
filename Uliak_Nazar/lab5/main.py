from dataclasses import dataclass
from abc import ABC, abstractmethod

from datetime import datetime


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float

    @property
    def first_name(self):
        if len(self.name.split()) == 1:
            return self.name
        return self.name.split()[0]

    @property
    def second_name(self):
        if len(self.name.split()) == 1:
            return ''
        return self.name.split()[1]


class Department:
    def __init__(self,
                 title: str,
                 students: list,
                 professors: list,
                 courses: list[str], # course names
                 requests: list):
        self.title = title
        self.students = students
        self.professors = professors
        self.courses = courses
        self.requests = requests

    def proceed_requests(self):
        print(f"Proceeding requests for {self.title} department")


class Staff(ABC):
    def __init__(self, personal_info: PersonalInfo):
        self._personal_info = personal_info

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info: PersonalInfo):
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
        else:
            raise TypeError('personal_info must be a PersonalInfo object')

    @abstractmethod
    def ask_sick_leave(self, department: Department) -> bool:
        print(f"Requesting sick leave for {self.personal_info.name}")

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        print(f"Sending request to {department.title}")


class Student(Staff, ABC):
    def __init__(self, personal_info: PersonalInfo, department: Department):
        super().__init__(personal_info)
        self.department = department
        self.average_grade = 0.0

    def ask_sick_leave(self, department: Department) -> bool:
        pass

    def send_request(self, department: Department) -> bool:
        pass


class PostgraduateStudent(Staff, ABC):
    def __init__(self, personal_info: PersonalInfo, department: Department, phd_status: str):
        super().__init__(personal_info)
        self.department = department
        self.phd_status = phd_status

    def ask_sick_leave(self, department: Department) -> bool:
        pass

    def send_request(self, department: Department) -> bool:
        pass


class Professor(Staff, ABC):
    def __init__(self, personal_info: PersonalInfo, department: Department):
        super().__init__(personal_info)
        self.department = department
        self.courses = []
        self.seminars = []

    def ask_sick_leave(self, department: Department) -> bool:
        pass

    def send_request(self, destination: Department) -> bool:
        pass

    def add_postgraduate_student(self, student: PostgraduateStudent) -> None:
        pass

    def request_support(self) -> None:
        pass


class Seminar:
    def __init__(self,
                 id: int,
                 title: str,
                 deadline: datetime,
                 assignments: list[dict],
                 status,
                 related_course: str):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.assignments = assignments
        self.status = status
        self.related_course = related_course

    def __str__(self):
        return f"{self.id}: {self.title}"

    def implement_item(self, item_name: str) -> str:
        pass

    def add_comment(self, comment: str) -> None:
        pass


class Course:
    def __init__(self, seminars: list[Seminar], students: list[Student]):
        self.seminars = seminars
        self.students = students


class Enrollment:
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
        self.grade = 0.0

    def enroll(self) -> None:
        if self.student in self.course.students:
            raise Exception('Student already enrolled')
        self.course.students.append(self.student)

    def unenroll(self) -> None:
        if self.student not in self.course.students:
            raise Exception('Student not enrolled')
        self.course.students.remove(self.student)


if __name__ == '__main__':
    # Create a PersonalInfo object
    personal_info = PersonalInfo(
        id=1,
        name="Jane Smith",
        address="456 Oak St",
        phone_number="555-5678",
        email="jane.smith@example.com",
        position=2,
        rank="Assistant",
        salary=60000.0
    )

    # Create a Department object
    department = Department(
        title="Computer Engineering",
        students=[],
        professors=[],
        courses=["Data Structures", "Computer Networks"],
        requests=[]
    )

    # Create a Student object
    student = Student(personal_info, department)
    student.average_grade = 90.0

    # Create a PostgraduateStudent object
    postgrad_student = PostgraduateStudent(personal_info, department, phd_status="Completed")

    # Create a Professor object
    professor = Professor(personal_info, department)

    # Create a Seminar object
    seminar = Seminar(
        id=1,
        title="Advanced Algorithms",
        deadline=datetime(2023, 6, 15),
        assignments=[{"name": "Assignment 1", "grade": 95}],
        status="Active",
        related_course="Data Structures"
    )

    # Create a Course object
    course = Course(seminars=[seminar], students=[student])

    # Create an Enrollment object
    enrollment = Enrollment(student, course)
    enrollment.grade = 95.0
    # enrollment.unenroll()

    # Print some information
    print("\nStudent Name:", student.personal_info.name)
    print("Department Title:", department.title)
    print("\nCourse Seminars:")
    for seminar in course.seminars:
        print(seminar)
    print("\nEnrolled Students:")
    for student in course.students:
        print(student.personal_info.name)
    print("\nEnrollment Grade:", enrollment.grade)
