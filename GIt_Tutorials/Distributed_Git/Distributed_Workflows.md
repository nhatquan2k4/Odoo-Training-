# Distributed Workflows trong Git

## Mục tiêu

Hiểu các kiểu làm việc nhóm phổ biến với Git: centralized workflow, integration-manager workflow và dictator workflow.

## 1. Distributed workflow là gì?

Git là hệ thống quản lý phiên bản phân tán. Mỗi developer có một bản sao đầy đủ của repository trên máy cá nhân.

Vì vậy, team có thể tổ chức cách làm việc theo nhiều kiểu khác nhau, không bắt buộc chỉ có một server trung tâm duy nhất.

## 2. Centralized workflow

Centralized workflow là kiểu làm việc giống mô hình tập trung.

Trong workflow này, cả team cùng làm việc với một repository trung tâm.

Ví dụ:

```text
Developer A  \
Developer B   ->  Central Repository
Developer C  /
```

Quy trình cơ bản:

```bash
git pull origin main
git add .
git commit -m "Update feature"
git push origin main
```

Đặc điểm:

- Mọi người cùng push/pull từ một repository chung.
- Dễ hiểu, phù hợp với team nhỏ.
- Thường dùng với GitHub/GitLab trong các project nội bộ.

Lưu ý:

- Cần pull code mới trước khi push để tránh conflict.
- Nếu nhiều người cùng push lên một branch, dễ phát sinh conflict hơn.

## 3. Integration-manager workflow

Integration-manager workflow thường dùng trong các project open source hoặc project có nhiều contributor.

Trong workflow này:

- Maintainer giữ repository chính.
- Contributor fork repository về tài khoản riêng.
- Contributor push thay đổi lên repository của họ.
- Maintainer xem xét và merge thay đổi vào repository chính.

Ví dụ:

```text
Contributor Repository  ->  Maintainer Repository
```

Quy trình thường gặp:

1. Contributor fork project.
2. Contributor clone repository của mình.
3. Contributor tạo branch, sửa code và push lên fork.
4. Contributor tạo Pull Request hoặc Merge Request.
5. Maintainer review và merge vào repository chính.

Đặc điểm:

- Contributor không cần quyền push trực tiếp vào repository chính.
- Maintainer kiểm soát chất lượng code trước khi merge.
- Phù hợp với project open source hoặc team cần review chặt chẽ.

## 4. Dictator workflow

Dictator workflow phù hợp với project rất lớn, có nhiều nhóm nhỏ cùng phát triển.

Trong workflow này có nhiều tầng quản lý code:

- Developer gửi thay đổi cho lieutenant.
- Lieutenant phụ trách một phần của project và tích hợp code từ developer.
- Dictator nhận code từ các lieutenant và merge vào repository chính.

Ví dụ:

```text
Developers -> Lieutenants -> Dictator -> Main Repository
```

Đặc điểm:

- Chia trách nhiệm review và merge theo từng phần của project.
- Phù hợp với project rất lớn, nhiều contributor.
- Quy trình phức tạp hơn, không cần thiết cho team nhỏ.

## 5. So sánh nhanh

| Workflow | Cách hoạt động | Phù hợp với |
| --- | --- | --- |
| Centralized | Mọi người làm việc với một repository chung | Team nhỏ, project nội bộ |
| Integration-manager | Contributor gửi thay đổi cho maintainer review và merge | Open source, team cần review |
| Dictator | Nhiều tầng tích hợp code trước khi vào repository chính | Project rất lớn |

## Kết luận

Git hỗ trợ nhiều workflow làm việc nhóm. Centralized workflow đơn giản và dễ dùng cho team nhỏ. Integration-manager workflow phù hợp khi cần review code trước khi merge, đặc biệt trong open source. Dictator workflow dùng cho project rất lớn, khi cần chia trách nhiệm quản lý code qua nhiều tầng.
