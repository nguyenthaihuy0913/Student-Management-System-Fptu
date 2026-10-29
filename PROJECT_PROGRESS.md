# PFP191 - Student Management System (SMS) - FPT University
## Project Context, Progress Tracking & Roadmap

* **Course**: PFP191 (Programming Fundamentals with Python)
* **Class**: AI2102 | **Group**: 4 | **Topic**: 4 (Student Management System)
* **Team Members**:
  * Nguyễn Thái Huy (SE211528) - Team Leader & Core Developer
  * Trần Võ Hồng Ngọc (SE211681)
  * Vũ Ngọc Anh (SE211294)
  * Nguyễn Thái Sơn (SE211746)
* **Supervising Lecturer**: Lê Thị Hồng Nga
* **Last Updated**: October 30, 2026

---

## 📌 1. Overall Status Summary

| Lab / Milestone | Status | Key Deliverables & Focus |
| :--- | :--- | :--- |
| **Lab 1 & 2** | ✅ Completed | Problem statement, functional requirements decomposition, flowcharts. |
| **Lab 3 (4.3)** | ✅ Completed | Functional implementation, loops, input validation, edge cases handling, report snippets. |
| **Lab 4 (4.4)** | 🔄 In Progress (50%) | OOP Design (Inheritance, Encapsulation, Polymorphism), modular architecture (`models/`, `utils/`, `services/`). |
| **Lab 5 (4.5)** | ⏳ Queued | Safe file persistence (`file_service.py`), Exception Handling (`try...except...finally`), Automated Test Cases (`tests/test_system.py`). |
| **Final Report** | ⏳ Queued | Formal Documentation according to `3. Huong_Dan_Sinh_Vien_PBL_CT.pdf` + AI Audit Log (+1.0 bonus). |

---

## 📂 2. Architecture & File Structure

```text
Student-Management-System-Fptu/
├── models/                         # [Lab 4] Data Models (OOP Entities)
│   ├── __init__.py                 # [DONE] Exports Person, Student, Result
│   ├── person.py                   # [DONE] Base class Person (Encapsulation, @property, __str__)
│   ├── student.py                  # [DONE] Subclass Student(Person) (Inheritance, to_file_line)
│   └── result.py                   # [DONE] Result class (Auto Pass/Fail logic, to_file_line)
│
├── utils/                          # [Lab 4] Shared Utilities & Validation
│   ├── __init__.py                 # [DONE] Exports all validation functions
│   └── validator.py                # [DONE] All FPTU input validation rules (No explanatory comments)
│
├── services/                       # [Lab 4 + Lab 5] Business Logic & Persistence
│   ├── __init__.py                 # [NEXT] Package init
│   ├── file_service.py             # [NEXT] Safe reading/writing of Student & Result objects
│   ├── student_manager.py          # [NEXT] StudentManager class managing List[Student]
│   └── result_manager.py           # [NEXT] ResultManager class managing List[Result]
│
├── tests/                          # [Lab 5] Verification Suite
│   └── test_system.py              # [QUEUED] Automated test cases for edge cases and file roundtrips
│
├── students.txt                    # [LIVE] Pipe-delimited UTF-8 student storage (8 columns)
├── results.txt                     # [LIVE] Pipe-delimited UTF-8 result storage (5 columns)
├── main.py                         # [NEXT] Clean CLI driver calling StudentManager & ResultManager
└── PROJECT_PROGRESS.md             # [THIS FILE] Context & State Persistence
```

---

## 🚀 3. Detailed Work Completed

### Step 1: Data Models (`models/`) - [DONE]
* **`models/person.py`**:
  * Implements `Person` base class with protected attributes (`_full_name`, `_date_of_birth`, `_gender`, `_phone`, `_email`).
  * Demonstrates **Encapsulation** using `@property` getters and setters.
  * Overrides `__str__` for clean string representation.
* **`models/student.py`**:
  * Demonstrates **Inheritance**: `class Student(Person):`.
  * Calls `super().__init__(...)` to reuse base demographic attributes.
  * Adds student-specific fields: `_student_id`, `_class_name`, `_status`.
  * Overrides `__str__` and implements `to_file_line()` for file serialization.
* **`models/result.py`**:
  * Encapsulates `_student_id`, `_course_id`, `_grade_fe`, `_grade_re`.
  * Dynamic Computed Property `@property def result_status(self)`:
    $$\text{Pass} \iff \text{FE} \ge 5.0 \lor (\text{FE} < 5.0 \land \text{RE} \ge 5.0)$$
  * Implements `to_file_line()` and `__str__`.
* **Testing**: Unit tests passed 100% across all 4 grading scenarios.

### Step 2: Input Validator (`utils/validator.py`) - [DONE]
* Centralized all input validation routines into a single reusable module.
* Clean code style: Strictly **no explanatory comments** as requested by the team leader.
* Implemented functions:
  * `input_student_id()`: Rejects `|`, validates 16 campus prefixes (`SE, SS, SA, SB, DE, DA, DS, HE, HA, HS, QE, QA, QS, CE, CA, CS`) + 6 digits, allows `0` to cancel.
  * `input_name()`: Cleans extra spaces between words (`" ".join(raw.split()).title()`), enforces alpha + space only.
  * `input_date_of_birth()`: Validates `DD/MM/YYYY`, calendar accuracy, and year range 1900 to current year.
  * `input_gender()`: Accepts `Male` / `Female` (case-insensitive).
  * `input_class_name()`: Alphanumeric 2–10 characters (e.g. `AI2102`).
  * `input_phone()`: Starts with `0`, exactly 10 digits.
  * `input_email()`: Enforces `@fpt.edu.vn` domain and valid format.
  * `input_status()`: Enforces `Active`, `Dropout`, `Suspended`.
  * `input_course_id()`: Alphanumeric 3–10 characters, uppercase, no space, allows `0` to cancel.
  * `input_score()`: Float range `0.0 - 10.0`, rounded to 1 decimal place.

---

## 🎯 4. Immediate Next Steps

1. **Step 3: Create `services/file_service.py`**:
   * Functions: `load_students(filepath) -> List[Student]`, `save_students(filepath, list_students)`.
   * Functions: `load_results(filepath) -> List[Result]`, `save_results(filepath, list_results)`.
   * Robust exception handling with `try...except FileNotFoundError...finally: file.flush(); file.close()`.
2. **Step 4: Create Business Managers**:
   * `services/student_manager.py`: `StudentManager` handling `self._students = []`, CRUD, active filter, search.
   * `services/result_manager.py`: `ResultManager` handling `self._results = []`, grade input, checking active status with `StudentManager`, sorting, passed student filtering.
3. **Step 5: Refactor `main.py`**:
   * Initialize file service, load objects into managers, run cleanly separated CLI menus.
4. **Step 6: Automated Testing (`tests/test_system.py`)**:
   * Build automated test suite for Lab 5 evaluation.

---

## 🗣️ 5. Cheat-Sheet for Oral Defense (Vấn đáp giảng viên)

* **Hỏi**: *"Tại sao nhóm dùng `@property`?"*
  * **Đáp**: *"Dạ thưa cô, ở Slide 11 bài Part 2 cô dạy về **Enhancing Encapsulation**, cô có hướng dẫn dùng `@property` để kiểm soát truy cập dữ liệu nội bộ. Nhóm em áp dụng để bảo vệ các thuộc tính của `Student` và giúp `Result` tự động suy ra trạng thái `Pass/Fail` mà không cần nhập tay ạ."*
* **Hỏi**: *"Kế thừa thể hiện ở đâu?"*
  * **Đáp**: *"Dạ lớp `Student` kế thừa lớp `Person` (`class Student(Person):`). Lớp `Student` gọi `super().__init__(...)` để tái sử dụng thông tin họ tên, ngày sinh, giới tính, SĐT, email từ `Person`, và chỉ bổ sung thêm mã số, lớp, và trạng thái sinh viên ạ."*
* **Hỏi**: *"Nếu mất điện hoặc ngắt đột ngột thì dữ liệu có bị hỏng file không?"*
  * **Đáp**: *"Dạ không, ở `services/file_service.py` tụi em luôn dùng khối `try...finally:` kết hợp `file.flush()` và `file.close()` để đẩy sạch dữ liệu từ buffer xuống ổ cứng trước khi đóng file ạ."*
