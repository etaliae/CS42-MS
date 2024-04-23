from django.contrib import admin
from .models import User

class LoginAdmin(admin.ModelAdmin):
    model = User

    list_display = ('email', 'username', 'password')


# admin.site.register(Professor, ProfessorAdmin)
admin.site.register(User, LoginAdmin)