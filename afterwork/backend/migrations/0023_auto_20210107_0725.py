# Generated by Django 3.1 on 2021-01-07 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20210107_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulelearn',
            name='schedule',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.scheduleteach'),
        ),
        migrations.AlterField(
            model_name='schedulelearn',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='learn_students', to='backend.Subscribers'),
        ),
    ]
