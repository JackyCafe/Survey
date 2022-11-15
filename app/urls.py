"""goodvillage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from app.views import index, register,ladar,ExperienceSurvey,user_login,inhabitants,survey,NoExperienceSurvey

app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inhabitants/',inhabitants,name='inhabitant'),
    path('ladar/',ladar,name='ladar'),
    path('survey/',survey,name='survey'),
    path('experience_survey/',ExperienceSurvey,name='experiencesurvey'), #有照護經建的問卷
    path('no_experience_survey/',NoExperienceSurvey,name='no_experience_survey'),# 沒照護經驗的問卷
    path('register/', register, name='register'),
]
