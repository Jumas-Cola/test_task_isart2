#!/bin/bash
python manage.py flush --no-input
python manage.py makemigrations shop
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
python manage.py migrate
python manage.py seed shop --number=15
