from django.contrib import admin
from .models import Danger, BomGetPlan, Performance, Counselor, BomUser, BomSetPlan
# from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class CounselorAdmin(admin.ModelAdmin):
    list_display = ('counselor_name','email')

class BomUserAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in BomUser._meta.get_fields() if field.name != "id"]
    # list_display_links = ['id', 'C_Name']
    ordering = ('id',)
    # list_editable = [field.name for field in BomUser._meta.get_fields() if field.name != "id" if field.name != "C_Name"]
    search_fields = [field.name for field in BomUser._meta.get_fields()]

class DangerAddAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Danger._meta.get_fields()]
    search_fields = [field.name for field in Danger._meta.get_fields()]


class BomSetPlanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BomSetPlan._meta.get_fields()]
    search_fields = [field.name for field in BomSetPlan._meta.get_fields()]

class BomGetPlanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BomGetPlan._meta.get_fields() if field.name != 'getplan_comment']
    search_fields = [field.name for field in BomGetPlan._meta.get_fields()]

class PerformanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Performance._meta.get_fields()]
    ordering = [field.name for field in Performance._meta.get_fields()]
    search_fields = [field.name for field in Performance._meta.get_fields()]


# admin register code
admin.site.register(Counselor, CounselorAdmin)
admin.site.register(BomUser, BomUserAdmin)
admin.site.register(BomSetPlan, BomSetPlanAdmin)
admin.site.register(Danger, DangerAddAdmin)
admin.site.register(BomGetPlan, BomGetPlanAdmin)
admin.site.register(Performance, PerformanceAdmin)