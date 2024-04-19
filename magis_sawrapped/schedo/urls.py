from django.urls import path

from .views import *

urlpatterns = [
    path('', UScheduleHTMxTableView.as_view(), name='index'),
    path('<int:pk>/details/', UserTableDetailView.as_view(), name='userTable-details'),
    path('add/', UserTableCreateView.as_view(), name='userTable-create'),
    path('<int:pk>/edit/', UserTableUpdateView.as_view(), name='userTable-update'),
    # path('index_card', index_card_view, name='index_card'),
]

app_name = "schedo"