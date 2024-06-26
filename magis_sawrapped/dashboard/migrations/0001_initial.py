# Generated by Django 5.0.3 on 2024-03-12 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('S', 'S'), ('WP', 'WP')], default='A', max_length=2)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedo.schoolyear')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='schedo.subject')),
            ],
        ),
    ]
