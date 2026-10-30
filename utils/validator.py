import re
from datetime import datetime

VALID_PREFIXES = ["SE", "SS", "SA", "SB", "DE", "DA", "DS", "HE", "HA", "HS", "QE", "QA", "QS", "CE", "CA", "CS"]


def validate_text(value):
    if value is None:
        raise ValueError("A value is required.")
    value = str(value).strip()
    if not value or any(char in value for char in "|\n\r\t"):
        raise ValueError("Text is required and cannot contain | or control characters.")
    return value


def validate_student_id(value):
    value = validate_text(value).upper()
    if not re.fullmatch(r"[A-Z]{2}[0-9]{6}", value) or value[:2] not in VALID_PREFIXES:
        raise ValueError("Student ID must use an allowed prefix and 6 digits.")
    return value


def validate_name(value):
    value = " ".join(validate_text(value).split()).title()
    letters = value.replace(" ", "").replace("-", "").replace("'", "").replace("’", "")
    if len(letters) < 2 or not letters.isalpha():
        raise ValueError("Name must contain at least two letters; spaces, hyphens and apostrophes are allowed.")
    return value


def validate_date_of_birth(value):
    value = validate_text(value)
    date = datetime.strptime(value, "%d/%m/%Y")
    if date.strftime("%d/%m/%Y") != value or not 1900 <= date.year <= 2008 or date.date() > datetime.today().date():
        raise ValueError("Use DD/MM/YYYY, with birth year between 1900 and 2008.")
    return value


def validate_gender(value):
    value = validate_text(value).title()
    if value not in ("Male", "Female"):
        raise ValueError("Gender must be Male or Female.")
    return value


def validate_class_name(value):
    value = validate_text(value).upper()
    if not re.fullmatch(r"([A-Z]{2}[0-9]{4}|[A-Z]{3}[0-9]{3})", value):
        raise ValueError("Class must use 2 letters + 4 digits or 3 letters + 3 digits.")
    return value


def validate_phone(value):
    value = validate_text(value)
    if not re.fullmatch(r"0[0-9]{9}", value):
        raise ValueError("Phone must contain 10 digits starting with 0.")
    return value


def validate_email(value):
    value = validate_text(value)
    if not value.isascii() or ".." in value or value.count("@") != 1:
        raise ValueError("Invalid email.")
    local, domain = value.split("@")
    if not re.fullmatch(r"[A-Za-z0-9_%+.-]+", local) or local.startswith(".") or local.endswith("."):
        raise ValueError("Invalid email local part.")
    parts = domain.split(".")
    if len(parts) < 2 or not parts[-1].isalpha() or len(parts[-1]) < 2:
        raise ValueError("Invalid email domain.")
    for part in parts:
        if not re.fullmatch(r"[A-Za-z0-9-]+", part) or part.startswith("-") or part.endswith("-"):
            raise ValueError("Invalid email domain.")
    return value


def validate_status(value):
    value = validate_text(value).title()
    if value not in ("Active", "Inactive", "Graduated"):
        raise ValueError("Status must be Active, Inactive or Graduated.")
    return value


def validate_course_id(value):
    value = validate_text(value).upper()
    if not re.fullmatch(r"[A-Z0-9]{2,10}", value):
        raise ValueError("Course ID must contain 2-10 letters/digits.")
    return value


def validate_score(value):
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    if isinstance(value, bool):
        raise ValueError("Score must be a number from 0 to 10.")
    score = float(str(value).replace(",", "."))
    if not 0 <= score <= 10:
        raise ValueError("Score must be between 0 and 10.")
    return score


def validate_credits(value):
    if isinstance(value, bool):
        raise ValueError("Credits must be a positive integer.")
    number = float(value)
    if not number > 0 or not number.is_integer():
        raise ValueError("Credits must be a positive integer.")
    return int(number)


def input_value(message, validator, allow_cancel=False, allow_empty=False):
    while True:
        raw = input(message).strip()
        if allow_cancel and raw == "0":
            return None
        if allow_empty and not raw:
            return None
        try:
            if not raw:
                raise ValueError("A value is required.")
            return validator(raw)
        except (ValueError, TypeError) as error:
            print("[Error]", error)


def input_student_id(message="Student ID: ", allow_cancel=False):
    return input_value(message, validate_student_id, allow_cancel)


def input_name(message="Full name: "):
    return input_value(message, validate_name)


def input_date_of_birth(message="Date of birth: "):
    return input_value(message, validate_date_of_birth)


def input_gender(message="Gender: "):
    return input_value(message, validate_gender)


def input_class_name(message="Class: "):
    return input_value(message, validate_class_name)


def input_phone(message="Phone: "):
    return input_value(message, validate_phone)


def input_email(message="Email: "):
    return input_value(message, validate_email)


def input_status(message="Status (Active/Inactive/Graduated): "):
    return input_value(message, validate_status)


def input_course_id(message="Course ID: ", allow_cancel=False):
    return input_value(message, validate_course_id, allow_cancel)


def input_score(message, allow_empty=False):
    return input_value(message, validate_score, allow_empty=allow_empty)
