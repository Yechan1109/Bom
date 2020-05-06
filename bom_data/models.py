from django.db import models
from bom_user.models import BomUser
# Create your models here.

Gender_choices = (
	('남자', '남자'),
    ('여자', '여자'))

class ChartData(models.Model):
    
    # 기본인적사항 db
    # C_Name = models.CharField(verbose_name='이름', max_length=30, unique=True)
    # second_id = models.ForeignKey(BomUser, on_delete=models.CASCADE)
    C_Name = models.CharField(null=True, blank=True, max_length=5, verbose_name='내담자')
    REG_Day = models.DateField(null=True, verbose_name='등록날짜')
    age = models.IntegerField(null=True, blank=True, verbose_name='연령')
    C_Gender = models.CharField(null=True, blank=True,choices=Gender_choices, max_length=2, verbose_name='성별')
    C_Institute = models.CharField(null=True, blank=True,default='', max_length=50, verbose_name='의뢰기관')
    # 계획 db
    medical_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치과 계획')
    medical_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='여성의학 계획')
    medical_A3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='한방의학 계획')
    medical_A4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='가정의학 계획')
    sum_medical_A = models.IntegerField(null=True, blank=True, default=0, verbose_name='진료 계획')
    sum_medical_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='각종검사 계획')
    sum_medical_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='약지급 계획')
    sum_medical_D = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방접종 계획')
    sum_medical_E = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부병원 계획')
    sum_medical_F = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방의학 계획')
    sum_mental_A  = models.IntegerField(null=True, blank=True, default=0, verbose_name='정신보건상담 계획')
    sum_mental_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='심리검사 계획')
    sum_mental_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='심리정서지원프로그램 계획')
    sum_case_A = models.IntegerField(null=True, blank=True, default=0, verbose_name='상담 계획')
    sum_case_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='1:1교육 계획')
    sum_case_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='기초생활지원 계획')

#     first_date = 
#     last_date = 
#     total_count = 
#     total_price = 
#     status = 
#     medical_A =
#     medical_B =
#     medical_C =
#     medical_D =
#     medical_E =
#     medical_F =
#     mental_A =
#     mental_B =
#     mental_C =
#     case_A =
#     case_B =
#     case_C =
#     clf_result = 

#     # add Chart
#     institute = 
#     medical_A1 = 
#     medical_A2 =
#     medical_A3 = 
#     medical_A4 = 
    def __str__(self):
        return self.C_Name

    class Meta:
        managed = True  # False면 migrations시 자동 저장을 막음
        db_table = 'bom_chartdata'
        verbose_name = '개인차트데이터'
        verbose_name_plural = '개인차트데이터'


class SetUser(models.Model):
    
    # 기본인적사항 db
    # C_Name = models.CharField(verbose_name='이름', max_length=30, unique=True)
    # second_id = models.ForeignKey(BomUser, on_delete=models.CASCADE)
    C_Name = models.CharField(null=True, blank=True, max_length=5, verbose_name='내담자')
    REG_Day = models.DateField(null=True, verbose_name='등록날짜')
    age = models.IntegerField(null=True, blank=True, verbose_name='연령')
    C_Gender = models.CharField(null=True, blank=True,choices=Gender_choices, max_length=2, verbose_name='성별')
    C_Institute = models.CharField(null=True, blank=True,default='', max_length=50, verbose_name='의뢰기관')
    # 계획 db
    medical_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치과 계획')
    medical_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='여성의학 계획')
    medical_A3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='한방의학 계획')
    medical_A4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='가정의학 계획')
    sum_medical_A = models.IntegerField(null=True, blank=True, default=0, verbose_name='진료 계획')
    sum_medical_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='각종검사 계획')
    sum_medical_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='약지급 계획')
    sum_medical_D = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방접종 계획')
    sum_medical_E = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부병원 계획')
    sum_medical_F = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방의학 계획')
    sum_mental_A  = models.IntegerField(null=True, blank=True, default=0, verbose_name='정신보건상담 계획')
    sum_mental_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='심리검사 계획')
    sum_mental_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='심리정서지원프로그램 계획')
    sum_case_A = models.IntegerField(null=True, blank=True, default=0, verbose_name='상담 계획')
    sum_case_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='1:1교육 계획')
    sum_case_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='기초생활지원 계획')

#     first_date = 
#     last_date = 
#     total_count = 
#     total_price = 
#     status = 
#     medical_A =
#     medical_B =
#     medical_C =
#     medical_D =
#     medical_E =
#     medical_F =
#     mental_A =
#     mental_B =
#     mental_C =
#     case_A =
#     case_B =
#     case_C =
#     clf_result = 

#     # add Chart
#     institute = 
#     medical_A1 = 
#     medical_A2 =
#     medical_A3 = 
#     medical_A4 = 
    def __str__(self):
        return self.C_Name

    class Meta:
        managed = True  # False면 migrations시 자동 저장을 막음
        db_table = 'bom_totaluser'
        verbose_name = 'User'
        verbose_name_plural = 'User'

class Test(models.Model):
    
    # 기본인적사항 db
    # C_Name = models.CharField(verbose_name='이름', max_length=30, unique=True)
    # second_id = models.ForeignKey(BomUser, on_delete=models.CASCADE)
    C_Name = models.CharField(null=True, blank=True, max_length=5, verbose_name='내담자')
    REG_Day = models.DateField(null=True, verbose_name='등록날짜')
    age = models.IntegerField(null=True, blank=True, verbose_name='연령')
    
    sum_medical_A = models.IntegerField(null=True, blank=True, default=0, verbose_name='진료 계획')
    sum_medical_B = models.IntegerField(null=True, blank=True, default=0, verbose_name='각종검사 계획')

    def __str__(self):
        return self.C_Name

    class Meta:
        managed = True  # False면 migrations시 자동 저장을 막음
        db_table = 'bom_test'
        verbose_name = 'Test'
        verbose_name_plural = 'Test'

class Accumulate(models.Model):

    name = models.CharField(null=True, blank=True, max_length=5, verbose_name='내담자')
    # 위기분류(danger), 사례지원진행(getplan) 누적 데이터 입력
    # 동일 이름 레코드가 누적되도록.. 가장 좋은 방법은 이름을 기준으로 입력값들이 자동으로 누적되어 하나의 레코드로만 표현되는 방법이 최상의 방법임.
    
    


    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'bom_accu'
        verbose_name = '누적데이터'
        verbose_name_plural = '누적데이터'