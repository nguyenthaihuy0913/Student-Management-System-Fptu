# PFP191 - Student Management System

Cập nhật 30/10/2026. Lớp AI2102, nhóm 4; giảng viên Lê Thị Hồng Nga.

## Lab 4 - mục 4.4

Đã triển khai và tích hợp:

- Person, Student(Person), Result; constructors, property, __str__.
- Validation dùng chung trong utils/validator.py; model kiểm tra khi khởi tạo/cập nhật.
- StudentManager quản lý list[Student], ResultManager quản lý list[Result].
- Menu gọi manager, main kết nối object từ File I/O tới manager.
- Result đủ trường đề bài; điểm float/None; FE chưa có -> status None, hiển thị Chưa có điểm theo lựa chọn nhóm.
- Một công thức Pass/Fail tại Result; mã định danh chỉ đọc qua property.
- UML, trách nhiệm module và giải thích kiến thức tại [README dự án](../README.md).
- 10 kiểm thử model/manager/CLI/round-trip đã qua; script đã xóa theo yêu cầu nhóm, dữ liệu thật giữ nguyên.

Lab 4 phần triển khai đã hoàn thành trong phạm vi trên; việc đánh giá/nộp bài theo giảng viên. Nhóm cần nắm thiết kế và chuẩn bị trình bày UML.

## Dữ liệu lịch sử

results.txt đã chuyển đủ 8 cột cho 4 bản ghi. PFP191: Programming Fundamentals with Python; MAE101: Mathematics for Engineering. Hai môn cùng Fall2026, mỗi môn 3 tín chỉ; cùng học kỳ và tín chỉ do nhóm xác nhận, Fall2026 dùng theo ngữ cảnh dự án. MSSV, điểm FE/RE và Pass/Fail giữ nguyên. Đã kiểm tra tải qua hai manager. Loader vẫn hỗ trợ file 5 cột cũ. Khóa kết quả vẫn là student_id + course_id; việc học lại khác kỳ cần xác nhận nếu mở rộng.

## Lab 5 - mục 4.5

Đã có File I/O object cơ bản và chặn khởi động khi tải dữ liệu lỗi; chưa hoàn thành Lab 5.

Còn lại:

1. Thiết kế an toàn ghi file phù hợp, xử lý ghi dở/lỗi một file; không khẳng định flush/close chống mất điện.
2. Lập và thực thi test cases lỗi dữ liệu/file/quyền truy cập, Ctrl+C, save failure, khởi động lại; bảng Expected/Actual/Pass-Fail và ảnh minh chứng.
3. Hoàn thiện phần File I/O & Testing và Experimental Results trong báo cáo.
4. REPORT.pdf, SLIDES.pptx; AI Audit Log tùy chọn, chỉ ghi tương tác và kiểm chứng thực tế.

Không thêm database/framework/GUI/GPA/Delete hoặc design pattern vào phạm vi Lab 4.
