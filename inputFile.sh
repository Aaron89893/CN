#!/bin/bash

read -p "Nhập tên file: " filename

echo "Nhập nội dung (nhấn Ctrl+D để kết thúc):"
content=$(cat)

echo "$content" > "$filename"

echo "Đã lưu nội dung vào file $filename"


#cat không có tham số → đọc từ stdin (bàn phím) Nó sẽ: cho bạn nhập nhiều dòng
#tiếp tục cho đến khi bạn nhấn Ctrl + D
#$(...) = command substitution → lấy output của cat gán vào biến content
