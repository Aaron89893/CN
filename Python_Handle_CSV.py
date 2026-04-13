#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XỬ LÝ FILE CSV TRONG PYTHON
"""

import csv


# =========================
# 1. MỞ FILE CSV VÀ IN NỘI DUNG
# =========================

def read_csv_way1():
    print("\n=== Cách 1: read() ===")
    with open('university_records.csv', 'r', encoding='utf-8') as f:
        print(f.read())


def read_csv_way2():
    print("\n=== Cách 2: open() ===")
    f = open('university_records.csv', 'r', encoding='utf-8')
    print(f.read())
    f.close()


# =========================
# 2. ĐỌC FILE CSV BẰNG CSV MODULE
# =========================

def read_csv_module():
    print("\n=== Đọc CSV bằng csv.reader ===")
    with open('university_records.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    print("\n=== In từng cột (ví dụ cột 2) ===")
    with open('university_records.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1:
                print(row[1])

    print("\n=== In từng dòng bằng readlines() ===")
    with open('university_records.csv', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())


# =========================
# 3. GHI FILE CSV
# =========================

def write_csv():
    print("\n=== Ghi file nhansu.csv ===")
    with open('nhansu.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['An', '25', 'IT Manager', 'HCM'])
        writer.writerow(['Thành', '30', 'Developer', 'HCM'])

    print("→ File sẽ được tạo nếu chưa tồn tại")
    print("→ Nếu tồn tại, dữ liệu cũ sẽ bị ghi đè")


# =========================
# 4. TẠO CSV TỪ DỮ LIỆU SẴN
# =========================

def create_csv_from_data():
    print("\n=== Tạo countries.csv ===")

    header = ['HoTen', 'Diachi', 'Thanhpho', 'Sdt']
    data = [
        ['Tran Hung', '123 Nguyen Van Troi', 'HCM', '12498654'],
        ['Nguyen Tai', '55/32/1 Nguyen Du', 'HCM', '765438'],
        ['Phan Thanh', '98 Ly Thai To', 'HCM', '99876543'],
        ['Nguyen Sang', '32/1 CMT8', 'DN', '977653'],
        ['Le Luu', '32/9 Dong Nai', 'HCM', '98765']
    ]

    with open('countries.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


# =========================
# 5. TẠO CSV TỪ FILE TXT
# =========================

def txt_to_csv():
    print("\n=== Chuyển sinhvien.txt → sinhvien.csv ===")

    with open('sinhvien.txt', 'r', encoding='utf-8') as txt_file:
        content = csv.reader(txt_file, delimiter=',')

        with open('sinhvien.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(content)


# =========================
# 6. BÀI TẬP NHANSU.TXT → CSV
# =========================

def nhansu_txt_to_csv():
    print("\n=== Tạo nhansu.csv từ nhansu.txt ===")

    with open('nhansu.txt', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')

        with open('nhansu_from_txt.csv', 'w', newline='', encoding='utf-8') as out:
            writer = csv.writer(out)
            writer.writerows(reader)

    print("\n=== In tiêu đề ===")
    with open('nhansu_from_txt.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)

    print("\n=== Nội dung file nhansu.txt ===")
    with open('nhansu.txt', encoding='utf-8') as f:
        print(f.read())


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    # Gọi từng hàm để test
    # (bạn có thể comment bớt nếu chưa có file)

    # read_csv_way1()
    # read_csv_way2()
    # read_csv_module()

    write_csv()
    create_csv_from_data()
    txt_to_csv()
    nhansu_txt_to_csv()