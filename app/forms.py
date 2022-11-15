from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput, DateInput, NumberInput

from app.conf import *
from app.models import UserProfile, Survey, Inhabitants


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        print(cd)
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password don't match")
            return cd['password2']


class UserProfileForm(forms.ModelForm):
    role = forms.CharField(widget=forms.RadioSelect(choices=ROLE_CHOICE), label='目前您的照顧角色')
    care_time = forms.CharField(widget=forms.RadioSelect(choices=CARE_TIME_CHOICE), label='已經照顧多久時間')

    class Meta:
        model = UserProfile
        fields = ['role', 'care_time', 'cared_person']


class InhabitantsForm(forms.ModelForm):
    birth = forms.CharField(widget=NumberInput(attrs={'type': 'date'}), label='生於民國幾年')
    city = forms.ChoiceField(choices=RESIDENCE_CHOICE, label='居住在')
    resident = forms.CharField()
    disease = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DISEASE_CHOICE, label='罹患疾病')
    mobility = forms.ChoiceField(choices=MOBILITY_CHOICE, label='移動能力')
    difficulty_care = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DIFFICULT_CARE_CHOICE,
                                                label='自理困難處')
    life_difficulty = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LIFE_CHOICE,
                                                label='生活困難處')  # 生活困難處
    cohabitant = forms.ChoiceField(choices=COHABITANT_CHOICE, label='跟誰一起住')  # 跟 誰一起住
    resource = forms.ChoiceField(choices=RESOURCE_CHOICE, label='目前使用的外部資源')
    exception = forms.ChoiceField(choices=EXCEPTION_CHOICE, label='家庭期待的照顧方式')
    budget = forms.ChoiceField(choices=BUDGET_CHOICE, label='預估家庭能付的照顧費')

    class Meta:
        model = Inhabitants
        fields = ['birth', 'city', 'resident', 'disease', 'mobility'
            , 'difficulty_care', 'life_difficulty', 'cohabitant', 'resource', 'exception', 'budget']

#有經驗的問卷

class ExperienceSurveyForm(forms.ModelForm):
    # 醫療
    q1 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='看診時，你或家人能夠理解並實際執行醫生之指示？')
    q2 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你或家人有足夠的儲蓄面對照顧狀況？')
    q3 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你或家人總是能夠陪伴照顧對象去門診？')
    q4 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你或家人能夠搜尋附近的醫療資源？')
    q5 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你知道此病症未來可能發生的變化？')
    # 生活
    q6 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                         label='你知道外籍看護、台籍看護、銀髮住宅、機構、日照或護理之家等照顧選項的優缺點？')
    q7 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你知道照顧過程與親人病症，可能遇到的潛在風險？')
    q8 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='當你需要協助時，可以找到其他人協助照顧？')
    q9 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                         label='你或家人能夠協助照顧親人的日常起居（例如：三餐、穿衣、社交、外出......等）？')
    q10 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                          label='你或家人能夠執行每日親人的身體照顧需求（例如：肢體運動、翻身拍背、如廁、盥洗……等）？')

    # 財務
    q11 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='親人是否有儲蓄能夠支付自己的照顧相關費用？')
    q12 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='親人是否願意將個人儲蓄用在自己的照顧相關費用上？')
    q13 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你是否能估計親人的醫療與照顧相關費用，所衍伸的花費金額？')
    q14 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你清楚可選擇的照顧選項之中，政府所提供的各項補助金額與申請條件？')
    q15 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你是否有評估過自己理想老後照顧方式所需之費用，並提前進行規劃與儲蓄？')
    # 法律
    q16 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你認為長輩於生活中口頭承諾遺產分配，是否能夠產生法律效益呢？')
    q17 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                          label='你是否知道，主要照顧者能藉由設定契約、信託、意定監護等方式，保障勞力與金錢長期付出對應之權益嗎？')
    q18 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                          label='你是否知道，若要避免維生醫療與侵入性治療（氣切、CPR...等），需提前申請並依規定簽署相關證明文件嗎？')
    q19 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你認為你的親友之間，是否會因為照顧責任或財產問題告上法庭？')
    q20 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你是否考慮過，讓長輩提前進行遺產規劃並預立遺囑來減少家中的紛爭？')
    # 心理
    q21 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='日常照顧過程中，你是否擁有一段自己獨處的時間\空間，放鬆與轉換心情？')
    q22 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='在家中，是否有其他家人能夠共同討論照顧上的壓力？')
    q23 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='是否會因為照顧的親人的身心狀況嚴重產生不捨或者同情，影響到照顧的情緒？')
    q24 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你是否會因為照顧時間太長，時長感到憤怒、疲憊與壓力大？')
    q25 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你面對照顧負面情緒時，你是否有管道能夠抒發壓力？')
    # 家庭
    q26 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你的家人們，能夠針對照顧與醫療方式達成共識')
    q27 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='在家中，是否有其他家人能夠共同討論照顧上的壓力？')
    q28 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='親人是否有儲蓄能夠支付自己的照顧相關費用？')
    q29 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                          label='是否有和其他家人同步每日照顧狀況（例如：看診紀錄、突發狀況、身體量測數字等等）的習慣？')
    q30 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你能夠與其他家人開啟照顧費用相關的討論 ，並取得共識？')


    class Meta:
        model = Survey
        fields = [field.name for field in Survey._meta.fields ]
        exclude = ['user',]


#沒經驗的
class NoExperienceSurveyForm(forms.ModelForm):
    q1 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='看診時，你或家人能夠理解並實際執行醫生之指示？')
    q2 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你或家人有足夠的儲蓄面對照顧狀況？')
    q3 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你或家人總是能夠陪伴照顧對象去門診？')

    q6 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                           label='你知道外籍看護、台籍看護、銀髮住宅、機構、日照或護理之家等照顧選項的優缺點？')
    q7 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你知道照顧過程與親人病症，可能遇到的潛在風險？')
    q8 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='當你需要協助時，可以找到其他人協助照顧？')


    # 財務
    q11 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='親人是否有儲蓄能夠支付自己的照顧相關費用？')
    q12 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='親人是否願意將個人儲蓄用在自己的照顧相關費用上？')
    q13 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你是否能估計親人的醫療與照顧相關費用，所衍伸的花費金額？')

    # 法律
    q16 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你認為長輩於生活中口頭承諾遺產分配，是否能夠產生法律效益呢？')
    q17 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                            label='你是否知道，主要照顧者能藉由設定契約、信託、意定監護等方式，保障勞力與金錢長期付出對應之權益嗎？')
    q18 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE),
                            label='你是否知道，若要避免維生醫療與侵入性治療（氣切、CPR...等），需提前申請並依規定簽署相關證明文件嗎？')

    # 心理
    q21 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='日常照顧過程中，你是否擁有一段自己獨處的時間\空間，放鬆與轉換心情？')
    q22 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='在家中，是否有其他家人能夠共同討論照顧上的壓力？')
    q23 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='是否會因為照顧的親人的身心狀況嚴重產生不捨或者同情，影響到照顧的情緒？')

    # 家庭
    q26 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='你的家人們，能夠針對照顧與醫療方式達成共識')
    q27 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='在家中，是否有其他家人能夠共同討論照顧上的壓力？')
    q28 = forms.CharField(widget=forms.RadioSelect(choices=SURVEY_CHOICE), label='親人是否有儲蓄能夠支付自己的照顧相關費用？')


    class Meta:
        model = Survey
        fields = [field.name for field in Survey._meta.fields]
        exclude = ['user','q4','q5','q9','q10','q14','q15','q19','q20','q24','q25','q29','q30' ]
