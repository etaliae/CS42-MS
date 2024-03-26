from django.contrib import admin
from .models import Department, Subject, Professor, SchoolYear, Time, Schedule, UserTable, UserSchedule

import string
# Register your models here.

class FirstLetterFilter(admin.SimpleListFilter):
    # This class was copied from
    # https://stackoverflow.com/questions/33322645/custom-admin-page-list-filter-by-first-letter
    title = 'First Letter'

    parameter_name = 'letter'
    letters = list(string.ascii_uppercase)

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        lookups = []
        for letter in self.letters:
            count = qs.filter(department_name__istartswith=letter).count()
            if count:
                lookups.append((letter, '{} ({})'.format(letter, count)))
        return lookups

    def queryset(self, request, queryset):
        filter_val = self.value()
        if filter_val in self.letters:
            return queryset.filter(department_name__istartswith=self.value())

class SubjectAdmin(admin.ModelAdmin):
    model = Subject

    list_display = ('department', 'subject_code', 'course_title', 'units')
    search_fields = ('department_name',)

    list_filter = ('department', 'units')

class SubjectInline(admin.TabularInline):
    model = Subject

class DepartmentAdmin(admin.ModelAdmin):
    model = Department

    search_fields = ('department_name',)

    list_filter = (FirstLetterFilter,)

    inlines = [SubjectInline,]

class ProfessorAdmin(admin.ModelAdmin):
    model = Professor

    list_display = ('department', 'last_name', 'given_name', 'middle_initial')

class SchoolYearAdmin(admin.ModelAdmin):
    model = SchoolYear

    list_display = ('school_year', 'semester')
    
class TimeAdmin(admin.ModelAdmin):
    model = Time

    list_display = ('start_time', 'end_time', 'day', 'room', 'modality',)
    
class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule

    list_display = ('subject', 'professor', 'time', 'section', 'max_no', 'lang', 'level', 'free_slots', 'remarks', 's', 'p')
    
class UserTableAdmin(admin.ModelAdmin):
    model = UserTable
    
    list_filter = ('user', 'name')
    
    list_display = ('user', 'name')

class UserScheduleAdmin(admin.ModelAdmin):
    model = UserSchedule
    
    list_filter = ('table', 'schedule')
    
    list_display = ('table', 'schedule')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(UserTable, UserTableAdmin)
admin.site.register(UserSchedule, UserScheduleAdmin)