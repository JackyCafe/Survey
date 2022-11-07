import os.path

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from app.forms import UserRegisterForm, UserProfileForm, SurveyForm, LoginForm, InhabitantsForm
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
    print(applyer.cared_person)
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
            return redirect('app:index')
    else:
        inhabitants_form = InhabitantsForm()

        obj = UserProfile.objects.get(user=user)
        inhabitant = obj.cared_person
    return render(request, 'account/inhabithants.html'
                  , {'inhabitants_form': inhabitants_form
                      , 'user': user
                      , 'applyer': applyer})


'''填寫問卷'''


def survey(request):
    survey_user: Survey
    user_id = request.user  # user object
    userprofile = UserProfile.objects.get(user=user_id)
    is_biginer = False
    if userprofile.care_time == '1':
        is_biginer = True  # 沒經驗的
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            survey_user = form.save(commit=False)
            survey_user.user = userprofile.user
            survey_user.save()
            return redirect('app:ladar')
    else:
        form = SurveyForm()
    return render(request, 'survey/survey.html',
                  {'form': form, 'userprofile': userprofile, 'is_biginer': is_biginer})


'''雷達'''


def ladar(request):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    user_id = request.user
    userprofile = UserProfile.objects.get(user_id=user_id)
    s = Survey.objects.filter(user=user_id).last()
    print(s)
    if userprofile.care_time == '1':
        q1 = s.q1
        q2 = s.q2
        q3 = s.q3
        q6 = s.q6
        q7 = s.q7
        q8 = s.q8
        q11 = s.q11
        q12 = s.q12
        q13 = s.q13
        q16 = s.q16
        q17 = s.q17
        q18 = s.q18
        q21 = s.q21
        q22 = s.q22
        q23 = s.q23
        q26 = s.q26
        q27 = s.q27
        q28 = s.q28
        v1 = (q1 + q2 + q3) / 15 * 5
        v2 = (q6 + q7 + q8) / 15 * 5
        v3 = (q11 + q12 + q13) / 15 * 5
        v4 = (q16 + q17 + q18) / 15 * 5
        v5 = (q21 + q22 + q23) / 15 * 5
        v6 = (q26 + q27 + q28) / 15 * 5
    else:
        pass

    labels = np.array([u"醫療 ", u" 生活 ", u" 財務 ", u" 法律 ", u" 心理 ", u" 家庭 "])
    stats = [v1, v2, v3, v4, v5, v6]

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
