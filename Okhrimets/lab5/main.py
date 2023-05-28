from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PersonalInfo:
    full_name: str
    age: int
    email: str

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name: str):
        self.full_name = full_name

    @property
    def name(self):
        first_name, last_name = self.full_name.split("_")
        return first_name, last_name

    def get_age(self):
        return self.age

    def set_age(self, age: int):
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email: str):
        self.email = email


class Staff(ABC):
    def __init__(self, personal_info):
        self._personal_info = personal_info

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, value):
        if isinstance(value, PersonalInfo):
            self._personal_info = value
        else:
            raise ValueError("personal_info must be an instance of PersonalInfo")

    def get_personal_info(self):
        return self._personal_info

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class PostgraduateStudent(Staff):
    def __init__(self, personal_info, phd_status):
        super().__init__(personal_info)
        self.phd_status = phd_status

    def method1(self):
        # Implementation of method1
        pass

    def method2(self):
        # Implementation of method2
        pass

    def get_phd_status(self):
        return self.phd_status

    def set_phd_status(self, phd_status: str):
        self.phd_status = phd_status


class Student(Staff):
    def __init__(self, personal_info):
        super().__init__(personal_info)
        self.courses = []
        self.assignments = []
        self.grades = {}

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses

    def submit_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments

    def view_grades(self):
        return self.grades

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if self.grades:
            total_grades = sum(self.grades.values())
            average_grade = total_grades / len(self.grades)
            return average_grade
        else:
            return 0.0

    def method1(self):
        # Implementation of method1
        pass

    def method2(self):
        # Implementation of method2
        pass

class Seminar:
    def __init__(self, seminar_id):
        self.seminar_id = seminar_id
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def remove_attendee(self, attendee):
        self.attendees.remove(attendee)

    def get_attendees(self):
        return self.attendees

    def get_average_attendance(self):
        if self.attendees:
            total_attendance = len(self.attendees)
            return total_attendance / len(self.attendees)
        else:
            return 0.0


class Course:
    def __init__(self, course_id):
        self.course_id = course_id
        self.seminar_list = []
        self.professors = []
        self.students = []

    def add_seminar(self, seminar):
        self.seminar_list.append(seminar)

    def remove_seminar(self, seminar):
        self.seminar_list.remove(seminar)

    def get_seminars(self):
        return self.seminar_list

    def enroll_student(self, student):
        self.students.append(student)

    def drop_student(self, student):
        self.students.remove(student)

    def get_enrolled_students(self):
        return self.students

    def add_professor(self, professor):
        if isinstance(professor, Professor):
            if professor not in self.professors:
                self.professors.append(professor)
            else:
                print(f"Professor {professor.personal_info.name} is already assigned to the course.")
        else:
            raise ValueError("professor must be an instance of Professor")

    def remove_professor(self, professor):
        if professor in self.professors:
            self.professors.remove(professor)
        else:
            print(f"Professor {professor.personal_info.name} is not assigned to the course.")

    def get_assigned_professors(self):
        return self.professors

    def get_students(self):
        return self.students


class Department:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def remove_professor(self, professor):
        self.professors.remove(professor)

    def get_students(self):
        return self.students

    def get_professors(self):
        return self.professors

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def enroll_student(self):
        self.course.enroll_student(self.student)

    def unenroll_student(self):
        self.course.drop_student(self.student)

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course


class Professor(Staff):
    def __init__(self, personal_info):
        super().__init__(personal_info)
        self.students = []

    def method1(self):
        # Implementation of method1
        pass

    def method2(self):
        # Implementation of method2
        pass

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_students(self):
        return self.students

    def remove_all_students(self):
        self.students = []


def main():
    # Create personal info objects
    personal_info1 = PersonalInfo("Oksana", 25, "oksana@gmail.com")
    personal_info2 = PersonalInfo("masha", 30, "masha@gmail.com")

    # Create staff objects
    postgrad_student = PostgraduateStudent(personal_info1, "PhD Candidate")
    student = Student(personal_info1)
    professor = Professor(personal_info2)

    # Create department object
    department = Department()

    # Add staff and students to the department
    department.add_student(student)
    department.add_professor(professor)

    # Create a course
    course = Course("CS101")

    # Add the course to the department
    department.add_course(course)

    # Enroll a student in a course
    enrollment = Enrollment(student, course)
    enrollment.enroll_student()

    # Add a seminar to the course
    seminar = Seminar("Seminar1")
    course.add_seminar(seminar)

    # Add a professor to the course
    course.add_professor(professor)

    # Add a student to the professor's list
    professor.add_student(student)

    # Print department information
    print("Department students:")
    for student in department.get_students():
        print(student.personal_info.get_full_name())

    print("Department professors:")
    for professor in department.get_professors():
        print(professor.personal_info.get_full_name())

    print("Department courses:")
    for course in department.get_courses():
        print(course.course_id)

    # Print course information
    print("Course seminars:")
    for seminar in course.get_seminars():
        print(seminar.seminar_id)

    print("Course professors:")
    for professor in course.get_assigned_professors():
        print(professor.personal_info.get_full_name())

    print("Course students:")
    for student in course.get_students():
        print(student.personal_info.get_full_name())


if __name__ == "__main__":
    main()