from django.contrib import admin
from .models import Grade


class GradeAdmin(admin.ModelAdmin):
    model = Grade

    list_display = ('semester', 'subject', 'grade',)


admin.site.register(Grade, GradeAdmin)
