#!/bin/sh
set -e  # exit on first error

python src/order_app/infrastructure/web/django_order_app/manage.py migrate
python src/order_app/infrastructure/web/django_order_app/manage.py init_users
python src/order_app/infrastructure/web/django_order_app/manage.py runserver 0.0.0.0:8000
