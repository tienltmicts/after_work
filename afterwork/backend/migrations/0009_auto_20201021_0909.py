# Generated by Django 3.1 on 2020-10-21 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_update_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulelearn',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='backend.subscribers'),
        ),
    ]
