import re
from datetime import datetime

VALID_PREFIXES = [
    "SE", "SS", "SA", "SB", "DE", "DA", "DS",
    "HE", "HA", "HS", "QE", "QA", "QS", "CE", "CA", "CS"
]


def input_student_id(message="Enter Student ID: ", allow_cancel=True):
    while True:
        raw = input(message).strip()
        if allow_cancel and raw == "0":
            return "0"
        if "|" in raw:
            print("[Error] Student ID cannot contain the '|' character.")
            continue
        if not re.match(r"^[A-Za-z]{2}\d{6}$", raw):
            print("[Error] Invalid format! Must be 2 letters followed by 6 digits (e.g., SE211528).")
            continue
        prefix = raw[:2].upper()
        if prefix not in VALID_PREFIXES:
            print(f"[Error] '{prefix}' is not a valid FPT University campus prefix!")
            continue
        return raw.upper()


def input_name(message="Enter Full Name: "):
    while True:
        raw = input(message).strip()
        if "|" in raw:
            print("[Error] Name cannot contain the '|' character.")
            continue
        name = " ".join(raw.split()).title()
        if not name:
            print("[Error] Name cannot be empty.")
            continue
        cleaned = name.replace(" ", "")
        if not cleaned.isalpha():
            print("[Error] Name can only contain alphabetical characters and spaces.")
            continue
        return name


def input_date_of_birth(message="Enter Date of Birth (DD/MM/YYYY): "):
    while True:
        raw = input(message).strip()
        if "|" in raw:
            print("[Error] Date of birth cannot contain the '|' character.")
            continue
        try:
            parsed_date = datetime.strptime(raw, "%d/%m/%Y")
            current_year = datetime.now().year
            if parsed_date.year < 1900 or parsed_date.year > current_year:
                print(f"[Error] Year must be between 1900 and {current_year}.")
                continue
            return raw
        except ValueError:
            print("[Error] Invalid date! Please use DD/MM/YYYY format with valid calendar days.")


def input_gender(message="Enter Gender (Male/Female): "):
    while True:
        raw = input(message).strip().lower()
        if raw == "male":
            return "Male"
        elif raw == "female":
            return "Female"
        else:
            print("[Error] Gender must be either 'Male' or 'Female'.")


def input_class_name(message="Enter Class Name: "):
    while True:
        raw = input(message).strip().upper()
        if "|" in raw:
            print("[Error] Class name cannot contain the '|' character.")
            continue
        if not raw:
            print("[Error] Class name cannot be empty.")
            continue
        if not re.match(r"^[A-Za-z0-9]{2,10}$", raw):
            print("[Error] Class name must be 2-10 alphanumeric characters (e.g., AI2102, SE1901).")
            continue
        return raw


def input_phone(message="Enter Phone Number: "):
    while True:
        raw = input(message).strip()
        if "|" in raw:
            print("[Error] Phone number cannot contain the '|' character.")
            continue
        if not re.match(r"^0\d{9}$", raw):
            print("[Error] Phone number must start with 0 and contain exactly 10 digits.")
            continue
        return raw


def input_email(message="Enter Email: "):
    while True:
        raw = input(message).strip()
        if "|" in raw:
            print("[Error] Email cannot contain the '|' character.")
            continue
        pattern = r"^[a-zA-Z0-9_.+-]+@fpt\.edu\.vn$"
        if not re.match(pattern, raw):
            print("[Error] Email must end with @fpt.edu.vn and contain valid characters.")
            continue
        return raw.lower()


def input_status(message="Enter Status (Active/Dropout/Suspended): "):
    valid_statuses = {"active": "Active", "dropout": "Dropout", "suspended": "Suspended"}
    while True:
        raw = input(message).strip().lower()
        if raw in valid_statuses:
            return valid_statuses[raw]
        print("[Error] Status must be one of: Active, Dropout, Suspended.")


def input_course_id(message="Enter Course ID: ", allow_cancel=True):
    while True:
        raw = input(message).strip()
        if allow_cancel and raw == "0":
            return "0"
        if "|" in raw:
            print("[Error] Course ID cannot contain '|' character.")
            continue
        if " " in raw or not raw:
            print("[Error] Course ID cannot be empty or contain spaces.")
            continue
        if not re.match(r"^[A-Za-z0-9]{3,10}$", raw):
            print("[Error] Course ID must be 3-10 alphanumeric characters (e.g., PFP191).")
            continue
        return raw.upper()


def input_score(message, allow_empty=False, min_val=0.0, max_val=10.0):
    while True:
        raw = input(message).strip()
        if allow_empty and raw == "":
            return ""
        if "|" in raw:
            print("[Error] Score cannot contain '|' character.")
            continue
        try:
            val = float(raw)
            if min_val <= val <= max_val:
                return str(round(val, 1))
            else:
                print(f"[Error] Score must be between {min_val} and {max_val}.")
        except ValueError:
            print("[Error] Invalid input! Score must be a valid numerical value.")


inputStudentID = input_student_id
inputName = input_name
inputDateOfBirth = input_date_of_birth
inputGender = input_gender
inputClassName = input_class_name
inputPhone = input_phone
inputEmail = input_email
inputStatus = input_status
inputCourseID = input_course_id
inputScore = input_score
