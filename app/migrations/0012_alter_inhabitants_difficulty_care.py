# Generated by Django 4.1.2 on 2022-10-31 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_inhabitants_difficulty_care_inhabitants_mobility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inhabitants',
            name='difficulty_care',
            field=models.CharField(max_length=255, null=True, verbose_name='自理困難處'),
        ),
    ]
