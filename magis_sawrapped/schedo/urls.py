from django.urls import path

from .views import *

urlpatterns = [
    path('', UScheduleHTMxTableView.as_view(), name='index'),
    path('<int:pk>/details/', UserTableDetailView.as_view(), name='userTable-details'),
    path('<int:pk>/edit/', UserTableEdit.as_view(), name='userTable-edit'),
    path('add/', UserTableAdd.as_view(), name='userTable-add'),
    path('landing/', landing, name="landing"),
    path('courses/', CourseHTMxTableView.as_view(), name="courses"),
]

app_name = "schedo"