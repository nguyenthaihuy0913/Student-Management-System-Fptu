# =======================================================
# MODULE: MAIN SYSTEM NAVIGATION & CLI
# File: main.py
# =======================================================

import file_io               
import student_management     
import result_management      

STUDENTS_FILE = "students.txt"
RESULTS_FILE = "results.txt"


def display_main_menu():
    print("\n========================================")
    print("    STUDENT MANAGEMENT SYSTEM (SMS)     ")
    print("========================================")
    print("1. Student Management")
    print("2. Result Management")
    print("3. Save and Exit")
    print("========================================")


def main():
    print("[System] Starting the system...")

    student_list = file_io.loadFromFile(STUDENTS_FILE)
    result_list = file_io.loadResultsFromFile(RESULTS_FILE)

    print(f"[System] Successfully loaded: {len(student_list)} students, {len(result_list)} result records.")

    while True:
        display_main_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            student_management.student_sub_menu(student_list)

        elif choice == "2":
            result_management.result_sub_menu(result_list, student_list)

        elif choice == "3":
            print("\n[System] Saving data to the file system...")
            save_students_ok = file_io.saveToFile(STUDENTS_FILE, student_list)
            save_results_ok = file_io.saveResultsToFile(RESULTS_FILE, result_list)

            if save_students_ok and save_results_ok:
                print("[System] Data has been saved safely!")
            else:
                print("[System Warning] An error occurred during the file writing process!")

            print("Exiting program. Goodbye!")
            break

        else:
            print("[Error] Invalid choice! Please select between 1 and 3.")


if __name__ == "__main__":
    main()
