from django.urls import path
from .views import (user_login, user_register)

urlpatterns = [
    path('register/', user_register, name='register'),
    path('', user_login, name='login'),
]

appname = "login"