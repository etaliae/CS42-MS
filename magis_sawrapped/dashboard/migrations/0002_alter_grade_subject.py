# Generated by Django 5.0.3 on 2024-03-12 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('schedo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedo.subject'),
        ),
    ]
