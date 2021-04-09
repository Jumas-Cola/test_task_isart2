#!/bin/bash
python manage.py flush --no-input
python manage.py makemigrations
python manage.py makemigrations shop
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
python manage.py seed shop --number=15
python manage.py runserver 0.0.0.0:8000
