# Branch trong Git

## Mục tiêu

Hiểu branch là gì và Git lưu branch như thế nào.

## 1. Branch là gì?

Branch là một nhánh phát triển riêng trong Git.

Khi làm việc với branch, ta có thể phát triển tính năng mới, sửa lỗi hoặc thử nghiệm code mà không ảnh hưởng trực tiếp đến nhánh chính.

Ví dụ:

- `main`: nhánh chính của dự án.
- `feature-login`: nhánh dùng để phát triển chức năng đăng nhập.
- `fix-bug`: nhánh dùng để sửa lỗi.

## 2. Git lưu dữ liệu bằng commit

Git lưu lịch sử dự án bằng các commit.

Mỗi commit là một snapshot của dự án tại một thời điểm. Commit cũng lưu thông tin về commit đứng trước nó, gọi là parent commit.

Ví dụ lịch sử commit:

```text
A --- B --- C
```

Trong đó:

- `A`, `B`, `C` là các commit.
- `C` là commit mới nhất.
- `B` là parent của `C`.

## 3. Git lưu branch như thế nào?

Trong Git, branch không phải là bản sao đầy đủ của source code.

Branch chỉ là một con trỏ nhẹ trỏ tới một commit.

Ví dụ:

```text
A --- B --- C  main
```

Ở đây, branch `main` đang trỏ tới commit `C`.

Khi tạo branch mới:

```bash
git branch testing
```

Git tạo thêm một con trỏ mới:

```text
A --- B --- C  main
             \
              testing
```

Lúc này `main` và `testing` cùng trỏ tới commit `C`.

## 4. HEAD là gì?

`HEAD` là con trỏ đặc biệt cho biết hiện tại bạn đang đứng ở branch nào.

Ví dụ:

```text
A --- B --- C  main
              ^
             HEAD
```

Nếu đang ở branch `main`, `HEAD` trỏ tới `main`.

Khi chuyển sang branch khác:

```bash
git switch testing
```

`HEAD` sẽ trỏ sang branch `testing`.

Trước đây, Git thường dùng `checkout` cho nhiều việc khác nhau:

```bash
git checkout testing
git checkout -b feature-login
git checkout -- README.md
```

Trong đó:

- `git checkout testing`: chuyển sang branch `testing`.
- `git checkout -b feature-login`: tạo branch mới và chuyển sang branch đó.
- `git checkout -- README.md`: hủy thay đổi trong file `README.md`.

Vì `checkout` làm nhiều nhiệm vụ nên dễ gây nhầm lẫn. Hiện nay, Git tách rõ hơn thành `switch` và `restore`.

`git switch` dùng cho thao tác với branch:

```bash
git switch testing
git switch -c feature-login
```

Trong đó:

- `git switch testing`: chuyển sang branch `testing`.
- `git switch -c feature-login`: tạo branch `feature-login` và chuyển sang branch đó.

`git restore` dùng để khôi phục hoặc hủy thay đổi của file:

```bash
git restore README.md
git restore --staged README.md
```

Trong đó:

- `git restore README.md`: hủy thay đổi chưa commit trong file `README.md`.
- `git restore --staged README.md`: đưa file ra khỏi staging area.

Tóm lại, `switch` dùng cho branch, còn `restore` dùng cho file. `checkout` vẫn dùng được, nhưng người mới học nên ưu tiên `switch` và `restore` để dễ hiểu hơn.

## 5. Khi commit trên branch

Khi tạo commit mới, branch hiện tại sẽ tự động di chuyển tới commit mới đó.

Ví dụ đang ở branch `testing` và tạo commit mới `D`:

```text
A --- B --- C  main
             \
              D  testing
```

Lúc này:

- `main` vẫn trỏ tới `C`.
- `testing` trỏ tới `D`.
- Lịch sử của hai branch bắt đầu khác nhau.

## 6. Vì sao branch trong Git nhẹ?

Branch trong Git nhẹ vì Git chỉ cần lưu một con trỏ tới commit, không cần sao chép toàn bộ thư mục source code.

Về bản chất, một branch là một reference chứa mã hash của commit mà nó đang trỏ tới.

Vì vậy, tạo branch trong Git rất nhanh.

## Kết luận

Branch là nhánh phát triển riêng trong Git. Git lưu branch như một con trỏ tới commit, không phải là bản sao của toàn bộ source code. `HEAD` cho biết branch hiện tại, và khi commit mới được tạo, branch hiện tại sẽ di chuyển tới commit đó.
