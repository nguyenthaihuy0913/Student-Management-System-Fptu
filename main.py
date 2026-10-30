from pathlib import Path
import file_io
from services import StudentManager, ResultManager
from student_management import student_sub_menu
from result_management import result_sub_menu

BASE_DIR = Path(__file__).resolve().parent
STUDENTS_FILE = BASE_DIR / "students.txt"
RESULTS_FILE = BASE_DIR / "results.txt"


def save_data(students, results):
    students_ok = file_io.save_records(STUDENTS_FILE, students.students)
    results_ok = file_io.save_records(RESULTS_FILE, results.results)
    if students_ok and results_ok:
        print("Data saved.")
        return True
    print("Save failed. Some data may not have been saved.")
    return False


def main():
    try:
        students = StudentManager(file_io.load_students(STUDENTS_FILE))
        results = ResultManager(students, file_io.load_results(RESULTS_FILE))
    except (OSError, ValueError, UnicodeError) as error:
        print("[Error] Cannot load data:", error)
        print("Startup stopped; original files have not been changed.")
        return
    print(f"Loaded {len(students.students)} students and {len(results.results)} results.")
    while True:
        try:
            print("\nSTUDENT MANAGEMENT SYSTEM")
            print("1. Student Management\n2. Result Management\n3. Save and Exit")
            choice = input("Choice: ").strip()
            if choice == "1":
                student_sub_menu(students)
            elif choice == "2":
                result_sub_menu(results)
            elif choice == "3":
                if save_data(students, results):
                    return
            else:
                print("Invalid choice.")
        except (KeyboardInterrupt, EOFError):
            print("\nSaving before exit...")
            if save_data(students, results):
                return
            print("Returning to menu so you can retry saving.")


if __name__ == "__main__":
    main()
