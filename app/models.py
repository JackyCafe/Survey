from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from app.conf import *


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userprofile')
    role = models.CharField(max_length=20,choices=ROLE_CHOICE,verbose_name='目前您的照顧角色',default='1')
    care_time = models.CharField(max_length=20,choices=CARE_TIME_CHOICE,verbose_name='已照顧多久時間',default=2)
    cared_person = models.CharField(max_length=20,verbose_name='我們如何稱呼這位家人',blank = True)


    def yearpublished(self):
        return self.birth.strftime("%Y")


class Inhabitants(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='inhabitant_user') #問卷填表人
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inhabitant_user')  # 問卷填表人
    birth = models.DateField(verbose_name='生於民國幾年')
    city = models.CharField(max_length=3,choices=RESIDENCE_CHOICE,verbose_name='居住縣市',null=True)
    resident = models.CharField(max_length=10,verbose_name='居住地',null=True)
    disease = models.CharField(max_length=255,null=True,blank=True)
    mobility = models.CharField(max_length=255,verbose_name='行動能力',null=True)
    difficulty_care = models.CharField(max_length=255,verbose_name='自理困難處',null=True) #自理困難處
    life_difficulty = models.CharField(max_length=255,null=True,verbose_name='生活困難處') #生活困難處
    cohabitant = models.CharField(max_length=255,null=True,verbose_name='跟誰一起住') #跟 誰一起住
    resource = models.CharField(max_length=255,null = True,verbose_name='使用外部資源')
    exception = models.CharField(max_length=255,null=True,verbose_name='家庭期待的照顧方式')
    budget = models.CharField(max_length=255,null=True,verbose_name='預估家庭能負擔的照顧費')


''' 
   todo 修改問卷題目 https://odd-red-6d8.notion.site/be67acb5b29b4cc79ef88785a54ad97d
   如果是沒有照顧經驗的人，問卷內容填寫潛力值
   如果有照顧經驗的人，問卷內容為潛力值+經驗值
 
'''
class Survey(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='usersurvey',)
    q1 = models.CharField(max_length=10,choices=SURVEY_CHOICE,null=True,default=0)
    q2 = models.CharField(max_length=10,choices=SURVEY_CHOICE,null=True,default=0)
    q3 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q4 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q5 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q6 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q7 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q8 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q9 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q10 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q11 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q12 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q13 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q14 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q15 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q16 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q17 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q18 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q19 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q20 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q21 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q22 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q23 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q24 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q25 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q26 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q27 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q28 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q29 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)
    q30 = models.CharField(max_length=10, choices=SURVEY_CHOICE,null=True,default=0)