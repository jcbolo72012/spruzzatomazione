# Generated by Django 2.2.7 on 2019-12-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watering',
            name='created_date',
            field=models.DateTimeField(verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='watering',
            name='deadline',
            field=models.DateTimeField(verbose_name='Deadline'),
        ),
    ]
