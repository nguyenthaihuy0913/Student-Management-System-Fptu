# Student Management System (SMS) - FPT University

A console-based Student and Academic Result Management System built with Python 3 for the **PFP191 (Programming Fundamentals with Python)** course at FPT University (Topic 4).

The system enforces strict input validation, real-world academic business logic (e.g. FPTU student ID formats, Pass/Fail criteria with Retake Exam, academic status constraints), and safe file persistence.

---

## 👥 Project Information

* **Course:** PFP191 - Programming Fundamentals with Python
* **Topic:** Topic 4 - Student Management System (SMS)
* **Class:** AI2102
* **Group:** Group 4
* **Supervising Lecturer:** Lê Thị Hồng Nga

### Team Members

| Student ID | Full Name | Role | Responsibilities |
| :--- | :--- | :--- | :--- |
| **SE211528** | **Nguyễn Thái Huy** | **Team Leader / Core Dev** | Project architecture, CLI integration (`main.py`), code review & optimization. |
| **SE211681** | **Trần Võ Hồng Ngọc** | **Core Developer** | Student profile management module (`student_management.py`), validation rules. |
| **SE211294** | **Vũ Ngọc Anh** | **Core Developer** | Result & grade management logic (`result_management.py`), pass/fail evaluation. |
| **SE211746** | **Nguyễn Thái Sơn** | **Developer** | File I/O persistence (`file_io.py`), exception handling & report documentation. |

---

## 🏗️ Project Structure

```text
Student-Management-System-Fptu/
│
├── main.py                   # Application entry point & main menu navigation
├── student_management.py     # Student profile operations & comprehensive input validation
├── result_management.py      # Course grade recording, Pass/Fail evaluation & query functions
├── file_io.py                # Plaintext file I/O handlers (reading/writing pipe-delimited data)
├── students.txt              # Plaintext database storing student profile records
├── results.txt               # Plaintext database storing academic grade records
│
├── PFP191_Report.md          # Technical project report (Markdown format)
├── PFP191_Report.docx        # Technical project report (Word format)
└── README.md                 # Project overview and user guide
```

---

## 📌 Features & Business Logic

### 1. Student Profile Management (`student_management.py`)
- **Add Student:** Register new students with primary key uniqueness check (prevents duplicate Student IDs).
- **Strict Input Validation:**
  - **Student ID:** Exactly 8 characters; 2-letter major prefix (`SE`, `SS`, `SA`, `SB`, `DE`, `DA`, `DS`, `HE`, `HA`, `HS`, `QE`, `QA`, `QS`, `CE`, `CA`, `CS`) followed by 6 digits.
  - **Full Name:** Letters, spaces, hyphens, and apostrophes only; minimum 2 characters.
  - **Date of Birth:** `DD/MM/YYYY` format, must be a valid calendar date between 1900 and 2008 (no future dates).
  - **Gender:** Case-insensitive acceptance of `Male` or `Female`.
  - **Class Name:** 6 characters (e.g. `AI2102`, `SE1901`, `PFP191`).
  - **Phone Number:** Exactly 10 digits starting with `0`.
  - **Email:** Strict RFC-like validation (requires valid local part, `@`, domain name, and valid extension like `.com`, `.edu.vn`).
  - **Status:** Choice between `Active`, `Inactive`, or `Graduated`.
- **Update Student:** Dedicated sub-menu allowing granular updates to any profile attribute.
- **Filter Students:** Search and filter records by Class Name or Status.
- **Display Options:**
  - View all currently `Active` students.
  - View the entire student roster.
- **Action Confirmation:** Prompts confirmation (`Y/N`) before navigating critical sub-menu operations.

### 2. Course Result Management (`result_management.py`)
- **Record Grades:**
  - Validates that the Student ID exists in the student roster.
  - **Academic Status Check:** Only students with `Active` status are eligible to enroll and receive grades.
  - **Duplicate Prevention:** Prevents entering duplicate grades for the same student and course ID.
  - **Grading Scale:** Scores from `0.0` to `10.0` (accepts both `,` and `.` decimal notations).
- **Two-Exam Constraint & Retake Logic:**
  - Final Exam (FE) score is entered first.
  - If `FE >= 5.0`: The student passes immediately.
  - If `FE < 5.0`: System enables entry for the Retake Exam (RE) (or can be skipped/left blank).
- **Pass / Fail Evaluation:**
  - $\text{Pass}$: When $\text{FE} \ge 5.0$ OR ($\text{FE} < 5.0$ AND $\text{RE} \ge 5.0$).
  - $\text{Fail}$: When both attempts fail to reach $5.0$.
- **Update Grades:** Allows editing FE/RE scores with automatic status re-evaluation. Blocked if the student has already `Graduated`.
- **Search & Reports:**
  - Search academic records by Student ID.
  - View all exam results sorted descending by status (`Pass` records displayed first).
  - Filter and display only students who have passed.

### 3. File I/O & Persistence (`file_io.py`)
- **Storage Format:** Clean pipe-delimited (`|`) UTF-8 flat files:
  - `students.txt`: `student_id|full_name|date_of_birth|gender|class_name|phone|email|status`
  - `results.txt`: `student_id|course_id|grade_fe|grade_re|result_status`
- **Safe Handling:** Built with robust `try-except-finally` blocks to guarantee file streams are properly flushed and closed, preventing data corruption or memory leaks.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher.
* No third-party packages required (uses Python standard libraries exclusively).

### Running the Application

1. Open a terminal / command prompt in the project root directory.
2. Run the application entry point:
   ```bash
   python main.py
   ```
3. Use the numeric console menu to navigate through features. When you choose `3. Save and Exit`, all changes are automatically saved to `students.txt` and `results.txt`.

---

## 📋 Sample Data Format

**students.txt**
```text
SE211528|Nguyen Thai Huy|15/09/2005|Male|AI2102|0901234567|huyntse211528@fpt.edu.vn|Active
SE211681|Tran Vo Hong Ngoc|20/04/2005|Female|AI2102|0912345678|ngoctvhse211681@fpt.edu.vn|Active
```

**results.txt**
```text
SE211528|PFP191|8.5||Pass
SE211681|PFP191|4.0|7.5|Pass
```