# Làm việc với Remote Repository

## Mục tiêu

Biết cách làm việc với remote repository trên GitHub/GitLab bằng các lệnh `remote`, `fetch`, `pull` và `push`.

## 1. Remote repository là gì?

Remote repository là repository được đặt ở nơi khác, thường là trên GitHub, GitLab hoặc một server nội bộ.

Remote giúp nhiều người cùng làm việc trên một dự án bằng cách đồng bộ code giữa máy cá nhân và server.

Ví dụ:

- Repository local: nằm trên máy cá nhân.
- Repository remote: nằm trên GitHub/GitLab.

## 2. Xem danh sách remote

Dùng `git remote` để xem các remote đang được cấu hình:

```bash
git remote
```

Dùng `-v` để xem cả URL:

```bash
git remote -v
```

Khi clone một repository, Git thường tự tạo remote tên là `origin`.

## 3. Thêm remote

Dùng `git remote add` để liên kết repository local với remote:

```bash
git remote add origin https://github.com/user/project.git
```

Cú pháp:

```bash
git remote add <name> <url>
```

Trong đó:

- `<name>` là tên remote, thường dùng `origin`.
- `<url>` là đường dẫn tới repository trên GitHub/GitLab.

## 4. `git fetch`

`git fetch` dùng để tải dữ liệu mới từ remote về local.

Ví dụ:

```bash
git fetch origin
```

Bản chất:

- Tải commit, branch và dữ liệu mới từ remote.
- Không tự động merge vào branch hiện tại.
- Dùng khi muốn xem thay đổi từ remote trước khi nhập vào code local.

## 5. `git pull`

`git pull` dùng để lấy thay đổi mới từ remote và nhập vào branch hiện tại.

Ví dụ:

```bash
git pull origin main
```

Bản chất:

- Thực hiện `git fetch`.
- Sau đó merge thay đổi từ remote vào branch hiện tại.

`git pull` thường được dùng khi muốn cập nhật code mới nhất từ GitHub/GitLab về máy.

## 6. `git push`

`git push` dùng để đẩy commit từ local lên remote.

Ví dụ:

```bash
git push origin main
```

Bản chất:

- Gửi các commit local lên remote repository.
- Giúp người khác có thể thấy và lấy thay đổi của mình.

Nếu remote đã có thay đổi mới mà local chưa có, Git có thể từ chối `push`. Khi đó cần `pull` hoặc `fetch` trước để cập nhật code.

## 7. Quy trình làm việc cơ bản với GitHub/GitLab

Clone repository:

```bash
git clone https://github.com/user/project.git
```

Kiểm tra remote:

```bash
git remote -v
```

Cập nhật code mới nhất:

```bash
git pull origin main
```

Sau khi sửa code và commit:

```bash
git push origin main
```

## Kết luận

Remote repository giúp đồng bộ code giữa máy cá nhân và GitHub/GitLab. `git fetch` tải dữ liệu mới nhưng chưa merge. `git pull` tải và merge vào branch hiện tại. `git push` đẩy commit local lên remote để chia sẻ với người khác.
