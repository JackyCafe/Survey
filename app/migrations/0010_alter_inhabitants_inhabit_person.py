# Generated by Django 4.1.2 on 2022-10-31 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_inhabitants_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inhabitants',
            name='inhabit_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inhabitant_person', to='app.userprofile'),
        ),
    ]
