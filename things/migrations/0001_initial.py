# Generated by Django 4.2.5 on 2023-10-01 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=120)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
