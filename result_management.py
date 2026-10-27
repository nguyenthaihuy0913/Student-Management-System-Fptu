from student_management import inputStudentID


def inputScore(prompt, allow_empty=False):
    while True:
        raw = input(prompt).strip().replace(",", ".")
        if allow_empty and raw == "":
            return None
        try:
            score = float(raw)
            if 0.0 <= score <= 10.0:
                return score
            print("[Error] Score must be between 0.0 and 10.0!")
        except ValueError:
            print("[Error] Invalid score! Please enter a valid number.")


def evaluateCourseStatus(grade_fe, grade_re):
    try:
        fe = float(grade_fe) if grade_fe not in (None, "") else 0.0
    except ValueError:
        fe = 0.0

    try:
        re = float(grade_re) if grade_re not in (None, "") else None
    except ValueError:
        re = None

    if fe >= 5.0:
        return "Pass"
    elif re is not None and re >= 5.0:
        return "Pass"
    else:
        return "Fail"


def displayResult(record):
    re_grade = record.get("grade_re", "")
    re_display = re_grade if re_grade not in (None, "") else "(none)"
    print("-----------------------------------")
    print(f"Student ID   : {record.get('student_id', '')}")
    print(f"Course ID    : {record.get('course_id', '')}")
    print(f"Final Exam   : {record.get('grade_fe', '')}")
    print(f"Retake Exam  : {re_display}")
    print(f"Result Status: {record.get('result_status', '')}")
    print("-----------------------------------")


def addCourseGrade(result_list, student_list):
    print("\n--- ADD COURSE GRADE ---")
    student_id = inputStudentID("Enter student ID: ")

    found_student = None
    for s in student_list:
        if s["student_id"] == student_id:
            found_student = s
            break

    if not found_student:
        print(f"[Error] Student ID {student_id} not found in student list! Please add student first.")
        return False

    if found_student["status"].lower() != "active":
        print(f"[Error] Cannot add grade! Student {student_id} is '{found_student['status']}'. Only 'Active' students can take courses.")
        return False

    course_id = input("Enter course ID (e.g. PFP191): ").strip().upper()

    for record in result_list:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            print("[Error] Grade record for this student and course already exists!")
            return False

    grade_fe = inputScore("Enter Final Exam (FE) grade (0-10): ")
    grade_re = None
    if grade_fe < 5.0:
        print("[System Info] FE score is below 5.0. Retake Exam (RE) can be entered.")
        grade_re = inputScore("Enter Re-take Exam (RE) grade (0-10, or press Enter to skip): ", allow_empty=True)

    result_status = evaluateCourseStatus(grade_fe, grade_re)

    new_record = {
        "student_id": student_id,
        "course_id": course_id,
        "grade_fe": str(grade_fe),
        "grade_re": str(grade_re) if grade_re is not None else "",
        "result_status": result_status
    }

    result_list.append(new_record)
    print(f"[Success] Grade added successfully! Final status: {result_status}")
    return True


def updateGradeOrStatus(result_list, student_list):
    print("\n--- UPDATE GRADE ---")
    student_id = inputStudentID("Enter student ID to update: ")

    found_student = None
    for s in student_list:
        if s["student_id"] == student_id:
            found_student = s
            break

    if found_student and found_student["status"].lower() == "graduated":
        print(f"[Error] Cannot update grade! Student {student_id} has already Graduated.")
        return False

    course_id = input("Enter course ID to update: ").strip().upper()

    found_record = None
    for record in result_list:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            found_record = record
            break

    if found_record is None:
        print(f"[Error] No grade record found for Student {student_id} in Course {course_id}!")
        return False

    print(f"[System] Updating grade for Student {student_id} - Course {course_id}:")
    new_fe = inputScore("Enter new Final Exam (FE) grade (0-10): ")
    new_re = None
    if new_fe < 5.0:
        print("[System Info] FE score is below 5.0. Retake Exam (RE) can be entered.")
        new_re = inputScore("Enter new Re-take Exam (RE) grade (0-10, or press Enter to skip): ", allow_empty=True)

    found_record["grade_fe"] = str(new_fe)
    found_record["grade_re"] = str(new_re) if new_re is not None else ""
    found_record["result_status"] = evaluateCourseStatus(new_fe, new_re)

    print(f"[Success] Grade updated successfully! New status: {found_record['result_status']}")
    return True


def searchEnrollments(result_list):
    print("\n--- SEARCH ENROLLMENTS ---")
    student_id = inputStudentID("Enter student ID to search: ")

    found = False
    for record in result_list:
        if record["student_id"] == student_id:
            if not found:
                print(f"\n===== ACADEMIC RECORDS FOR STUDENT {student_id} =====")
            displayResult(record)
            found = True

    if not found:
        print(f"[Info] No grade records found for student {student_id}.")


def displayExamResults(result_list):
    print("\n--- ALL EXAM RESULTS (SORTED BY STATUS) ---")
    if not result_list:
        print("[Info] No exam results available.")
        return

    sorted_results = sorted(result_list, key=lambda x: str(x.get("result_status", "")), reverse=True)
    for record in sorted_results:
        displayResult(record)


def displayPassedStudents(result_list):
    print("\n--- PASSED STUDENTS ---")
    passed = [r for r in result_list if str(r.get("result_status", "")).strip().lower() == "pass"]
    if not passed:
        print("[Info] No passed students found.")
        return

    print(f"[Info] Found {len(passed)} passed record(s):")
    for record in passed:
        displayResult(record)


def result_sub_menu(result_list, student_list):
    while True:
        print("\n========== RESULT MANAGEMENT ==========")
        print("1. Add student's course grade")
        print("2. Update student's grade or status")
        print("3. Search enrollments by student ID")
        print("4. Display exam results (sorted by status)")
        print("5. Display passed students")
        print("0. Return to main menu")
        print("=======================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            addCourseGrade(result_list, student_list)
        elif choice == "2":
            updateGradeOrStatus(result_list, student_list)
        elif choice == "3":
            searchEnrollments(result_list)
        elif choice == "4":
            displayExamResults(result_list)
        elif choice == "5":
            displayPassedStudents(result_list)
        elif choice == "0":
            print("Returning to main menu...")
            break
        else:
            print("[Error] Invalid choice! Please try again.")


openResultSubMenu = result_sub_menu