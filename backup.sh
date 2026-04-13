#!/bin/bash

read -p "Nhap ten thu muc Backup: " backup_name

backup_dir="$HOME/Desktop/$backup_name"
source_dir="$HOME/Documents/Data"

# Nếu chưa tồn tại thì tạo
if [ ! -d "$backup_dir" ]; then
    echo "Thu muc Backup chua ton tai. Tien hanh tao thu muc."
    mkdir -p "$backup_dir"
fi

# Lấy thời gian hiện tại
time_now=$(date +"%H:%M:%S")

file_name="Backup_$time_now.tar"

# Tạo file tar
tar -cvf "$backup_dir/$file_name" -C "$HOME/Documents" Data > /dev/null

echo "Sao luu du lieu thanh cong!"