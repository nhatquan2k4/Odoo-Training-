# Rebase trong Git

Nguồn tham khảo: [Pro Git - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

## Mục tiêu

Hiểu `git rebase` là gì, khác gì với `git merge`, cách dùng cơ bản và khi nào không nên rebase.

## 1. Rebase là gì?

`git rebase` là cách đưa các commit của một branch sang một base mới.

Nói đơn giản, rebase lấy các commit trên branch hiện tại và phát lại chúng trên đầu một branch khác.

Ví dụ:

```text
A --- B --- C  main
       \
        D --- E  feature
```

Nếu đang ở branch `feature` và chạy:

```bash
git rebase main
```

Git sẽ lấy commit `D`, `E` và phát lại trên đầu `main`:

```text
A --- B --- C  main
             \
              D' --- E'  feature
```

`D'` và `E'` có nội dung tương tự `D` và `E`, nhưng là commit mới vì lịch sử đã được viết lại.

## 2. Cách dùng rebase cơ bản

Chuyển sang branch cần rebase:

```bash
git switch feature
```

Rebase branch đó lên `main`:

```bash
git rebase main
```

Sau đó có thể merge về `main` bằng fast-forward:

```bash
git switch main
git merge feature
```

## 3. Rebase khác merge như thế nào?

`merge` kết hợp hai branch và thường tạo merge commit nếu hai branch đã tách lịch sử.

Ví dụ:

```bash
git switch main
git merge feature
```

`rebase` không tạo merge commit trong trường hợp cơ bản. Nó viết lại lịch sử của branch hiện tại để các commit trông như được tạo sau commit mới nhất của branch base.

So sánh nhanh:

| Tiêu chí | Merge | Rebase |
| --- | --- | --- |
| Cách hoạt động | Gộp hai nhánh lại | Phát lại commit lên base mới |
| Lịch sử commit | Giữ đúng lịch sử phân nhánh | Lịch sử thẳng, dễ đọc hơn |
| Merge commit | Có thể tạo merge commit | Thường không tạo merge commit |
| Có viết lại lịch sử không? | Không | Có |

## 4. Vì sao dùng rebase?

Rebase thường được dùng để làm lịch sử commit gọn hơn trước khi merge code.

Lợi ích:

- Lịch sử commit tuyến tính, dễ đọc hơn.
- Tránh nhiều merge commit không cần thiết.
- Giúp branch feature cập nhật theo branch chính trước khi tạo Pull Request hoặc Merge Request.

Ví dụ cập nhật branch feature theo `main`:

```bash
git switch feature-login
git fetch origin
git rebase origin/main
```

## 5. Khi rebase bị conflict

Nếu có conflict trong quá trình rebase, Git sẽ dừng lại để bạn sửa.

Quy trình xử lý:

```bash
git status
```

Sửa file bị conflict, sau đó:

```bash
git add file_name
git rebase --continue
```

Nếu muốn hủy rebase và quay lại trạng thái trước đó:

```bash
git rebase --abort
```

## 6. `git pull --rebase`

`git pull` thông thường thường tương đương:

```bash
git fetch
git merge
```

Nếu dùng:

```bash
git pull --rebase
```

Git sẽ fetch thay đổi mới từ remote, rồi rebase commit local của bạn lên trên commit mới từ remote.

Cách này giúp tránh tạo merge commit khi chỉ muốn cập nhật code mới nhất từ remote.

## 7. Lưu ý quan trọng khi dùng rebase

Không nên rebase các commit đã push lên remote và đã có người khác dựa vào để làm việc.

Lý do:

- Rebase tạo commit mới và thay đổi lịch sử commit.
- Nếu người khác đã pull commit cũ về máy, lịch sử giữa các máy có thể bị lệch.
- Khi push lại sau rebase, thường phải dùng force push, dễ gây rối cho team.

Nguyên tắc an toàn:

- Có thể rebase commit local chưa push.
- Có thể rebase branch cá nhân nếu chưa ai dùng branch đó.
- Không rebase branch chung như `main`, `develop` hoặc branch nhiều người đang làm nếu chưa thống nhất với team.

## Kết luận

`git rebase` dùng để phát lại commit của branch hiện tại lên một base mới, giúp lịch sử commit thẳng và dễ đọc hơn. Khác với merge, rebase có viết lại lịch sử commit, nên cần dùng cẩn thận. Quy tắc quan trọng là không rebase commit đã public hoặc commit mà người khác đang dựa vào.
