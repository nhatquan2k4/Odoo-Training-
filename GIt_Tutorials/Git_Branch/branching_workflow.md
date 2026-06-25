# Branching Workflow trong project thực tế

## Mục tiêu

Hiểu cách dùng branch để tổ chức công việc trong project thực tế.

## 1. Branching workflow là gì?

Branching workflow là cách team quy định việc tạo branch, làm việc trên branch, kiểm tra code và merge code về branch chính.

Mục đích là giúp project:

- Tách riêng từng phần công việc.
- Giữ branch chính ổn định.
- Dễ review code.
- Dễ thử nghiệm hoặc bỏ đi một hướng làm không phù hợp.

## 2. Long-running branches

Long-running branches là các branch tồn tại lâu dài trong project.

Các branch này thường đại diện cho các mức độ ổn định khác nhau của code.

Ví dụ:

- `main`: chứa code ổn định, có thể release.
- `develop`: chứa code đang phát triển, dùng để tích hợp tính năng.
- `next` hoặc `testing`: chứa code mới hơn, cần kiểm thử thêm.

Ví dụ workflow:

```text
feature branch -> develop -> main
```

Ý nghĩa:

- Code mới được làm trên feature branch.
- Khi làm xong, merge vào `develop` để test.
- Khi ổn định, merge từ `develop` vào `main`.

Không phải project nào cũng cần nhiều branch lâu dài. Với project nhỏ, có thể chỉ cần `main` và các feature branch ngắn hạn.

## 3. Topic branches

Topic branch là branch ngắn hạn, được tạo ra cho một công việc cụ thể.

Ví dụ:

- `feature-login`: làm chức năng đăng nhập.
- `fix-payment-error`: sửa lỗi thanh toán.
- `hotfix-config`: sửa lỗi cấu hình khẩn cấp.

Topic branch thường được tạo, làm việc, merge và xóa sau khi hoàn tất.

Ví dụ:

```bash
git switch main
git pull origin main
git switch -c feature-login
```

Sau khi làm xong:

```bash
git add .
git commit -m "Add login feature"
git push origin feature-login
```

Sau đó thường tạo Pull Request hoặc Merge Request trên GitHub/GitLab để review và merge.

## 4. Vì sao nên dùng topic branch?

Topic branch giúp mỗi công việc được tách riêng.

Lợi ích:

- Dễ xem thay đổi của từng tính năng.
- Dễ review code.
- Dễ bỏ branch nếu hướng làm không phù hợp.
- Nhiều người có thể làm nhiều việc song song.
- Branch chính ít bị ảnh hưởng bởi code chưa hoàn thiện.

## 5. Branch là local cho tới khi push

Khi tạo branch trên máy cá nhân, branch đó chỉ tồn tại trong local repository.

Ví dụ:

```bash
git switch -c feature-login
```

Lúc này Git chưa gửi branch lên GitHub/GitLab.

Muốn chia sẻ branch với người khác, cần push:

```bash
git push origin feature-login
```

## 6. Workflow thực tế đơn giản

Một workflow phổ biến cho team nhỏ:

```text
main
  |
  |-- feature-login
  |-- fix-user-error
  |-- feature-report
```

Quy trình:

1. Cập nhật code mới nhất từ `main`.
2. Tạo branch riêng cho task.
3. Commit thay đổi trên branch đó.
4. Push branch lên remote.
5. Tạo Pull Request hoặc Merge Request.
6. Review và merge vào `main`.
7. Xóa branch sau khi merge.

Các lệnh thường dùng:

```bash
git switch main
git pull origin main
git switch -c feature-login
git add .
git commit -m "Add login feature"
git push origin feature-login
```

## 7. Cách đặt tên branch

Nên đặt tên branch theo mục đích công việc:

```text
feature/login
fix/user-error
hotfix/payment-config
```

Một số prefix thường gặp:

- `feature/`: tính năng mới.
- `fix/`: sửa lỗi.
- `hotfix/`: sửa lỗi khẩn cấp.
- `refactor/`: chỉnh sửa cấu trúc code, không đổi behavior.

## Kết luận

Trong project thực tế, branch giúp tách công việc và giữ branch chính ổn định. Long-running branches dùng cho các mức ổn định lâu dài như `main`, `develop`, `testing`. Topic branches dùng cho từng task cụ thể và thường được xóa sau khi merge. Branch chỉ nằm ở local cho tới khi được push lên remote.
