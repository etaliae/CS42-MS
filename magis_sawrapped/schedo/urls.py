from django.urls import path

from .views import UserTableDetailView, UScheduleHTMxTableView, landing, CourseHTMxTableView

urlpatterns = [
    path('', UScheduleHTMxTableView.as_view(), name='index'),
    path('<int:pk>/details/', UserTableDetailView.as_view(), name='userTable-details'),
    path('landing/', landing, name="landing"),
    path('courses/', CourseHTMxTableView.as_view(), name="courses"),
]

app_name = "schedo"