# Generated by Django 3.1 on 2020-08-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200831_0823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulelearn',
            old_name='teacher',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='schedulelearn',
            name='schedule',
        ),
        migrations.AddField(
            model_name='schedulelearn',
            name='schedule',
            field=models.ManyToManyField(blank=True, to='backend.ScheduleTeach'),
        ),
    ]
