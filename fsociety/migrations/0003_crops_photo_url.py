# Generated by Django 3.0.5 on 2020-06-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsociety', '0002_auto_20200530_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='crops',
            name='photo_url',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]