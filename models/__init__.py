"""
Models package for Student Management System.
Exposes core entity classes: Person, Student, and Result.
"""

from models.person import Person
from models.student import Student
from models.result import Result

__all__ = ["Person", "Student", "Result"]
