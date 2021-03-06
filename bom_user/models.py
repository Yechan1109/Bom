from django.db import models
from datetime import date
# Create your models here.

class Counselor(models.Model):
    counselor_name = models.CharField(max_length=5, verbose_name='상담자')
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    email = models.EmailField(verbose_name='이메일')
    # 누적 DB로 구성해야 함 ex) Counselor_data..
    # 상담일
    # 내담자
    
    def __str__(self):
        return self.counselor_name
    
    class Meta:
        db_table = 'bom_coun'
        verbose_name = '직원명단'
        verbose_name_plural = '직원명단'


Coun_choices = (
	('이성영', '이성영'),
    ('정현재', '정현재'),
    ('김현정', '김현정'),
    ('문보라', '문보라'),
    ('박지숙', '박지숙'),
    ('김수미', '김수미'),
    ('강주연', '강주연'),
    ('노미나', '노미나'),
    ('곽은영', '곽은영'))

Gender_choices = (
	('남자', '남자'),
    ('여자', '여자'))
Res_choices = (
	('자가', '자가'),
    ('전세', '전세'),
    ('월룸(월세)', '월룸(월세)'),
    ('고시텔(원세)','고시텔(원세)'),
    ('기타','기타'))
Yn_choices = (
	('없음', '없음'),
    ('있음', '있음'))
His_choices = (
	('전화 및 SNS', '전화 및 SNS'),
    ('대면', '대면'),
    ('기타', '기타'))  
Rou_choices = (
	('선생님', '선생님'),
    ('기관소개', '기관소개'),
    ('기타','기타'))
Ss_choices = (
	('기초수급', '기초수급'),
    ('차상위', '차상위'),
    ('의료급여','의료급여'),
    ('기타','기타'))
Fam_choices = (
	('조손가정', '조손가정'),
    ('한부모', '한부모'),
    ('부모','부모'),
    ('독립','독립'),
    ('동거','동거'),
    ('기타','기타'))
Edu_choices = (
	('초등','초등'),
    ('중등','중등'),
    ('고등','고등'),
    ('기타','기타'))
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
medical = (
	('대면', '대면'),
    ('전화', '전화'),
    ('SNS','SNS'))
den = (
	('스켈링', '스켈링'),
    ('보철', '보철'),
    ('충치','충치'),
    ('기타','기타'))

class BomUser(models.Model):
    # user_id = models.AutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    C_Name = models.CharField(verbose_name='내담자 이름', max_length=5, unique=True, null=True)
    C_Jumin = models.CharField(null=True, blank=True,max_length=13,verbose_name='주민등록번호')
    age = models.IntegerField(null=True, blank=True, verbose_name='연령')
    REG_Day = models.DateField(null=True, verbose_name='등록날짜')
    F_Coun = models.CharField(choices=Coun_choices, blank=True,max_length=3,null=True,verbose_name='최초상담자')
    C_Gender = models.CharField(null=True, blank=True,choices=Gender_choices, max_length=2, verbose_name='성별')
    C_Kakaoid = models.CharField(null=True, blank=True,max_length=20,verbose_name='카카오 아이디')
    C_Tel = models.CharField(null=True, blank=True,max_length=15,verbose_name='전화번호')
    C_CN = models.CharField(null=True, blank=True,max_length=15,verbose_name='긴급연락처')
    C_Address1 = models.CharField(null=True, blank=True,max_length=100,verbose_name='주소')
    C_Address2 = models.CharField(null=True, blank=True,max_length=100,verbose_name='현주거지')

    C_Residential = models.CharField(choices=Res_choices, blank=True,max_length=10,null=True,verbose_name='주거형태')
    C_Residential_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='주거형태(기타)')
    C_History = models.CharField(choices=Yn_choices, blank=True,max_length=10,null=True,verbose_name='상담이력')
    C_History_select = models.CharField(choices=His_choices, blank=True,max_length=10,null=True,verbose_name='상담이력(유형)')
    C_Route = models.CharField(choices=Rou_choices, blank=True,max_length=10,null=True,verbose_name='의뢰경로')
    C_Route_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='의뢰경로(기타)')
    C_Institute = models.CharField(null=True, blank=True,default='', max_length=50, verbose_name='의뢰기관')
    C_Incharge_name = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='의뢰인 이름')
    C_Incharge_tel = models.CharField(null=True, blank=True, max_length=30, verbose_name='의뢰인 연락처')
    C_Otherhistory = models.CharField(null=True, blank=True, max_length=30, verbose_name='타기관 이용경험')
    C_Disorder = models.CharField(choices=Yn_choices, blank=True,max_length=10,null=True,verbose_name='장애여부')
    C_Disorder_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='장애명')
    C_Ssgrade = models.CharField(choices=Ss_choices, blank=True,max_length=10,null=True,verbose_name='보호구분')
    C_Ssgrade_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='보호구분(기타)')
    C_Family = models.CharField(choices=Fam_choices, blank=True,max_length=10,null=True,verbose_name='가족형태')
    C_Family_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='가족형태(기타)')
    C_Job = models.CharField(choices=Yn_choices, blank=True,max_length=10,null=True,verbose_name='직업')
    C_Job_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='직업명')
    C_Ecostatus1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(알바)')
    C_Ecostatus2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(취업)')
    C_Ecostatus3 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(부모지원)')
    C_Ecostatus4 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(기타)')
    C_Education = models.CharField(choices=Edu_choices, blank=True,max_length=10,null=True,verbose_name='최종학력')
    C_Education_text = models.CharField(null=True, blank=True,default='', max_length=30, verbose_name='최종학력(기타)')

    def __str__(self):
        return self.C_Name

    class Meta:
        db_table = 'bom_user'
        verbose_name = '1.기본인적사항'
        verbose_name_plural = '1.기본인적사항'


# verylow=1
# low=2
# medium=3
# high=4
# veryhigh=5
choices = ((0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5))

reverse_choices = ((0, 0),
    (1, 5),
    (2, 4),
    (3, 3),
    (4, 2),
    (5, 1))

class Danger(models.Model):
    # ctname = models.CharField(primary_key=True, verbose_name='이름', max_length=10)
    # danger_id = models.ForeignKey(BomUser, on_delete=models.CASCADE)
    danger_name = models.CharField(null=True, verbose_name='내담자 이름', max_length=10)
    survey_date = models.DateField(auto_now=True, verbose_name='작성일')
    survey1_1 = models.IntegerField(choices=choices,null=True, blank=True, default=0, verbose_name='survey1_1')
    survey1_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey1_2')
    survey1_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey1_3')
    survey1_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey1_4')
    survey1_5 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey1_5')
    survey2_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey2_1')
    survey2_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey2_2')
    survey2_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey2_3')
    survey2_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey2_4')
    survey2_5 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey2_5')
    
    survey3_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey3_1')
    survey3_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey3_2')
    survey3_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey3_3')
    survey3_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey3_4')
    survey3_5 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey3_5')
    survey4_1 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey4_1')
    survey4_2 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey4_2')
    survey4_3 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey4_3')
    survey4_4 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey4_4')
    
    survey5_1 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey5_1')
    survey5_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey5_2')
    survey5_3 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey5_3')
    # 추가 데이터
    survey5_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey5_4')
    survey5_5 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey5_5')
    
    survey6_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey6_1')
    survey6_2 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='survey6_2')
    survey6_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey6_3')

    survey7_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey7_1')
    survey7_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey7_2')
    survey7_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey7_3')
    # 제거
    # survey8_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey8_1')
    # survey8_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey8_2')
    # survey8_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey8_3')
    survey9_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey9_1')
    survey9_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey9_2')
    survey9_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey9_3')

    survey10_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey10_1')
    survey10_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey10_2')
    survey10_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey10_3')
    survey11_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey11_1')
    survey11_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey11_2')
    survey11_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey11_3')
    survey11_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='survey11_4')

    danger_comment = models.TextField(null=True, blank=True,max_length=5000, verbose_name='comment')
    danger_sentence = models.TextField(null=True, blank=True,max_length=5000, verbose_name='sentence')

    # total_sum = models.IntegerField(verbose_name='총 점수')

    def __str__(self):
        return self.danger_name

    class Meta:
        db_table = 'bom_danger'
        verbose_name = '3.위기분류'
        verbose_name_plural = '3.위기분류'


class BomSetPlan(models.Model):

    # setplan_name = models.OneToOneField(BomUser, on_delete=models.CASCADE)
    setplan_name = models.CharField(verbose_name='내담자 이름', max_length=10, unique=True)
    medical_start = models.DateField(null=True, verbose_name='의료지원 시작일')
    medical_end = models.DateField(null=True, verbose_name='의료지원 종료일')
    mental_start = models.DateField(null=True, verbose_name='심리지원 시작일')
    mental_end = models.DateField(null=True, verbose_name='심리지원 종료일')
    case_start = models.DateField(null=True, verbose_name='사례관리 시작일')
    case_end = models.DateField(null=True, verbose_name='사례관리 종료일')
    setplan_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='계획 작성일')
    # 의료지원
    medical_A1_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치과 월빈도')
    medical_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치과 총빈도')
    medical_A1_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='치과 내용')
    medical_A2_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='여성의학 월빈도')
    medical_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='여성의학 총빈도')
    medical_A2_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='여성의학 내용')
    medical_A3_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='한방의학 월빈도')
    medical_A3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='한방의학 총빈도')
    medical_A3_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='한방의학 내용')
    medical_A4_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='가정의학 월빈도')
    medical_A4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='가정의학 총빈도')
    medical_A4_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='가정의학 내용')
    medical_B1_YN = models.BooleanField(default=False, verbose_name='여성의학 검사 여부')
    medical_B1_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='여성의학 검사 내용')
    medical_B2_YN = models.BooleanField(default=False, verbose_name='기초검사 여부')
    medical_B2_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='기초검사 내용')
    medical_B3_YN = models.BooleanField(default=False, verbose_name='항체검사 여부')
    medical_B3_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='항체검사 내용')
    medical_B4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타검사명')
    medical_B4_YN = models.BooleanField(default=False, verbose_name='기타검사 여부') # 추가됨
    medical_B4_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='기타검사 내용')

    medical_C1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='치료제 월빈도')
    medical_C1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치료제 총빈도')
    medical_C1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='치료제 내용')
    medical_C2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='영양제 월빈도')
    medical_C2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='영양제 총빈도')
    medical_C2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='영양제 내용')
    medical_C3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='임신테스트기 월빈도')
    medical_C3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='임신테스트기 총빈도')
    medical_C3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타1 내용')
    medical_C4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타2 이름')
    medical_C4_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='기타2 월빈도')
    medical_C4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타2 총빈도')
    medical_C4_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타2 내용')
    medical_C5_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타3 이름')
    medical_C5_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타3 월빈도')
    medical_C5_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타3 총빈도')
    medical_C5_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타3 내용')

    medical_D1_Num = models.IntegerField(null=True, blank=True, default=0, verbose_name='간염예방접종 차수')
    medical_D1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='간염예방접종 내용')
    medical_D2_Num = models.IntegerField(null=True, blank=True, default=0, verbose_name='자궁경부암접종 차수')
    medical_D2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='자궁경부암접종 내용')
    medical_D3_YN = models.BooleanField(default=False, verbose_name='독감예방 여부')
    medical_D3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='독감예방접종 내용')
    medical_D4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타1 접종 이름')
    medical_D4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타1 접종 총빈도')
    medical_D4_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타1 접종 내용')
    medical_D5_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타1 접종 이름')
    medical_D5_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타1 접종 총빈도')
    medical_D5_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타1 접종 내용')
    medical_D6_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타1 접종 이름')
    medical_D6_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타1 접종 총빈도')
    medical_D6_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타1 접종 내용')

    medical_E1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='외부(치과) 월빈도')
    medical_E1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부(치과) 총빈도')
    medical_E1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='외부(치과) 내용')
    medical_E2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='외부(여성) 월빈도')
    medical_E2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부(여성) 총빈도')
    medical_E2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='외부(여성) 내용')
    medical_E3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='외부(기타) 이름')
    medical_E3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='외부(기타) 월빈도')
    medical_E3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부(기타) 총빈도')
    medical_E3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='외부(기타) 내용')

    medical_F1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='잇솔질 월빈도')
    medical_F1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='잇솔질 총빈도')
    medical_F1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='잇솔질 내용')
    medical_F2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='안경지원 월빈도')
    medical_F2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='안경지원 총빈도')
    medical_F2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='안경지원 내용')
    medical_F3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='몸펴기 월빈도')
    medical_F3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='몸펴기 총빈도')
    medical_F3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='몸펴기 내용')
    medical_F4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='예방(기타) 이름')
    medical_F4_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방(기타) 월빈도')
    medical_F4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방(기타) 총빈도')
    medical_F4_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='예방(기타) 내용')
    
    # 심리지원
    mental_A1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='정신(대면) 월빈도')
    mental_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='정신(대면) 총빈도')
    mental_A1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='정신(대면) 내용')
    mental_A2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='정신(전화) 월빈도')
    mental_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='정신(전화) 총빈도')
    mental_A2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='정신(전화) 내용')
    mental_B1_TF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='종합심리검사 총빈도')
    mental_B2_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    mental_B2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타 총빈도')
    mental_C1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='원예 월빈도')
    mental_C1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='원예 총빈도')
    mental_C1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='원예 내용')
    mental_C2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='몸치유 월빈도')
    mental_C2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='몸치유 총빈도')
    mental_C2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='몸치유 내용')
    mental_C3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    mental_C3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='기타 월빈도')
    mental_C3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타 총빈도')
    mental_C3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타 내용')

    # 사례관리
    case_A1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(대면) 월빈도')
    case_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(대면) 총빈도')
    case_A1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='사례(대면) 내용')
    case_A2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(심층) 월빈도')
    case_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(심층) 총빈도')
    case_A2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='사례(심층) 내용')
    case_A3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(전화) 월빈도')
    case_A3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(전화) 총빈도')
    case_A3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='사례(전화) 내용')
    case_A4_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(SNS) 월빈도')
    case_A4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(SNS) 총빈도')
    case_A4_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='사례(SNS) 내용')
    case_B1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='성건강 월빈도')
    case_B1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='성건강 총빈도')
    case_B1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='성건강 내용')
    case_B2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='관계 월빈도')
    case_B2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='관계 총빈도')
    case_B2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='관계 내용')
    case_B3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    case_B3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='기타 월빈도')
    case_B3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타 총빈도')
    case_B3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타 내용')
    case_C1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='먹거리 월빈도')
    case_C1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='먹거리 총빈도')
    case_C1_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='기타 내용')
    case_C2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='물품 월빈도')
    case_C2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='물품 총빈도')
    case_C2_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='물품 내용')
    case_C3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='교통비 월빈도')
    case_C3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='교통비 총빈도')
    case_C3_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='교통비 내용')
    case_C4_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='자원연계 월빈도')
    case_C4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='자원연계 총빈도')
    case_C4_Text = models.CharField(blank=True, default='', max_length=50, verbose_name='자원연계 내용')

    setplan_comment = models.TextField(null=True, blank=True,max_length=5000, verbose_name='comment')
    setplan_sentence = models.TextField(null=True, blank=True,max_length=5000, verbose_name='sentence')

    sum_medical_A = models.IntegerField(null=True, blank=True, verbose_name='진료 total')
    sum_medical_B = models.IntegerField(null=True, blank=True, verbose_name='각종검사 total')
    sum_medical_C = models.IntegerField(null=True, blank=True, verbose_name='약지급 total')
    sum_medical_D = models.IntegerField(null=True, blank=True, verbose_name='예방접종 total')
    sum_medical_E = models.IntegerField(null=True, blank=True, verbose_name='외부병원 total')
    sum_medical_F = models.IntegerField(null=True, blank=True, verbose_name='예방의학 total')
    sum_mental_A  = models.IntegerField(null=True, blank=True, verbose_name='정신보건상담 total')
    sum_mental_B = models.IntegerField(null=True, blank=True, verbose_name='심리검사 total')
    sum_mental_C = models.IntegerField(null=True, blank=True, verbose_name='심리정서지원프로그램 total')
    sum_case_A = models.IntegerField(null=True, blank=True, verbose_name='상담 total')
    sum_case_B = models.IntegerField(null=True, blank=True, verbose_name='1:1교육 total')
    sum_case_C = models.IntegerField(null=True, blank=True, verbose_name='기초생활지원 total')


    def __str__(self):
        return self.setplan_name
    
    class Meta:
        db_table = 'bom_setplan'
        verbose_name = '2.사례지원계획'
        verbose_name_plural = '2.사례지원계획'

class BomGetPlan(models.Model):
    # getplan_id = models.ForeignKey(BomUser, on_delete=models.CASCADE)
    getplan_name = models.CharField(null=True, verbose_name='내담자 이름', max_length=10)
    getplan_date = models.DateField(null=True, verbose_name='진행 날짜')
    # 의료지원
    inmedical_A1_YN = models.BooleanField(default=False, verbose_name='평일진료 여부(치과)')
    inmedical_A1_YN2 = models.BooleanField(default=False, verbose_name='야간진료 여부(치과)')
    inmedical_A1_select = models.CharField(choices=den, blank=True,max_length=3,null=True,verbose_name='치괴 진료명')
    inmedical_A1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_A2_YN = models.BooleanField(default=False, verbose_name='평일진료 여부(여성의학)')
    inmedical_A2_YN2 = models.BooleanField(default=False, verbose_name='야간진료 여부(여성의학)')
    inmedical_A2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_A3_YN = models.BooleanField(default=False, verbose_name='평일진료 여부(한방의학)')
    inmedical_A3_YN2 = models.BooleanField(default=False, verbose_name='야간진료 여부(한방의학)')
    inmedical_A3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_A4_YN = models.BooleanField(default=False, verbose_name='평일진료 여부(가정의학)')
    inmedical_A4_YN2 = models.BooleanField(default=False, verbose_name='야간진료 여부(가정의학)')
    inmedical_A4_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_B1_YN = models.BooleanField(default=False, verbose_name='여성의학검사 여부')
    inmedical_B1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_B2_YN = models.BooleanField(default=False, verbose_name='기초검사 여부')
    inmedical_B2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_B3_YN = models.BooleanField(default=False, verbose_name='항체검사 여부')
    inmedical_B3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_B4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_B4_YN = models.BooleanField(default=False, verbose_name='기타 여부')
    inmedical_B4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B4_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_C1_YN = models.BooleanField(default=False, verbose_name='치료제 여부')
    inmedical_C1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_C2_YN = models.BooleanField(default=False, verbose_name='영양제 여부')
    inmedical_C2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    
    inmedical_C3_YN = models.BooleanField(default=False, verbose_name='임신테스트기 여부')
    inmedical_C3_F = models.IntegerField(null=True, blank=True, default=0, verbose_name='수량')
    inmedical_C3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_C4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타1 이름')
    inmedical_C4_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_C4_YN = models.BooleanField(default=False, verbose_name='기타1 여부')
    inmedical_C5_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타2 이름')
    inmedical_C5_YN = models.BooleanField(default=False, verbose_name='기타2 여부')
    inmedical_C5_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_D1_Num = models.IntegerField(null=True, blank=True, default=0, verbose_name='간염 여부(차수)')
    inmedical_D1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_D2_Num = models.IntegerField(null=True, blank=True, default=0, verbose_name='자궁경부암 여부(차수)')
    inmedical_D2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_D3_YN = models.BooleanField(default=False, verbose_name='독감예방 여부')
    inmedical_D3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_D4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_D4_YN = models.BooleanField(default=False, verbose_name='기타1 여부')
    inmedical_D4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D4_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_D5_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_D5_YN = models.BooleanField(default=False, verbose_name='기타2 여부')
    inmedical_D5_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D5_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_D6_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_D6_YN = models.BooleanField(default=False, verbose_name='기타3 여부')
    inmedical_D6_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D6_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_E1_YN = models.BooleanField(default=False, verbose_name='외부병원(치과) 여부')
    inmedical_E1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_E1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_E2_YN = models.BooleanField(default=False, verbose_name='외부병원(여성) 여부')
    inmedical_E2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_E2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_E3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_E3_YN = models.BooleanField(default=False, verbose_name='기타 여부')
    inmedical_E3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_E3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_F1_YN = models.BooleanField(default=False, verbose_name='잇솔질교육 여부')
    inmedical_F1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_F2_YN = models.BooleanField(default=False, verbose_name='안경지원 여부')
    inmedical_F2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_F2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_F3_YN = models.BooleanField(default=False, verbose_name='몸펴기운동 지원 여부')
    inmedical_F3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmedical_F4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_F4_YN = models.BooleanField(default=False, verbose_name='기타 여부')
    inmedical_F4_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    inmedical_G1 = models.CharField(choices=medical, blank=True,max_length=3,null=True,verbose_name='의료상담')
    inmedical_G1_Text = models.TextField(null=True, blank=True,max_length=500, verbose_name='내용')


    # 심리지원
    inmental_A1_YN = models.BooleanField(default=False, verbose_name='정신(대면) 여부')
    inmental_A1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_A1_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='내용')
    inmental_A2_YN = models.BooleanField(default=False, verbose_name='정신(전화) 여부')
    inmental_A2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_A2_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='내용')

    inmental_B1_YN = models.BooleanField(default=False, verbose_name='종합심리검사 여부')
    inmental_B1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_B1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmental_B2_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmental_B2_YN = models.BooleanField(default=False, verbose_name='기타 여부')
    inmental_B2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_B2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    
    inmental_C1_YN = models.BooleanField(default=False, verbose_name='원예치료 여부')
    inmental_C1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmental_C2_YN = models.BooleanField(default=False, verbose_name='몸치유 여부')
    inmental_C2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    inmental_C3_name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmental_C3_YN = models.BooleanField(default=False, verbose_name='기타 여부')
    inmental_C3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    # 사례관리
    incase_A1_YN = models.BooleanField(default=False, verbose_name='상담(대면)')
    incase_A1_YN2 = models.BooleanField(default=False, verbose_name='수강명령 상담(대면)')
    incase_A1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_A2_YN = models.BooleanField(default=False, verbose_name='상담(심층)')
    incase_A2_YN2 = models.BooleanField(default=False, verbose_name='수강명령 상담(심층)')
    incase_A2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_A3_YN = models.BooleanField(default=False, verbose_name='상담(전화)')
    incase_A3_YN2 = models.BooleanField(default=False, verbose_name='수강명령 상담(전화)')
    incase_A3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_A4_YN = models.BooleanField(default=False, verbose_name='상담(SNS)')
    incase_A4_YN2 = models.BooleanField(default=False, verbose_name='수강명령 상담(SNS)')
    incase_A4_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')

    incase_B1_YN = models.BooleanField(default=False, verbose_name='성건강 여부')
    incase_B1_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    incase_B2_YN = models.BooleanField(default=False, verbose_name='관계 여부')
    incase_B2_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')
    incase_B3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    incase_B3_YN = models.BooleanField(default=False, verbose_name='기타 여부')
    incase_B3_Text = models.CharField(blank=True, default='', max_length=70, verbose_name='내용')

    incase_C1_YN = models.BooleanField(default=False, verbose_name='먹거리 여부')
    incase_C1_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='내용')
    incase_C2_YN = models.BooleanField(default=False, verbose_name='물품 여부')
    incase_C2_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='내용')
    incase_C3_YN = models.BooleanField(default=False, verbose_name='교통비 여부')
    incase_C3_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='내용')
    incase_C4_YN = models.BooleanField(default=False, verbose_name='자원연계 여부')
    incase_C4_Text = models.CharField(blank=True, default='', max_length=100, verbose_name='내용')
    incase_C5_TC = models.IntegerField(null=True, blank=True, default=0, verbose_name='총비용')

    getplan_comment = models.TextField(null=True, blank=True,max_length=5000, verbose_name='comment')
    getplan_sentence = models.TextField(null=True, blank=True,max_length=5000, verbose_name='sentence')
    
    sum_inmedical_A = models.IntegerField(null=True, blank=True, verbose_name='진료 total')
    sum_inmedical_A2 = models.IntegerField(null=True, blank=True, verbose_name='진료(야간) total')
    sum_inmedical_B = models.IntegerField(null=True, blank=True, verbose_name='각종검사 total')
    sum_inmedical_C = models.IntegerField(null=True, blank=True, verbose_name='약지급 total')
    sum_inmedical_D = models.IntegerField(null=True, blank=True, verbose_name='예방접종 total')
    sum_inmedical_E = models.IntegerField(null=True, blank=True, verbose_name='외부병원 total')
    sum_inmedical_F = models.IntegerField(null=True, blank=True, verbose_name='예방의학 total')
    sum_inmental_A  = models.IntegerField(null=True, blank=True, verbose_name='정신보건상담 total')
    sum_inmental_B = models.IntegerField(null=True, blank=True, verbose_name='심리검사 total')
    sum_inmental_C = models.IntegerField(null=True, blank=True, verbose_name='심리정서지원프로그램 total')
    sum_incase_A = models.IntegerField(null=True, blank=True, verbose_name='상담 total')
    sum_incase_A2 = models.IntegerField(null=True, blank=True, verbose_name='상담(수강명령) total')
    sum_incase_B = models.IntegerField(null=True, blank=True, verbose_name='1:1교육 total')
    sum_incase_C = models.IntegerField(null=True, blank=True, verbose_name='기초생활지원 total')
    sum_cost = models.IntegerField(null=True, blank=True, verbose_name='총 누적금액')


    def __str__(self):
        return self.getplan_name

    class Meta:
        db_table = 'bom_getplan'
        verbose_name = '4.사례지원진행'
        verbose_name_plural = '4.사례지원진행'


class Performance(models.Model):
    
    perfor_date = models.DateField(verbose_name='진행 날짜')
    perfor_people = models.IntegerField(verbose_name='인원')
    perfor_count = models.IntegerField(verbose_name='건수')
    perfor_program = models.CharField(choices=program_name, max_length=30, verbose_name='프로그램')
    def __str__(self):
        return self.perfor_program
    
    class Meta:
        db_table = 'bom_performance'
        verbose_name = '5.실적등록'
        verbose_name_plural = '5.실적등록'

