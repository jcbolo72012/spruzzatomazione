# Generated by Django 2.2.7 on 2019-12-01 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watering', '0006_remove_watering_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watering',
            old_name='name',
            new_name='title',
        ),
    ]
