# Generated by Django 5.0.3 on 2024-04-23 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_grade_options_grade_semester_and_more'),
        ('login', '0002_remove_user_id_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='user_email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.user'),
        ),
    ]
