from django.urls import path

from .views import UScheduleHTMxTableView, landing, CourseHTMxTableView

urlpatterns = [
    path('', UScheduleHTMxTableView.as_view(), name='index'),
    path('landing/', landing, name="landing"),
    path('courses/', CourseHTMxTableView.as_view(), name="courses"),
]

app_name = "schedo"