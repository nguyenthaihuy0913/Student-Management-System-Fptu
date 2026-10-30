# Giải thích từng dòng code

[Quay lại mục lục](HUONG_DAN_DOC_CODE.md)

Code nguyên bản nằm ở cột giữa; chú giải ở cột cuối. Dòng dài được giữ đúng nội dung. Với lệnh trải nhiều dòng, chú giải nêu rõ dòng bắt đầu tương ứng.


## Các cú pháp cần hiểu trước khi đọc bảng

| Cú pháp thực tế | Cách đọc bằng tiếng Việt |
| --- | --- |
| `self` | Object hiện tại. Hai Student khác nhau có self và dữ liệu riêng |
| `self.full_name = ...` | Gọi setter full_name; setter mới ghi `_full_name` sau khi validation thành công |
| `value[:2]` | Hai ký tự đầu; `value[2:]` là phần từ ký tự thứ ba trở đi |
| `parts[-1]` | Phần tử cuối, dùng kiểm tra đuôi tên miền |
| `Path(__file__).resolve().parent` | Lấy đường dẫn tuyệt đối file main.py rồi lấy thư mục cha |
| `BASE_DIR / "results.txt"` | Ghép đường dẫn bằng Path, không phải phép chia số |
| `None` / `""` / `0` | Chưa có giá trị / chuỗi rỗng / số không; không được coi ba trường hợp là một |
| `a is None` | Kiểm tra đúng đối tượng None; không phải so sánh điểm với 0 |
| `condition and expression` | Chỉ tính expression nếu condition đúng; bảo vệ phép so sánh với None |
| `x or []` | Nếu x là giá trị falsy (ví dụ None hoặc list rỗng), dùng list rỗng |
| `any(...)` | Đúng khi ít nhất một phần tử/điều kiện bên trong đúng |
| `re.fullmatch(pattern, value)` | Toàn bộ chuỗi phải đúng mẫu, không chỉ một đoạn |
| `[A-Z]{2}[0-9]{6}` | Hai chữ cái ASCII và sáu chữ số ASCII |
| `([A-Z]{2}[0-9]{4}\|[A-Z]{3}[0-9]{3})` | Một trong hai dạng lớp, dấu phân cách trong regex có nghĩa “hoặc” |
| `strptime(..., "%d/%m/%Y")` | Đọc ngày từ chuỗi; sai lịch sẽ raise ValueError |
| `strftime(...)` | Đổi ngày ra chuỗi để so lại đúng định dạng |
| `float(...)` / `int(...)` | Đổi sang số thực/số nguyên; phone không đổi sang số vì mất 0 đầu |
| `number.is_integer()` | Số thực không có phần lẻ: 3.0 đúng, 3.5 sai |
| `isinstance(value, bool)` | Chặn True/False trước khi xử lý điểm/tín chỉ như số |
| `lambda r: r.result_status or ""` | Hàm nhỏ nhận r, trả status hoặc chuỗi rỗng làm khóa sắp xếp |
| `[r for r in ... if ...]` | Tạo list mới bằng cách duyệt các r và giữ r thỏa điều kiện |
| `enumerate(file, 1)` | Duyệt dòng đồng thời lấy số dòng bắt đầu từ 1 |
| `"\n"` | Ký tự xuống dòng trong file/console; không phải hai ký tự slash và n khi Python chạy |
| `parts[2] or None` | Nếu cột văn bản rỗng thì chuyển thành None |
| `f"{value}"` | Chèn giá trị vào chuỗi; biểu thức trong dấu ngoặc nhọn được tính trước |
| `@staticmethod` | Method không cần object/self, thường là xử lý độc lập dùng chung trong class |
| `raise` / `except` | Đẩy lỗi lên / bắt đúng loại lỗi; có thể đi qua nhiều hàm gọi |

Dòng `import` có thể chạy code cấp module của file được nạp lần đầu; với dự án này các module chủ yếu định nghĩa class/hàm. Menu chỉ bắt đầu từ main(), không phải do import tự gọi input.


## main.py

Điểm bắt đầu: tải object, khởi tạo manager, điều hướng menu và lưu khi thoát.

[Đọc source](../../main.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from pathlib import Path</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>import file_io</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 3 | <code>from services import StudentManager, ResultManager</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>from student_management import student_sub_menu</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>from result_management import result_sub_menu</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 7 | <code>BASE_DIR = Path(__file__).resolve().parent</code> | Tính Path(__file__).resolve().parent rồi gán vào BASE_DIR. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 8 | <code>STUDENTS_FILE = BASE_DIR / &quot;students.txt&quot;</code> | Tính BASE_DIR / &#x27;students.txt&#x27; rồi gán vào STUDENTS_FILE. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 9 | <code>RESULTS_FILE = BASE_DIR / &quot;results.txt&quot;</code> | Tính BASE_DIR / &#x27;results.txt&#x27; rồi gán vào RESULTS_FILE. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 12 | <code>def save_data(students, results):</code> | Định nghĩa save_data; Thử lưu cả hai file, chỉ trả True khi cả hai thành công; không có rollback nếu chỉ một file lưu được. |
| 13 | <code>    students_ok = file_io.save_records(STUDENTS_FILE, students.students)</code> | Tính file_io.save_records(STUDENTS_FILE, students.students) rồi gán vào students_ok. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 14 | <code>    results_ok = file_io.save_records(RESULTS_FILE, results.results)</code> | Tính file_io.save_records(RESULTS_FILE, results.results) rồi gán vào results_ok. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 15 | <code>    if students_ok and results_ok:</code> | Kiểm tra students_ok and results_ok. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 16 | <code>        print(&quot;Data saved.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 17 | <code>        return True</code> | Kết thúc hàm, trả True cho nơi gọi. |
| 18 | <code>    print(&quot;Save failed. Some data may not have been saved.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 19 | <code>    return False</code> | Kết thúc hàm, trả False cho nơi gọi. |
| 22 | <code>def main():</code> | Định nghĩa main; Tải Student trước Result để kiểm tra quan hệ; tải lỗi thì dừng, menu lặp đến khi lưu thành công. |
| 23 | <code>    try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 24 | <code>        students = StudentManager(file_io.load_students(STUDENTS_FILE))</code> | Tính StudentManager(file_io.load_students(STUDENTS_FILE)) rồi gán vào students. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 25 | <code>        results = ResultManager(students, file_io.load_results(RESULTS_FILE))</code> | Tính ResultManager(students, file_io.load_results(RESULTS_FILE)) rồi gán vào results. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 26 | <code>    except (OSError, ValueError, UnicodeError) as error:</code> | Bắt (OSError, ValueError, UnicodeError) và đặt tên lỗi là error; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 27 | <code>        print(&quot;[Error] Cannot load data:&quot;, error)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 28 | <code>        print(&quot;Startup stopped; original files have not been changed.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 29 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 30 | <code>    print(f&quot;Loaded {len(students.students)} students and {len(results.results)} results.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 31 | <code>    while True:</code> | Lặp trong khi True. while True chỉ dừng khi return/ngoại lệ, hoặc chuyển vòng bằng continue. |
| 32 | <code>        try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 33 | <code>            print(&quot;\nSTUDENT MANAGEMENT SYSTEM&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 34 | <code>            print(&quot;1. Student Management\n2. Result Management\n3. Save and Exit&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 35 | <code>            choice = input(&quot;Choice: &quot;).strip()</code> | Tính input(&#x27;Choice: &#x27;).strip() rồi gán vào choice. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 36 | <code>            if choice == &quot;1&quot;:</code> | Kiểm tra choice == &#x27;1&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 37 | <code>                student_sub_menu(students)</code> | Gọi student_sub_menu(students). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 38 | <code>            elif choice == &quot;2&quot;:</code> | Kiểm tra choice == &#x27;2&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 39 | <code>                result_sub_menu(results)</code> | Gọi result_sub_menu(results). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 40 | <code>            elif choice == &quot;3&quot;:</code> | Kiểm tra choice == &#x27;3&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 41 | <code>                if save_data(students, results):</code> | Kiểm tra save_data(students, results). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 42 | <code>                    return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 43 | <code>            else:</code> | Nhánh thay thế: chỉ chạy khi các điều kiện if/elif trước đó trong cùng chuỗi đều sai. |
| 44 | <code>                print(&quot;Invalid choice.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 45 | <code>        except (KeyboardInterrupt, EOFError):</code> | Bắt (KeyboardInterrupt, EOFError); xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 46 | <code>            print(&quot;\nSaving before exit...&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 47 | <code>            if save_data(students, results):</code> | Kiểm tra save_data(students, results). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 48 | <code>                return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 49 | <code>            print(&quot;Returning to menu so you can retry saving.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 52 | <code>if __name__ == &quot;__main__&quot;:</code> | Kiểm tra __name__ == &#x27;__main__&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 53 | <code>    main()</code> | Gọi main(). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |

## models/person.py

Thông tin cá nhân dùng chung. Constructor gọi setter để kiểm tra ngay lúc tạo object.

[Đọc source](../../models/person.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from utils.validator import validate_name, validate_date_of_birth, validate_gender, validate_phone, validate_email</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>class Person:</code> | Định nghĩa class Person. Thân class khai báo các method/property. |
| 7 | <code>    def __init__(self, full_name, date_of_birth, gender, phone, email):</code> | Constructor: chạy khi tạo object; self là chính object mới, tham số mặc định chỉ dùng khi không truyền giá trị. |
| 8 | <code>        self.full_name = full_name</code> | Gán full_name vào self.full_name; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 9 | <code>        self.date_of_birth = date_of_birth</code> | Gán date_of_birth vào self.date_of_birth; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 10 | <code>        self.gender = gender</code> | Gán gender vào self.gender; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 11 | <code>        self.phone = phone</code> | Gán phone vào self.phone; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 12 | <code>        self.email = email</code> | Gán email vào self.email; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 14 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 15 | <code>    def full_name(self):</code> | Getter của property full_name: đọc bằng object.full_name, không thêm dấu (). |
| 16 | <code>        return self._full_name</code> | Kết thúc hàm, trả self._full_name cho nơi gọi. |
| 18 | <code>    @full_name.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 19 | <code>    def full_name(self, value):</code> | Setter: được gọi khi gán object.full_name = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 20 | <code>        self._full_name = validate_name(value)</code> | Lưu validate_name(value) vào self._full_name. Thuộc tính _... dùng theo quy ước nội bộ. |
| 22 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 23 | <code>    def date_of_birth(self):</code> | Getter của property date_of_birth: đọc bằng object.date_of_birth, không thêm dấu (). |
| 24 | <code>        return self._date_of_birth</code> | Kết thúc hàm, trả self._date_of_birth cho nơi gọi. |
| 26 | <code>    @date_of_birth.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 27 | <code>    def date_of_birth(self, value):</code> | Setter: được gọi khi gán object.date_of_birth = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 28 | <code>        self._date_of_birth = validate_date_of_birth(value)</code> | Lưu validate_date_of_birth(value) vào self._date_of_birth. Thuộc tính _... dùng theo quy ước nội bộ. |
| 30 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 31 | <code>    def gender(self):</code> | Getter của property gender: đọc bằng object.gender, không thêm dấu (). |
| 32 | <code>        return self._gender</code> | Kết thúc hàm, trả self._gender cho nơi gọi. |
| 34 | <code>    @gender.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 35 | <code>    def gender(self, value):</code> | Setter: được gọi khi gán object.gender = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 36 | <code>        self._gender = validate_gender(value)</code> | Lưu validate_gender(value) vào self._gender. Thuộc tính _... dùng theo quy ước nội bộ. |
| 38 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 39 | <code>    def phone(self):</code> | Getter của property phone: đọc bằng object.phone, không thêm dấu (). |
| 40 | <code>        return self._phone</code> | Kết thúc hàm, trả self._phone cho nơi gọi. |
| 42 | <code>    @phone.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 43 | <code>    def phone(self, value):</code> | Setter: được gọi khi gán object.phone = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 44 | <code>        self._phone = validate_phone(value)</code> | Lưu validate_phone(value) vào self._phone. Thuộc tính _... dùng theo quy ước nội bộ. |
| 46 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 47 | <code>    def email(self):</code> | Getter của property email: đọc bằng object.email, không thêm dấu (). |
| 48 | <code>        return self._email</code> | Kết thúc hàm, trả self._email cho nơi gọi. |
| 50 | <code>    @email.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 51 | <code>    def email(self, value):</code> | Setter: được gọi khi gán object.email = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 52 | <code>        self._email = validate_email(value)</code> | Lưu validate_email(value) vào self._email. Thuộc tính _... dùng theo quy ước nội bộ. |
| 54 | <code>    def __str__(self):</code> | Cách biểu diễn dễ đọc khi gọi str(object) hoặc print(object). |
| 55 | <code>        return f&quot;{self._full_name} &#124; {self._date_of_birth} &#124; {self._gender} &#124; {self._phone} &#124; {self._email}&quot;</code> | Kết thúc hàm, trả f&#x27;{self._full_name} &#124; {self._date_of_birth} &#124; {self._gender} &#124; {self._phone} &#124; {self._email}&#x27; cho nơi gọi. |

## models/student.py

Student kế thừa Person; bổ sung MSSV, lớp, trạng thái. MSSV không có setter.

[Đọc source](../../models/student.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from utils.validator import validate_student_id, validate_class_name, validate_status</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>from models.person import Person</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 7 | <code>class Student(Person):</code> | Định nghĩa class Student kế thừa Person. Thân class khai báo các method/property. |
| 9 | <code>    def __init__(</code> | Constructor: chạy khi tạo object; self là chính object mới, tham số mặc định chỉ dùng khi không truyền giá trị. |
| 10 | <code>        self,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 11 | <code>        student_id,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 12 | <code>        full_name,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 13 | <code>        date_of_birth,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 14 | <code>        gender,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 15 | <code>        class_name,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 16 | <code>        phone,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 17 | <code>        email,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 18 | <code>        status=&quot;Active&quot;,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 19 | <code>    ):</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 20 | <code>        super().__init__(full_name, date_of_birth, gender, phone, email)</code> | Gọi constructor Person để khởi tạo/kiểm tra các trường cá nhân trên cùng object Student. |
| 21 | <code>        self._student_id = validate_student_id(student_id)</code> | Lưu validate_student_id(student_id) vào self._student_id. Thuộc tính _... dùng theo quy ước nội bộ. |
| 22 | <code>        self.class_name = class_name</code> | Gán class_name vào self.class_name; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 23 | <code>        self.status = status</code> | Gán status vào self.status; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 25 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 26 | <code>    def student_id(self):</code> | Getter của property student_id: đọc bằng object.student_id, không thêm dấu (). |
| 27 | <code>        return self._student_id</code> | Kết thúc hàm, trả self._student_id cho nơi gọi. |
| 29 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 30 | <code>    def class_name(self):</code> | Getter của property class_name: đọc bằng object.class_name, không thêm dấu (). |
| 31 | <code>        return self._class_name</code> | Kết thúc hàm, trả self._class_name cho nơi gọi. |
| 33 | <code>    @class_name.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 34 | <code>    def class_name(self, value):</code> | Setter: được gọi khi gán object.class_name = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 35 | <code>        self._class_name = validate_class_name(value)</code> | Lưu validate_class_name(value) vào self._class_name. Thuộc tính _... dùng theo quy ước nội bộ. |
| 37 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 38 | <code>    def status(self):</code> | Getter của property status: đọc bằng object.status, không thêm dấu (). |
| 39 | <code>        return self._status</code> | Kết thúc hàm, trả self._status cho nơi gọi. |
| 41 | <code>    @status.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 42 | <code>    def status(self, value):</code> | Setter: được gọi khi gán object.status = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 43 | <code>        self._status = validate_status(value)</code> | Lưu validate_status(value) vào self._status. Thuộc tính _... dùng theo quy ước nội bộ. |
| 45 | <code>    def to_file_line(self):</code> | Định nghĩa to_file_line; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 46 | <code>        return f&quot;{self._student_id}&#124;{self._full_name}&#124;{self._date_of_birth}&#124;{self._gender}&#124;{self._class_name}&#124;{self._phone}&#124;{self._email}&#124;{self._status}\n&quot;</code> | Kết thúc hàm, trả f&#x27;{self._student_id}&#124;{self._full_name}&#124;{self._date_of_birth}&#124;{self._gender}&#124;{self._class_name}&#124;{self._phone}&#124;{self._email}&#124;{self._status}\n&#x27; cho nơi gọi. |
| 48 | <code>    def to_dict(self):</code> | Định nghĩa to_dict; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 49 | <code>        return {</code> | Trả dictionary mới ánh xạ tên trường tới giá trị; không thay object đang có. |
| 50 | <code>            &quot;student_id&quot;: self._student_id,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 51 | <code>            &quot;full_name&quot;: self._full_name,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 52 | <code>            &quot;date_of_birth&quot;: self._date_of_birth,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 53 | <code>            &quot;gender&quot;: self._gender,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 54 | <code>            &quot;class_name&quot;: self._class_name,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 55 | <code>            &quot;phone&quot;: self._phone,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 56 | <code>            &quot;email&quot;: self._email,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 57 | <code>            &quot;status&quot;: self._status,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 58 | <code>        }</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 60 | <code>    def __str__(self):</code> | Cách biểu diễn dễ đọc khi gọi str(object) hoặc print(object). |
| 61 | <code>        return f&quot;[{self._student_id}] {self._full_name} ({self._class_name}) - {self._status}&quot;</code> | Kết thúc hàm, trả f&#x27;[{self._student_id}] {self._full_name} ({self._class_name}) - {self._status}&#x27; cho nơi gọi. |

## models/result.py

Thông tin một kết quả môn học; điểm float/None, trạng thái tính động, xuất chuỗi/file.

[Đọc source](../../models/result.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from utils.validator import validate_student_id, validate_course_id, validate_text, validate_score, validate_credits</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>class Result:</code> | Định nghĩa class Result. Thân class khai báo các method/property. |
| 7 | <code>    def __init__(</code> | Constructor: chạy khi tạo object; self là chính object mới, tham số mặc định chỉ dùng khi không truyền giá trị. |
| 8 | <code>        self, student_id, course_id, course_name, semester, credits,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 9 | <code>        grade_fe=None, grade_re=None,</code> | Tiếp danh sách tham số của __init__; các tham số này chưa phải thao tác xử lý. |
| 10 | <code>    ):</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 11 | <code>        self._student_id = validate_student_id(student_id)</code> | Lưu validate_student_id(student_id) vào self._student_id. Thuộc tính _... dùng theo quy ước nội bộ. |
| 12 | <code>        self._course_id = validate_course_id(course_id)</code> | Lưu validate_course_id(course_id) vào self._course_id. Thuộc tính _... dùng theo quy ước nội bộ. |
| 13 | <code>        self.course_name = course_name</code> | Gán course_name vào self.course_name; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 14 | <code>        self.semester = semester</code> | Gán semester vào self.semester; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 15 | <code>        self.credits = credits</code> | Gán credits vào self.credits; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 16 | <code>        self.grade_fe = grade_fe</code> | Gán grade_fe vào self.grade_fe; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 17 | <code>        self.grade_re = grade_re</code> | Gán grade_re vào self.grade_re; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 19 | <code>    @staticmethod</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 20 | <code>    def _format_grade(grade):</code> | Định nghĩa _format_grade; Chuyển tiếp đến validate_score; không làm tròn hay nhân bản công thức xét điểm. |
| 21 | <code>        return validate_score(grade)</code> | Kết thúc hàm, trả validate_score(grade) cho nơi gọi. |
| 23 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 24 | <code>    def course_name(self):</code> | Getter của property course_name: đọc bằng object.course_name, không thêm dấu (). |
| 25 | <code>        return self._course_name</code> | Kết thúc hàm, trả self._course_name cho nơi gọi. |
| 27 | <code>    @course_name.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 28 | <code>    def course_name(self, value):</code> | Setter: được gọi khi gán object.course_name = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 29 | <code>        self._course_name = None if value is None else validate_text(value)</code> | Lưu None if value is None else validate_text(value) vào self._course_name. Thuộc tính _... dùng theo quy ước nội bộ. |
| 31 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 32 | <code>    def semester(self):</code> | Getter của property semester: đọc bằng object.semester, không thêm dấu (). |
| 33 | <code>        return self._semester</code> | Kết thúc hàm, trả self._semester cho nơi gọi. |
| 35 | <code>    @semester.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 36 | <code>    def semester(self, value):</code> | Setter: được gọi khi gán object.semester = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 37 | <code>        self._semester = None if value is None else validate_text(value)</code> | Lưu None if value is None else validate_text(value) vào self._semester. Thuộc tính _... dùng theo quy ước nội bộ. |
| 39 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 40 | <code>    def credits(self):</code> | Getter của property credits: đọc bằng object.credits, không thêm dấu (). |
| 41 | <code>        return self._credits</code> | Kết thúc hàm, trả self._credits cho nơi gọi. |
| 43 | <code>    @credits.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 44 | <code>    def credits(self, value):</code> | Setter: được gọi khi gán object.credits = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 45 | <code>        self._credits = None if value is None else validate_credits(value)</code> | Lưu None if value is None else validate_credits(value) vào self._credits. Thuộc tính _... dùng theo quy ước nội bộ. |
| 47 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 48 | <code>    def student_id(self):</code> | Getter của property student_id: đọc bằng object.student_id, không thêm dấu (). |
| 49 | <code>        return self._student_id</code> | Kết thúc hàm, trả self._student_id cho nơi gọi. |
| 51 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 52 | <code>    def course_id(self):</code> | Getter của property course_id: đọc bằng object.course_id, không thêm dấu (). |
| 53 | <code>        return self._course_id</code> | Kết thúc hàm, trả self._course_id cho nơi gọi. |
| 55 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 56 | <code>    def grade_fe(self):</code> | Getter của property grade_fe: đọc bằng object.grade_fe, không thêm dấu (). |
| 57 | <code>        return self._grade_fe</code> | Kết thúc hàm, trả self._grade_fe cho nơi gọi. |
| 59 | <code>    @grade_fe.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 60 | <code>    def grade_fe(self, value):</code> | Setter: được gọi khi gán object.grade_fe = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 61 | <code>        self._grade_fe = self._format_grade(value)</code> | Lưu self._format_grade(value) vào self._grade_fe. Thuộc tính _... dùng theo quy ước nội bộ. |
| 63 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 64 | <code>    def grade_re(self):</code> | Getter của property grade_re: đọc bằng object.grade_re, không thêm dấu (). |
| 65 | <code>        return self._grade_re</code> | Kết thúc hàm, trả self._grade_re cho nơi gọi. |
| 67 | <code>    @grade_re.setter</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 68 | <code>    def grade_re(self, value):</code> | Setter: được gọi khi gán object.grade_re = value; kiểm tra trước khi đổi thuộc tính nội bộ. |
| 69 | <code>        self._grade_re = self._format_grade(value)</code> | Lưu self._format_grade(value) vào self._grade_re. Thuộc tính _... dùng theo quy ước nội bộ. |
| 71 | <code>    @staticmethod</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 72 | <code>    def evaluate_status(grade_fe, grade_re=None):</code> | Định nghĩa evaluate_status; FE None -&gt; None. FE&gt;=5 -&gt; Pass. FE&lt;5 và RE&gt;=5 -&gt; Pass. Còn lại Fail; chưa có RE vẫn Fail nếu FE đã dưới 5. |
| 73 | <code>        fe = Result._format_grade(grade_fe)</code> | Tính Result._format_grade(grade_fe) rồi gán vào fe. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 74 | <code>        re = Result._format_grade(grade_re)</code> | Tính Result._format_grade(grade_re) rồi gán vào re. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 75 | <code>        if fe is None:</code> | Kiểm tra fe is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 76 | <code>            return None</code> | Kết thúc hàm, trả None cho nơi gọi. |
| 77 | <code>        if fe &gt;= 5.0 or (re is not None and re &gt;= 5.0):</code> | Kiểm tra fe &gt;= 5.0 or (re is not None and re &gt;= 5.0). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 78 | <code>            return &quot;Pass&quot;</code> | Kết thúc hàm, trả &#x27;Pass&#x27; cho nơi gọi. |
| 79 | <code>        return &quot;Fail&quot;</code> | Kết thúc hàm, trả &#x27;Fail&#x27; cho nơi gọi. |
| 81 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 82 | <code>    def result_status(self):</code> | Getter của property result_status: đọc bằng object.result_status, không thêm dấu (). |
| 83 | <code>        return self.evaluate_status(self._grade_fe, self._grade_re)</code> | Kết thúc hàm, trả self.evaluate_status(self._grade_fe, self._grade_re) cho nơi gọi. |
| 85 | <code>    def to_file_line(self):</code> | Định nghĩa to_file_line; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 86 | <code>        fe = &quot;&quot; if self._grade_fe is None else str(self._grade_fe)</code> | Gán fe = &#x27;&#x27; nếu self._grade_fe is None; ngược lại dùng str(self._grade_fe). |
| 87 | <code>        re = &quot;&quot; if self._grade_re is None else str(self._grade_re)</code> | Gán re = &#x27;&#x27; nếu self._grade_re is None; ngược lại dùng str(self._grade_re). |
| 88 | <code>        status = self.result_status or &quot;&quot;</code> | Tính self.result_status or &#x27;&#x27; rồi gán vào status. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 89 | <code>        name = self._course_name or &quot;&quot;</code> | Tính self._course_name or &#x27;&#x27; rồi gán vào name. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 90 | <code>        semester = self._semester or &quot;&quot;</code> | Tính self._semester or &#x27;&#x27; rồi gán vào semester. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 91 | <code>        credits = &quot;&quot; if self._credits is None else str(self._credits)</code> | Gán credits = &#x27;&#x27; nếu self._credits is None; ngược lại dùng str(self._credits). |
| 92 | <code>        return f&quot;{self._student_id}&#124;{self._course_id}&#124;{name}&#124;{semester}&#124;{credits}&#124;{fe}&#124;{re}&#124;{status}\n&quot;</code> | Kết thúc hàm, trả f&#x27;{self._student_id}&#124;{self._course_id}&#124;{name}&#124;{semester}&#124;{credits}&#124;{fe}&#124;{re}&#124;{status}\n&#x27; cho nơi gọi. |
| 94 | <code>    def to_dict(self):</code> | Định nghĩa to_dict; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 95 | <code>        return {</code> | Trả dictionary mới ánh xạ tên trường tới giá trị; không thay object đang có. |
| 96 | <code>            &quot;student_id&quot;: self._student_id,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 97 | <code>            &quot;course_id&quot;: self._course_id,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 98 | <code>            &quot;course_name&quot;: self._course_name,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 99 | <code>            &quot;semester&quot;: self._semester,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 100 | <code>            &quot;credits&quot;: self._credits,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 101 | <code>            &quot;grade_fe&quot;: self._grade_fe,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 102 | <code>            &quot;grade_re&quot;: self._grade_re,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 103 | <code>            &quot;result_status&quot;: self.result_status,</code> | Một trường trong dictionary trả về: giá trị bên phải được đọc từ object hiện tại. |
| 104 | <code>        }</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 106 | <code>    def __str__(self):</code> | Cách biểu diễn dễ đọc khi gọi str(object) hoặc print(object). |
| 107 | <code>        fe_info = &quot;Chưa có điểm&quot; if self._grade_fe is None else str(self._grade_fe)</code> | Gán fe_info = &#x27;Chưa có điểm&#x27; nếu self._grade_fe is None; ngược lại dùng str(self._grade_fe). |
| 108 | <code>        re_info = f&quot;, RE: {self._grade_re}&quot; if self._grade_re is not None else &quot;&quot;</code> | Gán re_info = f&#x27;, RE: {self._grade_re}&#x27; nếu self._grade_re is not None; ngược lại dùng &#x27;&#x27;. |
| 109 | <code>        status = self.result_status or &quot;Chưa có điểm&quot;</code> | Tính self.result_status or &#x27;Chưa có điểm&#x27; rồi gán vào status. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 110 | <code>        name = self._course_name or &quot;[Missing course name]&quot;</code> | Tính self._course_name or &#x27;[Missing course name]&#x27; rồi gán vào name. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 111 | <code>        semester = self._semester or &quot;[Missing semester]&quot;</code> | Tính self._semester or &#x27;[Missing semester]&#x27; rồi gán vào semester. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 112 | <code>        credits = self._credits if self._credits is not None else &quot;?&quot;</code> | Gán credits = self._credits nếu self._credits is not None; ngược lại dùng &#x27;?&#x27;. |
| 113 | <code>        return f&quot;[{self._student_id}] {self._course_id} - {name} ({semester}, {credits} credits) - FE: {fe_info}{re_info} =&gt; {status}&quot;</code> | Kết thúc hàm, trả f&#x27;[{self._student_id}] {self._course_id} - {name} ({semester}, {credits} credits) - FE: {fe_info}{re_info} =&gt; {status}&#x27; cho nơi gọi. |

## services/student_manager.py

Quản lý danh sách Student; bảo vệ khóa trùng và cung cấp tìm/sửa/lọc.

[Đọc source](../../services/student_manager.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from models import Student</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from utils.validator import validate_student_id</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>class StudentManager:</code> | Định nghĩa class StudentManager. Thân class khai báo các method/property. |
| 6 | <code>    def __init__(self, students=None):</code> | Constructor: chạy khi tạo object; self là chính object mới, tham số mặc định chỉ dùng khi không truyền giá trị. |
| 7 | <code>        self._students = []</code> | Lưu [] vào self._students. Thuộc tính _... dùng theo quy ước nội bộ. |
| 8 | <code>        for student in students or []:</code> | Lần lượt gán từng phần tử của students or [] cho student rồi chạy thân vòng lặp. |
| 9 | <code>            self.add(student)</code> | Gọi self.add(student). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 11 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 12 | <code>    def students(self):</code> | Getter của property students: đọc bằng object.students, không thêm dấu (). |
| 13 | <code>        return self._students.copy()</code> | Kết thúc hàm, trả self._students.copy() cho nơi gọi. |
| 15 | <code>    def find(self, student_id):</code> | Định nghĩa find; Chuẩn hóa mã rồi duyệt tuyến tính; gặp khớp trả object đang được manager giữ, không tìm thấy trả None. |
| 16 | <code>        student_id = validate_student_id(student_id)</code> | Tính validate_student_id(student_id) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 17 | <code>        for student in self._students:</code> | Lần lượt gán từng phần tử của self._students cho student rồi chạy thân vòng lặp. |
| 18 | <code>            if student.student_id == student_id:</code> | Kiểm tra student.student_id == student_id. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 19 | <code>                return student</code> | Kết thúc hàm, trả student cho nơi gọi. |
| 20 | <code>        return None</code> | Kết thúc hàm, trả None cho nơi gọi. |
| 22 | <code>    def add(self, student):</code> | Định nghĩa add; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 23 | <code>        if not isinstance(student, Student):</code> | Kiểm tra not isinstance(student, Student). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 24 | <code>            raise ValueError(&quot;Expected a Student object.&quot;)</code> | Phát sinh ValueError(&#x27;Expected a Student object.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 25 | <code>        if self.find(student.student_id) is not None:</code> | Kiểm tra self.find(student.student_id) is not None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 26 | <code>            raise ValueError(&quot;Student ID already exists.&quot;)</code> | Phát sinh ValueError(&#x27;Student ID already exists.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 27 | <code>        self._students.append(student)</code> | Thêm object vào cuối list đang giữ; không tạo bản sao object: self._students.append(student). |
| 29 | <code>    def update(self, student_id, field, value):</code> | Định nghĩa update; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 30 | <code>        student = self.find(student_id)</code> | Tính self.find(student_id) rồi gán vào student. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 31 | <code>        if student is None:</code> | Kiểm tra student is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 32 | <code>            raise ValueError(&quot;Student not found.&quot;)</code> | Phát sinh ValueError(&#x27;Student not found.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 33 | <code>        if field == &quot;full_name&quot;:</code> | Kiểm tra field == &#x27;full_name&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 34 | <code>            student.full_name = value</code> | Gán value vào student.full_name; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 35 | <code>        elif field == &quot;date_of_birth&quot;:</code> | Kiểm tra field == &#x27;date_of_birth&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 36 | <code>            student.date_of_birth = value</code> | Gán value vào student.date_of_birth; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 37 | <code>        elif field == &quot;gender&quot;:</code> | Kiểm tra field == &#x27;gender&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 38 | <code>            student.gender = value</code> | Gán value vào student.gender; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 39 | <code>        elif field == &quot;class_name&quot;:</code> | Kiểm tra field == &#x27;class_name&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 40 | <code>            student.class_name = value</code> | Gán value vào student.class_name; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 41 | <code>        elif field == &quot;phone&quot;:</code> | Kiểm tra field == &#x27;phone&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 42 | <code>            student.phone = value</code> | Gán value vào student.phone; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 43 | <code>        elif field == &quot;email&quot;:</code> | Kiểm tra field == &#x27;email&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 44 | <code>            student.email = value</code> | Gán value vào student.email; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 45 | <code>        elif field == &quot;status&quot;:</code> | Kiểm tra field == &#x27;status&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 46 | <code>            student.status = value</code> | Gán value vào student.status; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 47 | <code>        else:</code> | Nhánh thay thế: chỉ chạy khi các điều kiện if/elif trước đó trong cùng chuỗi đều sai. |
| 48 | <code>            raise ValueError(&quot;Invalid student field.&quot;)</code> | Phát sinh ValueError(&#x27;Invalid student field.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 50 | <code>    def filter(self, condition):</code> | Định nghĩa filter; So sánh chính xác lớp hoặc status sau khi chuyển chữ thường; không tìm một phần tên. |
| 51 | <code>        condition = condition.strip().lower()</code> | Tính condition.strip().lower() rồi gán vào condition. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 52 | <code>        matches = []</code> | Tính [] rồi gán vào matches. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 53 | <code>        for student in self._students:</code> | Lần lượt gán từng phần tử của self._students cho student rồi chạy thân vòng lặp. |
| 54 | <code>            if student.class_name.lower() == condition or student.status.lower() == condition:</code> | Kiểm tra student.class_name.lower() == condition or student.status.lower() == condition. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 55 | <code>                matches.append(student)</code> | Thêm object vào cuối list đang giữ; không tạo bản sao object: matches.append(student). |
| 56 | <code>        return matches</code> | Kết thúc hàm, trả matches cho nơi gọi. |
| 58 | <code>    def active_students(self):</code> | Định nghĩa active_students; Tái sử dụng filter thay vì viết lại vòng lặp. |
| 59 | <code>        return self.filter(&quot;Active&quot;)</code> | Kết thúc hàm, trả self.filter(&#x27;Active&#x27;) cho nơi gọi. |

## services/result_manager.py

Quản lý Result, kiểm tra sinh viên liên quan, phân biệt tải lịch sử với thêm mới.

[Đọc source](../../services/result_manager.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from models import Result</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from utils.validator import validate_student_id, validate_course_id, validate_score, validate_text, validate_credits</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>class ResultManager:</code> | Định nghĩa class ResultManager. Thân class khai báo các method/property. |
| 6 | <code>    def __init__(self, student_manager, results=None):</code> | Constructor: chạy khi tạo object; self là chính object mới, tham số mặc định chỉ dùng khi không truyền giá trị. |
| 7 | <code>        self._student_manager = student_manager</code> | Lưu student_manager vào self._student_manager. Thuộc tính _... dùng theo quy ước nội bộ. |
| 8 | <code>        self._results = []</code> | Lưu [] vào self._results. Thuộc tính _... dùng theo quy ước nội bộ. |
| 9 | <code>        for result in results or []:</code> | Lần lượt gán từng phần tử của results or [] cho result rồi chạy thân vòng lặp. |
| 10 | <code>            self.add(result, loading=True)</code> | Gọi self.add(result, loading=True). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 12 | <code>    @property</code> | @property khai báo getter đọc như thuộc tính; @...setter khai báo cập nhật; @staticmethod cho phép gọi qua class mà không cần self. |
| 13 | <code>    def results(self):</code> | Getter của property results: đọc bằng object.results, không thêm dấu (). |
| 14 | <code>        return self._results.copy()</code> | Kết thúc hàm, trả self._results.copy() cho nơi gọi. |
| 16 | <code>    def find(self, student_id, course_id):</code> | Định nghĩa find; Chuẩn hóa mã rồi duyệt tuyến tính; gặp khớp trả object đang được manager giữ, không tìm thấy trả None. |
| 17 | <code>        student_id = validate_student_id(student_id)</code> | Tính validate_student_id(student_id) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 18 | <code>        course_id = validate_course_id(course_id)</code> | Tính validate_course_id(course_id) rồi gán vào course_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 19 | <code>        for result in self._results:</code> | Lần lượt gán từng phần tử của self._results cho result rồi chạy thân vòng lặp. |
| 20 | <code>            if result.student_id == student_id and result.course_id == course_id:</code> | Kiểm tra result.student_id == student_id and result.course_id == course_id. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 21 | <code>                return result</code> | Kết thúc hàm, trả result cho nơi gọi. |
| 22 | <code>        return None</code> | Kết thúc hàm, trả None cho nơi gọi. |
| 24 | <code>    def check_student(self, student_id, require_active=True):</code> | Định nghĩa check_student; Bắt buộc sinh viên tồn tại; chỉ kiểm tra Active nếu require_active=True. |
| 25 | <code>        student = self._student_manager.find(student_id)</code> | Tính self._student_manager.find(student_id) rồi gán vào student. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 26 | <code>        if student is None:</code> | Kiểm tra student is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 27 | <code>            raise ValueError(&quot;Student not found.&quot;)</code> | Phát sinh ValueError(&#x27;Student not found.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 28 | <code>        if require_active and student.status != &quot;Active&quot;:</code> | Kiểm tra require_active and student.status != &#x27;Active&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 29 | <code>            raise ValueError(&quot;Only Active students can have grades added or updated.&quot;)</code> | Phát sinh ValueError(&#x27;Only Active students can have grades added or updated.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 31 | <code>    def add(self, result, loading=False):</code> | Định nghĩa add; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 32 | <code>        if not isinstance(result, Result):</code> | Kiểm tra not isinstance(result, Result). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 33 | <code>            raise ValueError(&quot;Expected a Result object.&quot;)</code> | Phát sinh ValueError(&#x27;Expected a Result object.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 34 | <code>        if not loading:</code> | Kiểm tra not loading. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 35 | <code>            validate_text(result.course_name)</code> | Gọi validator để kiểm tra; dù không dùng giá trị trả về, dữ liệu sai vẫn raise ValueError. |
| 36 | <code>            validate_text(result.semester)</code> | Gọi validator để kiểm tra; dù không dùng giá trị trả về, dữ liệu sai vẫn raise ValueError. |
| 37 | <code>            validate_credits(result.credits)</code> | Gọi validator để kiểm tra; dù không dùng giá trị trả về, dữ liệu sai vẫn raise ValueError. |
| 38 | <code>        self.check_student(result.student_id, require_active=not loading)</code> | Gọi self.check_student(result.student_id, require_active=not loading). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 39 | <code>        if self.find(result.student_id, result.course_id) is not None:</code> | Kiểm tra self.find(result.student_id, result.course_id) is not None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 40 | <code>            raise ValueError(&quot;Student/course result already exists.&quot;)</code> | Phát sinh ValueError(&#x27;Student/course result already exists.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 41 | <code>        self._results.append(result)</code> | Thêm object vào cuối list đang giữ; không tạo bản sao object: self._results.append(result). |
| 43 | <code>    def update_grades(self, student_id, course_id, grade_fe, grade_re=None):</code> | Định nghĩa update_grades; Kiểm tra toàn bộ điểm mới vào biến tạm trước khi gán, tránh FE bị đổi trước khi phát hiện RE sai. Xóa RE nếu FE trống hoặc đã đạt. |
| 44 | <code>        self.check_student(student_id)</code> | Gọi self.check_student(student_id). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 45 | <code>        result = self.find(student_id, course_id)</code> | Tính self.find(student_id, course_id) rồi gán vào result. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 46 | <code>        if result is None:</code> | Kiểm tra result is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 47 | <code>            raise ValueError(&quot;Result not found.&quot;)</code> | Phát sinh ValueError(&#x27;Result not found.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 48 | <code>        fe = validate_score(grade_fe)</code> | Tính validate_score(grade_fe) rồi gán vào fe. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 49 | <code>        re = validate_score(grade_re)</code> | Tính validate_score(grade_re) rồi gán vào re. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 50 | <code>        if fe is None or fe &gt;= 5:</code> | Kiểm tra fe is None or fe &gt;= 5. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 51 | <code>            re = None</code> | Tính None rồi gán vào re. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 52 | <code>        result.grade_fe = fe</code> | Gán fe vào result.grade_fe; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 53 | <code>        result.grade_re = re</code> | Gán re vào result.grade_re; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 55 | <code>    def update_course_details(self, student_id, course_id, course_name, semester, credits):</code> | Định nghĩa update_course_details; Cho phép bổ sung thông tin môn cho sinh viên không Active; kiểm tra ba giá trị trước khi cập nhật. |
| 56 | <code>        self.check_student(student_id, require_active=False)</code> | Gọi self.check_student(student_id, require_active=False). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 57 | <code>        result = self.find(student_id, course_id)</code> | Tính self.find(student_id, course_id) rồi gán vào result. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 58 | <code>        if result is None:</code> | Kiểm tra result is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 59 | <code>            raise ValueError(&quot;Result not found.&quot;)</code> | Phát sinh ValueError(&#x27;Result not found.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 60 | <code>        name = validate_text(course_name)</code> | Tính validate_text(course_name) rồi gán vào name. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 61 | <code>        term = validate_text(semester)</code> | Tính validate_text(semester) rồi gán vào term. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 62 | <code>        count = validate_credits(credits)</code> | Tính validate_credits(credits) rồi gán vào count. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 63 | <code>        result.course_name = name</code> | Gán name vào result.course_name; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 64 | <code>        result.semester = term</code> | Gán term vào result.semester; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 65 | <code>        result.credits = count</code> | Gán count vào result.credits; nếu là property thì Python gọi setter tương ứng, có thể phát sinh ValueError. |
| 67 | <code>    def search(self, student_id):</code> | Định nghĩa search; List comprehension tạo list mới chứa các Result có MSSV khớp; các object bên trong vẫn là object gốc. |
| 68 | <code>        student_id = validate_student_id(student_id)</code> | Tính validate_student_id(student_id) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 69 | <code>        return [r for r in self._results if r.student_id == student_id]</code> | Duyệt và lọc để tạo list mới: [r for r in self._results if r.student_id == student_id]. List mới vẫn tham chiếu các object gốc. |
| 71 | <code>    def sorted_results(self):</code> | Định nghĩa sorted_results; Tạo list mới; khóa Pass/Fail/chuỗi rỗng, reverse=True đặt Pass trước Fail trước chưa có điểm. |
| 72 | <code>        return sorted(self._results, key=lambda r: r.result_status or &quot;&quot;, reverse=True)</code> | Kết thúc hàm, trả sorted(self._results, key=lambda r: r.result_status or &#x27;&#x27;, reverse=True) cho nơi gọi. |
| 74 | <code>    def passed_results(self):</code> | Định nghĩa passed_results; Lọc theo property tính động, không dựa vào status cũ trong file. |
| 75 | <code>        return [r for r in self._results if r.result_status == &quot;Pass&quot;]</code> | Duyệt và lọc để tạo list mới: [r for r in self._results if r.result_status == &#x27;Pass&#x27;]. List mới vẫn tham chiếu các object gốc. |

## student_management.py

Giao diện sinh viên: nhận input, gọi manager và in kết quả; không tự quản lý list.

[Đọc source](../../student_management.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from models import Student</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from utils.validator import (</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 3 | <code>    input_student_id, input_name, input_date_of_birth, input_gender,</code> | Tiếp lệnh bắt đầu ở dòng 2: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>    input_class_name, input_phone, input_email, input_status,</code> | Tiếp lệnh bắt đầu ở dòng 2: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>)</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 8 | <code>def display_students(students):</code> | Định nghĩa display_students; Nếu list rỗng in thông báo; nếu có thì in __str__ và chi tiết cá nhân từng Student. |
| 9 | <code>    if not students:</code> | Kiểm tra not students. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 10 | <code>        print(&quot;No matching students.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 11 | <code>    for student in students:</code> | Lần lượt gán từng phần tử của students cho student rồi chạy thân vòng lặp. |
| 12 | <code>        print(student)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 13 | <code>        print(f&quot;DOB: {student.date_of_birth} &#124; Gender: {student.gender}&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 14 | <code>        print(f&quot;Phone: {student.phone} &#124; Email: {student.email}&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 17 | <code>def add_student(manager):</code> | Định nghĩa add_student; Hủy bằng None; kiểm tra mã trùng trước khi nhập hồ sơ; tạo Student qua constructor rồi giao manager thêm. |
| 18 | <code>    student_id = input_student_id(&quot;Student ID (0 to cancel): &quot;, True)</code> | Tính input_student_id(&#x27;Student ID (0 to cancel): &#x27;, True) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 19 | <code>    if student_id is None:</code> | Kiểm tra student_id is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 20 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 21 | <code>    if manager.find(student_id) is not None:</code> | Kiểm tra manager.find(student_id) is not None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 22 | <code>        raise ValueError(&quot;Student ID already exists.&quot;)</code> | Phát sinh ValueError(&#x27;Student ID already exists.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 23 | <code>    student = Student(</code> | Tính Student(student_id, input_name(), input_date_of_birth(&#x27;DOB (DD/MM/YYYY): &#x27;), input_gender(), input_class_name(), input_phone(), input_email(), input_status()) rồi gán vào student. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 24 | <code>        student_id, input_name(), input_date_of_birth(&quot;DOB (DD/MM/YYYY): &quot;),</code> | Tiếp lệnh bắt đầu ở dòng 23: Tính Student(student_id, input_name(), input_date_of_birth(&#x27;DOB (DD/MM/YYYY): &#x27;), input_gender(), input_class_name(), input_phone(), input_email(), input_status()) rồi gán vào student. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 25 | <code>        input_gender(), input_class_name(), input_phone(), input_email(), input_status(),</code> | Tiếp lệnh bắt đầu ở dòng 23: Tính Student(student_id, input_name(), input_date_of_birth(&#x27;DOB (DD/MM/YYYY): &#x27;), input_gender(), input_class_name(), input_phone(), input_email(), input_status()) rồi gán vào student. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 26 | <code>    )</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 27 | <code>    manager.add(student)</code> | Gọi manager.add(student). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 28 | <code>    print(&quot;Student added.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 31 | <code>def update_student(manager):</code> | Định nghĩa update_student; Dictionary ánh xạ lựa chọn sang tên thuộc tính và hàm nhập; vòng lặp cho sửa nhiều trường, 0 quay lại. |
| 32 | <code>    student_id = input_student_id(&quot;Student ID (0 to cancel): &quot;, True)</code> | Tính input_student_id(&#x27;Student ID (0 to cancel): &#x27;, True) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 33 | <code>    if student_id is None:</code> | Kiểm tra student_id is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 34 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 35 | <code>    if manager.find(student_id) is None:</code> | Kiểm tra manager.find(student_id) is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 36 | <code>        raise ValueError(&quot;Student not found.&quot;)</code> | Phát sinh ValueError(&#x27;Student not found.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 37 | <code>    fields = {</code> | Tạo dictionary fields; các cặp khóa/giá trị có thể là ánh xạ trường dữ liệu hoặc lựa chọn menu sang hàm nhập. |
| 38 | <code>        &quot;1&quot;: (&quot;full_name&quot;, input_name),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 39 | <code>        &quot;2&quot;: (&quot;date_of_birth&quot;, input_date_of_birth),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 40 | <code>        &quot;3&quot;: (&quot;gender&quot;, input_gender),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 41 | <code>        &quot;4&quot;: (&quot;class_name&quot;, input_class_name),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 42 | <code>        &quot;5&quot;: (&quot;phone&quot;, input_phone),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 43 | <code>        &quot;6&quot;: (&quot;email&quot;, input_email),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 44 | <code>        &quot;7&quot;: (&quot;status&quot;, input_status),</code> | Một phần tử của dictionary: bên trái là khóa; bên phải là giá trị hoặc hàm được lưu, chưa gọi hàm nếu không có (). |
| 45 | <code>    }</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 46 | <code>    while True:</code> | Lặp trong khi True. while True chỉ dừng khi return/ngoại lệ, hoặc chuyển vòng bằng continue. |
| 47 | <code>        print(&quot;1. Name  2. DOB  3. Gender  4. Class  5. Phone  6. Email  7. Status  0. Back&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 48 | <code>        choice = input(&quot;Choice: &quot;).strip()</code> | Tính input(&#x27;Choice: &#x27;).strip() rồi gán vào choice. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 49 | <code>        if choice == &quot;0&quot;:</code> | Kiểm tra choice == &#x27;0&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 50 | <code>            return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 51 | <code>        if choice not in fields:</code> | Kiểm tra choice not in fields. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 52 | <code>            print(&quot;Invalid choice.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 53 | <code>            continue</code> | Bỏ phần còn lại của vòng hiện tại và quay lại kiểm tra/lấy phần tử kế tiếp. |
| 54 | <code>        field, reader = fields[choice]</code> | Tách các phần tử trả về từ fields[choice] lần lượt vào (field, reader) (unpacking). |
| 55 | <code>        manager.update(student_id, field, reader(&quot;New value: &quot;))</code> | Gọi manager.update(student_id, field, reader(&#x27;New value: &#x27;)). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 56 | <code>        print(&quot;Student updated.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 59 | <code>def student_sub_menu(manager):</code> | Định nghĩa student_sub_menu; Vòng lặp menu; ValueError từ model/manager được in rồi quay lại menu. Ctrl+C/EOF truyền lên main. |
| 60 | <code>    while True:</code> | Lặp trong khi True. while True chỉ dừng khi return/ngoại lệ, hoặc chuyển vòng bằng continue. |
| 61 | <code>        print(&quot;\nSTUDENT MANAGEMENT&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 62 | <code>        print(&quot;1. Add student\n2. Update student\n3. Filter students\n4. Active students\n5. All students\n0. Back&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 63 | <code>        choice = input(&quot;Choice: &quot;).strip()</code> | Tính input(&#x27;Choice: &#x27;).strip() rồi gán vào choice. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 64 | <code>        try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 65 | <code>            if choice == &quot;0&quot;:</code> | Kiểm tra choice == &#x27;0&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 66 | <code>                return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 67 | <code>            if choice == &quot;1&quot;:</code> | Kiểm tra choice == &#x27;1&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 68 | <code>                add_student(manager)</code> | Gọi add_student(manager). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 69 | <code>            elif choice == &quot;2&quot;:</code> | Kiểm tra choice == &#x27;2&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 70 | <code>                update_student(manager)</code> | Gọi update_student(manager). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 71 | <code>            elif choice == &quot;3&quot;:</code> | Kiểm tra choice == &#x27;3&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 72 | <code>                condition = input(&quot;Class/status (0 to cancel): &quot;).strip()</code> | Tính input(&#x27;Class/status (0 to cancel): &#x27;).strip() rồi gán vào condition. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 73 | <code>                if condition != &quot;0&quot;:</code> | Kiểm tra condition != &#x27;0&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 74 | <code>                    display_students(manager.filter(condition))</code> | Gọi display_students(manager.filter(condition)). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 75 | <code>            elif choice == &quot;4&quot;:</code> | Kiểm tra choice == &#x27;4&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 76 | <code>                display_students(manager.active_students())</code> | Gọi display_students(manager.active_students()). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 77 | <code>            elif choice == &quot;5&quot;:</code> | Kiểm tra choice == &#x27;5&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 78 | <code>                display_students(manager.students)</code> | Gọi display_students(manager.students). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 79 | <code>            else:</code> | Nhánh thay thế: chỉ chạy khi các điều kiện if/elif trước đó trong cùng chuỗi đều sai. |
| 80 | <code>                print(&quot;Invalid choice.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 81 | <code>        except ValueError as error:</code> | Bắt ValueError và đặt tên lỗi là error; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 82 | <code>            print(&quot;[Error]&quot;, error)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |

## result_management.py

Giao diện kết quả: nhập thông tin môn/điểm, gọi manager; status không nhập tay.

[Đọc source](../../result_management.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from models import Result</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from utils.validator import (</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 3 | <code>    input_student_id, input_course_id, input_score, input_value,</code> | Tiếp lệnh bắt đầu ở dòng 2: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>    validate_text, validate_credits,</code> | Tiếp lệnh bắt đầu ở dòng 2: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>)</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 8 | <code>def display_results(results):</code> | Định nghĩa display_results; In __str__ từng Result, bao gồm tình trạng thiếu thông tin hoặc chưa có điểm. |
| 9 | <code>    if not results:</code> | Kiểm tra not results. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 10 | <code>        print(&quot;No matching results.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 11 | <code>    for result in results:</code> | Lần lượt gán từng phần tử của results cho result rồi chạy thân vòng lặp. |
| 12 | <code>        print(result)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 15 | <code>def read_grades():</code> | Định nghĩa read_grades; FE cho phép trống. Chỉ hỏi RE khi FE đã có và dưới 5; trả tuple (fe,re). |
| 16 | <code>    fe = input_score(&quot;FE (0-10, blank if not graded): &quot;, True)</code> | Tính input_score(&#x27;FE (0-10, blank if not graded): &#x27;, True) rồi gán vào fe. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 17 | <code>    re = None</code> | Tính None rồi gán vào re. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 18 | <code>    if fe is not None and fe &lt; 5:</code> | Kiểm tra fe is not None and fe &lt; 5. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 19 | <code>        re = input_score(&quot;RE (0-10, blank if not graded): &quot;, True)</code> | Tính input_score(&#x27;RE (0-10, blank if not graded): &#x27;, True) rồi gán vào re. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 20 | <code>    return fe, re</code> | Kết thúc hàm, trả (fe, re) cho nơi gọi. |
| 23 | <code>def read_course_details():</code> | Định nghĩa read_course_details; Nhập đủ tên môn, học kỳ, tín chỉ. Hiện học kỳ chỉ kiểm tra văn bản, chưa bắt mẫu Spring/Summer/Fall. |
| 24 | <code>    name = input_value(&quot;Course name: &quot;, validate_text)</code> | Tính input_value(&#x27;Course name: &#x27;, validate_text) rồi gán vào name. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 25 | <code>    semester = input_value(&quot;Semester (e.g. Fall2026): &quot;, validate_text)</code> | Tính input_value(&#x27;Semester (e.g. Fall2026): &#x27;, validate_text) rồi gán vào semester. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 26 | <code>    credits = input_value(&quot;Credits: &quot;, validate_credits)</code> | Tính input_value(&#x27;Credits: &#x27;, validate_credits) rồi gán vào credits. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 27 | <code>    return name, semester, credits</code> | Kết thúc hàm, trả (name, semester, credits) cho nơi gọi. |
| 30 | <code>def add_result(manager):</code> | Định nghĩa add_result; Kiểm tra Active và khóa trùng trước khi nhập môn/điểm, tạo Result rồi thêm qua manager. |
| 31 | <code>    student_id = input_student_id(&quot;Student ID (0 to cancel): &quot;, True)</code> | Tính input_student_id(&#x27;Student ID (0 to cancel): &#x27;, True) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 32 | <code>    if student_id is None:</code> | Kiểm tra student_id is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 33 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 34 | <code>    manager.check_student(student_id)</code> | Gọi manager.check_student(student_id). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 35 | <code>    course_id = input_course_id(&quot;Course ID (0 to cancel): &quot;, True)</code> | Tính input_course_id(&#x27;Course ID (0 to cancel): &#x27;, True) rồi gán vào course_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 36 | <code>    if course_id is None:</code> | Kiểm tra course_id is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 37 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 38 | <code>    if manager.find(student_id, course_id) is not None:</code> | Kiểm tra manager.find(student_id, course_id) is not None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 39 | <code>        raise ValueError(&quot;Student/course result already exists.&quot;)</code> | Phát sinh ValueError(&#x27;Student/course result already exists.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 40 | <code>    name, semester, credits = read_course_details()</code> | Tách các phần tử trả về từ read_course_details() lần lượt vào (name, semester, credits) (unpacking). |
| 41 | <code>    fe, re = read_grades()</code> | Tách các phần tử trả về từ read_grades() lần lượt vào (fe, re) (unpacking). |
| 42 | <code>    manager.add(Result(student_id, course_id, name, semester, credits, fe, re))</code> | Gọi manager.add(Result(student_id, course_id, name, semester, credits, fe, re)). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 43 | <code>    print(&quot;Result added.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 46 | <code>def update_result(manager):</code> | Định nghĩa update_result; Cho xem kết quả của sinh viên bất kỳ; sửa điểm kiểm tra Active ở manager, sửa thông tin môn không yêu cầu Active. |
| 47 | <code>    student_id = input_student_id(&quot;Student ID (0 to cancel): &quot;, True)</code> | Tính input_student_id(&#x27;Student ID (0 to cancel): &#x27;, True) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 48 | <code>    if student_id is None:</code> | Kiểm tra student_id is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 49 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 50 | <code>    manager.check_student(student_id, require_active=False)</code> | Gọi manager.check_student(student_id, require_active=False). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 51 | <code>    course_id = input_course_id(&quot;Course ID (0 to cancel): &quot;, True)</code> | Tính input_course_id(&#x27;Course ID (0 to cancel): &#x27;, True) rồi gán vào course_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 52 | <code>    if course_id is None:</code> | Kiểm tra course_id is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 53 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 54 | <code>    result = manager.find(student_id, course_id)</code> | Tính manager.find(student_id, course_id) rồi gán vào result. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 55 | <code>    if result is None:</code> | Kiểm tra result is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 56 | <code>        raise ValueError(&quot;Result not found.&quot;)</code> | Phát sinh ValueError(&#x27;Result not found.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 57 | <code>    print(result)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 58 | <code>    print(&quot;1. Replace FE/RE (blank clears score)\n2. Update course details\n0. Cancel&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 59 | <code>    choice = input(&quot;Choice: &quot;).strip()</code> | Tính input(&#x27;Choice: &#x27;).strip() rồi gán vào choice. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 60 | <code>    if choice == &quot;1&quot;:</code> | Kiểm tra choice == &#x27;1&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 61 | <code>        fe, re = read_grades()</code> | Tách các phần tử trả về từ read_grades() lần lượt vào (fe, re) (unpacking). |
| 62 | <code>        manager.update_grades(student_id, course_id, fe, re)</code> | Gọi manager.update_grades(student_id, course_id, fe, re). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 63 | <code>    elif choice == &quot;2&quot;:</code> | Kiểm tra choice == &#x27;2&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 64 | <code>        name, semester, credits = read_course_details()</code> | Tách các phần tử trả về từ read_course_details() lần lượt vào (name, semester, credits) (unpacking). |
| 65 | <code>        manager.update_course_details(student_id, course_id, name, semester, credits)</code> | Gọi manager.update_course_details(student_id, course_id, name, semester, credits). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 66 | <code>    elif choice == &quot;0&quot;:</code> | Kiểm tra choice == &#x27;0&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 67 | <code>        return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 68 | <code>    else:</code> | Nhánh thay thế: chỉ chạy khi các điều kiện if/elif trước đó trong cùng chuỗi đều sai. |
| 69 | <code>        raise ValueError(&quot;Invalid choice.&quot;)</code> | Phát sinh ValueError(&#x27;Invalid choice.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 70 | <code>    print(&quot;Result updated.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 73 | <code>def result_sub_menu(manager):</code> | Định nghĩa result_sub_menu; Vòng lặp menu kết quả; các chức năng trả về lại đây, 0 trở về main. |
| 74 | <code>    while True:</code> | Lặp trong khi True. while True chỉ dừng khi return/ngoại lệ, hoặc chuyển vòng bằng continue. |
| 75 | <code>        print(&quot;\nRESULT MANAGEMENT&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 76 | <code>        print(&quot;1. Add result\n2. Update result\n3. Search by student ID\n4. All results (status descending)\n5. Passed results\n0. Back&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 77 | <code>        choice = input(&quot;Choice: &quot;).strip()</code> | Tính input(&#x27;Choice: &#x27;).strip() rồi gán vào choice. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 78 | <code>        try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 79 | <code>            if choice == &quot;0&quot;:</code> | Kiểm tra choice == &#x27;0&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 80 | <code>                return</code> | Kết thúc hàm ngay và trả None; không tiếp tục các dòng phía sau trong hàm. |
| 81 | <code>            if choice == &quot;1&quot;:</code> | Kiểm tra choice == &#x27;1&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 82 | <code>                add_result(manager)</code> | Gọi add_result(manager). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 83 | <code>            elif choice == &quot;2&quot;:</code> | Kiểm tra choice == &#x27;2&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 84 | <code>                update_result(manager)</code> | Gọi update_result(manager). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 85 | <code>            elif choice == &quot;3&quot;:</code> | Kiểm tra choice == &#x27;3&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 86 | <code>                student_id = input_student_id(&quot;Student ID (0 to cancel): &quot;, True)</code> | Tính input_student_id(&#x27;Student ID (0 to cancel): &#x27;, True) rồi gán vào student_id. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 87 | <code>                if student_id is not None:</code> | Kiểm tra student_id is not None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 88 | <code>                    display_results(manager.search(student_id))</code> | Gọi display_results(manager.search(student_id)). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 89 | <code>            elif choice == &quot;4&quot;:</code> | Kiểm tra choice == &#x27;4&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 90 | <code>                display_results(manager.sorted_results())</code> | Gọi display_results(manager.sorted_results()). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 91 | <code>            elif choice == &quot;5&quot;:</code> | Kiểm tra choice == &#x27;5&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 92 | <code>                display_results(manager.passed_results())</code> | Gọi display_results(manager.passed_results()). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 93 | <code>            else:</code> | Nhánh thay thế: chỉ chạy khi các điều kiện if/elif trước đó trong cùng chuỗi đều sai. |
| 94 | <code>                print(&quot;Invalid choice.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 95 | <code>        except ValueError as error:</code> | Bắt ValueError và đặt tên lỗi là error; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 96 | <code>            print(&quot;[Error]&quot;, error)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |

## utils/validator.py

Hàm validate kiểm tra giá trị; hàm input gọi validate và cho nhập lại khi sai.

[Đọc source](../../utils/validator.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>import re</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from datetime import datetime</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>VALID_PREFIXES = [&quot;SE&quot;, &quot;SS&quot;, &quot;SA&quot;, &quot;SB&quot;, &quot;DE&quot;, &quot;DA&quot;, &quot;DS&quot;, &quot;HE&quot;, &quot;HA&quot;, &quot;HS&quot;, &quot;QE&quot;, &quot;QA&quot;, &quot;QS&quot;, &quot;CE&quot;, &quot;CA&quot;, &quot;CS&quot;]</code> | Tính [&#x27;SE&#x27;, &#x27;SS&#x27;, &#x27;SA&#x27;, &#x27;SB&#x27;, &#x27;DE&#x27;, &#x27;DA&#x27;, &#x27;DS&#x27;, &#x27;HE&#x27;, &#x27;HA&#x27;, &#x27;HS&#x27;, &#x27;QE&#x27;, &#x27;QA&#x27;, &#x27;QS&#x27;, &#x27;CE&#x27;, &#x27;CA&#x27;, &#x27;CS&#x27;] rồi gán vào VALID_PREFIXES. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 7 | <code>def validate_text(value):</code> | Định nghĩa validate_text; Chặn None, chuỗi rỗng và ký tự &#124;, xuống dòng, tab để giữ cấu trúc file. |
| 8 | <code>    if value is None:</code> | Kiểm tra value is None. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 9 | <code>        raise ValueError(&quot;A value is required.&quot;)</code> | Phát sinh ValueError(&#x27;A value is required.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 10 | <code>    value = str(value).strip()</code> | Tính str(value).strip() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 11 | <code>    if not value or any(char in value for char in &quot;&#124;\n\r\t&quot;):</code> | Kiểm tra not value or any((char in value for char in &#x27;&#124;\n\r\t&#x27;)). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 12 | <code>        raise ValueError(&quot;Text is required and cannot contain &#124; or control characters.&quot;)</code> | Phát sinh ValueError(&#x27;Text is required and cannot contain &#124; or control characters.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 13 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 16 | <code>def validate_student_id(value):</code> | Định nghĩa validate_student_id; Chữ hoa, prefix thuộc 16 mã và sáu số ASCII. Không tra cứu sinh viên tồn tại ở đây. |
| 17 | <code>    value = validate_text(value).upper()</code> | Tính validate_text(value).upper() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 18 | <code>    if not re.fullmatch(r&quot;[A-Z]{2}[0-9]{6}&quot;, value) or value[:2] not in VALID_PREFIXES:</code> | Kiểm tra not re.fullmatch(&#x27;[A-Z]{2}[0-9]{6}&#x27;, value) or value[:2] not in VALID_PREFIXES. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 19 | <code>        raise ValueError(&quot;Student ID must use an allowed prefix and 6 digits.&quot;)</code> | Phát sinh ValueError(&#x27;Student ID must use an allowed prefix and 6 digits.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 20 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 23 | <code>def validate_name(value):</code> | Định nghĩa validate_name; Chuẩn hóa khoảng trắng/title; bỏ các dấu cho phép trong bản kiểm tra rồi đòi ít nhất hai chữ cái. |
| 24 | <code>    value = &quot; &quot;.join(validate_text(value).split()).title()</code> | Tính &#x27; &#x27;.join(validate_text(value).split()).title() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 25 | <code>    letters = value.replace(&quot; &quot;, &quot;&quot;).replace(&quot;-&quot;, &quot;&quot;).replace(&quot;&#x27;&quot;, &quot;&quot;).replace(&quot;’&quot;, &quot;&quot;)</code> | Tính value.replace(&#x27; &#x27;, &#x27;&#x27;).replace(&#x27;-&#x27;, &#x27;&#x27;).replace(&quot;&#x27;&quot;, &#x27;&#x27;).replace(&#x27;’&#x27;, &#x27;&#x27;) rồi gán vào letters. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 26 | <code>    if len(letters) &lt; 2 or not letters.isalpha():</code> | Kiểm tra len(letters) &lt; 2 or not letters.isalpha(). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 27 | <code>        raise ValueError(&quot;Name must contain at least two letters; spaces, hyphens and apostrophes are allowed.&quot;)</code> | Phát sinh ValueError(&#x27;Name must contain at least two letters; spaces, hyphens and apostrophes are allowed.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 28 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 31 | <code>def validate_date_of_birth(value):</code> | Định nghĩa validate_date_of_birth; strptime kiểm tra ngày thật; kiểm tra lại định dạng đủ 2 số, năm 1900–2008 và không tương lai. |
| 32 | <code>    value = validate_text(value)</code> | Tính validate_text(value) rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 33 | <code>    date = datetime.strptime(value, &quot;%d/%m/%Y&quot;)</code> | Tính datetime.strptime(value, &#x27;%d/%m/%Y&#x27;) rồi gán vào date. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 34 | <code>    if date.strftime(&quot;%d/%m/%Y&quot;) != value or not 1900 &lt;= date.year &lt;= 2008 or date.date() &gt; datetime.today().date():</code> | Kiểm tra date.strftime(&#x27;%d/%m/%Y&#x27;) != value or not 1900 &lt;= date.year &lt;= 2008 or date.date() &gt; datetime.today().date(). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 35 | <code>        raise ValueError(&quot;Use DD/MM/YYYY, with birth year between 1900 and 2008.&quot;)</code> | Phát sinh ValueError(&#x27;Use DD/MM/YYYY, with birth year between 1900 and 2008.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 36 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 39 | <code>def validate_gender(value):</code> | Định nghĩa validate_gender; Chỉ Male/Female sau chuẩn hóa title. |
| 40 | <code>    value = validate_text(value).title()</code> | Tính validate_text(value).title() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 41 | <code>    if value not in (&quot;Male&quot;, &quot;Female&quot;):</code> | Kiểm tra value not in (&#x27;Male&#x27;, &#x27;Female&#x27;). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 42 | <code>        raise ValueError(&quot;Gender must be Male or Female.&quot;)</code> | Phát sinh ValueError(&#x27;Gender must be Male or Female.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 43 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 46 | <code>def validate_class_name(value):</code> | Định nghĩa validate_class_name; Regex chấp nhận 2 chữ + 4 số hoặc 3 chữ + 3 số ASCII. |
| 47 | <code>    value = validate_text(value).upper()</code> | Tính validate_text(value).upper() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 48 | <code>    if not re.fullmatch(r&quot;([A-Z]{2}[0-9]{4}&#124;[A-Z]{3}[0-9]{3})&quot;, value):</code> | Kiểm tra not re.fullmatch(&#x27;([A-Z]{2}[0-9]{4}&#124;[A-Z]{3}[0-9]{3})&#x27;, value). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 49 | <code>        raise ValueError(&quot;Class must use 2 letters + 4 digits or 3 letters + 3 digits.&quot;)</code> | Phát sinh ValueError(&#x27;Class must use 2 letters + 4 digits or 3 letters + 3 digits.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 50 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 53 | <code>def validate_phone(value):</code> | Định nghĩa validate_phone; Đúng 10 số ASCII, đầu 0; không chuyển sang int để giữ số 0 đầu. |
| 54 | <code>    value = validate_text(value)</code> | Tính validate_text(value) rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 55 | <code>    if not re.fullmatch(r&quot;0[0-9]{9}&quot;, value):</code> | Kiểm tra not re.fullmatch(&#x27;0[0-9]{9}&#x27;, value). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 56 | <code>        raise ValueError(&quot;Phone must contain 10 digits starting with 0.&quot;)</code> | Phát sinh ValueError(&#x27;Phone must contain 10 digits starting with 0.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 57 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 60 | <code>def validate_email(value):</code> | Định nghĩa validate_email; Kiểm tra ASCII, local/domain, dấu chấm, từng nhãn miền; không kiểm tra hộp thư có thật. |
| 61 | <code>    value = validate_text(value)</code> | Tính validate_text(value) rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 62 | <code>    if not value.isascii() or &quot;..&quot; in value or value.count(&quot;@&quot;) != 1:</code> | Kiểm tra not value.isascii() or &#x27;..&#x27; in value or value.count(&#x27;@&#x27;) != 1. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 63 | <code>        raise ValueError(&quot;Invalid email.&quot;)</code> | Phát sinh ValueError(&#x27;Invalid email.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 64 | <code>    local, domain = value.split(&quot;@&quot;)</code> | Tách các phần tử trả về từ value.split(&#x27;@&#x27;) lần lượt vào (local, domain) (unpacking). |
| 65 | <code>    if not re.fullmatch(r&quot;[A-Za-z0-9_%+.-]+&quot;, local) or local.startswith(&quot;.&quot;) or local.endswith(&quot;.&quot;):</code> | Kiểm tra not re.fullmatch(&#x27;[A-Za-z0-9_%+.-]+&#x27;, local) or local.startswith(&#x27;.&#x27;) or local.endswith(&#x27;.&#x27;). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 66 | <code>        raise ValueError(&quot;Invalid email local part.&quot;)</code> | Phát sinh ValueError(&#x27;Invalid email local part.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 67 | <code>    parts = domain.split(&quot;.&quot;)</code> | Tính domain.split(&#x27;.&#x27;) rồi gán vào parts. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 68 | <code>    if len(parts) &lt; 2 or not parts[-1].isalpha() or len(parts[-1]) &lt; 2:</code> | Kiểm tra len(parts) &lt; 2 or not parts[-1].isalpha() or len(parts[-1]) &lt; 2. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 69 | <code>        raise ValueError(&quot;Invalid email domain.&quot;)</code> | Phát sinh ValueError(&#x27;Invalid email domain.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 70 | <code>    for part in parts:</code> | Lần lượt gán từng phần tử của parts cho part rồi chạy thân vòng lặp. |
| 71 | <code>        if not re.fullmatch(r&quot;[A-Za-z0-9-]+&quot;, part) or part.startswith(&quot;-&quot;) or part.endswith(&quot;-&quot;):</code> | Kiểm tra not re.fullmatch(&#x27;[A-Za-z0-9-]+&#x27;, part) or part.startswith(&#x27;-&#x27;) or part.endswith(&#x27;-&#x27;). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 72 | <code>            raise ValueError(&quot;Invalid email domain.&quot;)</code> | Phát sinh ValueError(&#x27;Invalid email domain.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 73 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 76 | <code>def validate_status(value):</code> | Định nghĩa validate_status; Chỉ Active/Inactive/Graduated. Đây là status sinh viên, khác status kết quả. |
| 77 | <code>    value = validate_text(value).title()</code> | Tính validate_text(value).title() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 78 | <code>    if value not in (&quot;Active&quot;, &quot;Inactive&quot;, &quot;Graduated&quot;):</code> | Kiểm tra value not in (&#x27;Active&#x27;, &#x27;Inactive&#x27;, &#x27;Graduated&#x27;). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 79 | <code>        raise ValueError(&quot;Status must be Active, Inactive or Graduated.&quot;)</code> | Phát sinh ValueError(&#x27;Status must be Active, Inactive or Graduated.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 80 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 83 | <code>def validate_course_id(value):</code> | Định nghĩa validate_course_id; Mã môn 2–10 chữ/số ASCII, chuẩn hóa hoa. |
| 84 | <code>    value = validate_text(value).upper()</code> | Tính validate_text(value).upper() rồi gán vào value. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 85 | <code>    if not re.fullmatch(r&quot;[A-Z0-9]{2,10}&quot;, value):</code> | Kiểm tra not re.fullmatch(&#x27;[A-Z0-9]{2,10}&#x27;, value). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 86 | <code>        raise ValueError(&quot;Course ID must contain 2-10 letters/digits.&quot;)</code> | Phát sinh ValueError(&#x27;Course ID must contain 2-10 letters/digits.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 87 | <code>    return value</code> | Kết thúc hàm, trả value cho nơi gọi. |
| 90 | <code>def validate_score(value):</code> | Định nghĩa validate_score; Trống -&gt; None; từ chối bool; đổi dấu phẩy rồi float; kiểm tra 0–10, cũng loại NaN/Infinity; không làm tròn. |
| 91 | <code>    if value is None or (isinstance(value, str) and not value.strip()):</code> | Kiểm tra value is None or (isinstance(value, str) and (not value.strip())). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 92 | <code>        return None</code> | Kết thúc hàm, trả None cho nơi gọi. |
| 93 | <code>    if isinstance(value, bool):</code> | Kiểm tra isinstance(value, bool). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 94 | <code>        raise ValueError(&quot;Score must be a number from 0 to 10.&quot;)</code> | Phát sinh ValueError(&#x27;Score must be a number from 0 to 10.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 95 | <code>    score = float(str(value).replace(&quot;,&quot;, &quot;.&quot;))</code> | Tính float(str(value).replace(&#x27;,&#x27;, &#x27;.&#x27;)) rồi gán vào score. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 96 | <code>    if not 0 &lt;= score &lt;= 10:</code> | Kiểm tra not 0 &lt;= score &lt;= 10. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 97 | <code>        raise ValueError(&quot;Score must be between 0 and 10.&quot;)</code> | Phát sinh ValueError(&#x27;Score must be between 0 and 10.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 98 | <code>    return score</code> | Kết thúc hàm, trả score cho nơi gọi. |
| 101 | <code>def validate_credits(value):</code> | Định nghĩa validate_credits; Loại bool; đổi float rồi yêu cầu số nguyên &gt;0. Môn 0 tín chỉ trên FAP hiện chưa được hỗ trợ. |
| 102 | <code>    if isinstance(value, bool):</code> | Kiểm tra isinstance(value, bool). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 103 | <code>        raise ValueError(&quot;Credits must be a positive integer.&quot;)</code> | Phát sinh ValueError(&#x27;Credits must be a positive integer.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 104 | <code>    number = float(value)</code> | Tính float(value) rồi gán vào number. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 105 | <code>    if not number &gt; 0 or not number.is_integer():</code> | Kiểm tra not number &gt; 0 or not number.is_integer(). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 106 | <code>        raise ValueError(&quot;Credits must be a positive integer.&quot;)</code> | Phát sinh ValueError(&#x27;Credits must be a positive integer.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 107 | <code>    return int(number)</code> | Kết thúc hàm, trả int(number) cho nơi gọi. |
| 110 | <code>def input_value(message, validator, allow_cancel=False, allow_empty=False):</code> | Định nghĩa input_value; Vòng lặp nhập chung. Hủy/trống được xử lý trước validate; ValueError/TypeError in lỗi rồi nhập lại. |
| 111 | <code>    while True:</code> | Lặp trong khi True. while True chỉ dừng khi return/ngoại lệ, hoặc chuyển vòng bằng continue. |
| 112 | <code>        raw = input(message).strip()</code> | Tính input(message).strip() rồi gán vào raw. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 113 | <code>        if allow_cancel and raw == &quot;0&quot;:</code> | Kiểm tra allow_cancel and raw == &#x27;0&#x27;. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 114 | <code>            return None</code> | Kết thúc hàm, trả None cho nơi gọi. |
| 115 | <code>        if allow_empty and not raw:</code> | Kiểm tra allow_empty and (not raw). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 116 | <code>            return None</code> | Kết thúc hàm, trả None cho nơi gọi. |
| 117 | <code>        try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 118 | <code>            if not raw:</code> | Kiểm tra not raw. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 119 | <code>                raise ValueError(&quot;A value is required.&quot;)</code> | Phát sinh ValueError(&#x27;A value is required.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 120 | <code>            return validator(raw)</code> | Kết thúc hàm, trả validator(raw) cho nơi gọi. |
| 121 | <code>        except (ValueError, TypeError) as error:</code> | Bắt (ValueError, TypeError) và đặt tên lỗi là error; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 122 | <code>            print(&quot;[Error]&quot;, error)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 125 | <code>def input_student_id(message=&quot;Student ID: &quot;, allow_cancel=False):</code> | Định nghĩa input_student_id; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 126 | <code>    return input_value(message, validate_student_id, allow_cancel)</code> | Kết thúc hàm, trả input_value(message, validate_student_id, allow_cancel) cho nơi gọi. |
| 129 | <code>def input_name(message=&quot;Full name: &quot;):</code> | Định nghĩa input_name; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 130 | <code>    return input_value(message, validate_name)</code> | Kết thúc hàm, trả input_value(message, validate_name) cho nơi gọi. |
| 133 | <code>def input_date_of_birth(message=&quot;Date of birth: &quot;):</code> | Định nghĩa input_date_of_birth; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 134 | <code>    return input_value(message, validate_date_of_birth)</code> | Kết thúc hàm, trả input_value(message, validate_date_of_birth) cho nơi gọi. |
| 137 | <code>def input_gender(message=&quot;Gender: &quot;):</code> | Định nghĩa input_gender; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 138 | <code>    return input_value(message, validate_gender)</code> | Kết thúc hàm, trả input_value(message, validate_gender) cho nơi gọi. |
| 141 | <code>def input_class_name(message=&quot;Class: &quot;):</code> | Định nghĩa input_class_name; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 142 | <code>    return input_value(message, validate_class_name)</code> | Kết thúc hàm, trả input_value(message, validate_class_name) cho nơi gọi. |
| 145 | <code>def input_phone(message=&quot;Phone: &quot;):</code> | Định nghĩa input_phone; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 146 | <code>    return input_value(message, validate_phone)</code> | Kết thúc hàm, trả input_value(message, validate_phone) cho nơi gọi. |
| 149 | <code>def input_email(message=&quot;Email: &quot;):</code> | Định nghĩa input_email; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 150 | <code>    return input_value(message, validate_email)</code> | Kết thúc hàm, trả input_value(message, validate_email) cho nơi gọi. |
| 153 | <code>def input_status(message=&quot;Status (Active/Inactive/Graduated): &quot;):</code> | Định nghĩa input_status; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 154 | <code>    return input_value(message, validate_status)</code> | Kết thúc hàm, trả input_value(message, validate_status) cho nơi gọi. |
| 157 | <code>def input_course_id(message=&quot;Course ID: &quot;, allow_cancel=False):</code> | Định nghĩa input_course_id; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 158 | <code>    return input_value(message, validate_course_id, allow_cancel)</code> | Kết thúc hàm, trả input_value(message, validate_course_id, allow_cancel) cho nơi gọi. |
| 161 | <code>def input_score(message, allow_empty=False):</code> | Định nghĩa input_score; nhận tham số và thực hiện các lệnh trong thân hàm; method có self làm việc trên object hiện tại. |
| 162 | <code>    return input_value(message, validate_score, allow_empty=allow_empty)</code> | Kết thúc hàm, trả input_value(message, validate_score, allow_empty=allow_empty) cho nơi gọi. |

## file_io.py

Chuyển dòng văn bản thành object và object thành dòng văn bản; hỗ trợ file kết quả cũ.

[Đọc source](../../file_io.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from models import Student, Result</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>def load_students(filepath):</code> | Định nghĩa load_students; Bỏ dòng rỗng, yêu cầu 8 cột, truyền các cột vào Student theo đúng thứ tự constructor. File thiếu trả list rỗng; lỗi khác truyền lên main. |
| 5 | <code>    students = []</code> | Tính [] rồi gán vào students. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 6 | <code>    try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 7 | <code>        with open(filepath, encoding=&quot;utf-8&quot;) as file:</code> | Mở tài nguyên bằng context manager: open(filepath, encoding=&#x27;utf-8&#x27;). Tự đóng khi ra khỏi khối, kể cả khi có lỗi. |
| 8 | <code>            for number, line in enumerate(file, 1):</code> | Lần lượt gán từng phần tử của enumerate(file, 1) cho (number, line) rồi chạy thân vòng lặp. |
| 9 | <code>                if not line.strip():</code> | Kiểm tra not line.strip(). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 10 | <code>                    continue</code> | Bỏ phần còn lại của vòng hiện tại và quay lại kiểm tra/lấy phần tử kế tiếp. |
| 11 | <code>                parts = [part.strip() for part in line.strip().split(&quot;&#124;&quot;)]</code> | Tạo list parts bằng duyệt/biến đổi từng phần tử: [part.strip() for part in line.strip().split(&#x27;&#124;&#x27;)]. |
| 12 | <code>                if len(parts) != 8:</code> | Kiểm tra len(parts) != 8. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 13 | <code>                    raise ValueError(f&quot;{filepath}, line {number}: expected 8 student fields.&quot;)</code> | Phát sinh ValueError(f&#x27;{filepath}, line {number}: expected 8 student fields.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 14 | <code>                students.append(Student(*parts))</code> | Thêm object vào cuối list đang giữ; không tạo bản sao object: students.append(Student(*parts)). |
| 15 | <code>    except FileNotFoundError:</code> | Bắt FileNotFoundError; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 16 | <code>        print(f&quot;[Info] {filepath} not found; starting empty.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 17 | <code>    return students</code> | Kết thúc hàm, trả students cho nơi gọi. |
| 20 | <code>def load_results(filepath):</code> | Định nghĩa load_results; 5 cột cũ: ba trường mới None. 8 cột mới: ô trống đổi None. Status cũ không được truyền vào Result mà được tính lại. |
| 21 | <code>    results = []</code> | Tính [] rồi gán vào results. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 22 | <code>    try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 23 | <code>        with open(filepath, encoding=&quot;utf-8&quot;) as file:</code> | Mở tài nguyên bằng context manager: open(filepath, encoding=&#x27;utf-8&#x27;). Tự đóng khi ra khỏi khối, kể cả khi có lỗi. |
| 24 | <code>            for number, line in enumerate(file, 1):</code> | Lần lượt gán từng phần tử của enumerate(file, 1) cho (number, line) rồi chạy thân vòng lặp. |
| 25 | <code>                if not line.strip():</code> | Kiểm tra not line.strip(). Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 26 | <code>                    continue</code> | Bỏ phần còn lại của vòng hiện tại và quay lại kiểm tra/lấy phần tử kế tiếp. |
| 27 | <code>                parts = [part.strip() for part in line.strip().split(&quot;&#124;&quot;)]</code> | Tạo list parts bằng duyệt/biến đổi từng phần tử: [part.strip() for part in line.strip().split(&#x27;&#124;&#x27;)]. |
| 28 | <code>                if len(parts) == 5:</code> | Kiểm tra len(parts) == 5. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 29 | <code>                    result = Result(parts[0], parts[1], None, None, None, parts[2], parts[3])</code> | Tính Result(parts[0], parts[1], None, None, None, parts[2], parts[3]) rồi gán vào result. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 30 | <code>                    print(f&quot;[Info] {parts[0]}/{parts[1]}: old format; course details need completing.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 31 | <code>                elif len(parts) == 8:</code> | Kiểm tra len(parts) == 8. Đúng chạy nhánh thụt lề; sai xét elif/else hoặc đi tiếp. |
| 32 | <code>                    result = Result(parts[0], parts[1], parts[2] or None, parts[3] or None,</code> | Tính Result(parts[0], parts[1], parts[2] or None, parts[3] or None, parts[4] or None, parts[5], parts[6]) rồi gán vào result. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 33 | <code>                                    parts[4] or None, parts[5], parts[6])</code> | Tiếp lệnh bắt đầu ở dòng 32: Tính Result(parts[0], parts[1], parts[2] or None, parts[3] or None, parts[4] or None, parts[5], parts[6]) rồi gán vào result. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 34 | <code>                else:</code> | Nhánh thay thế: chỉ chạy khi các điều kiện if/elif trước đó trong cùng chuỗi đều sai. |
| 35 | <code>                    raise ValueError(f&quot;{filepath}, line {number}: expected 5 old or 8 new result fields.&quot;)</code> | Phát sinh ValueError(f&#x27;{filepath}, line {number}: expected 5 old or 8 new result fields.&#x27;). Ngừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không phải chỉ in thông báo. |
| 36 | <code>                results.append(result)</code> | Thêm object vào cuối list đang giữ; không tạo bản sao object: results.append(result). |
| 37 | <code>    except FileNotFoundError:</code> | Bắt FileNotFoundError; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 38 | <code>        print(f&quot;[Info] {filepath} not found; starting empty.&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 39 | <code>    return results</code> | Kết thúc hàm, trả results cho nơi gọi. |
| 42 | <code>def save_records(filepath, records):</code> | Định nghĩa save_records; Tạo hết chuỗi trước khi mở file w; with đóng file. Ghi dở vẫn có thể mất dữ liệu; chỉ bắt OSError/ValueError. |
| 43 | <code>    try:</code> | Bắt đầu vùng có xử lý ngoại lệ; chỉ những loại được ghi ở except tương ứng mới được bắt. |
| 44 | <code>        lines = [record.to_file_line() for record in records]</code> | Tạo list lines bằng duyệt/biến đổi từng phần tử: [record.to_file_line() for record in records]. |
| 45 | <code>        with open(filepath, &quot;w&quot;, encoding=&quot;utf-8&quot;) as file:</code> | Mở tài nguyên bằng context manager: open(filepath, &#x27;w&#x27;, encoding=&#x27;utf-8&#x27;). Tự đóng khi ra khỏi khối, kể cả khi có lỗi. |
| 46 | <code>            file.writelines(lines)</code> | Gọi file.writelines(lines). Hàm chạy xong mới sang dòng kế; ngoại lệ có thể truyền ngược về menu/main. |
| 47 | <code>        return True</code> | Kết thúc hàm, trả True cho nơi gọi. |
| 48 | <code>    except (OSError, ValueError) as error:</code> | Bắt (OSError, ValueError) và đặt tên lỗi là error; xong nhánh này thì tiếp tục sau try/except, trừ khi return. |
| 49 | <code>        print(f&quot;[Error] Cannot save {filepath}: {error}&quot;)</code> | Hiển thị ra console. In Student/Result sẽ tự gọi __str__; f-string chèn các giá trị trong ngoặc nhọn. |
| 50 | <code>        return False</code> | Kết thúc hàm, trả False cho nơi gọi. |

## models/__init__.py

Xuất các class để nơi khác dùng from models import Student, Result.

[Đọc source](../../models/__init__.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from models.person import Person</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from models.student import Student</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 3 | <code>from models.result import Result</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>__all__ = [&quot;Person&quot;, &quot;Student&quot;, &quot;Result&quot;]</code> | Tính [&#x27;Person&#x27;, &#x27;Student&#x27;, &#x27;Result&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |

## services/__init__.py

Xuất hai manager ở cấp package.

[Đọc source](../../services/__init__.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from services.student_manager import StudentManager</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>from services.result_manager import ResultManager</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |

## utils/__init__.py

Xuất các hàm nhập; __all__ liệt kê tên xuất khi dùng import *. Không tự chạy nhập liệu.

[Đọc source](../../utils/__init__.py)

| Dòng | Code | Giải thích |
| --- | --- | --- |
| 1 | <code>from utils.validator import (</code> | Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 2 | <code>    input_student_id,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 3 | <code>    input_name,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 4 | <code>    input_date_of_birth,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 5 | <code>    input_gender,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 6 | <code>    input_class_name,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 7 | <code>    input_phone,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 8 | <code>    input_email,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 9 | <code>    input_status,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 10 | <code>    input_course_id,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 11 | <code>    input_score,</code> | Tiếp lệnh bắt đầu ở dòng 1: Nạp tên từ module/package để sử dụng bên dưới; import chỉ định nghĩa/nạp code, không đồng nghĩa đã gọi hàm. |
| 12 | <code>)</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |
| 14 | <code>__all__ = [</code> | Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 15 | <code>    &quot;input_student_id&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 16 | <code>    &quot;input_name&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 17 | <code>    &quot;input_date_of_birth&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 18 | <code>    &quot;input_gender&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 19 | <code>    &quot;input_class_name&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 20 | <code>    &quot;input_phone&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 21 | <code>    &quot;input_email&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 22 | <code>    &quot;input_status&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 23 | <code>    &quot;input_course_id&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 24 | <code>    &quot;input_score&quot;,</code> | Tiếp lệnh bắt đầu ở dòng 14: Tính [&#x27;input_student_id&#x27;, &#x27;input_name&#x27;, &#x27;input_date_of_birth&#x27;, &#x27;input_gender&#x27;, &#x27;input_class_name&#x27;, &#x27;input_phone&#x27;, &#x27;input_email&#x27;, &#x27;input_status&#x27;, &#x27;input_course_id&#x27;, &#x27;input_score&#x27;] rồi gán vào __all__. Nếu vế phải gọi hàm thì hàm hoàn tất trước khi gán. |
| 25 | <code>]</code> | Đóng biểu thức/cấu trúc nhiều dòng; không phải một lệnh nghiệp vụ riêng. |

## Đối chiếu phiên bản source

| File | Số dòng | SHA-256 |
| --- | --- | --- |
| main.py | 53 | `ceb5de0a0c5df14971abee0fa030adbec1610b4295fcb6555b33c2b6a65e2644` |
| models/person.py | 55 | `d74f2bdbd28a6f8d87078110fc044ed0fcb9bc5e6c618759ec950085d80c5c09` |
| models/student.py | 61 | `071314adb217d483d747b491a2d6925544d0ebce2294867ec7da0b22d397e484` |
| models/result.py | 113 | `76477575af93ccaa7cd42c1bda94364bf3783cc18e9d7c9fe5eb5631057affdf` |
| services/student_manager.py | 59 | `204800eca337f393374db53bda31fe529997e3702770f1fa141f26e7742c5bdc` |
| services/result_manager.py | 75 | `cba4e6c1e607ac60477cdc68f634e00d08ca1e19dcef04511cf30450d00c7aa0` |
| student_management.py | 82 | `0a4e6f78819f7b38b571c4d118844dd33522b8b20c24b627b65c0147cd1a7a4f` |
| result_management.py | 96 | `3133fc313578b900fab35e626eb1e762d2f06d61a6db4253da6ea708b030d00f` |
| utils/validator.py | 162 | `cdefefdfe64715a52a821748caa50a865ff0600957dd6eec4536d6f86c048581` |
| file_io.py | 50 | `0dec8f4c33c0376fe831b8e9aa51ae75ece6b3ece441b213d62768082424827e` |
| models/__init__.py | 5 | `cb24d0055c623167a783907de0e451c4a1ddca5561b2f172d91adcaa956a17d8` |
| services/__init__.py | 2 | `2de53f8dae372ca35883ae6503ce5c88d1d9d04d79ce90d790a862533df956bb` |
| utils/__init__.py | 25 | `abd334ae710485c357d7f8789d6574e9f1b0ecd81fa4d308ff8f24002d154d3f` |
