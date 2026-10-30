# Code Atlas — SMS / PFP191

Web học tương tác tiếng Việt, tông sáng, buildless HTML/CSS/JavaScript. Không thay đổi logic Python hoặc file dữ liệu của ứng dụng.

## Chạy tại máy

Từ thư mục gốc dự án:

```powershell
python -m http.server 4173 --directory docs/learning-web/dist
```

Mở http://localhost:4173. Cũng có thể mở dist/index.html trực tiếp; Mermaid được đóng gói sẵn, font dùng Google Fonts và có font dự phòng nếu offline.

## Nội dung

- UML 5 class, chọn từng lớp, phóng to/thu nhỏ.
- 95 flowchart, chạy từng bước/tự động, chọn nhánh, chọn trực tiếp node và tự cuộn theo node đang chạy.
- 13 file / 838 dòng code với giải thích theo dòng, tìm kiếm, đi tới hàm, đọc tự động và tiến độ lưu localStorage.
- Ba mô phỏng có animation: thêm kết quả, cập nhật điểm, chưa có FE; thanh kéo thử Pass/Fail và câu hỏi tự kiểm.
- Tài liệu Markdown gốc có thể tải xuống.

Đây là bản chụp code ngày 30/10/2026. Khi thay Python sau này cần cập nhật data.js và tài liệu đi kèm. Mô phỏng không thực thi Python thật. Thông tin mẫu minh họa, không tải students.txt/results.txt lên web.

## Kiểm chứng

Đã kiểm tra render toàn bộ 95 flowchart trên trình duyệt; kiểm tra UML, đọc code tự động, mô phỏng bước và trạng thái None. JavaScript đã qua node --check. Script kiểm tra dùng một lần không lưu trong repository.

Mermaid 11 được đóng gói trong dist/mermaid.min.js (MIT). Nguồn: https://www.npmjs.com/package/mermaid.

## Bản mô phỏng dữ liệu

Trang mặc định #cinema: 8 bài phim / 58 cảnh, minh họa tạo sinh viên, duyệt list tìm kiếm, thêm kết quả, cập nhật điểm qua biến tạm, None so với 0, sorted/lọc Pass, serialize/đọc lại file và ValueError/nhập lại. Thẻ dữ liệu di chuyển bằng Web Animations API; các giá trị trước/sau, lời giải thích và dòng source được đồng bộ theo cảnh. Có phát/tạm dừng, cảnh trước/sau, thanh chọn cảnh, tốc độ và chế độ tập trung. Trên điện thoại bảng giữ cỡ chữ và camera cuộn theo thẻ thay vì thu chữ quá nhỏ.

Font nội dung tăng lên 16–19px, phụ đề 19–21px; code 14–15px. UML/flowchart không bị ép nhỏ toàn bộ vào khung; có thể cuộn và zoom.

Đã kiểm tra đủ 58 cảnh qua UI không lỗi JavaScript; đối chiếu đủ 58 tham chiếu source; không giữ file kiểm tra dùng một lần trong repository. Mô phỏng sorted chỉ minh họa khóa và kết quả, không tự nhận mô phỏng thuật toán nội bộ Python.
