# Generated by Django 3.1 on 2020-08-31 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=255)),
                ('current_address', models.TextField()),
                ('position', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Students')], default='student', max_length=255)),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Subscribers',
                'verbose_name_plural': 'Subscribers',
                'db_table': 'subscribers',
            },
        ),
        migrations.CreateModel(
            name='Time_of_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Time_of_day',
                'verbose_name_plural': 'Time_of_day',
                'db_table': 'time_of_day',
            },
        ),
    ]
