# Git hoạt động như thế nào?

## Mục tiêu

Hiểu cách Git lưu trữ dữ liệu và quy trình cơ bản khi làm việc với Git.

## 1. Git lưu dữ liệu bằng snapshot

Git không chỉ lưu từng thay đổi nhỏ của file. Mỗi lần commit, Git ghi lại trạng thái của toàn bộ dự án tại thời điểm đó, gọi là một snapshot.

Nếu file không thay đổi, Git không lưu lại file đó lần nữa mà chỉ trỏ tới phiên bản đã có trước đó. Cách này giúp Git quản lý lịch sử hiệu quả hơn.

## 2. Git hoạt động chủ yếu trên máy cá nhân

Khi dùng Git, toàn bộ lịch sử dự án được lưu trong máy của bạn. Vì vậy, nhiều thao tác như xem lịch sử, so sánh thay đổi hoặc commit có thể thực hiện mà không cần internet.

Khi cần chia sẻ code với người khác, bạn mới đồng bộ thay đổi lên remote repository như GitHub hoặc GitLab.

## 3. Git kiểm tra dữ liệu bằng mã hash

Git dùng mã hash để nhận diện và kiểm tra dữ liệu. Mỗi nội dung được lưu trong Git đều có một mã định danh riêng.

Nhờ vậy, nếu dữ liệu bị thay đổi hoặc hỏng, Git có thể phát hiện được.

## 4. Ba trạng thái chính trong Git

Một file trong Git thường đi qua ba trạng thái:

- `Modified`: file đã được chỉnh sửa nhưng chưa đưa vào vùng chuẩn bị commit.
- `Staged`: file đã được chọn để đưa vào commit tiếp theo.
- `Committed`: thay đổi đã được lưu vào lịch sử Git.

## 5. Quy trình làm việc cơ bản

Quy trình Git thường diễn ra như sau:

1. Chỉnh sửa file trong thư mục làm việc.
2. Dùng `git add` để đưa file vào trạng thái staged.
3. Dùng `git commit` để lưu snapshot vào lịch sử Git.

## Kết luận

Git hoạt động bằng cách lưu các snapshot của dự án theo thời gian. Git làm việc chủ yếu trên máy cá nhân, kiểm tra dữ liệu bằng mã hash và quản lý file qua ba trạng thái: modified, staged và committed.
