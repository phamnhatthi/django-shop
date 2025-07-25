#!/usr/bin/env bash

# Cài dependencies
pip install -r requirements.txt

# Chạy migrate
python manage.py migrate

# (Tùy chọn) collectstatic nếu dùng static file:
# python manage.py collectstatic --noinput
