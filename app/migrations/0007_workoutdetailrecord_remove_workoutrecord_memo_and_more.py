# Generated by Django 4.0.1 on 2022-02-19 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_workoutmenu_day_of_week_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOutDetailRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(blank=True, null=True, verbose_name='回数')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='重量')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='メモ')),
            ],
        ),
        migrations.RemoveField(
            model_name='workoutrecord',
            name='memo',
        ),
        migrations.DeleteModel(
            name='WorkOutRepsRecord',
        ),
        migrations.AddField(
            model_name='workoutdetailrecord',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.workoutrecord'),
        ),
    ]
