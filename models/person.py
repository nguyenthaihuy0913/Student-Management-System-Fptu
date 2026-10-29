"""
Person Model
Base class representing human demographic information.
"""


class Person:
    """Represents common personal identity attributes."""

    def __init__(self, full_name, date_of_birth, gender, phone, email):
        self._full_name = full_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._phone = phone
        self._email = email

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def __str__(self):
        return f"{self._full_name} | {self._date_of_birth} | {self._gender} | {self._phone} | {self._email}"
