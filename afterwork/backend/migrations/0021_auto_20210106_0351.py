# Generated by Django 3.1 on 2021-01-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_subscribers_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='position',
            field=models.CharField(choices=[('0', 'Student'), ('1', 'Teacher')], default='1', max_length=255),
        ),
    ]