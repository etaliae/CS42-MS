from django.urls import path
from .views import (dashboard, GradeListView, GradeUpdateView,
                    GradeDeleteView, GradeCreateView)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('grades/', GradeListView.as_view(), name='grades-list'),
    path('grades/<int:pk>/edit/', GradeUpdateView.as_view(), name='grade-update'),
    path('grades/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade-delete'),
    path('grades/add/', GradeCreateView.as_view(), name='grade-create'),
]

app_name = "dashboard"
