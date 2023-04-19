# PicoCTF

## Specialer

Sau khi `nc` thì sử dụng `ls` để xem cấu trúc folder ~/ thì thấy không có command đấy. Vì vậy mình đã sử dụng `cd` sau đó `Tab` 2 lần để check các file trong folder.

Những command như `cat` cũng không dùng được, nên sử dụng `Tab` 2 lần mình search được những command có thể dùng. Đây là một bash shell cơ bản.

Khi `cd` vào các folder mình thấy có các file `.txt`, nên mình in từng file để tìm flag bằng lệnh

```bash
echo "$(<filename)"
```

Sau khi kiểm tra tất cả các file, mình tìm được flag.
