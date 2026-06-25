# Quản lý branch trong project thực tế

## Mục tiêu

Hiểu cách dùng và quản lý branch khi làm việc trong một project thực tế.

## 1. Vì sao cần quản lý branch?

Trong project thực tế, nhiều người có thể cùng làm việc trên các tính năng hoặc lỗi khác nhau.

Branch giúp tách từng phần công việc riêng ra khỏi branch chính, ví dụ:

- `main`: chứa code ổn định.
- `feature-login`: phát triển chức năng đăng nhập.
- `fix-user-error`: sửa lỗi liên quan đến user.
- `hotfix-payment`: sửa lỗi khẩn cấp.

Sau khi công việc hoàn tất, branch thường được merge về branch chính rồi xóa đi để repository gọn hơn.

## 2. Xem danh sách branch

Dùng lệnh:

```bash
git branch
```

Git sẽ hiển thị danh sách branch local.

Branch có dấu `*` là branch hiện tại:

```text
  feature-login
* main
  testing
```

## 3. Xem commit cuối của từng branch

Dùng:

```bash
git branch -v
```

Lệnh này giúp xem mỗi branch đang trỏ tới commit nào và commit message gần nhất là gì.

## 4. Xem branch đã merge

Dùng:

```bash
git branch --merged
```

Lệnh này hiển thị các branch đã được merge vào branch hiện tại.

Những branch đã merge thường có thể xóa an toàn:

```bash
git branch -d feature-login
```

## 5. Xem branch chưa merge

Dùng:

```bash
git branch --no-merged
```

Lệnh này hiển thị các branch còn thay đổi chưa được merge vào branch hiện tại.

Nếu xóa branch chưa merge bằng `-d`, Git sẽ cảnh báo và không cho xóa để tránh mất code:

```bash
git branch -d testing
```

Nếu chắc chắn muốn xóa dù chưa merge, dùng:

```bash
git branch -D testing
```

Cần cẩn thận với `-D` vì có thể làm mất công việc chưa được merge.

## 6. Đổi tên branch

Đổi tên branch local:

```bash
git branch --move old-name new-name
```

Ví dụ:

```bash
git branch --move feature-login feature-auth
```

Nếu branch đã được push lên remote, cần push tên mới:

```bash
git push --set-upstream origin feature-auth
```

Sau đó có thể xóa branch cũ trên remote:

```bash
git push origin --delete feature-login
```

Không nên tự ý đổi tên các branch quan trọng như `main` hoặc branch đang có nhiều người cùng dùng nếu chưa thống nhất với team.

## 7. Quy trình dùng branch trong project

Một quy trình cơ bản thường gặp:

```bash
git switch main
git pull origin main
git switch -c feature-login
```

Sau khi làm xong:

```bash
git add .
git commit -m "Add login feature"
git switch main
git merge feature-login
git branch -d feature-login
```

Ý nghĩa:

- Cập nhật branch chính.
- Tạo branch riêng cho công việc mới.
- Commit thay đổi trên branch đó.
- Merge về branch chính khi hoàn tất.
- Xóa branch sau khi không còn cần dùng.

## Kết luận

Quản lý branch giúp project rõ ràng và dễ phối hợp hơn. `git branch` dùng để xem branch, `git branch -v` xem commit cuối, `--merged` kiểm tra branch đã merge, `--no-merged` kiểm tra branch còn việc chưa merge, và `-d` dùng để xóa branch đã hoàn tất.
