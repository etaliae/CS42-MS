# Generated by Django 5.0.3 on 2024-03-12 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_grade_subject'),
        ('schedo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['-semester', 'grade']},
        ),
        migrations.AddField(
            model_name='grade',
            name='semester',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedo.schoolyear'),
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(fields=('semester', 'subject'), name='sem_and_sub__uniq'),
        ),
    ]
