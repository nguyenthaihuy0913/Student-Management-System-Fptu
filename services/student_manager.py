from models import Student
from utils.validator import validate_student_id


class StudentManager:
    def __init__(self, students=None):
        self._students = []
        for student in students or []:
            self.add(student)

    @property
    def students(self):
        return self._students.copy()

    def find(self, student_id):
        student_id = validate_student_id(student_id)
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None

    def add(self, student):
        if not isinstance(student, Student):
            raise ValueError("Expected a Student object.")
        if self.find(student.student_id) is not None:
            raise ValueError("Student ID already exists.")
        self._students.append(student)

    def update(self, student_id, field, value):
        student = self.find(student_id)
        if student is None:
            raise ValueError("Student not found.")
        if field == "full_name":
            student.full_name = value
        elif field == "date_of_birth":
            student.date_of_birth = value
        elif field == "gender":
            student.gender = value
        elif field == "class_name":
            student.class_name = value
        elif field == "phone":
            student.phone = value
        elif field == "email":
            student.email = value
        elif field == "status":
            student.status = value
        else:
            raise ValueError("Invalid student field.")

    def filter(self, condition):
        condition = condition.strip().lower()
        matches = []
        for student in self._students:
            if student.class_name.lower() == condition or student.status.lower() == condition:
                matches.append(student)
        return matches

    def active_students(self):
        return self.filter("Active")
