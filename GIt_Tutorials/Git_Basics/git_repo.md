# Tạo và tải Git Repository

## Mục tiêu

Biết cách tạo repository bằng `git init`, tải repository bằng `git clone`, và hiểu bản chất của hai lệnh này.

## Git Repository là gì?

Git repository là thư mục dự án được Git quản lý. Bên trong repository có thư mục `.git`, nơi Git lưu thông tin lịch sử, cấu hình và dữ liệu cần thiết để theo dõi thay đổi của dự án.

Có hai cách cơ bản để có một Git repository trên máy cá nhân:

- Tạo repository mới từ một thư mục có sẵn bằng `git init`.
- Tải một repository đã tồn tại từ nơi khác bằng `git clone`.

## 1. Tạo repository bằng `git init`

`git init` dùng để biến một thư mục bình thường thành Git repository.

Ví dụ:

```bash
cd my_project
git init
```

Sau khi chạy lệnh này, Git sẽ tạo thư mục `.git` bên trong `my_project`.

Bản chất của `git init`:

- Khởi tạo Git repository mới trong thư mục hiện tại.
- Tạo thư mục `.git` để Git lưu dữ liệu quản lý phiên bản.
- Chưa tự động theo dõi các file có sẵn trong thư mục.

Nếu muốn Git bắt đầu theo dõi file, cần dùng:

```bash
git add .
git commit -m "Initial commit"
```

## 2. Tải repository bằng `git clone`

`git clone` dùng để sao chép một repository đã tồn tại từ remote về máy cá nhân.

Ví dụ:

```bash
git clone https://github.com/user/project.git
```

Lệnh này sẽ tạo một thư mục mới, tải dữ liệu của repository về và chuẩn bị sẵn project để làm việc.

Bản chất của `git clone`:

- Sao chép repository từ remote về máy cá nhân.
- Tải gần như toàn bộ lịch sử thay đổi của dự án.
- Tự động tạo thư mục `.git`.
- Tự động checkout phiên bản mới nhất để có thể làm việc ngay.
- Tự động liên kết repository local với remote ban đầu.

Có thể đặt tên thư mục khi clone:

```bash
git clone https://github.com/user/project.git my_project
```

## Kết luận

`git init` dùng để bắt đầu quản lý một thư mục bằng Git. `git clone` dùng để tải một repository đã tồn tại về máy. Cả hai cách đều tạo ra một Git repository local để có thể bắt đầu làm việc.
