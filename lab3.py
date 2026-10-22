# List to store all course results
result_list = []

# --- EVALUATE COURSE STATUS ---
def evaluateCourseStatus(grade_fe, grade_re):
    if grade_fe >= 5.0:
        return "Pass"
    elif grade_re is not None and grade_re >= 5.0:
        return "Pass"
    else:
        return "Fail"

# --- 1. ADD COURSE GRADE ---
def addCourseGrade():
    print("\n--- ADD COURSE GRADE ---")
    
    # Use the teammate's ID validation function
    student_id = inputStudentID("Enter student ID: ")

    # Check if the student exists in the teammate's student_list
    student_exists = False
    for student in student_list:
        if student["student_id"] == student_id:
            student_exists = True
            break
            
    if not student_exists:
        print(f"Error: Student ID {student_id} not found! Please add student first.")
        return False

    course_id = input("Enter course ID (e.g. PFP191): ").strip().upper()

    # Check if a grade record for this course already exists
    for record in result_list:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            print("Error: Grade record for this course already exists!")
            return False

    semester = input("Enter semester (e.g., Fall2026): ").strip()
    
    try:
        credits = int(input("Enter number of credits: "))
        grade_fe = float(input("Enter Final Exam (FE) grade (0-10): "))
    except ValueError:
        print("Error: Credits must be an integer and grade must be a number!")
        return False

    grade_re = None
    if grade_fe < 5.0:
        re_input = input("Enter Re-take Exam (RE) grade (or press Enter to skip): ").strip()
        if re_input != "":
            try:
                grade_re = float(re_input)
            except ValueError:
                print("Invalid RE grade. Set to None.")

    result_status = evaluateCourseStatus(grade_fe, grade_re)

    new_record = {
        "student_id": student_id,
        "course_id": course_id,
        "semester": semester,
        "credits": credits,
        "grade_fe": grade_fe,
        "grade_re": grade_re,
        "result_status": result_status
    }

    result_list.append(new_record)
    print(f"Grade added successfully! Final status: {result_status}")
    return True

# --- 2. UPDATE GRADE OR STATUS ---
def updateGradeOrStatus():
    print("\n--- UPDATE GRADE ---")
    student_id = inputStudentID("Enter student ID to update: ")
    course_id = input("Enter course ID to update: ").strip().upper()

    found_record = None
    for record in result_list:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            found_record = record
            break

    if found_record is None:
        print("Error: Grade record not found!")
        return False

    try:
        new_fe = float(input("Enter new Final Exam (FE) grade (0-10): "))
    except ValueError:
        print("Error: Grade must be a number!")
        return False

    new_re = None
    if new_fe < 5.0:
        re_input = input("Enter new Re-take Exam (RE) grade (or press Enter to skip): ").strip()
        if re_input != "":
            try:
                new_re = float(re_input)
            except ValueError:
                print("Invalid RE grade.")
    
    found_record["grade_fe"] = new_fe
    found_record["grade_re"] = new_re
    found_record["result_status"] = evaluateCourseStatus(new_fe, new_re)
    
    print(f"Grade updated successfully! New status: {found_record['result_status']}")
    return True

# --- 3. SEARCH ENROLLMENTS ---
def searchEnrollments():
    print("\n--- SEARCH ENROLLMENTS ---")
    student_id = inputStudentID("Enter student ID to search: ")
    
    found = False
    for record in result_list:
        if record["student_id"] == student_id:
            if not found:
                 print(f"Academic records for student {student_id}:")
            print(f"- Course: {record['course_id']} | FE: {record['grade_fe']} | RE: {record['grade_re']} | Status: {record['result_status']}")
            found = True

    if not found:
        print(f"No grade records found for student {student_id}.")

# --- 4. DISPLAY EXAM RESULTS ---
def displayExamResults():
    print("\n--- ALL EXAM RESULTS ---")
    if len(result_list) == 0:
        print("No exam results available.")
        return

    for record in result_list:
        print(f"ID: {record['student_id']} | Course: {record['course_id']} | FE: {record['grade_fe']} | RE: {record['grade_re']} | Status: {record['result_status']}")

# --- 5. DISPLAY PASSED STUDENTS ---
def displayPassedStudents():
    print("\n--- PASSED STUDENTS ---")
    found = False
    for record in result_list:
        if record["result_status"] == "Pass":
            print(f"ID: {record['student_id']} | Course: {record['course_id']} | Status: Pass")
            found = True

    if not found:
        print("No passed students found.")

# --- RESULT MANAGEMENT SUB-MENU ---
def openResultSubMenu():
    while True:
        print("\n========== RESULT MANAGEMENT ==========")
        print("1. Add course grade")
        print("2. Update grade or status")
        print("3. Search enrollments")
        print("4. Display exam results")
        print("5. Display passed students")
        print("0. Return to main menu")
        print("=======================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            addCourseGrade()
        elif choice == "2":
            updateGradeOrStatus()
        elif choice == "3":
            searchEnrollments()
        elif choice == "4":
            displayExamResults()
        elif choice == "5":
            displayPassedStudents()
        elif choice == "0":
            break
        else:
            print("Invalid choice! Please try again.")