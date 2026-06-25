# Ghi nhận thay đổi trong Git

## Mục tiêu

Biết cách kiểm tra trạng thái file, đưa file vào staging area, commit thay đổi và bỏ qua file không cần quản lý bằng `.gitignore`.

## 1. Trạng thái file trong Git

Trong Git, file thường thuộc một trong các trạng thái sau:

- `Untracked`: file mới, Git chưa theo dõi.
- `Modified`: file đã được chỉnh sửa nhưng chưa chuẩn bị commit.
- `Staged`: file đã được đưa vào vùng chuẩn bị commit.
- `Committed`: thay đổi đã được lưu vào lịch sử Git.

Quy trình cơ bản:

```bash
edit file -> git add -> git commit
```

## 2. `git status`

`git status` dùng để xem trạng thái hiện tại của repository.

Ví dụ:

```bash
git status
```

Lệnh này cho biết:

- File nào chưa được Git theo dõi.
- File nào đã chỉnh sửa.
- File nào đã được đưa vào staging area.
- Có thay đổi nào sẵn sàng commit hay chưa.

Có thể dùng dạng ngắn gọn:

```bash
git status -s
```

## 3. `git add`

`git add` dùng để đưa file vào staging area.

Ví dụ:

```bash
git add README.md
```

Hoặc thêm tất cả thay đổi:

```bash
git add .
```

Bản chất của `git add` là chọn nội dung sẽ được đưa vào commit tiếp theo. Nếu sửa file sau khi đã `git add`, cần chạy `git add` lại để cập nhật phiên bản mới nhất vào staging area.

## 4. `git commit`

`git commit` dùng để lưu các thay đổi đang nằm trong staging area vào lịch sử Git.

Ví dụ:

```bash
git commit -m "Add README file"
```

Bản chất của `git commit`:

- Tạo một snapshot mới của dự án.
- Chỉ lưu những thay đổi đã được `git add`.
- Lưu kèm thông điệp commit để mô tả thay đổi.

## 5. `.gitignore`

`.gitignore` là file dùng để khai báo những file hoặc thư mục Git không cần theo dõi.

Thường dùng để bỏ qua:

- File log.
- File tạm.
- Thư mục build.
- File cấu hình cá nhân.
- Thư mục dependency như `node_modules/`.

Ví dụ `.gitignore`:

```gitignore
*.log
node_modules/
dist/
.env
```

Một số quy tắc cơ bản:

- Dòng bắt đầu bằng `#` là ghi chú.
- `*.log` bỏ qua tất cả file có đuôi `.log`.
- `build/` bỏ qua cả thư mục `build`.
- `!file.txt` dùng để không bỏ qua một file cụ thể.

## Kết luận

`git status` giúp kiểm tra trạng thái repository. `git add` chọn thay đổi cho commit tiếp theo. `git commit` lưu thay đổi vào lịch sử Git. `.gitignore` giúp tránh đưa các file không cần thiết vào repository.
