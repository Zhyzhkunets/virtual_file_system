# Generated by Django 3.2.7 on 2021-09-19 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_manager', '0002_alter_folderpermission_folder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folderpermission',
            name='name',
        ),
    ]
