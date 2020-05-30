# Generated by Django 3.0.5 on 2020-05-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('maxtemp', models.IntegerField(max_length=4)),
                ('mintemp', models.IntegerField(max_length=4)),
                ('maxppt', models.IntegerField(max_length=4)),
                ('minppt', models.IntegerField(max_length=4)),
            ],
        ),
    ]