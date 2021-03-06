# Generated by Django 3.1 on 2020-08-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleteach',
            name='room',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ngay ket thuc'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ngay bat dau'),
        ),
        migrations.AlterField(
            model_name='time_of_day',
            name='end_time',
            field=models.CharField(choices=[('7h', '7h'), ('8h', '8h'), ('9h', '9h'), ('10h', '10h'), ('11h', '11h'), ('14h', '14h'), ('15h', '15h'), ('16h', '16h'), ('17h', '17h'), ('18h', '18h'), ('19h', '19h'), ('20h', '20h')], default='9h', max_length=255),
        ),
        migrations.AlterField(
            model_name='time_of_day',
            name='start_time',
            field=models.CharField(choices=[('7h', '7h'), ('8h', '8h'), ('9h', '9h'), ('10h', '10h'), ('11h', '11h'), ('14h', '14h'), ('15h', '15h'), ('16h', '16h'), ('17h', '17h'), ('18h', '18h'), ('19h', '19h'), ('20h', '20h')], default='7h', max_length=255),
        ),
    ]
