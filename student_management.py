from models import Student
from utils.validator import (
    input_student_id, input_name, input_date_of_birth, input_gender,
    input_class_name, input_phone, input_email, input_status,
)


def display_students(students):
    if not students:
        print("No matching students.")
    for student in students:
        print(student)
        print(f"DOB: {student.date_of_birth} | Gender: {student.gender}")
        print(f"Phone: {student.phone} | Email: {student.email}")


def add_student(manager):
    student_id = input_student_id("Student ID (0 to cancel): ", True)
    if student_id is None:
        return
    if manager.find(student_id) is not None:
        raise ValueError("Student ID already exists.")
    student = Student(
        student_id, input_name(), input_date_of_birth("DOB (DD/MM/YYYY): "),
        input_gender(), input_class_name(), input_phone(), input_email(), input_status(),
    )
    manager.add(student)
    print("Student added.")


def update_student(manager):
    student_id = input_student_id("Student ID (0 to cancel): ", True)
    if student_id is None:
        return
    if manager.find(student_id) is None:
        raise ValueError("Student not found.")
    fields = {
        "1": ("full_name", input_name),
        "2": ("date_of_birth", input_date_of_birth),
        "3": ("gender", input_gender),
        "4": ("class_name", input_class_name),
        "5": ("phone", input_phone),
        "6": ("email", input_email),
        "7": ("status", input_status),
    }
    while True:
        print("1. Name  2. DOB  3. Gender  4. Class  5. Phone  6. Email  7. Status  0. Back")
        choice = input("Choice: ").strip()
        if choice == "0":
            return
        if choice not in fields:
            print("Invalid choice.")
            continue
        field, reader = fields[choice]
        manager.update(student_id, field, reader("New value: "))
        print("Student updated.")


def student_sub_menu(manager):
    while True:
        print("\nSTUDENT MANAGEMENT")
        print("1. Add student\n2. Update student\n3. Filter students\n4. Active students\n5. All students\n0. Back")
        choice = input("Choice: ").strip()
        try:
            if choice == "0":
                return
            if choice == "1":
                add_student(manager)
            elif choice == "2":
                update_student(manager)
            elif choice == "3":
                condition = input("Class/status (0 to cancel): ").strip()
                if condition != "0":
                    display_students(manager.filter(condition))
            elif choice == "4":
                display_students(manager.active_students())
            elif choice == "5":
                display_students(manager.students)
            else:
                print("Invalid choice.")
        except ValueError as error:
            print("[Error]", error)
