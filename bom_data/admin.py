from django.contrib import admin
from .models import ChartData, SetUser


class ChartDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ChartData._meta.get_fields()]
    # list_display = ('C_Name',)

class SetuserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SetUser._meta.get_fields()]




admin.site.register(ChartData, ChartDataAdmin)
admin.site.register(SetUser, SetuserAdmin)