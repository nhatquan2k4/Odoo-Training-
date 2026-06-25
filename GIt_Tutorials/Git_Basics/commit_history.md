# Xem lịch sử commit
    
## Mục tiêu

Biết cách xem lịch sử commit của repository bằng `git log`.

## 1. `git log` là gì?

`git log` là lệnh dùng để xem lịch sử commit trong repository.

Ví dụ:

```bash
git log
```

Mặc định, `git log` hiển thị các commit theo thứ tự mới nhất trước.

Thông tin thường thấy trong mỗi commit:

- Commit hash.
- Tên và email của author.
- Thời gian commit.
- Commit message.

## 2. Xem lịch sử ngắn gọn

Dùng `--oneline` để mỗi commit hiển thị trên một dòng:

```bash
git log --oneline
```

Cách này phù hợp khi muốn xem nhanh danh sách commit.

## 3. Xem thay đổi trong từng commit

Dùng `-p` hoặc `--patch` để xem chi tiết nội dung thay đổi trong mỗi commit:

```bash
git log -p
```

Có thể giới hạn số commit cần xem:

```bash
git log -p -2
```

Lệnh trên chỉ xem chi tiết 2 commit gần nhất.

## 4. Xem thống kê thay đổi

Dùng `--stat` để xem file nào thay đổi và số dòng được thêm hoặc xóa:

```bash
git log --stat
```

## 5. Một số cách lọc lịch sử commit

Xem số lượng commit gần nhất:

```bash
git log -3
```

Xem commit theo thời gian:

```bash
git log --since="2 weeks ago"
```

Xem commit theo author:

```bash
git log --author="Quan"
```

Xem commit liên quan đến một file:

```bash
git log -- path/to/file
```

## Kết luận

`git log` giúp xem lại lịch sử thay đổi của repository. Đây là lệnh quan trọng để biết dự án đã thay đổi như thế nào, ai đã commit và nội dung chính của từng commit là gì.
