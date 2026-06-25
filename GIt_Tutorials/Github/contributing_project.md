# Contributing to a Project trên GitHub

## Mục tiêu

Hiểu quy trình đóng góp code vào project trên GitHub bằng các bước quan trọng: `fork`, `clone`, tạo `branch`, `push` và tạo `Pull Request`.

## 1. Tổng quan workflow

Khi không có quyền push trực tiếp vào repository gốc, ta thường dùng workflow:

```text
Fork -> Clone -> Branch -> Commit -> Push -> Pull Request
```

Ý nghĩa:

- `Fork`: tạo bản copy của repository về tài khoản GitHub của mình.
- `Clone`: tải repository fork về máy cá nhân.
- `Branch`: tạo nhánh riêng để làm task.
- `Commit`: lưu thay đổi vào lịch sử Git.
- `Push`: đẩy branch lên GitHub.
- `Pull Request`: gửi yêu cầu merge code vào repository gốc.

## 2. Fork project

Fork là thao tác tạo một bản copy của repository gốc sang tài khoản GitHub của bạn.

Ví dụ:

```text
Original repository: github.com/original/project
Your fork:           github.com/your-name/project
```

Bản chất:

- Repository fork thuộc tài khoản của bạn.
- Bạn có quyền push lên fork của mình.
- Repository gốc không bị thay đổi khi bạn push lên fork.
- Muốn đóng góp ngược lại repository gốc, cần tạo Pull Request.

Fork thường dùng trong open source hoặc project mà bạn không có quyền push trực tiếp.

## 3. Clone fork về máy

Sau khi fork, clone repository của bạn về máy:

```bash
git clone https://github.com/your-name/project.git
cd project
```

Hoặc dùng SSH:

```bash
git clone git@github.com:your-name/project.git
cd project
```

Sau khi clone, remote `origin` thường trỏ tới fork của bạn:

```bash
git remote -v
```

Ví dụ:

```text
origin  https://github.com/your-name/project.git (fetch)
origin  https://github.com/your-name/project.git (push)
```

## 4. Thêm remote upstream

`upstream` thường dùng để trỏ tới repository gốc.

```bash
git remote add upstream https://github.com/original/project.git
```

Kiểm tra lại:

```bash
git remote -v
```

Khi đó thường có:

```text
origin    repository fork của bạn
upstream  repository gốc
```

Ý nghĩa:

- `origin`: nơi bạn push code lên.
- `upstream`: nơi bạn lấy code mới nhất từ project gốc.

## 5. Tạo branch riêng cho task

Không nên làm trực tiếp trên `main`. Nên tạo branch riêng cho từng task:

```bash
git switch -c feature-login
```

Ví dụ tên branch:

```text
feature/login
fix/user-error
docs/update-readme
```

Branch riêng giúp thay đổi rõ ràng, dễ review và dễ quản lý Pull Request.

## 6. Commit thay đổi

Sau khi sửa code, kiểm tra trạng thái:

```bash
git status
git diff
```

Thêm file vào staging area:

```bash
git add .
```

Commit:

```bash
git commit -m "Add login feature"
```

Commit message nên ngắn gọn, mô tả đúng thay đổi.

## 7. Push branch lên GitHub

Đẩy branch lên fork của bạn:

```bash
git push origin feature-login
```

Nếu muốn thiết lập upstream cho branch:

```bash
git push -u origin feature-login
```

Sau khi push, branch sẽ xuất hiện trên GitHub trong repository fork của bạn.

## 8. Tạo Pull Request

Pull Request là yêu cầu đề xuất merge thay đổi từ branch của bạn vào repository gốc.

Thông thường:

```text
base repository: original/project
base branch:     main
head repository: your-name/project
compare branch:  feature-login
```

Khi tạo Pull Request, nên viết:

- Tiêu đề rõ ràng.
- Mô tả thay đổi đã làm.
- Lý do cần thay đổi.
- Cách test nếu có.
- Issue liên quan nếu có.

Pull Request giúp maintainer review code, comment, yêu cầu sửa hoặc merge vào project.

## 9. Cập nhật Pull Request sau review

Nếu reviewer yêu cầu sửa, chỉ cần tiếp tục commit trên cùng branch và push lại:

```bash
git add .
git commit -m "Update login validation"
git push origin feature-login
```

Pull Request sẽ tự động cập nhật theo commit mới trên branch đó.

## 10. Đồng bộ fork với repository gốc

Trước khi làm task mới hoặc trước khi cập nhật Pull Request, nên lấy code mới nhất từ repository gốc.

```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

Ý nghĩa:

- `git fetch upstream`: lấy code mới từ repository gốc.
- `git merge upstream/main`: nhập thay đổi mới vào `main` local.
- `git push origin main`: cập nhật `main` trên fork của bạn.

Sau đó tạo branch mới từ `main` đã cập nhật:

```bash
git switch -c new-feature
```

## 11. Workflow đầy đủ

Ví dụ workflow thường dùng:

```bash
git clone https://github.com/your-name/project.git
cd project
git remote add upstream https://github.com/original/project.git

git switch main
git fetch upstream
git merge upstream/main

git switch -c feature-login
# sửa code
git add .
git commit -m "Add login feature"
git push -u origin feature-login
```

Sau đó lên GitHub tạo Pull Request từ `your-name:feature-login` vào `original:main`.

## 12. Lưu ý quan trọng

- Mỗi task nên có một branch riêng.
- Không nên làm nhiều tính năng không liên quan trong cùng một Pull Request.
- Luôn đọc hướng dẫn đóng góp của project nếu có file `CONTRIBUTING.md`.
- Nên cập nhật code mới nhất từ `upstream` trước khi bắt đầu task.
- Sau khi Pull Request được merge, có thể xóa branch đã dùng.

## Kết luận

Workflow đóng góp quan trọng trên GitHub là `fork`, `clone`, tạo `branch`, `commit`, `push` và tạo `Pull Request`. Fork giúp bạn có bản copy riêng để push code. Pull Request giúp gửi thay đổi về repository gốc để review và merge. Đây là quy trình rất phổ biến khi làm việc với open source hoặc project có review code.
