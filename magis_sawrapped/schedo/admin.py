from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subject, SchoolYear, Time, Schedule


class SubjectAdmin(admin.ModelAdmin):
    model = Subject

    list_display = ('subject_code', 'course_title', 'units')


class SchoolYearAdmin(admin.ModelAdmin):
    model = SchoolYear

    list_display = ('school_year', 'semester')
    
class TimeAdmin(admin.ModelAdmin):
    model = Time

    list_display = ('time', 'day', 'room', 'modality',)
    
class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule

    list_display = ('subject', 'time', 'section', 'max_no', 'lang', 'level', 'free_slots', 'remarks', 's', 'p')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Schedule, ScheduleAdmin)