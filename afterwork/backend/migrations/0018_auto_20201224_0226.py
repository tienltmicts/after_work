# Generated by Django 3.1 on 2020-12-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20201224_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Updated'),
        ),
    ]