# Generated by Django 4.1.2 on 2022-10-30 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_userprofile_birth_userprofile_care_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth',
        ),
    ]
