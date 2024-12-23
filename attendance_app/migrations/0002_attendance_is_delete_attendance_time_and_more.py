# Generated by Django 5.1.4 on 2024-12-16 06:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendance',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='direction',
            field=models.CharField(choices=[('Personal Out', 'Personal Out'), ('Check In', 'Check In'), ('Check Out', 'Check Out'), ('Personal In', 'Personal In')], max_length=100),
        ),
    ]
