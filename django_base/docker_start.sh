#bin/bash
python manage.py makemigrations && python manage.py migrate && gunicorn django_base.wsgi:application -w 3 -b :8000 --timeout 2000 --reload
