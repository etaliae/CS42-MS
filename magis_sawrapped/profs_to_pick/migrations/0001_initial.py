# Generated by Django 5.0.3 on 2024-03-12 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('professor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedo.professor')),
                ('subject', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedo.subject')),
            ],
        ),
    ]
