from models import Result
from utils.validator import (
    input_student_id, input_course_id, input_score, input_value,
    validate_text, validate_credits,
)


def display_results(results):
    if not results:
        print("No matching results.")
    for result in results:
        print(result)


def read_grades():
    fe = input_score("FE (0-10, blank if not graded): ", True)
    re = None
    if fe is not None and fe < 5:
        re = input_score("RE (0-10, blank if not graded): ", True)
    return fe, re


def read_course_details():
    name = input_value("Course name: ", validate_text)
    semester = input_value("Semester (e.g. Fall2026): ", validate_text)
    credits = input_value("Credits: ", validate_credits)
    return name, semester, credits


def add_result(manager):
    student_id = input_student_id("Student ID (0 to cancel): ", True)
    if student_id is None:
        return
    manager.check_student(student_id)
    course_id = input_course_id("Course ID (0 to cancel): ", True)
    if course_id is None:
        return
    if manager.find(student_id, course_id) is not None:
        raise ValueError("Student/course result already exists.")
    name, semester, credits = read_course_details()
    fe, re = read_grades()
    manager.add(Result(student_id, course_id, name, semester, credits, fe, re))
    print("Result added.")


def update_result(manager):
    student_id = input_student_id("Student ID (0 to cancel): ", True)
    if student_id is None:
        return
    manager.check_student(student_id, require_active=False)
    course_id = input_course_id("Course ID (0 to cancel): ", True)
    if course_id is None:
        return
    result = manager.find(student_id, course_id)
    if result is None:
        raise ValueError("Result not found.")
    print(result)
    print("1. Replace FE/RE (blank clears score)\n2. Update course details\n0. Cancel")
    choice = input("Choice: ").strip()
    if choice == "1":
        fe, re = read_grades()
        manager.update_grades(student_id, course_id, fe, re)
    elif choice == "2":
        name, semester, credits = read_course_details()
        manager.update_course_details(student_id, course_id, name, semester, credits)
    elif choice == "0":
        return
    else:
        raise ValueError("Invalid choice.")
    print("Result updated.")


def result_sub_menu(manager):
    while True:
        print("\nRESULT MANAGEMENT")
        print("1. Add result\n2. Update result\n3. Search by student ID\n4. All results (status descending)\n5. Passed results\n0. Back")
        choice = input("Choice: ").strip()
        try:
            if choice == "0":
                return
            if choice == "1":
                add_result(manager)
            elif choice == "2":
                update_result(manager)
            elif choice == "3":
                student_id = input_student_id("Student ID (0 to cancel): ", True)
                if student_id is not None:
                    display_results(manager.search(student_id))
            elif choice == "4":
                display_results(manager.sorted_results())
            elif choice == "5":
                display_results(manager.passed_results())
            else:
                print("Invalid choice.")
        except ValueError as error:
            print("[Error]", error)
