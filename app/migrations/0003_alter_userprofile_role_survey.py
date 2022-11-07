# Generated by Django 4.1.2 on 2022-10-24 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('負責主要照顧責任', '負責主要照顧責任'), ('協助家人顧顧與蒐集資訊', '協助家人顧顧與蒐集資訊'), ('從事照顧相關工作的人', '從事照顧相關工作的人'), ('對照護議題感興趣', '對照護議題感興趣')], default='1', max_length=20, verbose_name='目前您的照顧角色'),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='照顧壓力大的時候，我希望可以自己靜一靜')),
                ('q2', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='參與團體活動，能夠放鬆我的照顧壓力')),
                ('q3', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='有聽說新的照顧用品對照顧對象有幫助，我會馬上嘗試')),
                ('q4', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='當購買新的照顧器材時，我會一步一步按照說明進行做操作')),
                ('q5', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='在進行照顧決策時，我會認為對於被照顧者有幫助，比起家人們的意願更重要')),
                ('q6', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='聽到照顧對象講的話不合邏輯時，我會理解他而不是說服他')),
                ('q7', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='照顧家人的時候，我會希望將所有會用到的資訊記錄下來')),
                ('q8', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='日常照顧充滿混亂，但我會盡力讓過程井井有條')),
                ('q9', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='分工照顧家人的時候，有能力的人應該要勇於承擔')),
                ('q10', models.CharField(choices=[('非常同意', '5'), ('同意', '4'), ('沒有意見', '3'), ('不同意', '2'), ('非常不同意', '1')], max_length=10, verbose_name='照顧家人的時候，可以出錢也可以出力，但照顧責任應該要公平')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usersurvey', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
