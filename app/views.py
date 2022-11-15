import os.path

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from app.forms import UserRegisterForm, UserProfileForm, ExperienceSurveyForm, LoginForm, InhabitantsForm, \
    NoExperienceSurveyForm
from app.models import UserProfile, Survey, Inhabitants
import numpy as np
from matplotlib import pyplot as plt

from goodvillage.settings import BASE_DIR


def index(request):
    return render(request, 'account/index.html')


'''使用者登入'''


def user_login(request):
    user: User
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(User, username=cd['username'])
            print(user)
            if user.check_password(cd['password']):
                login(request, user)
                return redirect('app:index')
            else:
                return HttpResponse('Disabled account')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


'''註冊 '''


def register(request):
    user_form: UserRegisterForm
    profile_form: UserProfileForm
    new_user: User
    user_profile: UserProfile

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            # print(user_form.cleaned_data['password'])
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = new_user
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('app:inhabitant')
        else:
            return HttpResponse("兩次密碼不一致")  # 兩次密碼不一致
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
        return render(request, 'account/register.html',
                      {'user_form': user_form,
                       'profile': profile_form})


'''填寫住民基本資料'''


def inhabitants(request):
    #
    user = request.user  # 問卷填表人
    applyer = UserProfile.objects.get(user=user)
    inhabitant: Inhabitants
    inhabitants_form: InhabitantsForm
    profile_form: UserProfileForm
    new_user: User
    if request.method == 'POST':
        inhabitants_form = InhabitantsForm(request.POST)
        if inhabitants_form.is_valid():
            inhabitant = inhabitants_form.save(commit=False)
            inhabitant.user = user
            inhabitant.save()
            return redirect('app:survey')
    else:
        inhabitants_form = InhabitantsForm()

        obj = UserProfile.objects.get(user=user)
        inhabitant = obj.cared_person
    return render(request, 'account/inhabithants.html'
                  , {'inhabitants_form': inhabitants_form
                      , 'user': user
                      , 'applyer': applyer})


def survey(request):
    user = request.user #
    userprofile = UserProfile.objects.get(user=user)
    if userprofile.care_time=='1':
      return  redirect('app:no_experience_survey')
    else:
      return   redirect('app:experiencesurvey')


'''填寫有經驗的問卷'''


def ExperienceSurvey(request):
    survey_user: Survey
    user_id = request.user  # user object
    userprofile = UserProfile.objects.get(user=user_id)
    print(userprofile)

    is_biginer = False
    if userprofile.care_time == '1':
        is_biginer = True  # 沒經驗的

    if request.method == 'POST':
        form = ExperienceSurveyForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            survey_user = form.save(commit=False)
            survey_user.user = userprofile.user
            survey_user.save()
            return redirect('app:ladar')
    else:

        form = ExperienceSurveyForm()


    return render(request, 'survey/survey.html',
                  {'form': form, 'userprofile': userprofile, 'is_biginer': is_biginer})



def NoExperienceSurvey(request):
    survey_user: Survey # survey model 的物件
    user_id = request.user  # user object
    userprofile = UserProfile.objects.get(user=user_id)
    if request.method == 'POST':
        form = NoExperienceSurveyForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            survey_user = form.save(commit=False)
            survey_user.user = userprofile.user
            survey_user.save()
            return redirect('app:ladar')
    else:

        form = NoExperienceSurveyForm()
    print('here')
    return render(request, 'survey/survey.html',
                  {'form': form, 'userprofile': userprofile})

'''雷達'''


def ladar(request):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    user_id = request.user
    userprofile = UserProfile.objects.get(user_id=user_id)
    s = Survey.objects.filter(user=user_id).last()
    q1 = int(s.q1)
    q2 = int(s.q2)
    q3 = int(s.q3)
    q4 = int(s.q4)
    q5 = int(s.q5)
    q6 = int(s.q6)
    q7 = int(s.q7)
    q8 = int(s.q8)
    q9 = int(s.q9)
    q10 = int(s.q10)
    q11 = int(s.q11)
    q12 = int(s.q12)
    q13 = int(s.q13)
    q14 = int(s.q14)
    q15 = int(s.q15)
    q16 = int(s.q16)
    q17 = int(s.q17)
    q18 = int(s.q18)
    q19 = int(s.q19)
    q20 = int(s.q20)
    q21 = int(s.q21)
    q22 = int(s.q22)
    q23 = int(s.q23)
    q24 = int(s.q24)
    q25 = int(s.q25)
    q26 = int(s.q26)
    q27 = int(s.q27)
    q28 = int(s.q28)
    q29 = int(s.q29)
    q30 = int(s.q15)
    if userprofile.care_time == '1':
        v1 = (q1 + q2 + q3) / 15 * 5
        v2 = (q6 + q7 + q8) / 15 * 5
        v3 = (q11 + q12 + q13) / 15 * 5
        v4 = (q16 + q17 + q18) / 15 * 5
        v5 = (q21 + q22 + q23) / 15 * 5
        v6 = (q26 + q27 + q28) / 15 * 5
    else:
        v1 = (q1 + q2 + q3+q4+q5) / 15 * 5
        v2 = (q6 + q7 + q8+q9+q10) / 15 * 5
        v3 = (q11 + q12 + q13+q14+q15) / 15 * 5
        v4 = (q16 + q17 + q18+q19+q20) / 15 * 5
        v5 = (q21 + q22 + q23+q24+q25) / 15 * 5
        v6 = (q26 + q27 + q28+q29+q30) / 15 * 5

    labels = np.array([u"醫療 ", u" 生活 ", u" 財務 ", u" 法律 ", u" 心理 ", u" 家庭 "])
    stats = [v1, v2, v3, v4, v5, v6]
    # print(stats)

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))  # 閉合
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)

    # 设置中文字体

    # plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    labels = np.concatenate((labels, [labels[0]]))
    # font = FontProperties(fname=r"C:\Windows\Fonts\Arial.ttf", size=14)
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    media_root = os.path.join(BASE_DIR, 'static', 'img')
    plt.savefig(media_root + '/ladar.jpg')
    # plt.show()

    return render(request, 'survey/Ladar.html', {'user': user_id, 'survey': survey})
