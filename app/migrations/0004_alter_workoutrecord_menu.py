# Generated by Django 4.0.1 on 2022-02-16 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_workoutrecord_sets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutrecord',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.workoutmenu', verbose_name='トレーニング名'),
        ),
    ]
