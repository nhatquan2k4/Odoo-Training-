# Tạo branch, chuyển branch và merge code

## Mục tiêu

Biết cách tạo branch, chuyển branch và merge code từ branch này sang branch khác.

## 1. Tạo branch

Branch giúp tách công việc ra khỏi nhánh chính để phát triển tính năng hoặc sửa lỗi riêng.

Tạo branch mới:

```bash
git branch feature-login
```

Lệnh này chỉ tạo branch mới, chưa chuyển sang branch đó.

Tạo branch mới và chuyển sang luôn:

```bash
git switch -c feature-login
```

Tương đương cách cũ:

```bash
git checkout -b feature-login
```

## 2. Chuyển branch

Chuyển sang branch khác:

```bash
git switch main
```

Hoặc:

```bash
git switch feature-login
```

Cách cũ vẫn dùng được:

```bash
git checkout feature-login
```

Lưu ý: trước khi chuyển branch, nên commit hoặc lưu lại các thay đổi đang làm. Nếu thay đổi chưa commit bị xung đột với branch muốn chuyển sang, Git có thể không cho chuyển branch.

## 3. Làm việc trên branch

Sau khi chuyển sang branch mới, có thể sửa code và commit như bình thường:

```bash
git add .
git commit -m "Add login feature"
```

Commit mới sẽ thuộc về branch hiện tại.

## 4. Merge code

`git merge` dùng để nhập thay đổi từ branch khác vào branch hiện tại.

Ví dụ muốn merge `feature-login` vào `main`:

```bash
git switch main
git merge feature-login
```

Ý nghĩa:

- Chuyển về branch `main`.
- Lấy thay đổi từ `feature-login` nhập vào `main`.

## 5. Fast-forward merge

Fast-forward xảy ra khi branch hiện tại chưa có commit mới nào khác kể từ lúc tách branch.

Khi đó Git chỉ cần di chuyển con trỏ branch tiến lên commit mới nhất.

Ví dụ:

```text
A --- B  main
       \
        C --- D  feature-login
```

Sau khi merge, `main` có thể trỏ thẳng tới `D`.

## 6. Three-way merge

Three-way merge xảy ra khi hai branch đều có commit mới riêng.

Ví dụ:

```text
A --- B --- E  main
       \
        C --- D  feature-login
```

Khi merge `feature-login` vào `main`, Git phải kết hợp thay đổi từ hai branch và tạo một merge commit mới.

## 7. Merge conflict

Merge conflict xảy ra khi hai branch cùng sửa một phần giống nhau trong cùng một file, khiến Git không tự quyết định được nên giữ nội dung nào.

Khi bị conflict, quy trình cơ bản là:

```bash
git status
```

Mở file bị conflict, sửa nội dung cho đúng, sau đó:

```bash
git add file_name
git commit
```

`git add` dùng để đánh dấu conflict đã được xử lý.

## 8. Xóa branch sau khi merge

Sau khi branch đã được merge và không còn cần nữa, có thể xóa:

```bash
git branch -d feature-login
```

Lệnh này chỉ xóa branch local, không xóa lịch sử commit đã được merge.

## Kết luận

Quy trình cơ bản khi làm việc với branch là tạo branch, chuyển sang branch đó, commit thay đổi, quay về branch chính và merge code. `git switch` dùng để chuyển branch, `git switch -c` dùng để tạo branch mới và chuyển sang luôn, còn `git merge` dùng để nhập thay đổi từ branch khác vào branch hiện tại.
