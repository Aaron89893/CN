#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XỬ LÝ FILE TEXT TRONG PYTHON
"""


# =========================
# 1. ĐỌC FILE TXT
# =========================

def read_file_way1():
    print("\n=== Cách 1 ===")
    taptin = open("file.txt", "r", encoding='utf-8')
    print(taptin.read())
    taptin.close()


def read_file_way2():
    print("\n=== Cách 2 ===")
    with open("file.txt", "r", encoding='utf-8') as file:
        data = file.read()
        print(data)


# =========================
# 2. ĐỌC N KÝ TỰ ĐẦU
# =========================

def read_n_chars():
    print("\n=== Đọc 10 ký tự đầu ===")
    file = open("file.txt", "r", encoding='utf-8')
    print(file.read(10))
    file.close()

    print("→ Số 10 nghĩa là đọc 10 ký tự đầu tiên của file")


# =========================
# 3. GHI FILE TXT
# =========================

def write_file():
    print("\n=== Ghi file baitap.txt ===")
    file = open('baitap.txt', 'w', encoding='utf-8')
    file.write("Nội dung cần lưu \n")
    file.write("Nội dung cần lưu")
    file.close()

    print("→ \\n là ký tự xuống dòng")


# =========================
# 4. ĐỌC TỪNG DÒNG (FIX CÚ PHÁP)
# =========================

def read_lines():
    print("\n=== Đọc từng dòng ===")
    with open("file.txt", "r", encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            print(line.strip())


# =========================
# 5 + 6. BÀI TẬP TRITUE.TXT
# =========================

def tritue_processing():
    print("\n=== Xử lý tritue.txt ===")

    # Đọc nội dung
    with open("tritue.txt", "r", encoding='utf-8') as f:
        content = f.read()
        print("\n--- Nội dung ---")
        print(content)

    # Đếm dòng, chữ, ký tự
    with open("tritue.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_chars = sum(len(line) for line in lines)
    num_words = sum(len(line.split()) for line in lines)

    print("\n--- Thống kê ---")
    print("Số dòng:", num_lines)
    print("Số chữ:", num_words)
    print("Số ký tự:", num_chars)

    # 3 dòng đầu
    print("\n--- 3 dòng đầu ---")
    for line in lines[:3]:
        print(line.strip())

    # Dòng 2 và 4
    print("\n--- Dòng 2 và 4 ---")
    if len(lines) >= 2:
        print(lines[1].strip())
    if len(lines) >= 4:
        print(lines[3].strip())

    # Thêm nội dung
    with open("tritue.txt", "a", encoding='utf-8') as f:
        f.write("\nNgày nay, trí tuệ nhân tạo đang được quan tâm rất nhiều.")
        f.write("\nBởi nó đã mang lại hiệu quả rất lớn đối với một vài lĩnh vực.")

    print("\n→ Đã thêm nội dung vào file")


# =========================
# 7. LIST → FILE
# =========================

def list_to_file():
    print("\n=== Ghi cadao.txt ===")

    lst = [
        "Ca dao",
        "Cá không ăn muối cá ương",
        "Con cãi cha mẹ",
        "Trăm đường con hư"
    ]

    with open("cadao.txt", "w", encoding='utf-8') as f:
        for line in lst:
            f.write(line + "\n")

    print("→ Mỗi phần tử là 1 dòng trong file")


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    # read_file_way1()
    # read_file_way2()
    # read_n_chars()
    # write_file()
    # read_lines()

    tritue_processing()
    list_to_file()