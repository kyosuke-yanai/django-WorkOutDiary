# Generated by Django 4.0.1 on 2022-02-15 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutrecord',
            name='sets',
        ),
    ]
