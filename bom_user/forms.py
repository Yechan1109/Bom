from django import forms

from .models import Danger, BomGetPlan, Performance, Counselor, BomUser, BomSetPlan
from bom_data.models import ChartData


class IndexForm(forms.Form):
    counselor_name = forms.CharField(
        error_messages={
            'required':'이름을 입력해주세요.'
        },
        max_length=64, label='이름'
    )
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        counselor_name = cleaned_data.get('counselor_name')
        password = cleaned_data.get('password')
        
        # date = cleaned_data.get('date')
        
        if counselor_name and password:
            try:
                counselor = Counselor.objects.get(counselor_name=counselor_name)
            except Counselor.DoesNotExist:
                self.add_error('counselor_name', '아이디가 없습니다.')
                return
            #앞 인자는 내가 입련한 값, 뒤 인자는 db에 있는 인코딩 값
            if not password == counselor.password:
                self.add_error('password','비밀번호를 틀렸습니다.')
            else:
                self.counselor_name = counselor.counselor_name
            
class ToadminForm(forms.Form):
    counselor_name = forms.CharField(
        error_messages={
            'required':'이름을 입력해주세요.'
        },
        max_length=64, label='이름'
    )
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        counselor_name = cleaned_data.get('counselor_name')
        password = cleaned_data.get('password')
        
        # date = cleaned_data.get('date')
        
        if counselor_name and password:
            try:
                counselor = Counselor.objects.get(counselor_name=counselor_name)
            except Counselor.DoesNotExist:
                self.add_error('counselor_name', '아이디가 없습니다.')
                return
            #앞 인자는 내가 입련한 값, 뒤 인자는 db에 있는 인코딩 값
            if not password == counselor.password:
                self.add_error('password','비밀번호를 틀렸습니다.')
            else:
                self.counselor_name = counselor.counselor_name

class UserForm(forms.Form):
    # 개인인적사항
    C_Name = forms.CharField(max_length=64, label='이름',required=False)
    C_Jumin = forms.CharField(label='주민번호',required=False)
    REG_Day = forms.DateField()
    coun_choices =[
    ('이성영', '이성영'),
    ('정현재', '정현재'),
    ('김현정', '김현정'),
    ('문보라', '문보라'),
    ('박지숙', '박지숙'),
    ('김수미', '김수미'),
    ('강주연', '강주연'),
    ('노미나', '노미나'),
    ('곽은영', '곽은영')]
    F_Coun = forms.ChoiceField(choices=coun_choices, label='최초상담자',required=False)

    gender_choices =[
    ('남자', '남자'),
    ('여자', '여자')]
    C_Gender = forms.ChoiceField(choices=gender_choices,required=False)

    C_Kakaoid = forms.CharField(max_length=50,required=False)
    C_Tel = forms.CharField(label='전화번호',required=False)
    C_CN = forms.CharField(label='긴급연락처',required=False)
    C_Address1 = forms.CharField()
    C_Address2 = forms.CharField()
    Res_choices = [
    ('자가', '자가'),
    ('전세', '전세'),
    ('월룸(월세)', '월룸(월세)'),
    ('고시텔(원세)','고시텔(원세)'),
    ('기타','기타')]
    Yn_choices = [
	('없음', '없음'),
    ('있음', '있음')]
    His_choices = [
	('전화 및 SNS', '전화 및 SNS'),
    ('대면', '대면'),
    ('기타', '기타')] 
    Rou_choices = [
	('선생님', '선생님'),
    ('기관소개', '기관소개'),
    ('기타','기타')]
    Ss_choices = [
	('기초수급', '기초수급'),
    ('차상위', '차상위'),
    ('의료급여','의료급여'),
    ('기타','기타')]
    Fam_choices = [
	('조손가정', '조손가정'),
    ('한부모', '한부모'),
    ('부모','부모'),
    ('독립','독립'),
    ('동거','동거'),
    ('기타','기타')]
    Edu_choices = [
	('초등','초등'),
    ('중등','중등'),
    ('고등','고등'),
    ('기타','기타')]
    C_Residential = forms.ChoiceField(choices=Res_choices)
    C_Residential_text = forms.CharField(max_length=30, required=False)
    C_History = forms.ChoiceField(choices=Yn_choices)
    C_History_select = forms.ChoiceField(choices=His_choices)
    C_Route = forms.ChoiceField(choices=Rou_choices)
    C_Route_text = forms.CharField(max_length=30, required=False)
    C_Institute = forms.CharField(max_length=30, required=False)
    C_Incharge_name = forms.CharField(max_length=30, required=False)
    C_Incharge_tel = forms.CharField(max_length=30, required=False)
    C_Otherhistory = forms.CharField(max_length=50, required=False)
    C_Disorder = forms.ChoiceField(choices=Yn_choices)
    C_Disorder_text = forms.CharField(max_length=30, required=False)
    C_Ssgrade = forms.ChoiceField(choices=Ss_choices)
    C_Ssgrade_text = forms.CharField(max_length=30, required=False)
    C_Family = forms.ChoiceField(choices=Fam_choices)
    C_Family_text = forms.CharField(max_length=30, required=False)
    C_Job = forms.ChoiceField(choices=Yn_choices)
    C_Job_text = forms.CharField(max_length=30, required=False)
    C_Ecostatus1 = forms.IntegerField(required=False)
    C_Ecostatus2 = forms.IntegerField(required=False)
    C_Ecostatus3 = forms.IntegerField(required=False)
    C_Ecostatus4 = forms.IntegerField(required=False)
    C_Education = forms.ChoiceField(choices=Edu_choices)
    C_Education_text = forms.CharField(max_length=30, required=False)

    def clean(self):
        cleaned_data = super().clean()
        # 개인인적사항
        C_Name = cleaned_data.get('C_Name')
        REG_Day = cleaned_data.get('REG_Day')
        C_Jumin = cleaned_data.get('C_Jumin')
        F_Coun = cleaned_data.get('F_Coun')
        C_Gender = cleaned_data.get('C_Gender')
        C_Kakaoid = cleaned_data.get('C_Kakaoid')
        C_Tel = cleaned_data.get('C_Tel')
        C_CN = cleaned_data.get('C_CN')
        C_Address1 = cleaned_data.get('C_Address1')
        C_Address2 = cleaned_data.get('C_Address2')
        # 추가인적사항
        C_Residential = cleaned_data.get('C_Residential')
        C_Residential_text = cleaned_data.get('C_Residential_text')
        C_History = cleaned_data.get('C_History')
        C_History_select = cleaned_data.get('C_History_select')
        C_Route = cleaned_data.get('C_Route')
        C_Route_text = cleaned_data.get('C_Route_text')
        C_Institute = cleaned_data.get('C_Institute')
        C_Incharge_name = cleaned_data.get('C_Incharge_name')
        C_Incharge_tel = cleaned_data.get('C_Incharge_tel')
        C_Otherhistory = cleaned_data.get('C_Otherhistory')
        C_Disorder = cleaned_data.get('C_Disorder')
        C_Disorder_text = cleaned_data.get('C_Disorder_text')
        C_Ssgrade = cleaned_data.get('C_Ssgrade')
        C_Ssgrade_text = cleaned_data.get('C_Ssgrade_text')
        C_Family = cleaned_data.get('C_Family')
        C_Family_text = cleaned_data.get('C_Family_text')
        C_Job = cleaned_data.get('C_Job')
        C_Job_text = cleaned_data.get('C_Job_text')
        C_Ecostatus1 = cleaned_data.get('C_Ecostatus1')
        C_Ecostatus2 = cleaned_data.get('C_Ecostatus2')
        C_Ecostatus3 = cleaned_data.get('C_Ecostatus3')
        C_Ecostatus4 = cleaned_data.get('C_Ecostatus4')
        C_Education = cleaned_data.get('C_Education')
        C_Education_text = cleaned_data.get('C_Education_text')

        if C_Jumin[0] == '9':
            age = 2020 - int('19' + C_Jumin[0:2]) + 1
        elif C_Jumin[0] == '0' or C_Jumin[0] =='1':
            age = 2020 - int('20' + C_Jumin[0:2]) + 1
        else:
            0

        # 개인인적사항 db
        bomuser = BomUser(
            C_Name=C_Name,
            REG_Day=REG_Day,
            C_Jumin=C_Jumin,
            age=age,
            F_Coun=F_Coun,
            C_Gender=C_Gender,
            C_Kakaoid=C_Kakaoid,
            C_Tel=C_Tel,
            C_CN=C_CN,
            C_Address1=C_Address1,
            C_Address2=C_Address2,
            C_Residential=C_Residential,
            C_Residential_text=C_Residential_text,
            C_History=C_History,
            C_History_select=C_History_select,
            C_Route=C_Route,
            C_Route_text=C_Route_text,
            C_Institute=C_Institute,
            C_Incharge_name=C_Incharge_name,
            C_Incharge_tel=C_Incharge_tel,
            C_Otherhistory=C_Otherhistory,
            C_Disorder=C_Disorder,
            C_Disorder_text=C_Disorder_text,
            C_Ssgrade=C_Ssgrade,
            C_Ssgrade_text=C_Ssgrade_text,
            C_Family=C_Family,
            C_Family_text=C_Family_text,
            C_Job=C_Job,
            C_Job_text=C_Job_text,
            C_Ecostatus1=C_Ecostatus1,
            C_Ecostatus2=C_Ecostatus2,
            C_Ecostatus3=C_Ecostatus3,
            C_Ecostatus4=C_Ecostatus4,
            C_Education=C_Education,
            C_Education_text=C_Education_text
        )
        bomuser.save()

        chartdata = ChartData(
            C_Name=C_Name,
            REG_Day=REG_Day,
            age=age,
            C_Gender=C_Gender,
            C_Institute=C_Institute,
        )
        chartdata.save()




class DangerForm(forms.Form):
    # 개인인적사항
    ctname = forms.CharField(max_length=10, label='이름',required=False)

    surveys =[
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "0")]
    reverse_surveys =[
    (5, "1"),
    (4, "2"),
    (3, "3"),
    (2, "4"),
    (1, "5"),
    (0, "0")]

    survey1_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey1_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey1_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey1_4 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey1_5 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey2_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey2_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey2_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey2_4 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey2_5 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey3_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey3_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey3_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey3_4 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey3_5 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey4_1 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    survey4_2 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    survey4_3 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    survey4_4 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    
    survey5_1 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    survey5_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey5_3 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    # 추가
    survey5_4 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey5_5 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    survey6_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey6_2 = forms.TypedChoiceField(choices=reverse_surveys, coerce=int, required=False,empty_value = 0)
    survey6_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey7_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey7_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey7_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    # 제거
    # survey8_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    # survey8_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    # survey8_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey9_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey9_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey9_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)

    survey10_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey10_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey10_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey11_1 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey11_2 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey11_3 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    survey11_4 = forms.TypedChoiceField(choices=surveys, coerce=int, required=False,empty_value = 0)
    danger_comment = forms.CharField(widget=forms.Textarea)
    danger_sentence = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        ctname = cleaned_data.get('ctname')
        survey1_1 = cleaned_data.get('survey1_1')
        survey1_2 = cleaned_data.get('survey1_2')
        survey1_3 = cleaned_data.get('survey1_3')
        survey1_4 = cleaned_data.get('survey1_4')
        survey1_5 = cleaned_data.get('survey1_5')
        survey2_1 = cleaned_data.get('survey2_1')
        survey2_2 = cleaned_data.get('survey2_2')
        survey2_3 = cleaned_data.get('survey2_3')
        survey2_4 = cleaned_data.get('survey2_4')
        survey2_5 = cleaned_data.get('survey2_5')
        survey3_1 = cleaned_data.get('survey3_1')
        survey3_2 = cleaned_data.get('survey3_2')
        survey3_3 = cleaned_data.get('survey3_3')
        survey3_4 = cleaned_data.get('survey3_4')
        survey3_5 = cleaned_data.get('survey3_5')

        survey4_1 = cleaned_data.get('survey4_1')
        survey4_2 = cleaned_data.get('survey4_2')
        survey4_3 = cleaned_data.get('survey4_3')
        survey4_4 = cleaned_data.get('survey4_4')

        survey5_1 = cleaned_data.get('survey5_1')
        survey5_2 = cleaned_data.get('survey5_2')
        survey5_3 = cleaned_data.get('survey5_3')
        survey5_4 = cleaned_data.get('survey5_4')
        survey5_5 = cleaned_data.get('survey5_5')
        survey6_1 = cleaned_data.get('survey6_1')
        survey6_2 = cleaned_data.get('survey6_2')
        survey6_3 = cleaned_data.get('survey6_3')
        survey7_1 = cleaned_data.get('survey7_1')
        survey7_2 = cleaned_data.get('survey7_2')
        survey7_3 = cleaned_data.get('survey7_3')
        survey9_1 = cleaned_data.get('survey9_1')
        survey9_2 = cleaned_data.get('survey9_2')
        survey9_3 = cleaned_data.get('survey9_3')
        survey10_1 = cleaned_data.get('survey10_1')
        survey10_2 = cleaned_data.get('survey10_2')
        survey10_3 = cleaned_data.get('survey10_3')
        survey11_1 = cleaned_data.get('survey11_1')
        survey11_2 = cleaned_data.get('survey11_2')
        survey11_3 = cleaned_data.get('survey11_3')
        survey11_4 = cleaned_data.get('survey11_4')

        danger_comment = cleaned_data.get('danger_comment')
        danger_sentence = cleaned_data.get('danger_sentence')
        

    

        # 위기분류  db
        danger = Danger(
            danger_name=ctname,
            survey1_1=survey1_1,
            survey1_2=survey1_2,
            survey1_3=survey1_3,
            survey1_4=survey1_4,
            survey1_5=survey1_5,
            survey2_1=survey2_1,
            survey2_2=survey2_2,
            survey2_3=survey2_3,
            survey2_4=survey2_4,
            survey2_5=survey2_5,
            survey3_1=survey3_1,
            survey3_2=survey3_2,
            survey3_3=survey3_3,
            survey3_4=survey3_4,
            survey3_5=survey3_5,
            survey4_1=survey4_1,
            survey4_2=survey4_2,
            survey4_3=survey4_3,
            survey4_4=survey4_4,

            survey5_1=survey5_1,
            survey5_2=survey5_2,
            survey5_3=survey5_3,
            survey5_4=survey5_4,
            survey5_5=survey5_5,
            survey6_1=survey6_1,
            survey6_2=survey6_2,
            survey6_3=survey6_3,
            survey7_1=survey7_1,
            survey7_2=survey7_2,
            survey7_3=survey7_3,
            survey9_1=survey9_1,
            survey9_2=survey9_2,
            survey9_3=survey9_3,
            survey10_1=survey10_1,
            survey10_2=survey10_2,
            survey10_3=survey10_3,
            survey11_1=survey11_1,
            survey11_2=survey11_2,
            survey11_3=survey11_3,
            survey11_4=survey11_4,
            danger_comment=danger_comment,
            danger_sentence=danger_sentence            
        )
        
        danger.save()        

class SetplanForm(forms.Form):
    #의료지원
    medical_start = forms.DateField()
    medical_end = forms.DateField()
    mental_start = forms.DateField()
    mental_end = forms.DateField()
    case_start = forms.DateField()
    case_end = forms.DateField()
    ctname = forms.CharField(max_length=10, label='이름',required=False)
    medical_A1_MF = forms.IntegerField(required=False, initial=0)
    medical_A1_TF = forms.IntegerField(initial=0)
    medical_A1_Text = forms.CharField(max_length=100, required=False)
    medical_A2_MF = forms.IntegerField(required=False)
    medical_A2_TF = forms.IntegerField()
    medical_A2_Text = forms.CharField(max_length=100, required=False)
    medical_A3_MF = forms.IntegerField()
    medical_A3_TF = forms.IntegerField()
    medical_A3_Text = forms.CharField(max_length=100, required=False)
    medical_A4_MF = forms.IntegerField()
    medical_A4_TF = forms.IntegerField()
    medical_A4_Text = forms.CharField(max_length=100, required=False)
    medical_B1_YN = forms.BooleanField(required=False)
    medical_B1_Text = forms.CharField(max_length=100, required=False)
    medical_B2_YN = forms.BooleanField(required=False)
    medical_B2_Text = forms.CharField(max_length=100, required=False)
    medical_B3_YN = forms.BooleanField(required=False)
    medical_B3_Text = forms.CharField(max_length=100, required=False)
    medical_B4_Name = forms.CharField(max_length=15, required=False)
    medical_B4_YN = forms.BooleanField(required=False)
    medical_B4_Text = forms.CharField(max_length=100, required=False)

    medical_C1_MF = forms.IntegerField()
    medical_C1_TF = forms.IntegerField()
    medical_C1_Text = forms.CharField(max_length=100, required=False)
    medical_C2_MF = forms.IntegerField()
    medical_C2_TF = forms.IntegerField()
    medical_C2_Text = forms.CharField(max_length=100, required=False)
    medical_C3_MF = forms.IntegerField()
    medical_C3_TF = forms.IntegerField()
    medical_C3_Text = forms.CharField(max_length=100, required=False)
    medical_C4_Name = forms.CharField(max_length=15, required=False)
    medical_C4_MF = forms.IntegerField()
    medical_C4_TF = forms.IntegerField()
    medical_C4_Text = forms.CharField(max_length=10, required=False)
    medical_C5_Name = forms.CharField(max_length=15, required=False)
    medical_C5_MF = forms.IntegerField()
    medical_C5_TF = forms.IntegerField()
    medical_C5_Text = forms.CharField(max_length=100, required=False)

    medical_D1_Num = forms.IntegerField()
    medical_D1_Text = forms.CharField(max_length=100, required=False)
    medical_D2_Num = forms.IntegerField()
    medical_D2_Text = forms.CharField(max_length=100, required=False)
    medical_D3_YN = forms.BooleanField(required=False)
    medical_D3_Text = forms.CharField(max_length=100, required=False)
    medical_D4_Name = forms.CharField(max_length=15, required=False)
    medical_D4_TF = forms.IntegerField()
    medical_D4_Text = forms.CharField(max_length=100, required=False)
    medical_D5_Name = forms.CharField(max_length=15, required=False)
    medical_D5_TF = forms.IntegerField()
    medical_D5_Text = forms.CharField(max_length=100, required=False)
    medical_D6_Name = forms.CharField(max_length=15, required=False)
    medical_D6_TF = forms.IntegerField()
    medical_D6_Text = forms.CharField(max_length=100, required=False)

    medical_E1_MF = forms.IntegerField()
    medical_E1_TF = forms.IntegerField()
    medical_E1_Text = forms.CharField(max_length=100, required=False)
    medical_E2_MF = forms.IntegerField()
    medical_E2_TF = forms.IntegerField()
    medical_E2_Text = forms.CharField(max_length=100, required=False)
    medical_E3_Name = forms.CharField(max_length=15, required=False)
    medical_E3_MF = forms.IntegerField()
    medical_E3_TF = forms.IntegerField()
    medical_E3_Text = forms.CharField(max_length=100, required=False)

    medical_F1_MF = forms.IntegerField()
    medical_F1_TF = forms.IntegerField()
    medical_F1_Text = forms.CharField(max_length=100, required=False)
    medical_F2_MF = forms.IntegerField()
    medical_F2_TF = forms.IntegerField()
    medical_F2_Text = forms.CharField(max_length=100, required=False)
    medical_F3_MF = forms.IntegerField()
    medical_F3_TF = forms.IntegerField()
    medical_F3_Text = forms.CharField(max_length=100, required=False)
    medical_F4_Name = forms.CharField(max_length=15, required=False)
    medical_F4_MF = forms.IntegerField()
    medical_F4_TF = forms.IntegerField()
    medical_F4_Text = forms.CharField(max_length=100, required=False)

    # 심리지원
    mental_A1_MF = forms.IntegerField()
    mental_A1_TF = forms.IntegerField()
    mental_A1_Text = forms.CharField(max_length=100, required=False)
    mental_A2_MF = forms.IntegerField()
    mental_A2_TF = forms.IntegerField()
    mental_A2_Text = forms.CharField(max_length=100, required=False)
    mental_B1_TF = forms.IntegerField()
    mental_B2_Name = forms.CharField(max_length=15, required=False)
    mental_B2_TF = forms.IntegerField()
    mental_C1_MF = forms.IntegerField()
    mental_C1_TF = forms.IntegerField()
    mental_C1_Text = forms.CharField(max_length=100, required=False)
    mental_C2_MF = forms.IntegerField()
    mental_C2_TF = forms.IntegerField()
    mental_C2_Text = forms.CharField(max_length=100, required=False)
    mental_C3_Name = forms.CharField(max_length=15, required=False)
    mental_C3_MF = forms.IntegerField()
    mental_C3_TF = forms.IntegerField()
    mental_C3_Text = forms.CharField(max_length=100, required=False)

    # 사례지원
    case_A1_MF = forms.IntegerField()
    case_A1_TF = forms.IntegerField()
    case_A1_Text = forms.CharField(max_length=300, required=False)
    case_A2_MF = forms.IntegerField()
    case_A2_TF = forms.IntegerField()
    case_A2_Text = forms.CharField(max_length=300, required=False)
    case_A3_MF = forms.IntegerField()
    case_A3_TF = forms.IntegerField()
    case_A3_Text = forms.CharField(max_length=300, required=False)
    case_A4_MF = forms.IntegerField()
    case_A4_TF = forms.IntegerField()
    case_A4_Text = forms.CharField(max_length=300, required=False)
    case_B1_MF = forms.IntegerField()
    case_B1_TF = forms.IntegerField()
    case_B1_Text = forms.CharField(max_length=100, required=False)
    case_B2_MF = forms.IntegerField()
    case_B2_TF = forms.IntegerField()
    case_B2_Text = forms.CharField(max_length=100, required=False)
    case_B3_Name = forms.CharField(max_length=15, required=False)
    case_B3_MF = forms.IntegerField()
    case_B3_TF = forms.IntegerField()
    case_B3_Text = forms.CharField(max_length=100, required=False)
    case_C1_MF = forms.IntegerField()
    case_C1_TF = forms.IntegerField()
    case_C1_Text = forms.CharField(max_length=100, required=False)
    case_C2_MF = forms.IntegerField()
    case_C2_TF = forms.IntegerField()
    case_C2_Text = forms.CharField(max_length=100, required=False)
    case_C3_MF = forms.IntegerField()
    case_C3_TF = forms.IntegerField()
    case_C3_Text = forms.CharField(max_length=100, required=False)
    case_C4_MF = forms.IntegerField()
    case_C4_TF = forms.IntegerField()
    case_C4_Text = forms.CharField(max_length=100, required=False)

    setplan_comment = forms.CharField(widget=forms.Textarea)
    setplan_sentence = forms.CharField(widget=forms.Textarea)

    
    

    def clean(self):
        cleaned_data = super().clean()
        medical_start = cleaned_data.get('medical_start')
        medical_end = cleaned_data.get('medical_end')
        mental_start = cleaned_data.get('mental_start')
        mental_end = cleaned_data.get('mental_end')
        case_start = cleaned_data.get('case_start')
        case_end = cleaned_data.get('case_end')
        # 의료지원
        ctname = cleaned_data.get('ctname')
        medical_A1_MF = cleaned_data.get('medical_A1_MF')
        medical_A1_TF = cleaned_data.get('medical_A1_TF')
        medical_A1_Text = cleaned_data.get('medical_A1_Text')
        medical_A2_MF = cleaned_data.get('medical_A2_MF')
        medical_A2_TF = cleaned_data.get('medical_A2_TF')
        medical_A2_Text = cleaned_data.get('medical_A2_Text')
        medical_A3_MF = cleaned_data.get('medical_A3_MF')
        medical_A3_TF = cleaned_data.get('medical_A3_TF')
        medical_A3_Text = cleaned_data.get('medical_A3_Text')
        medical_A4_MF = cleaned_data.get('medical_A4_MF')
        medical_A4_TF = cleaned_data.get('medical_A4_TF')
        medical_A4_Text = cleaned_data.get('medical_A4_Text')
        medical_B1_YN = cleaned_data.get('medical_B1_YN')
        medical_B1_Text = cleaned_data.get('medical_B1_Text')
        medical_B2_YN = cleaned_data.get('medical_B2_YN')
        medical_B2_Text = cleaned_data.get('medical_B2_Text')
        medical_B3_YN = cleaned_data.get('medical_B3_YN')
        medical_B3_Text = cleaned_data.get('medical_B3_Text')
        medical_B4_YN = cleaned_data.get('medical_B4_YN')
        medical_B4_Name = cleaned_data.get('medical_B4_Name')
        medical_B4_Text = cleaned_data.get('medical_B4_Text')

        medical_C1_MF = cleaned_data.get('medical_C1_MF')
        medical_C1_TF = cleaned_data.get('medical_C1_TF')
        medical_C1_Text = cleaned_data.get('medical_C1_Text')
        medical_C2_MF = cleaned_data.get('medical_C2_MF')
        medical_C2_TF = cleaned_data.get('medical_C2_TF')
        medical_C2_Text = cleaned_data.get('medical_C2_Text')
        medical_C3_MF = cleaned_data.get('medical_C3_MF')
        medical_C3_TF = cleaned_data.get('medical_C3_TF')
        medical_C3_Text = cleaned_data.get('medical_C3_Text')
        medical_C4_Name = cleaned_data.get('medical_C4_Name')
        medical_C4_MF = cleaned_data.get('medical_C4_MF')
        medical_C4_TF = cleaned_data.get('medical_C4_TF')
        medical_C4_Text = cleaned_data.get('medical_C4_Text')
        medical_C5_Name = cleaned_data.get('medical_C5_Name')
        medical_C5_MF = cleaned_data.get('medical_C5_MF')
        medical_C5_TF = cleaned_data.get('medical_C5_TF')
        medical_C5_Text = cleaned_data.get('medical_C5_Text')

        medical_D1_Num = cleaned_data.get('medical_D1_Num')
        medical_D1_Text = cleaned_data.get('medical_D1_Text')
        medical_D2_Num = cleaned_data.get('medical_D2_Num')
        medical_D2_Text = cleaned_data.get('medical_D2_Text')
        medical_D3_YN = cleaned_data.get('medical_D3_YN')
        medical_D3_Text = cleaned_data.get('medical_D3_Text')
        medical_D4_Name = cleaned_data.get('medical_D4_Name')
        medical_D4_TF = cleaned_data.get('medical_D4_TF')
        medical_D4_Text = cleaned_data.get('medical_D4_Text')
        medical_D5_Name = cleaned_data.get('medical_D5_Name')
        medical_D5_TF = cleaned_data.get('medical_D5_TF')
        medical_D5_Text = cleaned_data.get('medical_D5_Text')
        medical_D6_Name = cleaned_data.get('medical_D6_Name')
        medical_D6_TF = cleaned_data.get('medical_D6_TF')
        medical_D6_Text = cleaned_data.get('medical_D6_Text')

        medical_E1_MF = cleaned_data.get('medical_E1_MF')
        medical_E1_TF = cleaned_data.get('medical_E1_TF')
        medical_E1_Text = cleaned_data.get('medical_E1_Text')
        medical_E2_MF = cleaned_data.get('medical_E2_MF')
        medical_E2_TF = cleaned_data.get('medical_E2_TF')
        medical_E2_Text = cleaned_data.get('medical_E2_Text')
        medical_E3_Name = cleaned_data.get('medical_E3_Name')
        medical_E3_MF = cleaned_data.get('medical_E3_MF')
        medical_E3_TF = cleaned_data.get('medical_E3_TF')
        medical_E3_Text = cleaned_data.get('medical_E3_Text')

        medical_F1_MF = cleaned_data.get('medical_F1_MF')
        medical_F1_TF = cleaned_data.get('medical_F1_TF')
        medical_F1_Text = cleaned_data.get('medical_F1_Text')
        medical_F2_MF = cleaned_data.get('medical_F2_MF')
        medical_F2_TF = cleaned_data.get('medical_F2_TF')
        medical_F2_Text = cleaned_data.get('medical_F2_Text')
        medical_F3_MF = cleaned_data.get('medical_F3_MF')
        medical_F3_TF = cleaned_data.get('medical_F3_TF')
        medical_F3_Text = cleaned_data.get('medical_F3_Text')
        medical_F4_Name = cleaned_data.get('medical_F4_Name')
        medical_F4_MF = cleaned_data.get('medical_F4_MF')
        medical_F4_TF = cleaned_data.get('medical_F4_TF')
        medical_F4_Text = cleaned_data.get('medical_F4_Text')

        # 심리지원
        mental_A1_MF = cleaned_data.get('mental_A1_MF')
        mental_A1_TF = cleaned_data.get('mental_A1_TF')
        mental_A1_Text = cleaned_data.get('mental_A1_Text')
        mental_A2_MF = cleaned_data.get('mental_A2_MF')
        mental_A2_TF = cleaned_data.get('mental_A2_TF')
        mental_A2_Text = cleaned_data.get('mental_A2_Text')
        mental_B1_TF = cleaned_data.get('mental_B1_TF')
        mental_B2_Name = cleaned_data.get('mental_B2_Name')
        mental_B2_TF = cleaned_data.get('mental_B2_TF')
        mental_C1_MF = cleaned_data.get('mental_C1_MF')
        mental_C1_TF = cleaned_data.get('mental_C1_TF')
        mental_C1_Text = cleaned_data.get('mental_C1_Text')
        mental_C2_MF = cleaned_data.get('mental_C2_MF')
        mental_C2_TF = cleaned_data.get('mental_C2_TF')
        mental_C2_Text = cleaned_data.get('mental_C2_Text')
        mental_C3_Name = cleaned_data.get('mental_C3_Name')
        mental_C3_MF = cleaned_data.get('mental_C3_MF')
        mental_C3_TF = cleaned_data.get('mental_C3_TF')
        mental_C3_Text = cleaned_data.get('mental_C3_Text')

        # 사례지원
        case_A1_MF = cleaned_data.get('case_A1_MF')
        case_A1_TF = cleaned_data.get('case_A1_TF = cleaned_data')
        case_A1_Text = cleaned_data.get('case_A1_Text')
        case_A2_MF = cleaned_data.get('case_A2_MF')
        case_A2_TF = cleaned_data.get('case_A2_TF')
        case_A2_Text = cleaned_data.get('case_A2_Text')
        case_A3_MF = cleaned_data.get('case_A3_MF')
        case_A3_TF = cleaned_data.get('case_A3_TF')
        case_A3_Text = cleaned_data.get('case_A3_Text')
        case_A4_MF = cleaned_data.get('case_A4_MF')
        case_A4_TF = cleaned_data.get('case_A4_TF')
        case_A4_Text = cleaned_data.get('case_A4_Text')
        case_B1_MF = cleaned_data.get('case_B1_MF')
        case_B1_TF = cleaned_data.get('case_B1_TF')
        case_B1_Text = cleaned_data.get('case_B1_Text')
        case_B2_MF = cleaned_data.get('case_B2_MF')
        case_B2_TF = cleaned_data.get('case_B2_TF')
        case_B2_Text = cleaned_data.get('case_B2_Text')
        case_B3_Name = cleaned_data.get('case_B3_Name')
        case_B3_MF = cleaned_data.get('case_B3_MF')
        case_B3_TF = cleaned_data.get('case_B3_TF')
        case_B3_Text = cleaned_data.get('case_B3_Text')
        case_C1_MF = cleaned_data.get('case_C1_MF')
        case_C1_TF = cleaned_data.get('case_C1_TF')
        case_C1_Text = cleaned_data.get('case_C1_Text')
        case_C2_MF = cleaned_data.get('case_C2_MF')
        case_C2_TF = cleaned_data.get('case_C2_TF')
        case_C2_Text = cleaned_data.get('case_C2_Text')
        case_C3_MF = cleaned_data.get('case_C3_MF')
        case_C3_TF = cleaned_data.get('case_C3_TF')
        case_C3_Text = cleaned_data.get('case_C3_Text')
        case_C4_MF = cleaned_data.get('case_C4_MF')
        case_C4_TF = cleaned_data.get('case_C4_TF')
        case_C4_Text = cleaned_data.get('case_C4_Text')
        setplan_comment = cleaned_data.get('setplan_comment')
        setplan_sentence = cleaned_data.get('setplan_sentence')

        if type(medical_A1_TF) != int:
            medical_A1_TF = 0
        if type(medical_A2_TF) != int:
            medical_A2_TF = 0
        if type(medical_A3_TF) != int:
            medical_A3_TF = 0
        if type(medical_A4_TF) != int:
            medical_A4_TF = 0

        if type(medical_C1_TF) != int:
            medical_C1_TF = 0
        if type(medical_C2_TF) != int:
            medical_C2_TF = 0
        if type(medical_C3_TF) != int:
            medical_C3_TF = 0
        if type(medical_C4_TF) != int:
            medical_C4_TF = 0
        if type(medical_C5_TF) != int:
            medical_C5_TF = 0

        if type(medical_D1_Num) != int:
            medical_D1_Num = 0
        if type(medical_D2_Num) != int:
            medical_D2_Num = 0
        if type(medical_D4_TF) != int:
            medical_D4_TF = 0
        if type(medical_D5_TF) != int:
            medical_D5_TF = 0
        if type(medical_D6_TF) != int:
            medical_D6_TF = 0

        if type(medical_E1_TF) != int:
            medical_E1_TF = 0
        if type(medical_E2_TF) != int:
            medical_E2_TF = 0
        if type(medical_E3_TF) != int:
            medical_E3_TF = 0

        if type(medical_F1_TF) != int:
            medical_F1_TF = 0
        if type(medical_F2_TF) != int:
            medical_F2_TF = 0
        if type(medical_F3_TF) != int:
            medical_F3_TF = 0
        if type(medical_F4_TF) != int:
            medical_F4_TF = 0

        if type(mental_A1_TF) != int:
            mental_A1_TF = 0
        if type(mental_A2_TF) != int:
            mental_A2_TF = 0

        if type(mental_B1_TF) != int:
            mental_B1_TF = 0
        if type(mental_B2_TF) != int:
            mental_B2_TF = 0

        if type(mental_C1_TF) != int:
            mental_C1_TF = 0
        if type(mental_C2_TF) != int:
            mental_C2_TF = 0
        if type(mental_C3_TF) != int:
            mental_C3_TF = 0

        if type(case_A1_TF) != int:
            case_A1_TF = 0
        if type(case_A2_TF) != int:
            case_A2_TF = 0
        if type(case_A3_TF) != int:
            case_A3_TF = 0
        if type(case_A4_TF) != int:
            case_A4_TF = 0
        
        if type(case_B1_TF) != int:
            case_B1_TF = 0
        if type(case_B2_TF) != int:
            case_B2_TF = 0
        if type(case_B3_TF) != int:
            case_B3_TF = 0

        if type(case_C1_TF) != int:
            case_C1_TF = 0
        if type(case_C2_TF) != int:
            case_C2_TF = 0
        if type(case_C3_TF) != int:
            case_C3_TF = 0
        if type(case_C4_TF) != int:
            case_C4_TF = 0
        



        # 사례지원계획 db
        bomsetplan = BomSetPlan(
            setplan_name=ctname,
            medical_start=medical_start,
            medical_end=medical_end,
            mental_start=mental_start,
            mental_end=mental_end,
            case_start=case_start,
            case_end=case_end,
            # set_A = set_A,
            medical_A1_MF=medical_A1_MF,
            medical_A1_TF=medical_A1_TF,
            medical_A1_Text=medical_A1_Text,
            medical_A2_MF=medical_A2_MF,
            medical_A2_TF=medical_A2_TF,
            medical_A2_Text=medical_A2_Text,
            medical_A3_MF=medical_A3_MF,
            medical_A3_TF=medical_A3_TF,
            medical_A3_Text=medical_A3_Text,
            medical_A4_MF=medical_A4_MF,
            medical_A4_TF=medical_A4_TF,
            medical_A4_Text=medical_A4_Text,
            medical_B1_YN=medical_B1_YN,
            medical_B1_Text=medical_B1_Text,
            medical_B2_YN=medical_B2_YN,
            medical_B2_Text=medical_B2_Text,
            medical_B3_YN=medical_B3_YN,
            medical_B3_Text=medical_B3_Text,
            medical_B4_Name=medical_B4_Name,
            medical_B4_YN=medical_B4_YN,
            medical_B4_Text=medical_B4_Text, 

            medical_C1_MF=medical_C1_MF,
            medical_C1_TF=medical_C1_TF,
            medical_C1_Text=medical_C1_Text,
            medical_C2_MF=medical_C2_MF,
            medical_C2_TF=medical_C2_TF,
            medical_C2_Text=medical_C2_Text,
            medical_C3_MF=medical_C3_MF,
            medical_C3_TF=medical_C3_TF,
            medical_C3_Text=medical_C3_Text,
            medical_C4_Name=medical_C4_Name,
            medical_C4_MF=medical_C4_MF,
            medical_C4_TF=medical_C4_TF,
            medical_C4_Text=medical_C4_Text,
            medical_C5_Name=medical_C5_Name,
            medical_C5_MF=medical_C5_MF,
            medical_C5_TF=medical_C5_TF,
            medical_C5_Text=medical_C5_Text,

            medical_D1_Num=medical_D1_Num,
            medical_D1_Text=medical_D1_Text,
            medical_D2_Num=medical_D2_Num,
            medical_D2_Text=medical_D2_Text,
            medical_D3_YN=medical_D3_YN,
            medical_D3_Text=medical_D3_Text,
            medical_D4_Name=medical_D4_Name,
            medical_D4_TF=medical_D4_TF,
            medical_D4_Text=medical_D4_Text,
            medical_D5_Name=medical_D5_Name,
            medical_D5_TF=medical_D5_TF,
            medical_D5_Text=medical_D5_Text,
            medical_D6_Name=medical_D6_Name,
            medical_D6_TF=medical_D6_TF,
            medical_D6_Text=medical_D6_Text,

            medical_E1_MF=medical_E1_MF,
            medical_E1_TF=medical_E1_TF,
            medical_E1_Text=medical_E1_Text,
            medical_E2_MF=medical_E2_MF,
            medical_E2_TF=medical_E2_TF,
            medical_E2_Text=medical_E2_Text,
            medical_E3_Name=medical_E3_Name,
            medical_E3_MF=medical_E3_MF,
            medical_E3_TF=medical_E3_TF,
            medical_E3_Text=medical_E3_Text,

            medical_F1_MF=medical_F1_MF,
            medical_F1_TF=medical_F1_TF,
            medical_F1_Text=medical_F1_Text,
            medical_F2_MF=medical_F2_MF,
            medical_F2_TF=medical_F2_TF,
            medical_F2_Text=medical_F2_Text,
            medical_F3_MF=medical_F3_MF,
            medical_F3_TF=medical_F3_TF,
            medical_F3_Text=medical_F3_Text,
            medical_F4_Name=medical_F4_Name,
            medical_F4_MF=medical_F4_MF,
            medical_F4_TF=medical_F4_TF,
            medical_F4_Text=medical_F4_Text,
            
            # 심리지원
            mental_A1_MF=mental_A1_MF,
            mental_A1_TF=mental_A1_TF,
            mental_A1_Text=mental_A1_Text,
            mental_A2_MF=mental_A2_MF,
            mental_A2_TF=mental_A2_TF,
            mental_A2_Text=mental_A2_Text,
            mental_B1_TF=mental_B1_TF,
            mental_B2_Name=mental_B2_Name,
            mental_B2_TF=mental_B2_TF,
            mental_C1_MF=mental_C1_MF,
            mental_C1_TF=mental_C1_TF,
            mental_C1_Text=mental_C1_Text,
            mental_C2_MF=mental_C2_MF,
            mental_C2_TF=mental_C2_TF,
            mental_C2_Text=mental_C2_Text,
            mental_C3_Name=mental_C3_Name,
            mental_C3_MF=mental_C3_MF,
            mental_C3_TF=mental_C3_TF,
            mental_C3_Text=mental_C3_Text,

            # 사례지원
            case_A1_MF=case_A1_MF,
            case_A1_TF=case_A1_TF,
            case_A1_Text=case_A1_Text,
            case_A2_MF=case_A2_MF,
            case_A2_TF=case_A2_TF,
            case_A2_Text=case_A2_Text,
            case_A3_MF=case_A3_MF,
            case_A3_TF=case_A3_TF,
            case_A3_Text=case_A3_Text,
            case_A4_MF=case_A4_MF,
            case_A4_TF=case_A4_TF,
            case_A4_Text=case_A4_Text,
            case_B1_MF=case_B1_MF,
            case_B1_TF=case_B1_TF,
            case_B1_Text=case_B1_Text,
            case_B2_MF=case_B2_MF,
            case_B2_TF=case_B2_TF,
            case_B2_Text=case_B2_Text,
            case_B3_Name=case_B3_Name,
            case_B3_MF=case_B3_MF,
            case_B3_TF=case_B3_TF,
            case_B3_Text=case_B3_Text,
            case_C1_MF=case_C1_MF,
            case_C1_TF=case_C1_TF,
            case_C1_Text=case_C1_Text,
            case_C2_MF=case_C2_MF,
            case_C2_TF=case_C2_TF,
            case_C2_Text=case_C2_Text,
            case_C3_MF=case_C3_MF,
            case_C3_TF=case_C3_TF,
            case_C3_Text=case_C3_Text,
            case_C4_MF=case_C4_MF,
            case_C4_TF=case_C4_TF,
            case_C4_Text=case_C4_Text,
            setplan_comment=setplan_comment,
            setplan_sentence=setplan_sentence,

            # medical_A1_TF=medical_A1_TF,
            # medical_A2_TF=medical_A2_TF,
            # medical_A3_TF=medical_A3_TF,
            # medical_A4_TF=medical_A4_TF,
            sum_medical_A=medical_A1_TF+medical_A2_TF+medical_A3_TF+medical_A4_TF,
            sum_medical_B=medical_B1_YN+medical_B2_YN+medical_B3_YN+medical_B4_YN,
            sum_medical_C=medical_C1_TF+medical_C2_TF+medical_C3_TF+medical_C4_TF+medical_C5_TF,
            sum_medical_D=medical_D1_Num+medical_D2_Num+medical_D3_YN+medical_D4_TF+medical_D5_TF+medical_D6_TF,
            sum_medical_E=medical_E1_TF+medical_E2_TF+medical_E3_TF,
            sum_medical_F=medical_F1_TF+medical_F2_TF+medical_F3_TF+medical_F4_TF,
            sum_mental_A=mental_A1_TF+mental_A2_TF,
            sum_mental_B=mental_B1_TF+mental_B2_TF,
            sum_mental_C=mental_C1_TF+mental_C2_TF+mental_C3_TF,
            sum_case_A=case_A1_TF+case_A2_TF+case_A3_TF+case_A4_TF,
            sum_case_B=case_B1_TF+case_B2_TF+case_B3_TF,
            sum_case_C=case_C1_TF+case_C2_TF+case_C3_TF+case_C4_TF

           
        )
        
        bomsetplan.save()
        
        # 이미 해당하는 이름이 있으면 merge해버리기(해야함)
        # chartdata = ChartData(
        #     C_Name=ctname,
        #     medical_A1_TF=medical_A1_TF,
        #     medical_A2_TF=medical_A2_TF,
        #     medical_A3_TF=medical_A3_TF,
        #     medical_A4_TF=medical_A4_TF,
        #     sum_medical_A=medical_A1_TF+medical_A2_TF+medical_A3_TF+medical_A4_TF,
        #     sum_medical_B=medical_B1_YN+medical_B2_YN+medical_B3_YN+medical_B4_YN,
        #     sum_medical_C=medical_C1_TF+medical_C2_TF+medical_C3_TF+medical_C4_TF+medical_C5_TF,
        #     sum_medical_D=medical_D1_Num+medical_D2_Num+medical_D3_YN+medical_D4_TF+medical_D5_TF+medical_D6_TF,
        #     sum_medical_E=medical_E1_TF+medical_E2_TF+medical_E3_TF,
        #     sum_medical_F=medical_F1_TF+medical_F2_TF+medical_F3_TF+medical_F4_TF,
        #     sum_mental_A=mental_A1_TF+mental_A2_TF,
        #     sum_mental_B=mental_B1_TF+mental_B2_TF,
        #     sum_mental_C=mental_C1_TF+mental_C2_TF+mental_C3_TF,
        #     sum_case_A=case_A1_TF+case_A2_TF+case_A3_TF+case_A4_TF,
        #     sum_case_B=case_B1_TF+case_B2_TF+case_B3_TF,
        #     sum_case_C=case_C1_TF+case_C2_TF+case_C3_TF+case_C4_TF
        # )
        # chartdata.save()



class GetplanForm(forms.Form):

    ctname = forms.CharField(max_length=10, label='이름',required=False)
    getplan_date = forms.DateField()
    # 의료지원
    inmedical_A1_YN = forms.BooleanField(required=False)
    inmedical_A1_YN2 = forms.BooleanField(required=False)
    den =[
    ('스켈링', '스켈링'),
    ('보철', '보철'),
    ('충치','충치'),
    ('기타','기타')]
    inmedical_A1_select = forms.ChoiceField(choices=den, label='치과 진료명',required=False)
    inmedical_A1_C = forms.IntegerField(required=False, initial=0)
    inmedical_A1_Text = forms.CharField(max_length=70, required=False)
    inmedical_A2_YN = forms.BooleanField(required=False, initial=0)
    inmedical_A2_YN2 = forms.BooleanField(required=False, initial='0')
    inmedical_A2_Text = forms.CharField(max_length=70, required=False)
    inmedical_A3_YN = forms.BooleanField(required=False, initial='0')
    inmedical_A3_YN2 = forms.BooleanField(required=False, initial='0')
    inmedical_A3_Text = forms.CharField(max_length=70, required=False)
    inmedical_A4_YN = forms.BooleanField(required=False, initial='0')
    inmedical_A4_YN2 = forms.BooleanField(required=False, initial='0')
    inmedical_A4_Text = forms.CharField(max_length=70, required=False)

    inmedical_B1_YN = forms.BooleanField(required=False, initial='0')
    inmedical_B1_C = forms.IntegerField(required=False, initial='0')
    inmedical_B1_Text = forms.CharField(max_length=70, required=False)
    inmedical_B2_YN = forms.BooleanField(required=False, initial='0')
    inmedical_B2_C = forms.IntegerField(required=False, initial='0')
    inmedical_B2_Text = forms.CharField(max_length=70, required=False)
    inmedical_B3_YN = forms.BooleanField(required=False, initial='0')
    inmedical_B3_C = forms.IntegerField(required=False, initial='0')
    inmedical_B3_Text = forms.CharField(max_length=70, required=False)
    inmedical_B4_Name = forms.CharField(max_length=15, required=False)
    inmedical_B4_YN = forms.BooleanField(required=False, initial='0')
    inmedical_B4_C = forms.IntegerField(required=False, initial='0')
    inmedical_B4_Text = forms.CharField(max_length=70, required=False)

    inmedical_C1_YN = forms.BooleanField(required=False)
    inmedical_C1_Text = forms.CharField(max_length=70, required=False)
    inmedical_C2_YN = forms.BooleanField(required=False)
    inmedical_C2_C = forms.IntegerField(required=False)
    inmedical_C2_Text = forms.CharField(max_length=70, required=False)

    inmedical_C3_YN = forms.BooleanField(required=False)
    inmedical_C3_F = forms.IntegerField(required=False, initial='0')
    inmedical_C3_C = forms.IntegerField(required=False)
    inmedical_C3_Text = forms.CharField(max_length=70, required=False)
    
    inmedical_C4_Name = forms.CharField(max_length=15, required=False)
    inmedical_C4_Text = forms.CharField(max_length=70, required=False)
    inmedical_C4_YN = forms.BooleanField(required=False)
    inmedical_C5_Name = forms.CharField(max_length=15, required=False)
    inmedical_C5_YN = forms.BooleanField(required=False)
    inmedical_C5_Text = forms.CharField(max_length=70, required=False)

    inmedical_D1_Num = forms.IntegerField()
    inmedical_D1_C = forms.IntegerField(required=False)
    inmedical_D1_Text = forms.CharField(max_length=70, required=False)
    inmedical_D2_Num = forms.IntegerField()
    inmedical_D2_C = forms.IntegerField(required=False)
    inmedical_D2_Text = forms.CharField(max_length=70, required=False)
    inmedical_D3_YN = forms.BooleanField(required=False)
    inmedical_D3_C = forms.IntegerField(required=False)
    inmedical_D3_Text = forms.CharField(max_length=70, required=False)
    inmedical_D4_Name = forms.CharField(max_length=15, required=False)
    inmedical_D4_YN = forms.BooleanField(required=False)
    inmedical_D4_C = forms.IntegerField(required=False)
    inmedical_D4_Text = forms.CharField(max_length=70, required=False)
    inmedical_D5_Name = forms.CharField(max_length=15, required=False)
    inmedical_D5_YN = forms.BooleanField(required=False)
    inmedical_D5_C = forms.IntegerField(required=False)
    inmedical_D5_Text = forms.CharField(max_length=70, required=False)
    inmedical_D6_Name = forms.CharField(max_length=15, required=False)
    inmedical_D6_YN = forms.BooleanField(required=False)
    inmedical_D6_C = forms.IntegerField(required=False)
    inmedical_D6_Text = forms.CharField(max_length=70, required=False)

    inmedical_E1_YN = forms.BooleanField(required=False)
    inmedical_E1_C = forms.IntegerField(required=False)
    inmedical_E1_Text = forms.CharField(max_length=70, required=False)
    inmedical_E2_YN = forms.BooleanField(required=False)
    inmedical_E2_C = forms.IntegerField(required=False)
    inmedical_E2_Text = forms.CharField(max_length=70, required=False)
    inmedical_E3_Name = forms.CharField(max_length=15, required=False)
    inmedical_E3_YN = forms.BooleanField(required=False)
    inmedical_E3_C = forms.IntegerField(required=False)
    inmedical_E3_Text = forms.CharField(max_length=70, required=False)

    inmedical_F1_YN = forms.BooleanField(required=False)
    inmedical_F1_Text = forms.CharField(max_length=70, required=False)
    inmedical_F2_YN = forms.BooleanField(required=False)
    inmedical_F2_C = forms.IntegerField(required=False)
    inmedical_F2_Text = forms.CharField(max_length=70, required=False)
    inmedical_F3_YN = forms.BooleanField(required=False)
    inmedical_F3_Text = forms.CharField(max_length=70, required=False)
    inmedical_F4_Name = forms.CharField(max_length=15, required=False)
    inmedical_F4_YN = forms.BooleanField(required=False)
    inmedical_F4_Text = forms.CharField(max_length=70, required=False)

    medical =[
    ('대면', '대면'),
    ('전화', '전화'),
    ('SNS', 'SNS')]
    inmedical_G1 = forms.ChoiceField(choices=medical, label='의료상담',required=False)
    inmedical_G1_Text = forms.CharField(widget=forms.Textarea)


    # 심리지원
    inmental_A1_YN = forms.BooleanField(required=False)
    inmental_A1_C = forms.IntegerField(required=False)
    inmental_A1_Text = forms.CharField(max_length=70, required=False)
    inmental_A2_YN = forms.BooleanField(required=False)
    inmental_A2_C = forms.IntegerField(required=False)
    inmental_A2_Text = forms.CharField(max_length=70, required=False)

    inmental_B1_YN = forms.BooleanField(required=False)
    inmental_B1_C = forms.IntegerField(required=False)
    inmental_B1_Text = forms.CharField(max_length=70, required=False)
    inmental_B2_Name = forms.CharField(max_length=15, required=False)
    inmental_B2_YN = forms.BooleanField(required=False)
    inmental_B2_C = forms.IntegerField(required=False)
    inmental_B2_Text = forms.CharField(max_length=70, required=False)
    
    inmental_C1_YN = forms.BooleanField(required=False)
    inmental_C1_Text = forms.CharField(max_length=70, required=False)
    inmental_C2_YN = forms.BooleanField(required=False)
    inmental_C2_Text = forms.CharField(max_length=70, required=False)
    inmental_C3_name = forms.CharField(max_length=15, required=False)
    inmental_C3_YN = forms.BooleanField(required=False)
    inmental_C3_Text = forms.CharField(max_length=70, required=False)

    # 사례관리
    incase_A1_YN = forms.BooleanField(required=False)
    incase_A1_YN2 = forms.BooleanField(required=False)
    incase_A1_Text = forms.CharField(max_length=200, required=False)
    incase_A2_YN = forms.BooleanField(required=False)
    incase_A2_YN2 = forms.BooleanField(required=False)
    incase_A2_Text = forms.CharField(max_length=200, required=False)
    incase_A3_YN = forms.BooleanField(required=False)
    incase_A3_YN2 = forms.BooleanField(required=False)
    incase_A3_Text = forms.CharField(max_length=200, required=False)
    incase_A4_YN = forms.BooleanField(required=False)
    incase_A4_YN2 = forms.BooleanField(required=False)
    incase_A4_Text = forms.CharField(max_length=200, required=False)

    incase_B1_YN = forms.BooleanField(required=False)
    incase_B1_Text = forms.CharField(max_length=70, required=False)
    incase_B2_YN = forms.BooleanField(required=False)
    incase_B2_Text = forms.CharField(max_length=70, required=False)
    incase_B3_Name = forms.CharField(max_length=15, required=False)
    incase_B3_YN = forms.BooleanField(required=False)
    incase_B3_Text = forms.CharField(max_length=70, required=False)

    incase_C1_YN = forms.BooleanField(required=False)
    incase_C1_Text = forms.CharField(max_length=100, required=False)
    incase_C2_YN = forms.BooleanField(required=False)
    incase_C2_Text = forms.CharField(max_length=100, required=False)
    incase_C3_YN = forms.BooleanField(required=False)
    incase_C3_Text = forms.CharField(max_length=100, required=False)
    incase_C4_YN = forms.BooleanField(required=False)
    incase_C4_Text = forms.CharField(max_length=100, required=False)
    incase_C5_TC = forms.IntegerField(required=False)

    getplan_comment = forms.CharField(widget=forms.Textarea)
    getplan_sentence = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        ctname = cleaned_data.get('ctname')
        getplan_date = cleaned_data.get('getplan_date')
        inmedical_A1_YN = cleaned_data.get('inmedical_A1_YN')
        inmedical_A1_YN2 = cleaned_data.get('inmedical_A1_YN2')
        inmedical_A1_select = cleaned_data.get('inmedical_A1_select')
        inmedical_A1_C = cleaned_data.get('inmedical_A1_C')
        inmedical_A1_Text = cleaned_data.get('inmedical_A1_Text')
        inmedical_A2_YN = cleaned_data.get('inmedical_A2_YN')
        inmedical_A2_YN2 = cleaned_data.get('inmedical_A2_YN2')
        inmedical_A2_Text = cleaned_data.get('inmedical_A2_Text')
        inmedical_A3_YN = cleaned_data.get('inmedical_A3_YN')
        inmedical_A3_YN2 = cleaned_data.get('inmedical_A3_YN2')
        inmedical_A3_Text = cleaned_data.get('inmedical_A3_Text')
        inmedical_A4_YN = cleaned_data.get('inmedical_A4_YN')
        inmedical_A4_YN2 = cleaned_data.get('inmedical_A4_YN2')
        inmedical_A4_Text = cleaned_data.get('inmedical_A4_Text')

        inmedical_B1_YN = cleaned_data.get('inmedical_B1_YN')
        inmedical_B1_C = cleaned_data.get('inmedical_B1_C')
        inmedical_B1_Text = cleaned_data.get('inmedical_B1_Text')
        inmedical_B2_YN = cleaned_data.get('inmedical_B2_YN')
        inmedical_B2_C = cleaned_data.get('inmedical_B2_C')
        inmedical_B2_Text = cleaned_data.get('inmedical_B2_Text')
        inmedical_B3_YN = cleaned_data.get('inmedical_B3_YN')
        inmedical_B3_C = cleaned_data.get('inmedical_B3_C')
        inmedical_B3_Text = cleaned_data.get('inmedical_B3_Text')
        inmedical_B4_Name = cleaned_data.get('inmedical_B4_Name')
        inmedical_B4_YN = cleaned_data.get('inmedical_B4_YN')
        inmedical_B4_C = cleaned_data.get('inmedical_B4_C')
        inmedical_B4_Text = cleaned_data.get('inmedical_B4_Text')

        inmedical_C1_YN = cleaned_data.get('inmedical_C1_YN')
        inmedical_C1_Text = cleaned_data.get('inmedical_C1_Text')
        inmedical_C2_YN = cleaned_data.get('inmedical_C2_YN')
        inmedical_C2_C = cleaned_data.get('inmedical_C2_C')
        inmedical_C2_Text = cleaned_data.get('inmedical_C2_Text')
        inmedical_C3_YN = cleaned_data.get('inmedical_C3_YN')
        inmedical_C3_F = cleaned_data.get('inmedical_C3_F')
        inmedical_C3_C = cleaned_data.get('inmedical_C3_C')
        inmedical_C3_Text = cleaned_data.get('inmedical_C3_Text')
        inmedical_C4_Name = cleaned_data.get('inmedical_C4_Name')
        inmedical_C4_Text = cleaned_data.get('inmedical_C4_Text')
        inmedical_C4_YN = cleaned_data.get('inmedical_C4_YN')
        inmedical_C5_Name = cleaned_data.get('inmedical_C5_Name')
        inmedical_C5_YN = cleaned_data.get('inmedical_C5_YN')
        inmedical_C5_Text = cleaned_data.get('inmedical_C5_Text')

        inmedical_D1_Num = cleaned_data.get('inmedical_D1_Num')
        inmedical_D1_C = cleaned_data.get('inmedical_D1_C')
        inmedical_D1_Text = cleaned_data.get('inmedical_D1_Text')
        inmedical_D2_Num = cleaned_data.get('inmedical_D2_Num')
        inmedical_D2_C = cleaned_data.get('inmedical_D2_C')
        inmedical_D2_Text = cleaned_data.get('inmedical_D2_Text')
        inmedical_D3_YN = cleaned_data.get('inmedical_D3_YN')
        inmedical_D3_C = cleaned_data.get('inmedical_D3_C')
        inmedical_D3_Text = cleaned_data.get('inmedical_D3_Text')
        inmedical_D4_Name = cleaned_data.get('inmedical_D4_Name')
        inmedical_D4_YN = cleaned_data.get('inmedical_D4_YN')
        inmedical_D4_C = cleaned_data.get('inmedical_D4_C')
        inmedical_D4_Text = cleaned_data.get('inmedical_D4_Text')
        inmedical_D5_Name = cleaned_data.get('inmedical_D5_Name')
        inmedical_D5_YN = cleaned_data.get('inmedical_D5_YN')
        inmedical_D5_C = cleaned_data.get('inmedical_D5_C')
        inmedical_D5_Text = cleaned_data.get('inmedical_D5_Text')
        inmedical_D6_Name = cleaned_data.get('inmedical_D6_Name')
        inmedical_D6_YN = cleaned_data.get('inmedical_D6_YN')
        inmedical_D6_C = cleaned_data.get('inmedical_D6_C')
        inmedical_D6_Text = cleaned_data.get('inmedical_D6_Text')

        inmedical_E1_YN = cleaned_data.get('inmedical_E1_YN')
        inmedical_E1_C = cleaned_data.get('inmedical_E1_C')
        inmedical_E1_Text = cleaned_data.get('inmedical_E1_Text')
        inmedical_E2_YN = cleaned_data.get('inmedical_E2_YN')
        inmedical_E2_C = cleaned_data.get('inmedical_E2_C')
        inmedical_E2_Text = cleaned_data.get('inmedical_E2_Text')
        inmedical_E3_Name = cleaned_data.get('inmedical_E3_Name')
        inmedical_E3_YN = cleaned_data.get('inmedical_E3_YN')
        inmedical_E3_C = cleaned_data.get('inmedical_E3_C')
        inmedical_E3_Text = cleaned_data.get('inmedical_E3_Text')

        inmedical_F1_YN = cleaned_data.get('inmedical_F1_YN')
        inmedical_F1_Text = cleaned_data.get('inmedical_F1_Text')
        inmedical_F2_YN = cleaned_data.get('inmedical_F2_YN')
        inmedical_F2_C = cleaned_data.get('inmedical_F2_C')
        inmedical_F2_Text = cleaned_data.get('inmedical_F2_Text')
        inmedical_F3_YN = cleaned_data.get('inmedical_F3_YN')
        inmedical_F3_Text = cleaned_data.get('inmedical_F3_Text')
        inmedical_F4_Name = cleaned_data.get('inmedical_F4_Name')
        inmedical_F4_YN = cleaned_data.get('inmedical_F4_YN')
        inmedical_F4_Text = cleaned_data.get('inmedical_F4_Text')

        inmedical_G1 = cleaned_data.get('inmedical_G1')
        inmedical_G1_Text = cleaned_data.get('inmedical_G1_Text')

        # 심리지원
        inmental_A1_YN = cleaned_data.get('inmental_A1_YN')
        inmental_A1_C = cleaned_data.get('inmental_A1_C')
        inmental_A1_Text = cleaned_data.get('inmental_A1_Text')
        inmental_A2_YN = cleaned_data.get('inmental_A2_YN')
        inmental_A2_C = cleaned_data.get('inmental_A2_C')
        inmental_A2_Text = cleaned_data.get('inmental_A2_Text')

        inmental_B1_YN = cleaned_data.get('inmental_B1_YN')
        inmental_B1_C = cleaned_data.get('inmental_B1_C')
        inmental_B1_Text = cleaned_data.get('inmental_B1_Text')
        inmental_B2_Name = cleaned_data.get('inmental_B2_Name')
        inmental_B2_YN = cleaned_data.get('inmental_B2_YN')
        inmental_B2_C = cleaned_data.get('inmental_B2_C')
        inmental_B2_Text = cleaned_data.get('inmental_B2_Text')
        
        inmental_C1_YN = cleaned_data.get('inmental_C1_YN')
        inmental_C1_Text = cleaned_data.get('inmental_C1_Text')
        inmental_C2_YN = cleaned_data.get('inmental_C2_YN')
        inmental_C2_Text = cleaned_data.get('inmental_C2_Text')
        inmental_C3_name = cleaned_data.get('inmental_C3_name')
        inmental_C3_YN = cleaned_data.get('inmental_C3_YN')
        inmental_C3_Text = cleaned_data.get('inmental_C3_Text')

        # 사례관리
        incase_A1_YN = cleaned_data.get('incase_A1_YN')
        incase_A1_YN2 = cleaned_data.get('incase_A1_YN2')
        incase_A1_Text = cleaned_data.get('incase_A1_Text')
        incase_A2_YN = cleaned_data.get('incase_A2_YN')
        incase_A2_YN2 = cleaned_data.get('incase_A2_YN2')
        incase_A2_Text = cleaned_data.get('incase_A2_Text')
        incase_A3_YN = cleaned_data.get('incase_A3_YN')
        incase_A3_YN2 = cleaned_data.get('incase_A3_YN2')
        incase_A3_Text = cleaned_data.get('incase_A3_Text')
        incase_A4_YN = cleaned_data.get('incase_A4_YN')
        incase_A4_YN2 = cleaned_data.get('incase_A4_YN2')
        incase_A4_Text = cleaned_data.get('incase_A4_Text')

        incase_B1_YN = cleaned_data.get('incase_B1_YN')
        incase_B1_Text = cleaned_data.get('incase_B1_Text')
        incase_B2_YN = cleaned_data.get('incase_B2_YN')
        incase_B2_Text = cleaned_data.get('incase_B2_Text')
        incase_B3_Name = cleaned_data.get('incase_B3_Name')
        incase_B3_YN = cleaned_data.get('incase_B3_YN')
        incase_B3_Text = cleaned_data.get('incase_B3_Text')

        incase_C1_YN = cleaned_data.get('incase_C1_YN')
        incase_C1_Text = cleaned_data.get('incase_C1_Text')
        incase_C2_YN = cleaned_data.get('incase_C2_YN')
        incase_C2_Text = cleaned_data.get('incase_C2_Text')
        incase_C3_YN = cleaned_data.get('incase_C3_YN')
        incase_C3_Text = cleaned_data.get('incase_C3_Text')
        incase_C4_YN = cleaned_data.get('incase_C4_YN')
        incase_C4_Text = cleaned_data.get('incase_C4_Text')
        incase_C5_TC = cleaned_data.get('incase_C5_TC')
        getplan_comment = cleaned_data.get('getplan_comment')
        getplan_sentence = cleaned_data.get('getplan_sentence')

        if type(inmedical_A1_C) != int:
            inmedical_A1_C = 0
        if type(inmedical_B1_C) != int:
            inmedical_B1_C = 0
        if type(inmedical_B2_C) != int:
            inmedical_B2_C = 0
        if type(inmedical_B3_C) != int:
            inmedical_B3_C = 0
        if type(inmedical_B4_C) != int:
            inmedical_B4_C = 0
        if type(inmedical_C2_C) != int:
            inmedical_C2_C = 0
        if type(inmedical_C3_C) != int:
            inmedical_C3_C = 0
        if type(inmedical_D1_C) != int:
            inmedical_D1_C = 0
        if type(inmedical_D2_C) != int:
            inmedical_D2_C = 0
        if type(inmedical_D3_C) != int:
            inmedical_D3_C = 0
        if type(inmedical_D4_C) != int:
            inmedical_D4_C = 0
        if type(inmedical_D5_C) != int:
            inmedical_D5_C = 0
        if type(inmedical_D6_C) != int:
            inmedical_D6_C = 0
        if type(inmedical_E1_C) != int:
            inmedical_E1_C = 0
        if type(inmedical_E2_C) != int:
            inmedical_E2_C = 0
        if type(inmedical_E3_C) != int:
            inmedical_E3_C = 0
        if type(inmedical_F2_C) != int:
            inmedical_F2_C = 0    

        if type(inmental_A1_C) != int:
            inmental_A1_C = 0
        if type(inmental_A2_C) != int:
            inmental_A2_C = 0
        if type(inmental_B1_C) != int:
            inmental_B1_C = 0
        if type(inmental_B2_C) != int:
            inmental_B2_C = 0
        if type(incase_C5_TC) != int:
            incase_C5_TC = 0

        if type(inmedical_D1_Num) != int:
            inmedical_D1_Num = 0
        if type(inmedical_D2_Num) != int:
            inmedical_D2_Num = 0

        bomgetplan = BomGetPlan(
            sum_inmedical_A=inmedical_A1_YN+inmedical_A2_YN+inmedical_A3_YN+inmedical_A4_YN,
            sum_inmedical_A2=inmedical_A1_YN2+inmedical_A2_YN2+inmedical_A3_YN2+inmedical_A4_YN2,
            sum_inmedical_B=inmedical_B1_YN+inmedical_B2_YN+inmedical_B3_YN+inmedical_B4_YN,
            sum_inmedical_C=inmedical_C1_YN+inmedical_C2_YN+inmedical_C3_YN+inmedical_C4_YN,
            sum_inmedical_D=inmedical_D1_Num+inmedical_D2_Num+inmedical_D3_YN+inmedical_D4_YN+inmedical_D5_YN+inmedical_D6_YN,
            sum_inmedical_E=inmedical_E1_YN+inmedical_E2_YN+inmedical_E3_YN,
            sum_inmedical_F=inmedical_F1_YN+inmedical_F2_YN+inmedical_F3_YN+inmedical_F4_YN,
            sum_inmental_A=inmental_A1_YN+inmental_A2_YN,
            sum_inmental_B=inmental_B1_YN+inmental_B2_YN,
            sum_inmental_C=inmental_C1_YN+inmental_C2_YN+inmental_C3_YN,
            sum_incase_A=incase_A1_YN+incase_A2_YN+incase_A3_YN+incase_A4_YN,
            sum_incase_A2=incase_A1_YN2+incase_A2_YN2+incase_A3_YN2+incase_A4_YN2,
            sum_incase_B=incase_B1_YN+incase_B2_YN+incase_B3_YN,
            sum_incase_C=incase_C1_YN+incase_C2_YN+incase_C3_YN+incase_C4_YN,
            sum_cost = inmedical_A1_C+inmedical_B1_C+inmedical_B2_C+inmedical_B3_C+inmedical_B4_C+inmedical_C2_C+inmedical_C3_C+inmedical_D1_C+inmedical_D2_C+inmedical_D3_C+inmedical_D4_C+inmedical_D5_C+inmedical_D6_C+inmedical_E1_C+inmedical_E2_C+inmedical_E3_C+inmedical_F2_C+inmental_A1_C+inmental_A2_C+inmental_B1_C+inmental_B2_C+incase_C5_TC,

            getplan_name=ctname,
            getplan_date=getplan_date,
            inmedical_A1_YN=inmedical_A1_YN,
            inmedical_A1_YN2=inmedical_A1_YN2,
            inmedical_A1_select=inmedical_A1_select,
            inmedical_A1_C=inmedical_A1_C,
            inmedical_A1_Text=inmedical_A1_Text,
            inmedical_A2_YN=inmedical_A2_YN,
            inmedical_A2_YN2=inmedical_A2_YN2,
            inmedical_A2_Text=inmedical_A2_Text,
            inmedical_A3_YN=inmedical_A3_YN,
            inmedical_A3_YN2=inmedical_A3_YN2,
            inmedical_A3_Text=inmedical_A3_Text,
            inmedical_A4_YN=inmedical_A4_YN,
            inmedical_A4_YN2=inmedical_A4_YN2,
            inmedical_A4_Text=inmedical_A4_Text,

            inmedical_B1_YN=inmedical_B1_YN,
            inmedical_B1_C=inmedical_B1_C,
            inmedical_B1_Text=inmedical_B1_Text,
            inmedical_B2_YN=inmedical_B2_YN,
            inmedical_B2_C=inmedical_B2_C,
            inmedical_B2_Text=inmedical_B2_Text,
            inmedical_B3_YN=inmedical_B3_YN,
            inmedical_B3_C=inmedical_B3_C,
            inmedical_B3_Text=inmedical_B3_Text,
            inmedical_B4_Name=inmedical_B4_Name,
            inmedical_B4_YN=inmedical_B4_YN,
            inmedical_B4_C=inmedical_B4_C,
            inmedical_B4_Text=inmedical_B4_Text,

            inmedical_C1_YN=inmedical_C1_YN,
            inmedical_C1_Text=inmedical_C1_Text,
            inmedical_C2_YN=inmedical_C2_YN,
            inmedical_C2_C=inmedical_C2_C,
            inmedical_C2_Text=inmedical_C2_Text,
            inmedical_C3_YN=inmedical_C3_YN,
            inmedical_C3_F=inmedical_C3_F,
            inmedical_C3_C=inmedical_C3_C,
            inmedical_C3_Text=inmedical_C3_Text,
            inmedical_C4_Name=inmedical_C4_Name,
            inmedical_C4_Text=inmedical_C4_Text,
            inmedical_C4_YN=inmedical_C4_YN,
            inmedical_C5_Name=inmedical_C5_Name,
            inmedical_C5_YN=inmedical_C5_YN,
            inmedical_C5_Text=inmedical_C5_Text,

            inmedical_D1_Num=inmedical_D1_Num,
            inmedical_D1_C=inmedical_D1_C,
            inmedical_D1_Text=inmedical_D1_Text,
            inmedical_D2_Num=inmedical_D2_Num,
            inmedical_D2_C=inmedical_D2_C,
            inmedical_D2_Text=inmedical_D2_Text,
            inmedical_D3_YN=inmedical_D3_YN,
            inmedical_D3_C=inmedical_D3_C,
            inmedical_D3_Text=inmedical_D3_Text,
            inmedical_D4_Name=inmedical_D4_Name,
            inmedical_D4_YN=inmedical_D4_YN,
            inmedical_D4_C=inmedical_D4_C,
            inmedical_D4_Text=inmedical_D4_Text,
            inmedical_D5_Name=inmedical_D5_Name,
            inmedical_D5_YN=inmedical_D5_YN,
            inmedical_D5_C=inmedical_D5_C,
            inmedical_D5_Text=inmedical_D5_Text,
            inmedical_D6_Name=inmedical_D6_Name,
            inmedical_D6_YN=inmedical_D6_YN,
            inmedical_D6_C=inmedical_D6_C,
            inmedical_D6_Text=inmedical_D6_Text,

            inmedical_E1_YN=inmedical_E1_YN,
            inmedical_E1_C=inmedical_E1_C,
            inmedical_E1_Text=inmedical_E1_Text,
            inmedical_E2_YN=inmedical_E2_YN,
            inmedical_E2_C=inmedical_E2_C,
            inmedical_E2_Text=inmedical_E2_Text,
            inmedical_E3_Name=inmedical_E3_Name,
            inmedical_E3_YN=inmedical_E3_YN,
            inmedical_E3_C=inmedical_E3_C,
            inmedical_E3_Text=inmedical_E3_Text,

            inmedical_F1_YN=inmedical_F1_YN,
            inmedical_F1_Text=inmedical_F1_Text,
            inmedical_F2_YN=inmedical_F2_YN,
            inmedical_F2_C=inmedical_F2_C,
            inmedical_F2_Text=inmedical_F2_Text,
            inmedical_F3_YN=inmedical_F3_YN,
            inmedical_F3_Text=inmedical_F3_Text,
            inmedical_F4_Name=inmedical_F4_Name,
            inmedical_F4_YN=inmedical_F4_YN,
            inmedical_F4_Text=inmedical_F4_Text,
            inmedical_G1=inmedical_G1,
            inmedical_G1_Text=inmedical_G1_Text,

            # 심리지원
            inmental_A1_YN=inmental_A1_YN,
            inmental_A1_C=inmental_A1_C,
            inmental_A1_Text=inmental_A1_Text,
            inmental_A2_YN=inmental_A2_YN,
            inmental_A2_C=inmental_A2_C,
            inmental_A2_Text=inmental_A2_Text,

            inmental_B1_YN=inmental_B1_YN,
            inmental_B1_C=inmental_B1_C,
            inmental_B1_Text=inmental_B1_Text,
            inmental_B2_Name=inmental_B2_Name,
            inmental_B2_YN=inmental_B2_YN,
            inmental_B2_C=inmental_B2_C,
            inmental_B2_Text=inmental_B2_Text,
            
            inmental_C1_YN=inmental_C1_YN,
            inmental_C1_Text=inmental_C1_Text,
            inmental_C2_YN=inmental_C2_YN,
            inmental_C2_Text=inmental_C2_Text,
            inmental_C3_name=inmental_C3_name,
            inmental_C3_YN=inmental_C3_YN,
            inmental_C3_Text=inmental_C3_Text,

            # 사례관리
            incase_A1_YN=incase_A1_YN,
            incase_A1_YN2=incase_A1_YN2,
            incase_A1_Text=incase_A1_Text,
            incase_A2_YN=incase_A2_YN,
            incase_A2_YN2=incase_A2_YN2,
            incase_A2_Text=incase_A2_Text,
            incase_A3_YN=incase_A3_YN,
            incase_A3_YN2=incase_A3_YN2,
            incase_A3_Text=incase_A3_Text,
            incase_A4_YN=incase_A4_YN,
            incase_A4_YN2=incase_A4_YN2,
            incase_A4_Text=incase_A4_Text,

            incase_B1_YN=incase_B1_YN,
            incase_B1_Text=incase_B1_Text,
            incase_B2_YN=incase_B2_YN,
            incase_B2_Text=incase_B2_Text,
            incase_B3_Name=incase_B3_Name,
            incase_B3_YN=incase_B3_YN,
            incase_B3_Text=incase_B3_Text,

            incase_C1_YN=incase_C1_YN,
            incase_C1_Text=incase_C1_Text,
            incase_C2_YN=incase_C2_YN,
            incase_C2_Text=incase_C2_Text,
            incase_C3_YN=incase_C3_YN,
            incase_C3_Text=incase_C3_Text,
            incase_C4_YN=incase_C4_YN,
            incase_C4_Text=incase_C4_Text,
            incase_C5_TC=incase_C5_TC,
            getplan_comment=getplan_comment,
            getplan_sentence=getplan_sentence
                
        )

        bomgetplan.save()

class PerformanceForm(forms.Form):
    program_name = (
        ('의료지원사업', (
            ('의료 아웃리치', '의료 아웃리치'),
            ('소녀돌봄약국지원', '소녀돌봄약국지원')
        )),
        ('교육지원사업', (
            ('성교육장이용', '성교육장이용'),
            ('찾아가는 성매매예방교육연극', '찾아가는 성매매예방교육연극'),
            ('종사자교육', '종사자교육'),
        )),
        ('성건강지원사업', (
            ('성건강수첩', '성건강수첩'),
            ('찾아가는 초등성건강교육', '찾아가는 초등성건강교육'),
            ('소그룹 성건강교육', '소그룹 성건강교육'),
            ('생리대 배분', '생리대 배분'),
            ('생리대 후원 확보', '생리대 후원 확보'),
        )),
        ('네트워크', (
            ('거리, 방문홍보', '온라인 홍보'),
            ('우편홍보', '우편홍보'),
            ('내외부 직원교육', '내외부 직원교육'),
            ('네트워크 및 사업협력','네트워크 및 사업협력'),
            ('대학생 타기관 교육, 네트워킹','대학생 타기관 교육, 네트워킹'),
            ('연합사례회의, 지원협력','연합사례회의, 지원협력'),
            ('후원처 자원발굴, 관리','후원처 자원발굴, 관리'),
            ('이용자 만족도조사, 질적인터뷰 등','이용자 만족도조사, 질적인터뷰 등'),
            ('자원봉사활동','자원봉사활동'),
        )),
    )
    perfor_program = forms.ChoiceField(
        error_messages={
            'required':'프로그램명을 입력해주세요.'
        },
        widget=forms.Select, choices=program_name, label='프로그램명',required=True)
    perfor_date = forms.CharField(
        error_messages={
            'required':'날짜를 입력해주세요.'
        },
        widget=forms.DateInput(attrs={'type':'date'}), label='진행 날짜', required=True)
    # perfor_date = forms.DateField(
    #     error_messages={
    #         'required':'날짜를 입력해주세요.'
    #     },
    #     label='진행 날짜', required=True)
    perfor_people = forms.IntegerField(
        error_messages={
            'required':'인원(건)을 입력해주세요.'
        },
        label='인원(건)',required=True)

    perfor_count = forms.IntegerField(
        error_messages={
            'required':'인원(건)을 입력해주세요.'
        },
        label='인원(건)',required=True)


    def clean(self):
        cleaned_data = super().clean()

        perfor_date = cleaned_data.get('perfor_date')
        perfor_people = cleaned_data.get('perfor_people')
        perfor_program = cleaned_data.get('perfor_program')
        perfor_count = cleaned_data.get('perfor_count')

        performance = Performance(

            perfor_program=perfor_program,
            perfor_date=perfor_date,
            perfor_people=perfor_people,
            perfor_count=perfor_count

        )

        performance.save()