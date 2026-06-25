# Git Protocols và Remote Hosting

## Mục tiêu

Hiểu các cách kết nối Git với remote repository: HTTP/HTTPS, SSH, SSH key và remote hosting.

## 1. Remote hosting là gì?

Remote hosting là dịch vụ lưu trữ Git repository trên server để nhiều người có thể cùng làm việc.

Ví dụ phổ biến:

- GitHub
- GitLab
- Bitbucket

Khi dùng remote hosting, repository không chỉ nằm trên máy cá nhân mà còn có một bản trên server. Nhờ đó, team có thể `push`, `pull`, review code và quản lý project dễ hơn.

## 2. HTTP/HTTPS

HTTP/HTTPS là cách kết nối remote repository thông qua URL web.

Ví dụ:

```bash
git clone https://github.com/user/project.git
```

Đặc điểm:

- Dễ dùng cho người mới.
- Không cần tạo SSH key ban đầu.
- Khi push code, thường cần đăng nhập hoặc dùng access token.
- Phù hợp khi clone nhanh một repository hoặc làm việc trong môi trường chưa cấu hình SSH.

HTTPS hiện được dùng phổ biến hơn HTTP vì có mã hóa và an toàn hơn.

## 3. SSH

SSH là giao thức dùng để kết nối an toàn tới server.

Ví dụ:

```bash
git clone git@github.com:user/project.git
```

Đặc điểm:

- Dùng SSH key để xác thực thay vì nhập username/password mỗi lần.
- Phù hợp khi thường xuyên push/pull code.
- Cần cấu hình SSH key trên máy cá nhân và thêm public key vào GitHub/GitLab.

## 4. SSH key là gì?

SSH key là cặp khóa dùng để xác thực với remote server.

SSH key gồm:

- Private key: nằm trên máy cá nhân, không chia sẻ cho người khác.
- Public key: được thêm vào GitHub/GitLab để server nhận diện bạn.

Khi kết nối bằng SSH, GitHub/GitLab kiểm tra public key đã đăng ký có khớp với private key trên máy bạn hay không. Nếu khớp, bạn được phép kết nối.

## 5. Tạo SSH key

Ví dụ tạo SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Sau đó public key thường nằm ở:

```bash
~/.ssh/id_ed25519.pub
```

Cần copy nội dung public key này và thêm vào phần SSH keys trong GitHub/GitLab.

## 6. Kiểm tra kết nối SSH

Với GitHub:

```bash
ssh -T git@github.com
```

Với GitLab:

```bash
ssh -T git@gitlab.com
```

Nếu cấu hình đúng, server sẽ nhận diện được tài khoản của bạn.

## 7. So sánh HTTPS và SSH

| Tiêu chí | HTTPS | SSH |
| --- | --- | --- |
| URL ví dụ | `https://github.com/user/project.git` | `git@github.com:user/project.git` |
| Xác thực | Token hoặc đăng nhập | SSH key |
| Dễ bắt đầu | Dễ hơn | Cần cấu hình ban đầu |
| Dùng lâu dài | Được | Rất phù hợp |
| Bảo mật | An toàn khi dùng HTTPS | An toàn nếu giữ private key cẩn thận |

## 8. Xem và đổi remote URL

Xem remote hiện tại:

```bash
git remote -v
```

Đổi remote sang HTTPS:

```bash
git remote set-url origin https://github.com/user/project.git
```

Đổi remote sang SSH:

```bash
git remote set-url origin git@github.com:user/project.git
```

## Kết luận

Remote hosting như GitHub/GitLab giúp lưu repository trên server để làm việc nhóm. HTTPS dễ dùng và phù hợp cho người mới. SSH cần cấu hình SSH key ban đầu nhưng thuận tiện hơn khi thường xuyên push/pull code. Private key phải được giữ bí mật, còn public key được thêm vào remote hosting để xác thực tài khoản.
