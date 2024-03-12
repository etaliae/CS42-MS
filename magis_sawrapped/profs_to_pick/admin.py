from django.contrib import admin
from .models import Professor, Review


class ProfessorAdmin(admin.ModelAdmin):
    model = Professor

    list_display = ('department', 'last_name', 'given_name', 'middle_initial',)


class ReviewAdmin(admin.ModelAdmin):
    model = Review

    list_display = ('professor', 'subject', 'review')


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Review, ReviewAdmin)
