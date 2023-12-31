# Generated by Django 4.2 on 2023-12-08 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=256)),
                ('release_date', models.DateField()),
                ('duration', models.DurationField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, validators=[django.core.validators.MaxValueValidator(limit_value=10)])),
                ('language', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('cbc', models.CharField(max_length=256)),
                ('movie_description', models.TextField(max_length=2000)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
