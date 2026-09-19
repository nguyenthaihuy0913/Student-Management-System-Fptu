# Student Management System (SMS)

A modular, console-based Student and Result Management System built with Python 3 for the **PFP191 (Programming Fundamentals with Python)** course at FPT University. The system demonstrates core software engineering practices, Object-Oriented Programming (OOP), file persistence, robust data validation, and exception handling.

---

## 📌 Features

### 1. Student Profile Management
- **Add Student:** Register new students with profile details (ID, full name, date of birth, gender, class, phone, email, status).
- **Duplicate Prevention:** Enforces primary key uniqueness for each student ID.
- **Update Records:** Modify student profiles by ID.
- **Filter & Search:** Filter by enrolled class or academic status (Active / Inactive / Graduated).
- **Active Roster:** Quickly view all currently active students.

### 2. Course Result & Enrollment Management
- **Course Enrollment & Grading:** Record student exam results including course ID, course name, semester, credits, Final Exam (FE), and Retake Exam (RE).
- **Two-Test Constraint:** Strictly enforces a maximum of two test attempts (FE and RE) per course.
- **Evaluation Logic:** Automatically determines `Pass` / `Fail` status:
  - `Pass` if FE >= 5.0 or (FE < 5.0 and RE >= 5.0).
- **Sorting & Reporting:** 
  - Search enrolled courses and grades by student ID.
  - Display full academic results sorted descending by status.
  - Filter and export the list of students with passing grades.

### 3. Architecture & Persistence
- **Modular Design:** Clean separation of concerns across `models/`, `services/`, and `utils/` packages.
- **OOP Principles:** Encapsulation via `@property` decorators and custom `__str__` representations.
- **File I/O:** Automatic data loading and saving to persistent plain-text files (`.txt`).
- **Defensive Programming:** Comprehensive exception handling for file read/write issues and malformed console inputs.

---

## 🏗️ Project Structure

```text
student-management-system/
│
├── data/
│   ├── students.txt          # Persistent student records
│   └── results.txt           # Persistent result records
│
├── models/
│   ├── __init__.py
│   ├── student.py            # Student class definition
│   └── result.py             # Result class definition and Pass/Fail logic
│
├── services/
│   ├── __init__.py
│   ├── student_service.py    # CRUD & filtering business logic for students
│   ├── result_service.py     # Grading, evaluation, and search logic
│   └── file_service.py       # File reading/writing handlers
│
├── utils/
│   ├── __init__.py
│   ├── validator.py          # Input validation (ID format, email, phone, ranges)
│   └── menu.py               # CLI navigation and formatting helpers
│
├── docs/
│   ├── REPORT.pdf            # Technical specification report
│   └── SLIDES.pptx           # Presentation deck
│
├── main.py                   # Application entry point
├── requirements.txt          # Environment dependencies (if any)
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher installed on your machine.

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

---

## 👥 Project Team (Group 4 - Class AI2102)

| Student ID | Full Name | Role | Responsibilities |
| :--- | :--- | :--- | :--- |
| **SE211528** | **Nguyễn Thái Huy** | **Team Leader / Core Dev** | Project setup, modular architecture, CLI integration, testing & code review. |
| **SE211681** | **Trần Võ Hồng Ngọc** | **Core Developer** | Data model design, Student management services, technical documentation (`REPORT.pdf`). |
| **SE211294** | **Vũ Ngọc Anh** | **Core Developer** | Result model, grading evaluation logic, File I/O persistence handlers. |
| **SE211746** | **Nguyễn Thái Sơn** | **Developer** | Data validation utilities, exception handling, presentation slides (`SLIDES.pptx`). |

* **Supervising Lecturer:** Lê Thị Hồng Nga
* **Institution:** FPT University

---

## 📄 License
This project is developed for academic purposes within the **PFP191** curriculum at FPT University.