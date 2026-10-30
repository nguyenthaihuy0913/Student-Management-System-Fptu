from utils.validator import validate_name, validate_date_of_birth, validate_gender, validate_phone, validate_email



class Person:

    def __init__(self, full_name, date_of_birth, gender, phone, email):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone = phone
        self.email = email

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = validate_name(value)

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = validate_date_of_birth(value)

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = validate_gender(value)

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = validate_phone(value)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = validate_email(value)

    def __str__(self):
        return f"{self._full_name} | {self._date_of_birth} | {self._gender} | {self._phone} | {self._email}"
