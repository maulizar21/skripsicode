# Generated by Django 3.2.16 on 2023-12-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeskripsi', '0003_auto_20231225_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presence',
            old_name='associated_class',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='presence',
            old_name='presence_time',
            new_name='schedule',
        ),
    ]