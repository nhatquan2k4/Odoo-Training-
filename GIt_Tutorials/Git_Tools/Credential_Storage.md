# Credential Storage trong Git

## Mục tiêu

Hiểu cách Git lưu thông tin đăng nhập hoặc token khi làm việc với remote repository qua HTTPS.

## 1. Credential là gì?

Credential là thông tin dùng để xác thực khi Git kết nối tới remote repository.

Ví dụ khi dùng HTTPS:

```bash
git clone https://github.com/user/project.git
git push origin main
```

Git có thể cần:

- Username.
- Password hoặc personal access token.
- Thông tin host, ví dụ `github.com`.

Hiện nay, nhiều dịch vụ như GitHub thường dùng personal access token thay cho password khi thao tác qua HTTPS.

## 2. Vì sao cần credential storage?

Nếu không cấu hình lưu credential, Git có thể hỏi username/token mỗi lần `push`, `pull` hoặc `fetch`.

Credential storage giúp Git ghi nhớ thông tin xác thực để lần sau dùng lại.

Git không tự lưu tùy tiện mà dùng `credential.helper` để quyết định lưu ở đâu và lưu như thế nào.

## 3. Credential helper là gì?

Credential helper là công cụ hỗ trợ Git lấy, lưu hoặc xóa credential.

Kiểm tra credential helper hiện tại:

```bash
git config --global credential.helper
```

Cấu hình credential helper:

```bash
git config --global credential.helper <helper>
```

Ví dụ:

```bash
git config --global credential.helper cache
```

## 4. Không lưu credential

Mặc định, Git có thể không lưu credential.

Khi đó, mỗi lần cần xác thực, Git sẽ hỏi lại username và token.

Ưu điểm:

- Không lưu thông tin nhạy cảm trên máy.

Nhược điểm:

- Bất tiện vì phải nhập lại nhiều lần.

## 5. `cache`

`cache` lưu credential tạm thời trong bộ nhớ.

Ví dụ:

```bash
git config --global credential.helper cache
```

Mặc định, credential được lưu tạm khoảng 15 phút.

Có thể chỉnh thời gian lưu:

```bash
git config --global credential.helper "cache --timeout=3600"
```

Ý nghĩa:

- `3600` là số giây.
- Sau thời gian này, Git sẽ hỏi lại credential.

Ưu điểm:

- Không lưu token xuống file trên disk.
- An toàn hơn `store`.

Nhược điểm:

- Hết thời gian cache thì phải nhập lại.

## 6. `store`

`store` lưu credential vào file trên disk.

Ví dụ:

```bash
git config --global credential.helper store
```

Mặc định, credential thường được lưu ở:

```bash
~/.git-credentials
```

Ưu điểm:

- Không cần nhập lại username/token.
- Dễ dùng.

Nhược điểm:

- Credential được lưu dạng plain text.
- Nếu ai đọc được file này, họ có thể thấy token.

Vì vậy, không nên dùng `store` trên máy dùng chung hoặc môi trường không an toàn.

## 7. Keychain hoặc Credential Manager

Trên một số hệ điều hành, Git có thể dùng kho bảo mật của hệ điều hành để lưu credential.

Ví dụ:

- macOS: `osxkeychain`.
- Windows: Git Credential Manager.
- Linux: tùy môi trường, có thể dùng credential manager hoặc libsecret.

Ví dụ trên macOS:

```bash
git config --global credential.helper osxkeychain
```

Git Credential Manager thường được cài kèm Git for Windows hoặc cài riêng.

Ưu điểm:

- An toàn hơn `store`.
- Token được lưu trong hệ thống quản lý credential của OS.
- Phù hợp khi làm việc lâu dài với GitHub/GitLab qua HTTPS.

## 8. Xóa credential đã lưu

Nếu token sai, hết hạn hoặc muốn đăng nhập lại, cần xóa credential đã lưu.

Với `store`, có thể kiểm tra file:

```bash
cat ~/.git-credentials
```

Sau đó xóa dòng tương ứng hoặc xóa file nếu chắc chắn:

```bash
rm ~/.git-credentials
```

Với Credential Manager hoặc Keychain, nên xóa trong công cụ quản lý credential của hệ điều hành.

Sau khi xóa, lần `push` hoặc `pull` tiếp theo Git sẽ hỏi lại username/token.

## 9. HTTPS và SSH khác nhau thế nào?

Khi dùng HTTPS, Git thường cần credential hoặc token:

```bash
https://github.com/user/project.git
```

Khi dùng SSH, Git xác thực bằng SSH key:

```bash
git@github.com:user/project.git
```

Nếu dùng SSH đúng cách, thường không cần credential helper cho username/token HTTPS.

## 10. Lưu ý bảo mật

- Không commit token vào repository.
- Không chia sẻ file `~/.git-credentials`.
- Không dùng `store` trên máy công cộng hoặc máy nhiều người dùng.
- Nếu token bị lộ, cần revoke token trên GitHub/GitLab.
- Nên ưu tiên credential manager/keychain hoặc SSH key cho môi trường làm việc lâu dài.

## Kết luận

Credential storage giúp Git ghi nhớ username/token khi kết nối remote qua HTTPS. `cache` lưu tạm trong bộ nhớ, `store` lưu vào file plain text, còn keychain hoặc credential manager lưu an toàn hơn trong hệ điều hành. Khi làm việc thực tế, nên ưu tiên SSH key hoặc credential manager thay vì lưu token plain text bằng `store`.
