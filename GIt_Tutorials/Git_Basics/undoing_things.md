# Sửa sai trong Git

## Mục tiêu

Biết cách sửa commit gần nhất, bỏ file khỏi staging area và hủy thay đổi chưa cần giữ lại.

## 1. Kiểm tra trước khi sửa

Trước khi hủy hoặc sửa thay đổi, nên dùng:

```bash
git status
```

`git status` giúp biết file đang ở trạng thái nào và thường gợi ý lệnh cần dùng để sửa sai.

## 2. Sửa commit gần nhất

Dùng `git commit --amend` khi muốn sửa commit vừa tạo.

Ví dụ sửa commit vì quên thêm file:

```bash
git add forgotten_file
git commit --amend
```

Bản chất:

- Git không tạo thêm một commit mới riêng biệt.
- Commit gần nhất sẽ được thay thế bằng commit mới.
- Có thể dùng để sửa nội dung commit hoặc sửa commit message.

Lưu ý: chỉ nên dùng `--amend` với commit còn ở máy local, chưa push lên remote.

## 3. Bỏ file khỏi staging area

Nếu đã chạy `git add` nhầm, dùng:

```bash
git restore --staged file_name
```

Ví dụ:

```bash
git restore --staged README.md
```

Bản chất:

- File được đưa ra khỏi staging area.
- Nội dung file trong working directory vẫn được giữ nguyên.
- File vẫn còn thay đổi, chỉ là chưa được chuẩn bị để commit.

## 4. Hủy thay đổi trong file

Nếu muốn bỏ toàn bộ thay đổi chưa commit của một file, dùng:

```bash
git restore file_name
```

Ví dụ:

```bash
git restore README.md
```

Bản chất:

- Git khôi phục file về trạng thái đã commit gần nhất.
- Các thay đổi local chưa commit trong file đó sẽ bị mất.

Cần cẩn thận với lệnh này vì thay đổi chưa commit thường không thể khôi phục lại.

## 5. Quy trình thường gặp

Xem trạng thái:

```bash
git status
```

Bỏ staged nếu add nhầm:

```bash
git restore --staged file_name
```

Hủy thay đổi nếu không muốn giữ:

```bash
git restore file_name
```

Sửa commit gần nhất:

```bash
git commit --amend
```

## Kết luận

Git hỗ trợ nhiều cách sửa sai. `git commit --amend` dùng để sửa commit gần nhất. `git restore --staged` dùng để bỏ file khỏi staging area. `git restore` dùng để hủy thay đổi trong working directory, nhưng cần dùng cẩn thận vì có thể làm mất thay đổi chưa commit.
