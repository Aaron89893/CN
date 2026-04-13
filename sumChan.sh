#!/bin/bash

# Kiểm tra số lượng đối số
if [ $# -lt 3 ] || [ $# -gt 7 ]; then
    echo "Loi: So luong doi so phai tu 3 den 7"
    exit 1
fi

sum=0

# Duyệt từng đối số
for num in "$@"
do
    if (( num % 2 == 0 )); then
        ((sum += num))
    fi
done

# Tạo thư mục nếu chưa có
dir="$HOME/Desktop/TINHTONG"
mkdir -p "$dir"

# Ghi file
output_file="$dir/tong.txt"

{
echo "Chuong trinh tinh tong"
echo "========================"
echo "So luong cac doi so duoc truyen vao: $# so."
echo "Tong cac so thoa dieu kien: $sum"
} > "$output_file"

echo "Da luu ket qua vao $output_file"