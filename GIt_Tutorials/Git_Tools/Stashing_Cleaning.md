# Stashing và Cleaning trong Git

## Mục tiêu

Biết dùng `git stash` khi đang sửa code nhưng cần chuyển branch hoặc pull code, và biết dùng `git clean` để dọn file chưa được Git theo dõi.

## 1. Vấn đề thường gặp

Khi đang sửa code dở, bạn có thể gặp các tình huống:

- Cần chuyển sang branch khác để sửa lỗi gấp.
- Cần `git pull` code mới nhưng working directory đang có thay đổi.
- Chưa muốn commit vì code chưa hoàn thiện.

Lúc này có thể dùng `git stash` để cất tạm thay đổi.

## 2. `git stash` là gì?

`git stash` dùng để lưu tạm các thay đổi chưa commit, sau đó đưa working directory về trạng thái sạch.

Ví dụ:

```bash
git stash
```

Hoặc dùng dạng rõ hơn:

```bash
git stash push
```

Bản chất:

- Lưu tạm thay đổi đang làm vào stash stack.
- Làm working directory sạch để có thể chuyển branch hoặc pull code.
- Có thể lấy lại thay đổi sau bằng `git stash apply` hoặc `git stash pop`.

## 3. Dùng stash khi cần chuyển branch

Kiểm tra trạng thái:

```bash
git status
```

Cất tạm thay đổi:

```bash
git stash push -m "WIP login feature"
```

Chuyển branch:

```bash
git switch main
```

Sau khi xong việc, quay lại branch cũ và lấy lại thay đổi:

```bash
git switch feature-login
git stash pop
```

## 4. Dùng stash khi cần pull code

Khi đang sửa dở nhưng cần cập nhật code mới:

```bash
git stash push -m "WIP before pull"
git pull origin main
git stash pop
```

Ý nghĩa:

- `git stash push`: cất tạm thay đổi local.
- `git pull`: lấy code mới từ remote.
- `git stash pop`: lấy lại thay đổi đã stash.

Nếu khi `stash pop` có conflict, cần sửa conflict như khi merge code.

## 5. Xem danh sách stash

Xem các stash đang có:

```bash
git stash list
```

Ví dụ:

```text
stash@{0}: On feature-login: WIP login feature
stash@{1}: On main: WIP before pull
```

## 6. Apply và pop khác nhau thế nào?

Lấy lại stash nhưng vẫn giữ stash trong danh sách:

```bash
git stash apply
```

Lấy lại stash và xóa stash đó khỏi danh sách:

```bash
git stash pop
```

Tóm lại:

- `apply`: áp dụng lại thay đổi, stash vẫn còn.
- `pop`: áp dụng lại thay đổi, sau đó xóa stash.

## 7. Stash cả file untracked

Mặc định, `git stash` chỉ lưu file tracked đã thay đổi.

Nếu có file mới chưa được Git theo dõi, dùng:

```bash
git stash -u
```

Hoặc:

```bash
git stash push --include-untracked
```

Lệnh này sẽ stash cả file modified, staged và untracked.

## 8. Tạo branch từ stash

Nếu muốn lấy stash ra làm tiếp trên branch mới:

```bash
git stash branch new-branch-name
```

Git sẽ tạo branch mới, apply stash vào branch đó và xóa stash nếu apply thành công.

## 9. Xóa stash

Xóa một stash cụ thể:

```bash
git stash drop stash@{0}
```

Xóa toàn bộ stash:

```bash
git stash clear
```

Cần cẩn thận với `clear` vì sẽ xóa tất cả stash.

## 10. `git clean` là gì?

`git clean` dùng để xóa các file untracked trong working directory.

Ví dụ file build, file tạm hoặc thư mục sinh ra khi chạy tool.

Trước khi xóa thật, luôn kiểm tra trước:

```bash
git clean -n -d
```

Nếu kết quả đúng như mong muốn, mới xóa:

```bash
git clean -f -d
```

Ý nghĩa:

- `-n`: dry-run, chỉ hiển thị file sẽ bị xóa.
- `-f`: force, xóa thật.
- `-d`: xóa cả thư mục untracked.

Lưu ý: `git clean` có thể làm mất file chưa được Git theo dõi, nên phải dùng cẩn thận.

## Kết luận

Khi đang sửa code nhưng cần chuyển branch hoặc pull code, dùng `git stash` để cất tạm thay đổi và lấy lại sau. `git stash pop` lấy lại thay đổi rồi xóa stash, còn `git stash apply` lấy lại nhưng vẫn giữ stash. `git clean` dùng để dọn file untracked, nhưng nên kiểm tra bằng `git clean -n -d` trước khi xóa thật.
