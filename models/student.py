"""
Student Model
Subclass of Person representing student-specific academic information.
"""

from models.person import Person


class Student(Person):
    """Represents an enrolled student, inheriting basic demographic details from Person."""

    def __init__(
        self,
        student_id,
        full_name,
        date_of_birth,
        gender,
        class_name,
        phone,
        email,
        status="Active",
    ):
        super().__init__(full_name, date_of_birth, gender, phone, email)
        self._student_id = student_id
        self._class_name = class_name
        self._status = status

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def to_file_line(self):
        """Format student data into pipe-delimited text line for file persistence."""
        return f"{self._student_id}|{self._full_name}|{self._date_of_birth}|{self._gender}|{self._class_name}|{self._phone}|{self._email}|{self._status}\n"

    def to_dict(self):
        """Convert object attributes to dictionary representation."""
        return {
            "student_id": self._student_id,
            "full_name": self._full_name,
            "date_of_birth": self._date_of_birth,
            "gender": self._gender,
            "class_name": self._class_name,
            "phone": self._phone,
            "email": self._email,
            "status": self._status,
        }

    def __str__(self):
        return f"[{self._student_id}] {self._full_name} ({self._class_name}) - {self._status}"
