# Generated by Django 5.0.4 on 2024-04-20 03:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('staff_position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_came', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_gone', models.DateTimeField(default=django.utils.timezone.now)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.staff')),
            ],
        ),
    ]