import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magis_sawrapped.settings')
django.setup()

from dashboard.models import Grade

# Get all existing grades
Grade.objects.all().delete
