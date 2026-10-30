# Chi tiết bộ kiểm thử Lab 5 / Lab 5 Test Cases Specification
**Dự án / Project:** Student Management System (SMS) - FPT University  
**Môn học / Course:** PFP191 – Programming Fundamentals with Python  
**Lớp / Class:** AI2102 | **Nhóm / Group:** 4  
**File thực thi / Runner:** `run_tests.py`

---

## MỤC LỤC / TABLE OF CONTENTS
1. [Tổng quan kết quả / Test Execution Summary](#1-tổng-quan-kết-quả--test-execution-summary)
2. [Chi tiết 8 Test Cases (Tiếng Việt)](#2-chi-tiết-8-test-cases-tiếng-việt)
   - [TC01: Xử lý khi không tìm thấy file dữ liệu](#tc01-xử-lý-khi-không-tìm-thấy-file-dữ-liệu-filenotfounderror)
   - [TC02: Chặn file dữ liệu bị hỏng hoặc sai số cột](#tc02-chặn-file-dữ-liệu-bị-hỏng-hoặc-sai-số-cột)
   - [TC03: Chặn trùng mã số sinh viên](#tc03-chặn-trùng-mã-số-sinh-viên-student-id)
   - [TC04: Kiểm tra tính hợp lệ của thang điểm](#tc04-kiểm-tra-tính-hợp-lệ-của-thang-điểm-00---100)
   - [TC05: Ràng buộc sinh viên Inactive không được nhập điểm](#tc05-ràng-buộc-sinh-viên-inactive-không-được-nhập-điểm)
   - [TC06: Tự động đánh giá kết quả Pass / Fail / Not graded](#tc06-tự-động-đánh-giá-kết-quả-pass--fail--not-graded)
   - [TC07: Kiểm thử toàn vẹn dữ liệu Round-trip (Ghi -> Nạp lại)](#tc07-kiểm-thử-toàn-vẹn-dữ-liệu-round-trip-ghi---nạp-lại)
   - [TC08: Bắt lỗi ngoại lệ phòng thủ khi lưu file thất bại](#tc08-bắt-lỗi-ngoại-lệ-phòng-thủ-khi-lưu-file-thất-bại-oserror)
3. [Lab 5 Test Specification & Report Content (English for Word Report)](#3-lab-5-test-specification--report-content-english)

---

## 1. TỔNG QUAN KẾT QUẢ / TEST EXECUTION SUMMARY

| ID | Tên kịch bản / Test Name | Mục tiêu / Objective | Kỳ vọng / Expected | Kết quả / Actual | Đánh giá / Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC01** | Missing Data File | Xử lý file không tồn tại | Trả về list rỗng `[]`, không crash | Báo Info, trả về `[]` | **PASS** |
| **TC02** | Corrupted File Columns | Chặn file sai định dạng cột | Bắt `ValueError`, dừng nạp | Ném `ValueError` dòng lỗi | **PASS** |
| **TC03** | Duplicate Student ID | Đảm bảo tính duy nhất của ID | Bắt `ValueError` trùng ID | Chặn thêm, ném `ValueError` | **PASS** |
| **TC04** | Invalid Score Range | Kiểm tra thang điểm 0 - 10 | Chặn điểm < 0, > 10, chữ cái | Ném `ValueError` | **PASS** |
| **TC05** | Inactive Student Grade | Ràng buộc nghiệp vụ trạng thái | Chỉ sinh viên `Active` mới có điểm | Chặn và báo lỗi `Active only` | **PASS** |
| **TC06** | Pass/Fail Logic | Công thức tính kết quả tự động | Pass/Fail/None chính xác | Đúng 100% 4 trường hợp | **PASS** |
| **TC07** | Persistence Round-trip | Bảo toàn dữ liệu qua file txt | Dữ liệu nạp lại khớp 100% | Khớp nguyên vẹn các trường | **PASS** |
| **TC08** | Defensive File Save | Phòng thủ lỗi ghi đĩa/quyền | Bắt `OSError`, trả về `False` | Bắt lỗi êm đẹp, không crash | **PASS** |

**Tỷ lệ đạt:** 8/8 Test Cases PASSED (100.0%)

---

## 2. CHI TIẾT 8 TEST CASES (TIẾNG VIỆT)

### TC01: Xử lý khi không tìm thấy file dữ liệu (FileNotFoundError)
- **Mục tiêu:** Kiểm tra phản ứng của hệ thống trong lần đầu khởi chạy khi các file dữ liệu `students.txt` hoặc `results.txt` chưa từng được tạo ra trên đĩa.
- **Tiền điều kiện:** Đường dẫn file trỏ đến một file không tồn tại (`non_existent.txt`).
- **Thao tác kiểm thử:** Gọi hàm `file_io.load_students(fake_path)` và `file_io.load_results(fake_path)`.
- **Kết quả kỳ vọng:** Hệ thống không bị văng crash chương trình; bắt được ngoại lệ `FileNotFoundError`, in thông báo `[Info]` thân thiện và khởi tạo danh sách rỗng `[]`.
- **Kết quả thực tế:** Chương trình in `[Info] ... not found; starting empty.` và trả về `[]`.
- **Đánh giá:** **PASS**.

---

### TC02: Chặn file dữ liệu bị hỏng hoặc sai số cột
- **Mục tiêu:** Ngăn chặn việc nạp dữ liệu rác hoặc dữ liệu bị sửa đổi thủ công trái phép làm sai lệch bộ nhớ của ứng dụng.
- **Tiền điều kiện:** Tạo một file tạm thời có dòng dữ liệu chỉ có 3 cột thay vì bắt buộc 8 cột (`SE211528|Nguyen Thai Huy|InvalidLine`).
- **Thao tác kiểm thử:** Gọi `file_io.load_students(corrupt_file)`.
- **Kết quả kỳ vọng:** Bắt được lỗi sai định dạng, ném ra ngoại lệ `ValueError` chỉ rõ số dòng bị sai để `main.py` dừng khởi động an toàn, bảo vệ dữ liệu gốc.
- **Kết quả thực tế:** Bắt được `ValueError: ... line 1: expected 8 student fields.`
- **Đánh giá:** **PASS**.

---

### TC03: Chặn trùng mã số sinh viên (Student ID)
- **Mục tiêu:** Bảo vệ tính toàn vẹn của thuộc tính định danh duy nhất (`student_id`), không cho phép 2 sinh viên có cùng mã số.
- **Tiền điều kiện:** `StudentManager` đã chứa sinh viên `SE211528` (Nguyễn Thái Huy).
- **Thao tác kiểm thử:** Tạo sinh viên thứ 2 cũng có mã `SE211528` và gọi `manager.add(s2)`.
- **Kết quả kỳ vọng:** Quản lý sinh viên từ chối thêm mới và ném ra ngoại lệ `ValueError("Student ID already exists.")`.
- **Kết quả thực tế:** Bắt được `ValueError: Student ID already exists.`
- **Đánh giá:** **PASS**.

---

### TC04: Kiểm tra tính hợp lệ của thang điểm (0.0 - 10.0)
- **Mục tiêu:** Đảm bảo điểm thi Final Exam (FE) và Retake Exam (RE) tuân thủ đúng quy chế đào tạo của trường FPT (từ 0.0 đến 10.0 điểm).
- **Tiền điều kiện:** Hàm thẩm định `validate_score`.
- **Thao tác kiểm thử:** Nhập các giá trị bất hợp lệ:
  1. Điểm âm: `-1.0`
  2. Điểm vượt ngưỡng: `10.5`
  3. Ký tự chữ cái: `"abc"`
- **Kết quả kỳ vọng:** Tất cả các giá trị không hợp lệ đều bị chặn và kích hoạt ngoại lệ `ValueError`.
- **Kết quả thực tế:** Cả 3 trường hợp đều bị từ chối chính xác bởi validator.
- **Đánh giá:** **PASS**.

---

### TC05: Ràng buộc sinh viên Inactive không được nhập điểm
- **Mục tiêu:** Kiểm tra quy tắc nghiệp vụ (Business Logic): Chỉ sinh viên đang có trạng thái `Active` mới được phép ghi nhận điểm môn học mới.
- **Tiền điều kiện:** Sinh viên `SE211294` có trạng thái học tập là `Inactive` (Thôi học / Tạm hoãn).
- **Thao tác kiểm thử:** Gọi `ResultManager.add()` để nhập điểm môn `PFP191` cho sinh viên này.
- **Kết quả kỳ vọng:** `ResultManager` gọi `check_student()` và phát hiện sinh viên không `Active`, ném ra lỗi `ValueError("Only Active students can have grades added or updated.")`.
- **Kết quả thực tế:** Bắt được thông báo lỗi chặn sinh viên Inactive chính xác.
- **Đánh giá:** **PASS**.

---

### TC06: Tự động đánh giá kết quả Pass / Fail / Not graded
- **Mục tiêu:** Kiểm chứng thuật toán tính trạng thái qua môn tự động theo đúng đề bài Topic 4 (`grade_fe >= 5.0` hoặc `grade_re >= 5.0`).
- **Tiền điều kiện:** Phương thức tĩnh `Result.evaluate_status(grade_fe, grade_re)`.
- **Thao tác kiểm thử:** Thử nghiệm 4 bộ điểm độc lập:
  1. `FE = 8.5`, `RE = None` -> Đạt ngay vòng thi đầu.
  2. `FE = 4.0`, `RE = 7.5` -> Vòng 1 dưới 5, thi lại vòng 2 đạt 7.5.
  3. `FE = 3.5`, `RE = 4.0` -> Cả 2 vòng đều dưới 5.0.
  4. `FE = None`, `RE = None` -> Chưa nhập điểm thi.
- **Kết quả kỳ vọng:** Lần lượt trả về: `"Pass"`, `"Pass"`, `"Fail"`, `None`.
- **Kết quả thực tế:** Hệ thống trả về chính xác 100% cả 4 trạng thái, không cần người dùng nhập tay trạng thái.
- **Đánh giá:** **PASS**.

---

### TC07: Kiểm thử toàn vẹn dữ liệu Round-trip (Ghi -> Nạp lại)
- **Mục tiêu:** Chứng minh chu trình lưu trữ (Persistence Life-cycle): dữ liệu từ Object trong bộ nhớ RAM ghi xuống file text trên đĩa cứng, sau đó nạp ngược lại thành Object mà không hề bị mất mát hay biến dạng.
- **Tiền điều kiện:** 2 đối tượng `Student` và 2 đối tượng `Result` đầy đủ thuộc tính và ký tự tiếng Việt.
- **Thao tác kiểm thử:**
  1. Gọi `file_io.save_records()` ghi ra file tạm.
  2. Gọi `file_io.load_students()` và `file_io.load_results()` đọc lại từ file tạm đó.
- **Kết quả kỳ vọng:** Danh sách nạp lại có số lượng và nội dung (MSSV, tên tiếng Việt, điểm số, trạng thái Pass) khớp tuyệt đối với ban đầu.
- **Kết quả thực tế:** Dữ liệu sau khi nạp lại bảo toàn nguyên vẹn 100%.
- **Đánh giá:** **PASS**.

---

### TC08: Bắt lỗi ngoại lệ phòng thủ khi lưu file thất bại (OSError)
- **Mục tiêu:** Đảm bảo hệ thống có cơ chế phòng vệ (Defensive Programming), không bị crash đột ngột nếu hệ điều hành từ chối thao tác ghi đĩa (ví dụ ổ đĩa không tồn tại, đầy bộ nhớ, hoặc thư mục chỉ đọc).
- **Tiền điều kiện:** Đường dẫn file trỏ đến một ổ đĩa không hề tồn tại trên máy tính (`Z:/NonExistentDrive_XYZ/invalid_file.txt`).
- **Thao tác kiểm thử:** Gọi `file_io.save_records(invalid_path, [])`.
- **Kết quả kỳ vọng:** Bắt được ngoại lệ hệ thống `OSError`, in thông báo lỗi `[Error] Cannot save ...` và trả về `False` để menu chính biết quá trình lưu thất bại, cho phép người dùng thử lại.
- **Kết quả thực tế:** Bắt được `[Errno 2] No such file or directory`, trả về `False` an toàn mà không crash ứng dụng.
- **Đánh giá:** **PASS**.

---

## 3. LAB 5 TEST SPECIFICATION & REPORT CONTENT (ENGLISH)
*(Phần này được viết bằng tiếng Anh học thuật, ông có thể copy trực tiếp vào **Mục 6. File I/O & Testing** trong file báo cáo Word)*

### 6.1. File Storage Architecture & Format Specification
The system utilizes plain-text flat files (`students.txt` and `results.txt`) for persistent data storage. Records are structured line-by-line, utilizing the pipe character (`|`) as a clean delimiter to prevent conflicts with standard comma-separated or space-separated user inputs:
- **Student Record Format (8 fields):**
  `student_id|full_name|date_of_birth|gender|class_name|phone|email|status`
- **Result Record Format (8 fields):**
  `student_id|course_id|course_name|semester|credits|grade_fe|grade_re|result_status`

### 6.2. Exception Handling & Defensive File Operations
The application implements defensive file management across all I/O boundary routines:
- **Safe Resource Management:** All file reads and writes are encapsulated within Python's `with open(...)` context managers, guaranteeing that system file handles are cleanly closed even if runtime exceptions occur.
- **Missing File Resilience:** When files are not found on startup (`FileNotFoundError`), the system gracefully issues an informational log and initializes an empty in-memory repository without crashing.
- **Corruption Prevention:** If an external process mutates records with an invalid column count, `file_io` raises a descriptive `ValueError`, causing `main.py` to abort startup immediately, thereby preventing accidental data corruption or overwrite.
- **Defensive Save Handling:** Disk write errors (`OSError`, `PermissionError`) are captured cleanly within `save_records()`, returning a boolean failure flag (`False`) so the main CLI menu can prompt the user to retry rather than losing unsaved progress.

### 6.3. Comprehensive Test Matrix & Experimental Verification

| Test ID | Test Scenario | Preconditions / Input | Expected Behavior | Actual Behavior | Result |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC01** | Missing data file handling | Target path points to non-existent file | Catch `FileNotFoundError`, return empty list `[]`, log info message | Handled cleanly, initialized empty collection | **PASS** |
| **TC02** | Malformed record handling | File line contains 3 columns instead of 8 | Raise `ValueError` indicating line and field count | Caught `ValueError: expected 8 student fields` | **PASS** |
| **TC03** | Primary key uniqueness check | Add student with already existing `student_id` | Raise `ValueError` ("Student ID already exists") | Rejected duplicate addition, raised error | **PASS** |
| **TC04** | Numerical grade bounds validation | Enter grade values: `-1.0`, `10.5`, `"abc"` | Raise `ValueError` for out-of-bounds or non-numeric inputs | All invalid scores rejected by `validate_score` | **PASS** |
| **TC05** | Academic status business rule | Attempt to add course grade for `Inactive` student | Enforce `Active` status constraint via `check_student()` | Blocked with `ValueError: Only Active students...` | **PASS** |
| **TC06** | Pass/Fail automated evaluation | Evaluate score pairs: `(8.5, None)`, `(4.0, 7.5)`, `(3.5, 4.0)`, `(None, None)` | Correctly evaluate: `Pass`, `Pass`, `Fail`, `None` | Evaluated accurately matching university grading logic | **PASS** |
| **TC07** | Persistence round-trip integrity | Save 2 students & 2 results to file, then reload | 100% data fidelity preserved across write/read cycle | Reloaded objects match original data perfectly | **PASS** |
| **TC08** | Storage write failure defense | Attempt save operation to an invalid drive path | Catch `OSError`, return `False`, prevent application crash | Returned `False` with error message, runtime stable | **PASS** |
