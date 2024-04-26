from django.urls import path

from .views import *

urlpatterns = [
    path('', UScheduleHTMxTableView.as_view(), name='index'),
    path('<int:pk>/details/', UserTableDetailView.as_view(), name='userTable-details'),
    path('addSchedule/', UserScheduleAdd.as_view(), name='userSchedule-add'),
    path('<int:pk>/schedule/', UserScheduleEditView.as_view(), name='userSchedule-edit'),
    path('<int:pk>/edit/', UserTableEdit.as_view(), name='userTable-edit'),
    path('', UserTableDelete.as_view(), name='userTable-delete'),
    path('add/', UserTableAdd.as_view(), name='userTable-add'),
    path('landing/', landing, name="landing"),
    path('courses/', CourseHTMxTableView.as_view(), name="courses"),
]

app_name = "schedo"