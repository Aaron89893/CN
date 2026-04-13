#!/usr/bin/env python3
baitho = [
    'Cái trống trường em',
    'Mùa hè cũng nghỉ',
    'Suốt ba tháng liền',
    'Trống nằm ngẫm nghĩ',
    'Buồn không hả trống',
    'Trong những ngày hè',
    'Bọn mình đi vắng',
    'Chỉ còn tiếng ve?'
]

# 1. Ghi file baitho.txt
with open("baitho.txt", "w", encoding="utf-8") as f:
    for line in baitho:
        f.write(line + "\n")

# 2. Đọc file và tính toán
with open("baitho.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Số dòng
so_dong = len(lines)

# Số từ
so_tu = sum(len(line.split()) for line in lines)

# Số ký tự (không tính khoảng trắng)
so_ky_tu = sum(len(line.replace(" ", "").replace("\n", "")) for line in lines)

# Lấy dòng chẵn (index bắt đầu từ 0 → dòng 2 là index 1)
dong_chan = [lines[i].strip() for i in range(1, so_dong, 2)]

# 3. Ghi kết quả
with open("kequa.txt", "w", encoding="utf-8") as f:
    f.write("Thong tin tap tin baitho.txt\n")
    f.write("============================\n")
    f.write(f"So luong tu: {so_tu}\n")
    f.write(f"So ky tu (khong khoang trang): {so_ky_tu}\n")
    f.write(f"So dong: {so_dong}\n")
    f.write("============================\n")

    for i, line in enumerate(dong_chan, start=2):
        f.write(f"Noi dung dong {i}: {line}\n")

print("Da tao file kequa.txt")