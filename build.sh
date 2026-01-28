#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Crear/Asegurar superusuario con TUS DATOS
echo "Asegurando superusuario..."
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='Alejandro').exists() or \
User.objects.create_superuser('Alejandro', 'tu-correo@gmail.com', 'TuClaveSegura123')" \
| python manage.py shell