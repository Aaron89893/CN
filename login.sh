#!/bin/bash

# Hardcoded credentials
USERNAME="admin"
PASSWORD="123456"

# Input
read -p "Enter username: " input_user
read -s -p "Enter password: " input_pass
echo ""

# Check
if [[ "$input_user" == "$USERNAME" && "$input_pass" == "$PASSWORD" ]]; then
    echo "Login successful ✅"
else
    echo "Login failed ❌"
fi
