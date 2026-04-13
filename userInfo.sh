#!/bin/bash

read -p "Nhập họ tên: " fullname
read -p "Nhập giới tính (nam/nu): " gender
read -p "Nhập năm sinh: " birthyear

current_year=$(date +%Y)
age=$((current_year - birthyear))

# Xác định cách xưng hô
if (( age < 20 )); then
    pronoun="bạn"
elif (( age <= 45 )); then
    if [[ "$gender" == "nam" ]]; then
        pronoun="anh"
    else
        pronoun="chị"
    fi
else
    if [[ "$gender" == "nam" ]]; then
        pronoun="chú"
    else
        pronoun="cô"
    fi
fi

echo "Xin chào $pronoun $fullname!"
echo "Năm nay $pronoun $age tuổi."
