# Remote Branch trong Git

## Mục tiêu

Hiểu `origin/main`, remote branch, remote-tracking branch, tracking branch và cách push/pull branch.

## 1. Remote branch là gì?

Remote branch là branch nằm trên remote repository, ví dụ trên GitHub hoặc GitLab.

Ví dụ:

- Local branch: `main`, `feature-login`.
- Remote branch: branch `main`, `feature-login` nằm trên GitHub/GitLab.

Local branch không tự động đồng bộ với remote branch. Muốn chia sẻ branch local lên remote, cần dùng `git push`.

## 2. `origin/main` là gì?

`origin/main` là remote-tracking branch.

Nó là con trỏ local đại diện cho trạng thái của branch `main` trên remote `origin` tại lần gần nhất bạn fetch hoặc pull.

Trong đó:

- `origin`: tên remote mặc định khi clone repository.
- `main`: tên branch trên remote.
- `origin/main`: bản ghi local cho biết remote `origin` đang có branch `main` ở commit nào.

Lưu ý: `origin` không phải tên đặc biệt bắt buộc. Nó chỉ là tên mặc định Git tạo khi dùng `git clone`.

## 3. Remote-tracking branch là gì?

Remote-tracking branch là branch local dùng để theo dõi trạng thái branch trên remote.

Ví dụ:

```text
origin/main
origin/feature-login
origin/fix-payment
```

Đặc điểm:

- Bạn không trực tiếp commit lên `origin/main`.
- Git tự cập nhật nó khi chạy `git fetch` hoặc `git pull`.
- Nó cho biết lần gần nhất bạn kết nối remote thì branch trên remote đang ở đâu.

Ví dụ cập nhật remote-tracking branch:

```bash
git fetch origin
```

Sau lệnh này, `origin/main` sẽ được cập nhật theo trạng thái mới nhất trên remote.

## 4. Tracking branch là gì?

Tracking branch là local branch được liên kết với một branch trên remote.

Ví dụ:

```text
main -> origin/main
feature-login -> origin/feature-login
```

Khi branch local có tracking branch, Git biết branch đó nên pull từ đâu và push lên đâu.

Kiểm tra branch đang tracking remote nào:

```bash
git branch -vv
```

Ví dụ kết quả:

```text
* main  abc123 [origin/main] Update README
```

Nghĩa là branch `main` local đang tracking `origin/main`.

## 5. Tạo local branch từ remote branch

Nếu remote có branch `origin/feature-login`, có thể tạo local branch để làm việc:

```bash
git switch -c feature-login origin/feature-login
```

Hoặc với Git cũ:

```bash
git checkout -b feature-login origin/feature-login
```

Sau đó bạn có branch local `feature-login` để chỉnh sửa và commit.

## 6. Push branch lên remote

Push branch local lên remote:

```bash
git push origin feature-login
```

Nếu muốn thiết lập tracking branch ngay khi push lần đầu:

```bash
git push -u origin feature-login
```

Sau khi có upstream/tracking branch, những lần sau có thể dùng ngắn gọn:

```bash
git push
```

## 7. Pull branch từ remote

Khi branch local đã tracking remote branch, có thể cập nhật bằng:

```bash
git pull
```

Bản chất của `git pull` thường là:

```bash
git fetch
git merge
```

Nếu muốn chỉ rõ remote và branch:

```bash
git pull origin main
```

Lệnh này lấy thay đổi từ `origin/main` và merge vào branch hiện tại.

## 8. Fetch khác pull như thế nào?

`git fetch` chỉ tải dữ liệu mới từ remote về và cập nhật remote-tracking branch.

```bash
git fetch origin
```

`git pull` tải dữ liệu mới rồi nhập vào branch hiện tại.

```bash
git pull origin main
```

Tóm lại:

- `fetch`: lấy dữ liệu về, chưa thay đổi code đang làm.
- `pull`: lấy dữ liệu về và merge vào branch hiện tại.

## 9. Xóa remote branch

Khi branch trên remote không còn cần dùng, có thể xóa:

```bash
git push origin --delete feature-login
```

Lệnh này xóa branch `feature-login` trên remote, không xóa branch local cùng tên.

## Kết luận

`origin/main` là remote-tracking branch, cho biết trạng thái branch `main` trên remote `origin` ở lần cập nhật gần nhất. Remote-tracking branch do Git tự cập nhật qua `fetch` hoặc `pull`. Tracking branch là local branch có liên kết với remote branch, giúp `git pull` và `git push` biết nên đồng bộ với branch nào.
