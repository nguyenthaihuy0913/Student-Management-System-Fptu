# PFP191 - Student Management System

Cập nhật 31/10/2026. Lớp AI2102, nhóm 4; giảng viên Lê Thị Hồng Nga.

## Lab 4 - mục 4.4 (Hoàn thành 100%)

Đã triển khai và tích hợp:

- Person, Student(Person), Result; constructors, property, __str__.
- Đồng bộ hiển thị trạng thái chưa có điểm thành "Not graded" (100% tiếng Anh cho source code và báo cáo).
- Validation dùng chung trong utils/validator.py; model kiểm tra khi khởi tạo/cập nhật.
- StudentManager quản lý list[Student], ResultManager quản lý list[Result].
- Menu gọi manager, main kết nối object từ File I/O tới manager.
- Một công thức Pass/Fail tại Result; mã định danh chỉ đọc qua property.
- UML kiến trúc đầy đủ tại docs/guides/01_UML_KIEN_TRUC.md.
- Hoàn thành phần Object-Oriented Design (Mục 5) trong báo cáo `docs/PFP191_Report (1).docx` kèm sơ đồ lớp UML và bảng 4 trụ cột OOP.

## Dữ liệu lịch sử

results.txt đã chuyển đủ 8 cột cho 4 bản ghi. PFP191: Programming Fundamentals with Python; MAE101: Mathematics for Engineering. Hai môn cùng Fall2026, mỗi môn 3 tín chỉ; cùng học kỳ và tín chỉ do nhóm xác nhận, Fall2026 dùng theo ngữ cảnh dự án. MSSV, điểm FE/RE và Pass/Fail giữ nguyên. Đã kiểm tra tải qua hai manager. Loader vẫn hỗ trợ file 5 cột cũ. Khóa kết quả vẫn là student_id + course_id; việc học lại khác kỳ cần xác nhận nếu mở rộng.

## Lab 5 - mục 4.5 (Tiến độ: ~80%)

Đã triển khai và kiểm chứng:

1. File I/O và Exception Handling: Đọc/ghi file text chuẩn định dạng pipe `|`, xử lý ngoại lệ an toàn (`FileNotFoundError` khởi tạo list rỗng, bắt `ValueError` khi sai cột bảo vệ file gốc, bắt `OSError` khi lưu đĩa lỗi, bắt `Ctrl+C` lưu trước khi thoát).
2. Xây dựng và thực thi bộ kiểm thử tự động `run_tests.py` bao quát 8 test cases thực tế (TC01 - TC08), tỷ lệ đạt 100% (8/8 PASS).
3. Biên soạn tài liệu chi tiết song ngữ Anh - Việt cho toàn bộ kịch bản kiểm thử tại [docs/LAB5_TEST_CASES.md](LAB5_TEST_CASES.md).
4. Chuẩn bị sẵn nội dung tiếng Anh học thuật cho Mục 6 (File I/O & Testing) để đưa vào file báo cáo Word.

Còn lại:

1. Dán nội dung Mục 6 từ `docs/LAB5_TEST_CASES.md` vào file báo cáo Word.
2. Chụp ảnh minh chứng màn hình console đưa vào Mục 7 (Experimental Results).
3. Xuất file REPORT.pdf và làm slide SLIDES.pptx.

Không thêm database/framework/GUI/GPA/Delete hoặc design pattern ngoài phạm vi môn học PFP191.
