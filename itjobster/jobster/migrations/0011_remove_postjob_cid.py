# Generated by Django 4.2.6 on 2023-11-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobster', '0010_remove_cprofile_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='cid',
        ),
    ]