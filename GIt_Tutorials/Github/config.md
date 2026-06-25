# GitHub Account Setup và Configuration

## Mục tiêu

Biết cách tạo tài khoản GitHub, cấu hình SSH key, profile và email để làm việc với GitHub.

## 1. Cấu hình Git trên máy cá nhân

Trước khi commit code, nên cấu hình tên và email cho Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Kiểm tra cấu hình:

```bash
git config --global user.name
git config --global user.email
```

Email trong Git config nên trùng với email đã thêm và xác minh trên GitHub để commit được liên kết đúng với tài khoản.

## 2. SSH key là gì?

SSH key dùng để xác thực máy cá nhân với GitHub khi push/pull code bằng SSH.

SSH key gồm:

- Private key: nằm trên máy cá nhân, không chia sẻ cho người khác.
- Public key: thêm vào GitHub để GitHub nhận diện máy của bạn.

Khi dùng SSH, bạn có thể làm việc với remote dạng:

```bash
git@github.com:user/project.git
```

## 3. Tạo SSH key

Tạo SSH key mới:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Nếu hệ thống cũ không hỗ trợ `ed25519`, có thể dùng RSA:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Public key thường nằm ở:

```bash
~/.ssh/id_ed25519.pub
```

Private key thường nằm ở:

```bash
~/.ssh/id_ed25519
```

Không đưa private key lên GitHub, không commit private key vào repository.

## 4. Thêm SSH key vào GitHub

Các bước cơ bản:

1. Copy nội dung public key, ví dụ:

```bash
cat ~/.ssh/id_ed25519.pub
```

2. Vào GitHub `Settings`.
3. Chọn `SSH and GPG keys`.
4. Chọn `New SSH key`.
5. Đặt tên key, ví dụ `Personal laptop`.
6. Dán public key vào ô `Key`.
7. Lưu lại.

Kiểm tra kết nối:

```bash
ssh -T git@github.com
```

Nếu cấu hình đúng, GitHub sẽ nhận diện được tài khoản.

## Kết luận

Để bắt đầu dùng GitHub, cần tạo tài khoản, xác minh email, cấu hình `user.name` và `user.email` trong Git, tạo SSH key và thêm public key vào GitHub. Profile và email nên được cấu hình rõ ràng để commit, Pull Request và hoạt động trên GitHub được liên kết đúng với tài khoản.
