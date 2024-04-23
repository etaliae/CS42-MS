# Generated by Django 5.0.3 on 2024-04-23 10:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_grade_user_email_grade_username'),
        ('schedo', '0008_usertable_userschedule'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['username', '-semester', 'grade']},
        ),
        migrations.RemoveConstraint(
            model_name='grade',
            name='sem_and_sub__uniq',
        ),
        migrations.AlterField(
            model_name='grade',
            name='username',
            field=models.ForeignKey(default='', limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(fields=('semester', 'subject', 'username'), name='sem_and_sub__uniq'),
        ),
    ]
