from django.urls import path

from .views import UScheduleHTMxTableView

urlpatterns = [
    path('', UScheduleHTMxTableView.as_view(), name='index'),
]

app_name = "schedo"