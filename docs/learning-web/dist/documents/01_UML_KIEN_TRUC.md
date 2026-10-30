# UML chi tiết và cách đọc kiến trúc

[Quay lại mục lục](HUONG_DAN_DOC_CODE.md)

## 1. Bản đồ toàn dự án

```mermaid
flowchart LR
    User[Thành viên nhập console] --> Main[main.py]
    Main --> SC[student_management.py]
    Main --> RC[result_management.py]
    Main --> IO[file_io.py]
    SC --> SM[StudentManager]
    RC --> RM[ResultManager]
    RM --> SM
    SM --> S[Student objects]
    RM --> R[Result objects]
    S --> P[Person]
    SC --> V[utils.validator]
    RC --> V
    S --> V
    P --> V
    R --> V
    IO --> S
    IO --> R
    IO <--> TXT[students.txt / results.txt]
```

Mũi tên trên là sử dụng/gọi, không phải tất cả đều là kế thừa. UML bên dưới mới thể hiện loại quan hệ class. File I/O tạo object rồi main đưa chúng vào manager. Menu không đọc/ghi file trực tiếp.

## 2. UML class đầy đủ

`+` là giao diện dùng bên ngoài. `#` biểu diễn thuộc tính nội bộ theo quy ước `_` trong code, không phải Python cấm truy cập. `~` trong List~Student~ là cú pháp kiểu generic của Mermaid. `?` trong phần giải thích nghĩa là cho phép None. Kiểu dữ liệu trong sơ đồ là diễn giải để học, không phải type annotation đã có trong source.

```mermaid
classDiagram
    direction TB
    Person <|-- Student : kế thừa
    StudentManager "1" o-- "0..*" Student : giữ list
    ResultManager "1" o-- "0..*" Result : giữ list
    ResultManager --> StudentManager : kiểm tra sinh viên
    Result "0..*" --> "1" Student : liên kết bằng student_id

    class Person {
        #str _full_name
        #str _date_of_birth
        #str _gender
        #str _phone
        #str _email
        +__init__(full_name, date_of_birth, gender, phone, email)
        +full_name getter_setter
        +date_of_birth getter_setter
        +gender getter_setter
        +phone getter_setter
        +email getter_setter
        +__str__() str
    }
    class Student {
        #str _student_id
        #str _class_name
        #str _status
        +__init__(student_id, full_name, date_of_birth, gender, class_name, phone, email, status)
        +student_id getter_only
        +class_name getter_setter
        +status getter_setter
        +to_file_line() str
        +to_dict() dict
        +__str__() str
    }
    class Result {
        #str _student_id
        #str _course_id
        #str_or_None _course_name
        #str_or_None _semester
        #int_or_None _credits
        #float_or_None _grade_fe
        #float_or_None _grade_re
        +__init__(student_id, course_id, course_name, semester, credits, grade_fe, grade_re)
        +student_id getter_only
        +course_id getter_only
        +course_name getter_setter
        +semester getter_setter
        +credits getter_setter
        +grade_fe getter_setter
        +grade_re getter_setter
        +result_status computed_getter
        +_format_grade(grade) float_or_None
        +evaluate_status(grade_fe, grade_re) str_or_None
        +to_file_line() str
        +to_dict() dict
        +__str__() str
    }
    class StudentManager {
        #List~Student~ _students
        +__init__(students)
        +students() list_copy
        +find(student_id) Student_or_None
        +add(student) None
        +update(student_id, field, value) None
        +filter(condition) List~Student~
        +active_students() List~Student~
    }
    class ResultManager {
        #StudentManager _student_manager
        #List~Result~ _results
        +__init__(student_manager, results)
        +results() list_copy
        +find(student_id, course_id) Result_or_None
        +check_student(student_id, require_active) None
        +add(result, loading) None
        +update_grades(student_id, course_id, grade_fe, grade_re) None
        +update_course_details(student_id, course_id, course_name, semester, credits) None
        +search(student_id) List~Result~
        +sorted_results() List~Result~
        +passed_results() List~Result~
    }
```

Property được ghi getter/setter để dễ nhận diện, không phải method nhận tham số có tên getter_setter. Trong code dùng `student.status`, không dùng `student.status()`. `_format_grade` và `evaluate_status` là staticmethod: không nhận self, có thể gọi `Result.evaluate_status(...)`.

Quan hệ Result -> Student là quan hệ dữ liệu thông qua mã, không có thuộc tính Student object bên trong Result. Chỉ manager bảo đảm mã tham chiếu tồn tại. Dùng aggregation vì các object được tạo trước khi đưa vào manager và vẫn có thể được nơi khác tham chiếu; không khẳng định vòng đời độc quyền như composition.

## 3. Một object Student được tạo như thế nào?

```mermaid
sequenceDiagram
    participant CLI as Menu sinh viên
    participant S as Student
    participant P as Person
    participant V as validator
    participant SM as StudentManager
    CLI->>S: Student(mã, tên, ngày sinh, giới tính, lớp, phone, email, status)
    S->>P: super().__init__(tên, ngày sinh, giới tính, phone, email)
    P->>P: self.full_name = tên
    P->>V: validate_name(tên)
    V-->>P: tên chuẩn hóa hoặc ValueError
    Note over P,V: Các trường ngày sinh, giới tính, phone, email cũng qua setter
    S->>V: validate_student_id(mã)
    S->>S: self.class_name / self.status gọi setter
    S-->>CLI: object Student đã hợp lệ
    CLI->>SM: add(student)
    SM->>SM: find(mã), chặn trùng
    SM->>SM: _students.append(student)
```

`super()` không tạo một Person độc lập nằm trong Student. Nó chạy constructor lớp cha trên cùng object Student. Các field kế thừa và field riêng đều thuộc object đó.

## 4. Một lần thêm kết quả đi qua đâu?

```mermaid
sequenceDiagram
    actor U as Người dùng
    participant CLI as result_management
    participant V as validator
    participant RM as ResultManager
    participant SM as StudentManager
    participant R as Result
    U->>CLI: Chọn thêm kết quả
    CLI->>V: input_student_id()
    CLI->>RM: check_student(mã)
    RM->>SM: find(mã)
    SM-->>RM: Student hoặc None
    Note over RM: Yêu cầu tồn tại và Active
    CLI->>V: Nhập mã môn
    CLI->>RM: find(mã, môn)
    CLI->>V: Nhập tên môn, học kỳ, tín chỉ
    CLI->>V: read_grades: FE, RE khi FE dưới 5
    CLI->>R: Result(...)
    R->>V: Kiểm tra mã / metadata / điểm
    CLI->>RM: add(result)
    RM->>RM: Kiểm tra metadata, sinh viên và trùng lần nữa
    RM->>RM: append(result)
    Note over RM: Mới thay bộ nhớ, chưa ghi file
```

Đọc đúng thứ tự thực tế ở flowchart/add_result: nhập MSSV -> check_student -> nhập mã môn -> find trùng -> nhập chi tiết môn -> nhập điểm -> tạo Result -> add. Flowchart và giải thích số dòng bên cạnh giúp đối chiếu từng bước.

## 5. Khi sửa điểm, status đổi như thế nào?

```mermaid
flowchart TD
    A[update_grades nhận FE và RE] --> B[Kiểm tra Student Active và Result tồn tại]
    B --> C[validate_score FE rồi RE vào biến tạm]
    C --> D{FE trống hoặc FE từ 5 trở lên?}
    D -->|Có| E[re = None]
    D -->|Không| F[Giữ RE mới đã kiểm tra]
    E --> G[Gán hai property grade_fe / grade_re]
    F --> G
    G --> H[Khi đọc result_status: gọi evaluate_status]
    H --> I{FE là None?}
    I -->|Có| J[Trả None: Chưa có điểm]
    I -->|Không| K{FE từ 5 trở lên hoặc RE đã có và từ 5 trở lên?}
    K -->|Có| L[Pass]
    K -->|Không| M[Fail]
```

Ví dụ: FE=4, RE=5 -> Pass. Đổi FE=6 -> RE bị xóa, vẫn Pass. Đổi FE trống -> FE/RE đều None, status None. Nhập FE=10.04 -> lỗi, không sửa điểm cũ. FE=4.96 vẫn dưới 5 vì không làm tròn. Status None khác chuỗi `"None"` và khác `"Fail"`.

## 6. File, object và chuỗi khác nhau ra sao?

| Giai đoạn | Biểu diễn | Ý nghĩa |
| --- | --- | --- |
| File | `SE211528\|PFP191\|Programming Fundamentals with Python\|Fall2026\|3\|4.0\|5.0\|Pass` | Tất cả là chữ, cột cách nhau bằng dấu phân cách |
| Sau split | list chuỗi `parts` | Cột credits và điểm vẫn chưa phải số |
| Sau Result(...) | credits int=3; FE float=4.0; RE float=5.0 | Constructor/property gọi validator để đổi kiểu |
| Đọc status | property trả `Pass` | Tính lại theo điểm, bỏ status lưu sẵn trong file |
| to_file_line | chuỗi 8 cột + ký tự xuống dòng | None được đổi thành ô trống, không ghi chữ None |
| to_dict | dictionary mới | Hỗ trợ biểu diễn/đối chiếu; không phải dữ liệu nghiệp vụ chính |

Có thể gọi `to_file_line()` trên Student và Result với cùng tên method nhưng cách tạo dòng khác nhau; đây là một ví dụ dùng chung giao diện trên object khác loại. `print(student)` chọn Student.__str__, thay vì Person.__str__ đã được override.

## 7. Những chỗ dễ hiểu nhầm khi vấn đáp

| Code/khái niệm | Cần hiểu đúng |
| --- | --- |
| `_students.copy()` | Chỉ sao chép list; Student bên trong vẫn là object gốc. Xóa phần tử trong bản sao không xóa list manager, nhưng sửa Student sẽ thấy thay đổi ở cả hai nơi |
| `find()` | Trả chính object đang được giữ, không clone object |
| `raise ValueError` | Dừng luồng hiện tại, tìm except phù hợp ở nơi gọi; không tự in lỗi |
| `loading=True` | Bỏ điều kiện Active và đủ metadata khi tải lịch sử, vẫn kiểm tra kiểu Result, MSSV tồn tại và khóa trùng |
| `require_active=False` | Chỉ bỏ kiểm tra Active; không bỏ kiểm tra tồn tại sinh viên |
| `sorted(...)` | Tạo list mới, không sắp xếp lại list nội bộ bằng in-place |
| `or ""` | None trở thành khóa rỗng để so sánh với chuỗi; chưa có điểm xếp sau Fail |
| `Student(*parts)` | Unpack 8 phần tử thành 8 đối số theo thứ tự constructor |
| `reader` trong dictionary menu | Hàm được giữ như một giá trị; `reader(...)` mới thực sự gọi hàm |
| `with open` | Bảo đảm đóng tài nguyên; không bảo đảm ghi nguyên tử hay chống mất điện |
| `__all__` | Danh sách tên xuất qua import *, không phải danh sách hàm phải chạy |
| `if __name__ == "__main__"` | Chỉ tự gọi main khi chạy file trực tiếp; import main không tự chạy menu |

## 8. Giới hạn hiện tại phải giải thích trung thực

- Học kỳ hiện dùng validate_text: chưa bắt buộc mẫu Spring/Summer/Fall + năm.
- Credits đang yêu cầu >0, chưa hỗ trợ môn 0 tín chỉ trong ảnh FAP; hai môn mẫu đều 3 tín chỉ.
- Result riêng lẻ cho phép metadata None để tải file cũ; add mới qua manager yêu cầu đủ metadata.
- Model không tự ép quan hệ FE/RE ở mọi lần gán trực tiếp; menu/manager điều khiển RE. Có thể gán RE vào Result khi FE None; status vẫn None.
- Hai file ghi lần lượt, không có rollback/backup tự động. Nếu một file thành công và file kia lỗi, trạng thái file có thể lệch.
- Khi EOF lặp lại và save liên tục thất bại, main có thể lặp báo lỗi; chưa xử lý đầy đủ tình huống này.
- Điều kiện ngày sinh đến 2008, prefix và Active là quy tắc nhóm giữ từ bản trước; không khẳng định mọi điều kiện đều do đề bắt buộc.
- Khóa kết quả là MSSV + mã môn, chưa hỗ trợ bản ghi riêng cho cùng môn ở nhiều học kỳ.

Các ghi chú trên mô tả code hiện tại, không âm thầm bổ sung tính năng hoặc coi Lab 5 đã hoàn thành.

## 9. Câu hỏi tự kiểm cho mỗi thành viên

1. Vì sao constructor dùng `self.phone = phone` thay vì luôn gán `_phone` trực tiếp?
2. Tại sao đổi mã sinh viên sau khi đã có kết quả là nguy hiểm?
3. Nếu FE sai nhưng file ghi Pass, chương trình sẽ lấy trạng thái nào?
4. Vì sao cùng một điểm được kiểm tra ở input rồi lại ở model?
5. Thêm object vào manager đã lưu xuống đĩa chưa?
6. Tại sao update_grades kiểm tra FE/RE trước khi gán cả hai?
7. File không tồn tại khác file có dữ liệu sai ở đường xử lý nào?
8. Vì sao property danh sách trả copy nhưng chưa phải bảo vệ tuyệt đối object bên trong?

Đáp án nằm lần lượt ở phần constructor/setter, liên kết MSSV, loader/Result, validation dùng chung, luồng lưu, update_grades, File I/O/main và bảng khái niệm phía trên.
