# Generated by Django 4.2 on 2023-12-08 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0004_remove_movies_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]