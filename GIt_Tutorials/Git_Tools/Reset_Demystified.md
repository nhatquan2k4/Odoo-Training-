# Git Reset Demystified

## Mục tiêu

Hiểu `git reset`, staging area và commit. Đây là phần quan trọng vì `reset` có thể thay đổi lịch sử commit, staging area và cả file trong working directory.

## 1. Ba vùng quan trọng trong Git

Để hiểu `git reset`, cần hiểu ba vùng chính:

```text
HEAD -> Staging Area (Index) -> Working Directory
```

### HEAD

`HEAD` đại diện cho commit hiện tại.

Thông thường, `HEAD` trỏ tới branch hiện tại, còn branch đó trỏ tới commit mới nhất.

Ví dụ:

```text
A --- B --- C  main
              ^
             HEAD
```

Ở đây, `HEAD` đang ở commit `C`.

### Staging Area

Staging Area, hay Index, là vùng chuẩn bị cho commit tiếp theo.

Khi chạy:

```bash
git add file.txt
```

Git đưa nội dung của `file.txt` vào staging area.

Khi chạy:

```bash
git commit
```

Git lấy nội dung trong staging area để tạo commit mới.

### Working Directory

Working Directory là thư mục làm việc thực tế trên máy, nơi bạn chỉnh sửa file.

Khi sửa code trong editor, thay đổi đầu tiên nằm ở working directory.

## 2. Quy trình commit cơ bản

Quy trình thông thường:

```text
Working Directory -> git add -> Staging Area -> git commit -> HEAD
```

Ví dụ:

```bash
echo "hello" > file.txt
git add file.txt
git commit -m "Add file"
```

Ý nghĩa:

- Sửa file: thay đổi nằm ở working directory.
- `git add`: đưa thay đổi vào staging area.
- `git commit`: lưu staging area thành commit mới.

## 3. `git reset` là gì?

`git reset` dùng để đưa Git về một trạng thái trước đó.

Tùy cách dùng, `reset` có thể tác động đến:

- `HEAD`: commit hiện tại.
- Staging area: vùng chuẩn bị commit.
- Working directory: file thực tế đang sửa.

Git reset xử lý theo thứ tự:

1. Di chuyển branch mà `HEAD` đang trỏ tới.
2. Cập nhật staging area.
3. Cập nhật working directory.

Ba chế độ reset khác nhau ở điểm dừng.

## 4. `git reset --soft`

`--soft` chỉ di chuyển `HEAD`, không thay đổi staging area và working directory.

Ví dụ:

```bash
git reset --soft HEAD~1
```

Ý nghĩa:

- Hủy commit gần nhất.
- Thay đổi của commit đó vẫn nằm trong staging area.
- File trong working directory vẫn giữ nguyên.

Dùng khi muốn sửa lại commit gần nhất nhưng vẫn giữ thay đổi đã staged.

Ví dụ thường gặp:

```bash
git reset --soft HEAD~1
git commit -m "New commit message"
```

## 5. `git reset --mixed`

`--mixed` là chế độ mặc định của `git reset`.

Ví dụ:

```bash
git reset HEAD~1
```

Tương đương:

```bash
git reset --mixed HEAD~1
```

Ý nghĩa:

- Hủy commit gần nhất.
- Đưa thay đổi ra khỏi staging area.
- File trong working directory vẫn giữ nguyên.

Dùng khi muốn hủy commit và hủy luôn trạng thái staged, nhưng vẫn giữ code đã sửa.

## 6. `git reset --hard`

`--hard` di chuyển `HEAD`, cập nhật staging area và cập nhật luôn working directory.

Ví dụ:

```bash
git reset --hard HEAD~1
```

Ý nghĩa:

- Hủy commit gần nhất.
- Xóa thay đổi khỏi staging area.
- Ghi đè working directory theo commit được reset về.

Lệnh này nguy hiểm vì có thể làm mất thay đổi chưa commit.

Chỉ dùng `--hard` khi chắc chắn không cần giữ các thay đổi hiện tại.

## 7. So sánh `soft`, `mixed`, `hard`

| Lệnh | HEAD | Staging Area | Working Directory |
| --- | --- | --- | --- |
| `git reset --soft HEAD~1` | Lùi commit | Giữ nguyên | Giữ nguyên |
| `git reset --mixed HEAD~1` | Lùi commit | Reset theo HEAD mới | Giữ nguyên |
| `git reset --hard HEAD~1` | Lùi commit | Reset theo HEAD mới | Reset theo HEAD mới |

Nói ngắn gọn:

- `soft`: hủy commit, giữ staged.
- `mixed`: hủy commit, bỏ staged, giữ code.
- `hard`: hủy commit, bỏ staged, bỏ luôn code đang sửa.

## 8. Reset file khỏi staging area

Nếu đã `git add` nhầm một file, có thể bỏ file khỏi staging area:

```bash
git reset file.txt
```

Hoặc cách hiện đại, rõ nghĩa hơn:

```bash
git restore --staged file.txt
```

Bản chất:

- File không còn nằm trong staging area.
- Nội dung file trong working directory vẫn được giữ.
- Thay đổi chưa bị mất.

Ví dụ:

```bash
git add file.txt
git reset file.txt
```

Sau lệnh trên, `file.txt` vẫn còn thay đổi, nhưng chưa được staged.

## 9. Reset về một commit cụ thể

Có thể reset về commit cụ thể bằng commit hash:

```bash
git reset --mixed abc123
```

Hoặc:

```bash
git reset --hard abc123
```

Cần kiểm tra lịch sử trước:

```bash
git log --oneline
```

Lưu ý: nếu reset các commit đã push lên remote, lịch sử local sẽ khác remote. Khi làm việc nhóm, không nên reset lịch sử đã public nếu chưa thống nhất với team.

## 10. Khi nào dùng reset?

Dùng `git reset --soft` khi:

- Commit nhầm message.
- Muốn gộp lại commit.
- Muốn commit lại nhưng giữ staged changes.

Dùng `git reset --mixed` khi:

- Commit nhầm.
- Muốn quay lại trước commit nhưng vẫn giữ code.
- Muốn bỏ staged changes.

Dùng `git reset --hard` khi:

- Muốn bỏ hoàn toàn thay đổi hiện tại.
- Muốn đưa branch về đúng trạng thái của một commit.
- Chắc chắn không cần giữ code chưa commit.

## 11. Reset và restore

Trong Git hiện đại, một số thao tác trước đây hay dùng `reset` có thể dùng `restore` cho dễ hiểu hơn.

Bỏ file khỏi staging area:

```bash
git restore --staged file.txt
```

Hủy thay đổi trong working directory:

```bash
git restore file.txt
```

`reset` vẫn rất quan trọng để hiểu Git, nhưng khi chỉ thao tác với file, `restore` thường rõ nghĩa hơn.

## 12. Lưu ý an toàn

Trước khi reset, nên kiểm tra:

```bash
git status
git log --oneline
```

Nếu chưa chắc có cần giữ thay đổi hay không, hãy stash trước:

```bash
git stash push -m "backup before reset"
```

Tránh dùng `git reset --hard` nếu chưa hiểu rõ thay đổi nào sẽ bị mất.

## Kết luận

`git reset` thao tác lên ba vùng quan trọng của Git: `HEAD`, staging area và working directory. `--soft` chỉ di chuyển `HEAD`, `--mixed` di chuyển `HEAD` và reset staging area, còn `--hard` reset cả working directory. Muốn dùng reset an toàn, cần luôn kiểm tra `git status`, hiểu code đang nằm ở vùng nào và đặc biệt cẩn thận với `git reset --hard`.
