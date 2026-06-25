# Contributing to a Project

## Mục tiêu

Hiểu cách đóng góp code vào một project dùng Git, bao gồm chuẩn bị commit, cập nhật code, push branch và gửi thay đổi để review.

## 1. Contributing là gì?

Contributing là quá trình đóng góp thay đổi vào một project.

Tùy project, cách đóng góp có thể khác nhau:

- Team nhỏ có quyền push trực tiếp vào repository chính.
- Team có maintainer cần review code trước khi merge.
- Project open source thường dùng fork và Pull Request.
- Một số project dùng patch qua email.

Vì vậy, trước khi đóng góp cần xem project đang dùng workflow nào.

## 2. Chuẩn bị commit sạch

Trước khi commit, nên kiểm tra thay đổi:

```bash
git status
git diff
```

Kiểm tra lỗi whitespace:

```bash
git diff --check
```

Nên chia commit theo từng thay đổi logic. Không nên gom nhiều việc không liên quan vào một commit lớn.

Ví dụ tốt:

```text
Add user login validation
Fix password error message
Update login tests
```

Ví dụ không tốt:

```text
Update code
Fix stuff
Change many files
```

## 3. Viết commit message rõ ràng

Commit message nên ngắn gọn và mô tả đúng thay đổi.

Ví dụ:

```bash
git commit -m "Add login validation"
```

Một commit message tốt nên trả lời được:

- Thay đổi gì?
- Vì sao thay đổi?
- Phạm vi thay đổi nằm ở đâu?

## 4. Làm việc trong team nhỏ

Với team nhỏ, mọi người thường có quyền push vào cùng một repository.

Quy trình cơ bản:

```bash
git pull origin main
git switch -c feature-login
git add .
git commit -m "Add login feature"
git push origin feature-login
```

Sau đó tạo Pull Request hoặc Merge Request để review và merge vào `main`.

Nếu push trực tiếp lên `main`, cần pull code mới nhất trước:

```bash
git pull origin main
git push origin main
```

Nếu push bị từ chối vì remote có commit mới, cần cập nhật local trước rồi push lại.

## 5. Đóng góp qua fork

Với project open source, contributor thường không có quyền push vào repository chính.

Quy trình phổ biến:

1. Fork repository về tài khoản của mình.
2. Clone fork về máy.
3. Tạo branch mới cho thay đổi.
4. Commit và push branch lên fork.
5. Tạo Pull Request về repository chính.

Ví dụ:

```bash
git clone https://github.com/your-name/project.git
cd project
git switch -c fix-login-error
git add .
git commit -m "Fix login error"
git push origin fix-login-error
```

Sau đó mở Pull Request trên GitHub/GitLab.

## 6. Cập nhật code trước khi gửi

Trước khi gửi Pull Request hoặc Merge Request, nên cập nhật branch của mình với branch chính.

Ví dụ:

```bash
git fetch origin
git switch fix-login-error
git rebase origin/main
```

Hoặc dùng merge:

```bash
git fetch origin
git merge origin/main
```

Mục tiêu là đảm bảo code của mình vẫn chạy tốt với phiên bản mới nhất của project.

## 7. Khi có conflict

Nếu có conflict khi pull, merge hoặc rebase:

```bash
git status
```

Mở file bị conflict, sửa nội dung, sau đó:

```bash
git add file_name
```

Nếu đang merge:

```bash
git commit
```

Nếu đang rebase:

```bash
git rebase --continue
```

## 8. Đóng góp bằng patch

Một số project không dùng Pull Request mà nhận patch qua email.

Tạo patch từ commit:

```bash
git format-patch origin/main
```

Lệnh này tạo file `.patch` để gửi cho maintainer.

Cách này ít gặp hơn trong các project dùng GitHub/GitLab, nhưng vẫn phổ biến ở một số project lớn hoặc lâu đời.

## Kết luận

Khi đóng góp vào project, cần hiểu workflow của project, tạo commit sạch, viết commit message rõ ràng, cập nhật code trước khi gửi và xử lý conflict nếu có. Với team nhỏ có thể push branch trực tiếp lên remote. Với project open source, quy trình phổ biến là fork repository, push branch lên fork và tạo Pull Request hoặc Merge Request.
