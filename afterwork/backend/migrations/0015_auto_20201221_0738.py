# Generated by Django 3.1 on 2020-12-21 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_remove_schedulelearn_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulelearn',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.timesubjects'),
        ),
        migrations.AlterField(
            model_name='schedulelearn',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.subjects'),
        ),
    ]
