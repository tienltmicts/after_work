# Generated by Django 3.1 on 2020-08-31 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200831_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='position',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], default='student', max_length=255),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='schedule_registere',
            field=models.ManyToManyField(blank=True, related_name='list_timeSubjects', to='backend.TimeSubjects'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subjects_teach',
            field=models.ManyToManyField(blank=True, related_name='list_subjects', to='backend.Subjects'),
        ),
        migrations.AlterField(
            model_name='timesubjects',
            name='day_of_week',
            field=models.CharField(choices=[('Thứ 2', 'Thứ 2'), ('Thứ 3', 'Thứ 3'), ('Thứ 4', 'Thứ 4'), ('Thứ 5', 'Thứ 5'), ('Thứ 6', 'Thứ 6'), ('Thứ 7', 'Thứ 7'), ('Chủ nhật', 'Chủ nhật')], default='1', max_length=255),
        ),
        migrations.CreateModel(
            name='ScheduleLearn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.timesubjects')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.subscribers')),
            ],
            options={
                'verbose_name': 'ScheduleLearn',
                'verbose_name_plural': 'ScheduleLearn',
                'db_table': 'schedule_learn',
            },
        ),
    ]
