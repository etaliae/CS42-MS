from django.contrib import admin
from .models import Review
from .resources import ReviewAdminResource
from import_export.admin import ImportExportModelAdmin


# class ProfessorAdmin(admin.ModelAdmin):
#     model = Professor

#     list_display = ('department', 'last_name', 'given_name', 'middle_initial',)

'''
class ReviewAdmin(admin.ModelAdmin):
    model = Review

    list_display = ('subject', 'professor', 'review')
'''


class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('subject', 'professor', 'review', 'sentiment')
    resource_class = ReviewAdminResource


# admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Review, ReviewAdmin)
