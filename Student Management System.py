# ==========================================
# STUDENT MANAGEMENT SYSTEM
# ==========================================
# Program structure:
#   1. Input functions   (ask the user and check the data)
#   2. displayStudent    (print one student)
#   3. Menu functions    (add, update, filter, display)
#   4. main()            (the menu loop)
# ==========================================

from datetime import datetime

valid_prefixes = ["SE", "SS", "SA", "SB", "DE", "DA", "DS", "HE", "HA", "HS", "QE", "QA", "QS", "CE", "CA", "CS"]


# ==========================================
# INPUT FUNCTIONS
# Each function repeats the question until the input is valid.
# ==========================================

def inputStudentID(message):
    while True:
        student_id = input(message).strip().upper()

        if len(student_id) != 8:
            print("Invalid Student ID!")
            print("ID must contain exactly 8 characters. Example: SE123456")

        elif student_id[:2] not in valid_prefixes:
            print("Invalid major code!")
            print("Allowed prefixes:", ", ".join(valid_prefixes))

        elif not (student_id[2:].isascii()
                  and student_id[2:].isdigit()):
            print("Invalid Student ID!")
            print("The last 6 characters must be digits (0-9).")

        else:
            return student_id


def inputName(message):
    while True:
        name = input(message).strip()

        # Remove the allowed symbols, then only letters should remain
        check_name = name.replace(" ", "")
        check_name = check_name.replace("-", "")
        check_name = check_name.replace("'", "")
        check_name = check_name.replace("’", "")

        if name != "" and check_name.isalpha() and len(check_name) > 2:
            return name
        else:
            print("Invalid name! Please enter a valid name.")
            print("Use only letters, spaces, hyphens and apostrophes.")
            print("Full name must contain more than 2 letters.")


def inputDateOfBirth(message):
    while True:
        date_of_birth = input(message).strip()

        # Only the conversion can raise an error, so only it is in "try"
        try:
            dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
        except ValueError:
            print("Invalid date!")
            print("The date must exist and use DD/MM/YYYY. Example: 28/09/2007")
            continue

         # Extra rule: reject unrealistic years such as 1850
        if dob.year < 1900:
            print("Year of birth must be 1900 or later!")

        # strptime also accepts "1/1/2000", so check the exact text format
        elif dob.strftime("%d/%m/%Y") != date_of_birth:
            print("Please use DD/MM/YYYY format! Example: 28/09/2007")
        elif dob.date() > datetime.today().date():
            print("Date of birth cannot be in the future!")

        elif dob.year >= 2009:
            print("Year of birth must be before 2009!")

        else:
            return date_of_birth


def inputGender(message):
    while True:
        gender = input(message).strip().lower()

        if gender == "male":
            return "Male"
        elif gender == "female":
            return "Female"
        else:
            print("Please enter Male or Female.")


def inputClassName(message):
    while True:
        class_name = input(message).strip().upper()

        if (len(class_name) == 6
                and class_name[:2].isalpha()
                and class_name[:2].isascii()
                and class_name[2:].isdigit()
                and class_name[2:].isascii()):
            return class_name
        else:
            print("Invalid class name!")
            print("Class name must have 2 letters followed by 4 digits.")
            print("Example: AI2102, SE1901, IT1902, IA1803, ...")


def inputPhone(message):
    while True:
        phone = input(message).strip()

        if (phone.isascii()
                and phone.isdigit()
                and len(phone) == 10
                and phone.startswith("0")):
            return phone
        else:
            print("Invalid phone number!")
            print("Phone must contain exactly 10 digits and start with 0.")


def inputEmail(message):
    while True:
        email = input(message).strip()

        # split() cuts the text at any space or tab
        if len(email.split()) != 1:
            print("Invalid email! It must not contain spaces.")
            continue

        if not email.isascii():
            print("Invalid email! Use only English letters, digits and symbols.")
            print("Example: vtgh@gmail.com, vtgh@fpt.edu, ...")
            continue

        if email.count("@") != 1:
            print("Invalid email! It must contain exactly one '@'.")
            print("Example: vtgh@gmail.com, vtgh@fpt.edu, ...")
            continue

        if ".." in email:
            print("Invalid email! It must not contain two dots in a row.")
            continue

        parts = email.split("@")
        local = parts[0]
        domain = parts[1]

        if local == "" or domain == "":
            print("Invalid email! There must be text before and after '@'.")
            print("Example: vtgh@gmail.com, vtgh@fpt.edu, ...")
            continue

        if local.startswith(".") or local.endswith("."):
            print("Invalid email! The part before '@' must not start or end with a dot.")
            continue

        # Check every character of the part before '@'
        valid_local = True
        for char in local:
            if not (char.isalnum() or char in "._%+-"):
                valid_local = False

        if not valid_local:
            print("Invalid email! The part before '@' may contain only")
            print("letters, digits and these symbols: . _ % + -")
            continue

        # Check the domain (the part after '@')
        domain_parts = domain.split(".")

        if len(domain_parts) < 2:
            print("Invalid email! The domain must contain a dot. Example: gmail.com")
            print("Example: vtgh289@gmail.com, AnVTGSE234156@fpt.edu")
            continue

        valid_domain = True
        for part in domain_parts:
            if part == "" or part.startswith("-") or part.endswith("-"):
                valid_domain = False
            elif not part.replace("-", "").isalnum():
                valid_domain = False

        if not valid_domain:
            print("Invalid email! Each domain part must use letters, digits or hyphens")
            print("and must not be empty or start/end with a hyphen.")
            continue

        # The ending of the domain (com, edu, vn, ...)
        suffix = domain_parts[-1]

        if not suffix.isalpha() or len(suffix) < 2:
            print("Invalid email! The ending (like .com or .edu) needs at least 2 letters.")
            continue

        return email




def inputUniquePhone(message, student_list, exclude_student=None):
    while True:
        phone = inputPhone(message)

        duplicated = any(
            student["phone"] == phone
            and student is not exclude_student
            for student in student_list
        )

        if duplicated:
            print("This phone number already exists! Please enter another phone number.")
        else:
            return phone


def inputUniqueEmail(message, student_list, exclude_student=None):
    while True:
        email = inputEmail(message)

        # Email is optional
        if email == "":
            return email

        duplicated = any(
            student["email"].strip().lower() == email.lower()
            and student["email"].strip() != ""
            and student is not exclude_student
            for student in student_list
        )

        if duplicated:
            print("This email already exists! Please enter another email.")
        else:
            return email


def inputStatus(message):
    while True:
        status = input(message).strip().lower()

        if status == "active":
            return "Active"

        elif status == "inactive":
            return "Inactive"

        elif status == "graduated":
            return "Graduated"

        else:
            print("Invalid status!")
            print("Please enter Active, Inactive or Graduated.")


# ==========================================
# DISPLAY ONE STUDENT (helper used by menu options 3, 4 and 5)
# ==========================================
def displayStudent(student):
    email = student["email"]

    print("-----------------------------------")
    print("Student ID:", student["student_id"])
    print("Full name:", student["full_name"])
    print("Date of birth:", student["date_of_birth"])
    print("Gender:", student["gender"])
    print("Class name:", student["class_name"])
    print("Phone:", student["phone"])
    print("Email:", email)
    print("Status:", student["status"])
    print("-----------------------------------")


# ==========================================
# MENU OPTION 1: ADD STUDENT
# ==========================================
def addStudent(student_list):
    student_id = inputStudentID("Enter student ID: ")

    # Does a student with this ID already exist?
    duplicated = False

    for student in student_list:
        if student["student_id"] == student_id:
            duplicated = True
            break

    # YES -> show a message and end (nothing is added)
    if duplicated:
        print("Student ID already exists!")
        return False

    # NO -> collect the other information
    full_name = inputName("Enter full name: ")
    date_of_birth = inputDateOfBirth("Enter date of birth (DD/MM/YYYY): ")
    gender = inputGender("Enter gender (Male/Female): ")
    class_name = inputClassName("Enter class name: ")
    phone = inputUniquePhone("Enter phone: ", student_list)
    email = inputUniqueEmail("Enter email (press Enter to skip): ", student_list)
    status = inputStatus("Enter status (Active/Inactive/Graduated): ")

    new_student = {
        "student_id": student_id,
        "full_name": full_name,
        "date_of_birth": date_of_birth,
        "gender": gender,
        "class_name": class_name,
        "phone": phone,
        "email": email,
        "status": status}

    student_list.append(new_student)

    print("Student added successfully!")
    return True


# ==========================================
# MENU OPTION 2: UPDATE STUDENT
# ==========================================

def updateStudent(student_list):
    while True:
        print("\n========== UPDATE STUDENT ==========")
        print("1. Update full name")
        print("2. Update date of birth")
        print("3. Update gender")
        print("4. Update class name")
        print("5. Update phone")
        print("6. Update email")
        print("7. Update status")
        print("0. Return to main menu")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Returning to main menu...")
            return

        elif choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Invalid choice! Please try again.")
            continue

        if len(student_list) == 0:
            print("Student list is empty! Please add a student first.")
            continue

        student_id = inputStudentID("Enter student ID to update: ")

    # Step 1: Search for the student
    found_student = None

    for student in student_list:
        if student["student_id"] == student_id:
            found_student = student
            break

    # Step 2: Check whether the student exists
    if found_student is None:
        print("Student not found!")
        return False

    # Step 3: Show the update menu
    while True:
        print("\n========== UPDATE STUDENT ==========")
        print("1. Update full name")
        print("2. Update date of birth")
        print("3. Update gender")
        print("4. Update class name")
        print("5. Update phone")
        print("6. Update email")
        print("7. Update status")
        print("0. Return to main menu")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            found_student["full_name"] = inputName(
                "Enter new full name: ")
            print("Full name updated successfully!")

        elif choice == "2":
            found_student["date_of_birth"] = inputDateOfBirth(
                "Enter new date of birth (DD/MM/YYYY): ")
            print("Date of birth updated successfully!")

        elif choice == "3":
            found_student["gender"] = inputGender(
                "Enter new gender (Male/Female): ")
            print("Gender updated successfully!")

        elif choice == "4":
            found_student["class_name"] = inputClassName(
                "Enter new class name: ")
            print("Class name updated successfully!")

        elif choice == "5":
            found_student["phone"] = inputUniquePhone(
                "Enter new phone: ", student_list, found_student)
            print("Phone updated successfully!")

        elif choice == "6":
            found_student["email"] = inputUniqueEmail(
                "Enter new email: ", student_list, found_student)
            print("Email updated successfully!")

        elif choice == "7":
            found_student["status"] = inputStatus(
                "Enter new status (Active/Inactive/Graduated): ")
            print("Status updated successfully!")

        elif choice == "0":
            print("Returning to main menu...")
            return True

        else:
            print("Invalid choice! Please try again.")

# ==========================================
# MENU OPTION 3: FILTER STUDENTS
# ==========================================
def filterStudents(student_list):
    filter_condition = input(
        "Enter class name or status to filter: ").strip().lower()

    if filter_condition == "":
        print("Filter condition cannot be empty!")
        return

    found = False

    for student in student_list:

        # MATCH -> display, otherwise skip to the next student
        if (student["class_name"].lower() == filter_condition
                or student["status"].lower() == filter_condition):
            displayStudent(student)
            found = True

    if not found:
        print("No matching students found!")


# ==========================================
# MENU OPTION 4: DISPLAY ACTIVE STUDENTS
# ==========================================
def displayActiveStudents(student_list):
    found = False

    for student in student_list:

        if student["status"].lower() == "active":
            displayStudent(student)
            found = True

    if not found:
        print("No active students found!")


# ==========================================
# MENU OPTION 5: DISPLAY ALL STUDENTS
# ==========================================
def displayAllStudents(student_list):
    if len(student_list) == 0:
        print("Student list is empty!")

    else:
        for student in student_list:
            displayStudent(student)


# ==========================================
# MAIN MENU
# ==========================================
def student_sub_menu(student_list):
    while True:
        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add student")
        print("2. Update student")
        print("3. Filter students")
        print("4. Display active students")
        print("5. Display all students")
        print("0. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            addStudent(student_list)

        elif choice == "2":
            updateStudent(student_list)

        elif choice == "3":
            filterStudents(student_list)

        elif choice == "4":
            displayActiveStudents(student_list)

        elif choice == "5":
            displayAllStudents(student_list)

        elif choice == "0":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice! Please try again.")



# ==========================================
# RUN PROGRAM
# ==========================================

student_list = []

student_sub_menu(student_list)

