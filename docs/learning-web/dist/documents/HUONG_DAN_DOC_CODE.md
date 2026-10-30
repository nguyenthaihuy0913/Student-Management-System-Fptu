# Hướng dẫn đọc code SMS cho nhóm PFP191

Bản chụp code ngày 30/10/2026. Chỉ bổ sung tài liệu, không sửa logic hay thêm comment vào source.

1. Đọc [UML và kiến trúc](01_UML_KIEN_TRUC.md) để biết mỗi lớp giữ gì và ai gọi ai.
2. Đọc [flowchart](02_FLOWCHART.md), bắt đầu từ main rồi theo chức năng mình phụ trách.
3. Mở [giải thích từng dòng](03_GIAI_THICH_TUNG_DONG.md) cùng source để đối chiếu. Bao phủ tất cả 13 file Python; dòng trống chỉ phân cách nên không chú giải riêng.

Sơ đồ dùng Mermaid. Mở Markdown bằng trình xem hỗ trợ Mermaid (ví dụ Markdown Preview của VS Code có hỗ trợ Mermaid). Mỗi method/hàm có flowchart riêng để không biến toàn dự án thành một sơ đồ quá lớn. Getter/setter cùng tên được phân biệt bằng loại và số dòng.

Số dòng và nội dung ở đây ứng với bản code được chụp; sửa source sau này có thể làm số dòng lệch. Phụ lục có SHA-256 để đối chiếu phiên bản. Đây là tài liệu học nội bộ, chưa thay thế report/slide bàn giao.

## Lộ trình học nhóm

- Huy: main -> menu -> manager; giải thích cách các phần kết nối.
- Ngọc: Person/Student -> validator -> StudentManager -> menu sinh viên.
- Anh: Result -> ResultManager -> menu kết quả; nắm rõ None, FE và RE.
- Sơn: file_io -> serialization -> main.save_data; giải thích lỗi truyền về đâu.
- Mỗi người vẫn nên đọc luồng khởi động, thêm điểm và lưu/thoát để hiểu toàn hệ thống.
