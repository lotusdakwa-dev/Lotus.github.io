import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestinscription.settings')
django.setup()

username = 'admin3'
email = 'admin@example.com'
password = 'lotus2026'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser créé !')
else:
    print('Superuser déjà présent.')