from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Subject, Professor, SchoolYear, Time, Schedule

class DepartmentAdmin(admin.ModelAdmin):
    model = Department

class SubjectAdmin(admin.ModelAdmin):
    model = Subject

    list_display = ('subject_code', 'course_title', 'units')

class ProfessorAdmin(admin.ModelAdmin):
    model = Professor

    list_display = ('department', 'last_name', 'given_name', 'middle_initial')

class SchoolYearAdmin(admin.ModelAdmin):
    model = SchoolYear

    list_display = ('school_year', 'semester')
    
class TimeAdmin(admin.ModelAdmin):
    model = Time

    list_display = ('time', 'day', 'room', 'modality',)
    
class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule

    list_display = ('subject', 'professor', 'time', 'section', 'max_no', 'lang', 'level', 'free_slots', 'remarks', 's', 'p')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Schedule, ScheduleAdmin)