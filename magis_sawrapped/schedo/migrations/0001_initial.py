# Generated by Django 5.0.3 on 2024-03-12 06:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.CharField(max_length=150, unique=True)),
                ('semester', models.CharField(choices=[('0', 'Intersession'), ('1', 'First Semester'), ('2', 'Second Semester')], default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=150)),
                ('units', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=9)),
                ('day', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=20)),
                ('modality', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=10)),
                ('max_no', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('lang', models.CharField(max_length=3)),
                ('level', models.CharField(max_length=1)),
                ('free_slots', models.IntegerField()),
                ('remarks', models.CharField(max_length=200)),
                ('s', models.CharField(max_length=1)),
                ('p', models.CharField(max_length=1)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedo.subject')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedo.time')),
            ],
        ),
    ]
