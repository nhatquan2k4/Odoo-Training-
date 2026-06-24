# Student Management System

## 1. Giới thiệu bài tập

**Student Management System** là chương trình quản lý sinh viên chạy trên terminal bằng Python.

Bài tập này dùng để tổng hợp kiến thức Python cơ bản trong Week 1, bao gồm:
- Biến và kiểu dữ liệu
- List, tuple, dictionary
- Indexing, slicing
- Toán tử số học
- Xử lý chuỗi
- Cấu trúc điều kiện
- Vòng lặp
- Function
- Return
- Try-except
- Validate dữ liệu người dùng nhập

---

## 2. Mục tiêu

Sau khi hoàn thành bài tập, củng cố kiến thức
- Khai báo và sử dụng biến.
- Sử dụng các kiểu dữ liệu: int, float, str, bool.
- Làm việc với list, tuple, dictionary.
- Sử dụng indexing và slicing.
- Viết chương trình với if, elif, else.
- Sử dụng vòng lặp for và while.
- Viết function có tham số và return.
- Xử lý lỗi nhập liệu bằng try-except.
- Xây dựng chương trình terminal có menu.

---

## 3. Cấu trúc project

```text
python_week1_project/
│
├── student_management.py
└── README.md
```

File chính của chương trình là:

```text
student_management.py
```

---

## 4. Cấu trúc dữ liệu

Chương trình sử dụng một list để lưu danh sách sinh viên:

```text
students = []
```

Mỗi sinh viên được lưu dưới dạng dictionary:

```text
{
    "id": "SV001",
    "name": "Nguyen Van An",
    "age": 20,
    "scores": [8.0, 7.5, 9.0],
    "is_active": True
}
```

Ý nghĩa các trường dữ liệu:

| Trường | Kiểu dữ liệu | Ý nghĩa |
|---|---|---|
| id | str | Mã sinh viên |
| name | str | Họ tên sinh viên |
| age | int | Tuổi sinh viên |
| scores | list[float] | Danh sách điểm |
| is_active | bool | Trạng thái còn học hay đã nghỉ |

Chương trình cũng sử dụng tuple để lưu các mức xếp loại:

```text
rank_levels = ("Yếu", "Trung bình", "Khá", "Giỏi", "Xuất sắc")
```

---

## 5. Menu chương trình

Khi chạy chương trình, hiển thị menu:

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Thêm sinh viên
2. Hiển thị danh sách sinh viên
3. Xem chi tiết sinh viên theo mã
4. Cập nhật điểm sinh viên
5. Tính điểm trung bình của một sinh viên
6. Tìm sinh viên có điểm trung bình cao nhất
7. Xếp loại sinh viên
8. Tìm sinh viên theo tên
9. Hiển thị 3 sinh viên đầu tiên
10. Thống kê lớp học
0. Thoát
Chọn chức năng:
```

Chương trình chạy liên tục bằng vòng lặp while cho đến khi người dùng chọn 0.

---

## 6. Chức năng chi tiết

### 6.1. Thêm sinh viên

Người dùng nhập:

```text
Nhập mã sinh viên:
Nhập tên sinh viên:
Nhập tuổi:
Nhập số lượng điểm:
Nhập điểm 1:
Nhập điểm 2:
...
Sinh viên còn học không? yes/no:
```

Yêu cầu:

- Mã sinh viên không được rỗng.
- Tên sinh viên không được rỗng.
- Tuổi phải là số nguyên lớn hơn 0.
- Điểm phải là số thực từ 0 đến 10.
- Nếu nhập yes thì lưu is_active là True.
- Nếu nhập no thì lưu is_active là False.
- Nếu nhập sai kiểu dữ liệu, chương trình phải xử lý bằng try-except.

Ví dụ:

```text
Nhập mã sinh viên: SV001
Nhập tên sinh viên: Nguyen Van An
Nhập tuổi: 20
Nhập số lượng điểm: 3
Nhập điểm 1: 8
Nhập điểm 2: 7.5
Nhập điểm 3: 9
Sinh viên còn học không? yes/no: yes
Thêm sinh viên thành công!
```

---

### 6.2. Hiển thị danh sách sinh viên

Nếu danh sách rỗng, hiển thị:

```text
Chưa có sinh viên nào.
```

Nếu có dữ liệu, hiển thị:

```text
Danh sách sinh viên:
1. SV001 - Nguyen Van An - Tuổi: 20 - Trạng thái: Đang học
2. SV002 - Tran Thi Binh - Tuổi: 21 - Trạng thái: Nghỉ học
```

Yêu cầu dùng vòng lặp for.

---

### 6.3. Xem chi tiết sinh viên theo mã

Người dùng nhập mã sinh viên.

Nếu tìm thấy, hiển thị:

```text
Mã sinh viên: SV001
Tên: Nguyen Van An
Tuổi: 20
Điểm: [8.0, 7.5, 9.0]
Điểm đầu tiên: 8.0
Điểm cuối cùng: 9.0
Trạng thái: Đang học
```

Nếu không tìm thấy:

```text
Không tìm thấy sinh viên.
```

Yêu cầu sử dụng:

- Dictionary
- List
- Indexing
- If-else

---

### 6.4. Cập nhật điểm sinh viên

Người dùng nhập mã sinh viên.

Nếu sinh viên tồn tại, người dùng nhập lại danh sách điểm mới.

Ví dụ:

```text
Nhập mã sinh viên: SV001
Nhập số lượng điểm mới: 2
Nhập điểm 1: 9
Nhập điểm 2: 8.5
Cập nhật điểm thành công!
```

Yêu cầu:

- Kiểm tra sinh viên có tồn tại hay không.
- Kiểm tra số lượng điểm hợp lệ.
- Kiểm tra từng điểm phải từ 0 đến 10.
- Dùng try-except khi nhập dữ liệu.

---

### 6.5. Tính điểm trung bình của một sinh viên

Người dùng nhập mã sinh viên.

Nếu tìm thấy, tính điểm trung bình:

```text
Điểm trung bình của Nguyen Van An là: 8.17
```

Công thức:

```text
Điểm trung bình = Tổng điểm / Số lượng điểm
```

Yêu cầu:

- Tự viết function tính tổng điểm bằng vòng lặp for.
- Không dùng sum() ở phiên bản đầu.
- Kết quả làm tròn 2 chữ số thập phân.

---

### 6.6. Tìm sinh viên có điểm trung bình cao nhất

Chương trình duyệt toàn bộ danh sách sinh viên để tìm sinh viên có điểm trung bình cao nhất.

Ví dụ:

```text
Sinh viên có điểm trung bình cao nhất:
Mã: SV002
Tên: Tran Thi Binh
Điểm trung bình: 9.25
```

Yêu cầu:

- Dùng vòng lặp for.
- Dùng biến lưu điểm trung bình cao nhất hiện tại.
- Dùng function tính điểm trung bình.

---

### 6.7. Xếp loại sinh viên

Quy tắc xếp loại:

| Điểm trung bình | Xếp loại |
|---|---|
| >= 9.0 | Xuất sắc |
| >= 8.0 | Giỏi |
| >= 6.5 | Khá |
| >= 5.0 | Trung bình |
| < 5.0 | Yếu |

Yêu cầu dùng if, elif, else.

---

### 6.8. Tìm sinh viên theo tên

Người dùng nhập từ khóa cần tìm.

Ví dụ:

```text
Nhập tên cần tìm: an
```

Nếu có sinh viên phù hợp:

```text
Kết quả tìm kiếm:
SV001 - Nguyen Van An
SV003 - Le An Minh
```

Yêu cầu:

- Không phân biệt chữ hoa chữ thường.
- Dùng lower().
- Dùng toán tử in.

Gợi ý xử lý:

```text
keyword.lower() in student["name"].lower()
```

---

### 6.9. Hiển thị 3 sinh viên đầu tiên

Chương trình hiển thị tối đa 3 sinh viên đầu tiên trong danh sách.

Yêu cầu dùng slicing:

```text
students[:3]
```

Nếu danh sách có ít hơn 3 sinh viên thì hiển thị tất cả.

---

### 6.10. Thống kê lớp học

Chương trình hiển thị:

```text
===== THỐNG KÊ LỚP HỌC =====
Tổng số sinh viên: 5
Số sinh viên đang học: 4
Số sinh viên đã nghỉ: 1
Tuổi trung bình: 20.6
Điểm trung bình cả lớp: 7.85
```

Yêu cầu:

- Dùng int, float, bool.
- Dùng vòng lặp for.
- Dùng toán tử cộng và chia.
- Dùng if để kiểm tra trạng thái is_active.

---

## 7. Danh sách function bắt buộc

Chương trình cần có ít nhất các function sau:

```text
def add_student(students):
    ...

def show_students(students):
    ...

def find_student_by_id(students, student_id):
    ...

def update_scores(students):
    ...

def calculate_total(scores):
    ...

def calculate_average(scores):
    ...

def find_best_student(students):
    ...

def classify_student(average):
    ...

def search_student_by_name(students):
    ...

def show_first_three_students(students):
    ...

def show_statistics(students):
    ...

def main():
    ...
```

---

## 8. Yêu cầu xử lý lỗi

Chương trình cần xử lý lỗi ở các phần:

- Nhập tuổi
- Nhập số lượng điểm
- Nhập điểm
- Nhập lựa chọn menu

Ví dụ xử lý lỗi:

```text
try:
    age = int(input("Nhập tuổi: "))
except ValueError:
    print("Tuổi phải là số nguyên.")
```

Nếu người dùng chọn menu không hợp lệ:

```text
Lựa chọn không hợp lệ. Vui lòng chọn lại.
```

---

## 9. Gợi ý luồng chương trình

```text
def main():
    students = []

    while True:
        print_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            student_id = input("Nhập mã sinh viên: ")
            student = find_student_by_id(students, student_id)

            if student is None:
                print("Không tìm thấy sinh viên.")
            else:
                print(student)
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")
```

---

## 10. Nâng cấp thêm

Nếu hoàn thành sớm, có thể làm thêm:

1. Không cho phép thêm hai sinh viên có cùng mã id.
2. Xóa sinh viên theo mã.
3. Cập nhật tên hoặc tuổi sinh viên.
4. Sắp xếp sinh viên theo điểm trung bình giảm dần.
5. Lưu dữ liệu sinh viên ra file txt hoặc json.
6. Đọc dữ liệu sinh viên từ file khi chương trình khởi động.

---

## 11. Kết quả mong muốn

Sau khi hoàn thành, người học cần có một chương trình terminal hoàn chỉnh cho phép:

- Thêm sinh viên
- Hiển thị danh sách sinh viên
- Xem chi tiết sinh viên
- Cập nhật điểm
- Tính điểm trung bình
- Tìm sinh viên điểm cao nhất
- Xếp loại sinh viên
- Tìm kiếm sinh viên
- Thống kê lớp học
- Xử lý lỗi nhập liệu

Bài tập này giúp củng cố toàn bộ kiến thức Python cơ bản trong tuần đầu tiên.
