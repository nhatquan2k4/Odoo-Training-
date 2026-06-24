# Product Inventory Management Advanced

## 1. Mục tiêu bài thực hành
Xây dựng một chương trình quản lý sản phẩm trong kho bằng Python chạy trên terminal, đồng thời quản lý toàn bộ quá trình phát triển bằng Git và GitHub.
Bài thực hành kết hợp hai nhóm kiến thức:

### Nhóm kiến thức Python
* List comprehension
* Lambda function
* Modules và libraries: `math`, `random`, `datetime`
* File input/output: đọc/ghi file `.txt`
* Object-oriented programming: class, object, method
* JSON handling: đọc/ghi file `.json`

### Nhóm kiến thức Git/GitHub
* Git repository
* Commit
* Branch local
* Branch remote
* Merge
* Conflict
* Remote `origin`
* Push, pull, fetch
* Pull Request
* `.gitignore`
* Stash
* Reset
* Tag
* GitHub repository

---

# 2. Mô tả chương trình
Xây dựng chương trình quản lý kho sản phẩm trên terminal.
Mỗi sản phẩm cần có các thông tin:

```text
Mã sản phẩm
Tên sản phẩm
Danh mục
Giá sản phẩm
Số lượng tồn kho
Trạng thái còn hàng / hết hàng
Ngày tạo sản phẩm
Ngày cập nhật gần nhất
```

Chương trình cần cho phép người dùng:
```text
1. Thêm sản phẩm
2. Hiển thị danh sách sản phẩm
3. Xem chi tiết sản phẩm theo mã
4. Cập nhật số lượng sản phẩm
5. Cập nhật giá sản phẩm
6. Xóa sản phẩm
7. Tìm kiếm sản phẩm theo tên
8. Lọc sản phẩm còn hàng
9. Sắp xếp sản phẩm theo giá
10. Sắp xếp sản phẩm theo tổng giá trị tồn kho
11. Tìm sản phẩm có giá cao nhất
12. Tính thống kê kho hàng
13. Lưu dữ liệu ra file JSON
14. Đọc dữ liệu từ file JSON
15. Ghi log thao tác ra file text
0. Thoát chương trình
```

---
# 3. Yêu cầu về cấu trúc project
```
Cấu trúc thư mục yêu cầu:

```text
├── main.py
├── product.py
├── inventory.py
├── storage.py
├── logger.py
├── products.json
├── logs.txt
├── README.md
└── .gitignore
```
Ý nghĩa các file:

| File            | Chức năng                                            |
| --------------- | ---------------------------------------------------- |
| `main.py`       | Chạy chương trình, hiển thị menu                     |
| `product.py`    | Chứa class `Product`                                 |
| `inventory.py`  | Chứa class `Inventory` để quản lý danh sách sản phẩm |
| `storage.py`    | Xử lý đọc/ghi JSON                                   |
| `logger.py`     | Ghi log thao tác người dùng                          |
| `products.json` | Lưu dữ liệu sản phẩm                                 |
| `logs.txt`      | Lưu lịch sử thao tác                                 |
| `README.md`     | Mô tả project, cách chạy, chức năng                  |
| `.gitignore`    | Bỏ qua file/thư mục không cần đưa lên Git            |

---

# 4. Yêu cầu Python chi tiết

## 4.1. Class Product

Tạo class `Product` trong file `product.py`.

Class cần có các thuộc tính:

```python
id
name
category
price
quantity
created_at
updated_at
```

Class cần có các method:

```python
is_available()
get_total_value()
to_dict()
from_dict()
display_info()
```

Ý nghĩa:

| Method              | Chức năng                                  |
| ------------------- | ------------------------------------------ |
| `is_available()`    | Trả về `True` nếu số lượng lớn hơn 0       |
| `get_total_value()` | Trả về `price * quantity`                  |
| `to_dict()`         | Chuyển object thành dictionary để lưu JSON |
| `from_dict()`       | Tạo object từ dictionary đọc từ JSON       |
| `display_info()`    | Hiển thị thông tin sản phẩm                |

---

## 4.2. Class Inventory

Tạo class `Inventory` trong file `inventory.py`.

Class này quản lý danh sách sản phẩm.

Thuộc tính chính:

```python
products = []
```

Các method bắt buộc:

```python
add_product()
show_products()
find_product_by_id()
update_quantity()
update_price()
delete_product()
search_product_by_name()
filter_available_products()
sort_products_by_price()
sort_products_by_total_value()
find_most_expensive_product()
show_statistics()
```

---

## 4.3. Sử dụng list comprehension

Bắt buộc dùng list comprehension ở các chức năng:
### Lọc sản phẩm còn hàng

```python
available_products = [product for product in products if product.is_available()]
```

### Tìm sản phẩm theo tên

```python
results = [product for product in products if keyword.lower() in product.name.lower()]
```

---

## 4.4. Sử dụng lambda function

Bắt buộc dùng lambda ở chức năng sắp xếp.

### Sắp xếp theo giá

```python
products.sort(key=lambda product: product.price)
```

### Sắp xếp theo tổng giá trị tồn kho

```python
products.sort(key=lambda product: product.get_total_value())
```

---

## 4.5. Sử dụng module `random`

Khi thêm sản phẩm, cho phép chương trình tự động tạo mã sản phẩm.

Ví dụ:

```text
P3842
P9012
P1205
```

Yêu cầu:

* Mã sản phẩm bắt đầu bằng chữ `P`
* Phần sau là số ngẫu nhiên gồm 4 chữ số
* Không được trùng với mã sản phẩm đã tồn tại

Gợi ý:

```python
import random

product_id = "P" + str(random.randint(1000, 9999))
```

---

## 4.6. Sử dụng module `datetime`

Khi thêm sản phẩm, lưu thời gian tạo:

```python
created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

Khi cập nhật giá hoặc số lượng, cập nhật lại:

```python
updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

---

## 4.7. File input/output với file text

Tạo file `logs.txt`.

Mỗi khi người dùng thực hiện thao tác, chương trình ghi log vào file.

Ví dụ nội dung `logs.txt`:

```text
[2026-06-23 10:15:20] Added product P001 - Laptop
[2026-06-23 10:17:01] Updated quantity of P001 to 5
[2026-06-23 10:20:44] Deleted product P002
```

Yêu cầu:

* Dùng `open()`
* Dùng mode `"a"` để ghi thêm log
* Không ghi đè log cũ

---

## 4.8. JSON handling

Tạo file `products.json` để lưu dữ liệu sản phẩm.

Khi chương trình khởi động:

```text
Đọc dữ liệu từ products.json nếu file tồn tại
```

Khi người dùng thoát chương trình:

```text
Tự động lưu danh sách sản phẩm vào products.json
```

Yêu cầu sử dụng:

```python
import json
```

Ví dụ cấu trúc JSON:

```json
[
  {
    "id": "P001",
    "name": "Laptop",
    "category": "Electronics",
    "price": 1500.0,
    "quantity": 10,
    "created_at": "2026-06-23 10:15:20",
    "updated_at": "2026-06-23 10:15:20"
  }
]
```

---

# 5. Yêu cầu xử lý lỗi

Chương trình phải xử lý các lỗi sau:

* Nhập sai lựa chọn menu
* Nhập giá không phải số
* Nhập số lượng không phải số nguyên
* Giá nhỏ hơn 0
* Số lượng nhỏ hơn 0
* Mã sản phẩm không tồn tại
* File `products.json` chưa tồn tại
* File JSON bị rỗng
* File JSON sai định dạng

Ví dụ:

```python
try:
    price = float(input("Nhập giá sản phẩm: "))
except ValueError:
    print("Giá sản phẩm phải là số.")
```

---

# 6. Yêu cầu Git/GitHub

## 6.1. Tạo `.gitignore`

Tạo file `.gitignore`.

Nội dung gợi ý:

```gitignore
__pycache__/
*.pyc
.env
.venv/
.idea/
```

Commit:

```bash
git add .gitignore
git commit -m "Add gitignore file"
```

---

## 6.2. Branch bắt buộc

Project phải có ít nhất các branch sau:

```text
main
feature-oop
feature-json-storage
feature-search-sort
feature-logging
feature-statistics
```

---

## 6.3. Làm chức năng OOP trên branch riêng

Tạo branch:

```bash
git checkout -b feature-oop
```

Thực hiện:

* Tạo `product.py`
* Tạo class `Product`
* Tạo `inventory.py`
* Tạo class `Inventory`

Commit:

```bash
git add .
git commit -m "Add Product and Inventory classes"
```

Merge vào `main`:

```bash
git checkout main
git merge feature-oop
```

---

## 6.4. Làm chức năng JSON trên branch riêng

Tạo branch:

```bash
git checkout -b feature-json-storage
```

Thực hiện:

* Tạo `storage.py`
* Viết hàm đọc dữ liệu từ `products.json`
* Viết hàm ghi dữ liệu vào `products.json`
* Chương trình tự đọc JSON khi khởi động
* Chương trình tự lưu JSON khi thoát

Commit:

```bash
git add .
git commit -m "Add JSON storage feature"
```

---

## 6.5. Làm chức năng search, filter, sort trên branch riêng

Tạo branch:

```bash
git checkout -b feature-search-sort
```

Thực hiện:

* Tìm sản phẩm theo tên
* Lọc sản phẩm còn hàng bằng list comprehension
* Sắp xếp sản phẩm theo giá bằng lambda
* Sắp xếp sản phẩm theo tổng giá trị tồn kho bằng lambda

Commit:

```bash
git add .
git commit -m "Add search filter and sort features"
```

---

## 6.6. Làm chức năng logging trên branch riêng

Tạo branch:

```bash
git checkout -b feature-logging
```

Thực hiện:

* Tạo `logger.py`
* Ghi log vào `logs.txt`
* Log các thao tác thêm, sửa, xóa sản phẩm
* Log thời gian bằng `datetime`

Commit:

```bash
git add .
git commit -m "Add logging feature"
```

---

## 6.7. Làm chức năng thống kê trên branch riêng

Tạo branch:

```bash
git checkout -b feature-statistics
```

Thực hiện thống kê:

```text
Tổng số loại sản phẩm
Tổng số lượng sản phẩm
Số sản phẩm còn hàng
Số sản phẩm hết hàng
Tổng giá trị kho hàng
Giá trung bình sản phẩm
Sản phẩm có giá cao nhất
```

Yêu cầu:

* Dùng `math` để làm tròn một số giá trị thống kê
* Dùng vòng lặp hoặc list comprehension hợp lý

Commit:

```bash
git add .
git commit -m "Add inventory statistics feature"
```

---


# 8. Yêu cầu xử lý conflict

Tạo và xử lý ít nhất 1 conflict.

Gợi ý:

Trên branch `main`, sửa menu trong `main.py`.

Sau đó trên branch `feature-logging`, cũng sửa cùng phần menu trong `main.py`.

Khi merge:

```bash
git checkout main
git merge feature-logging
```

Nếu xảy ra conflict, mở file bị conflict, sửa lại nội dung, sau đó:

```bash
git add .
git commit -m "Resolve conflict in main menu"
```

---

# 9. Yêu cầu thực hành stash

Tạo một thay đổi chưa commit trong `main.py`, ví dụ sửa text menu.

Kiểm tra:

```bash
git status
```

Lưu tạm thay đổi:

```bash
git stash
```

Chuyển sang branch khác:

```bash
git checkout main
```

Lấy lại thay đổi:

```bash
git stash pop
```

Sau đó commit:

```bash
git add .
git commit -m "Update menu text after stash"
```

---

# 10. Yêu cầu thực hành reset

Tạo một commit thử nghiệm:

```bash
echo "temporary test" > test_reset.txt
git add .
git commit -m "Temporary reset test"
```

Xem lịch sử:

```bash
git log --oneline
```

Thực hiện reset mềm:

```bash
git reset --soft HEAD~1
```

Kiểm tra:

```bash
git status
```

Sau đó commit lại với message phù hợp hơn:

```bash
git commit -m "Add reset practice file"
```

Không bắt buộc dùng `git reset --hard`.

---

# 11. Yêu cầu tạo tag

Sau khi hoàn thành project, tạo tag phiên bản đầu tiên:

```bash
git tag v1.0
git push origin v1.0
```

Kiểm tra:

```bash
git tag
```

---
