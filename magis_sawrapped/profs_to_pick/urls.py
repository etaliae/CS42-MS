from django.urls import path
from .views import (ProfessorListView, ProfessorDetailView)

urlpatterns = [
    # path('', search, name='vizprof-search'),
    path('', ProfessorListView.as_view(), name='vizprof'),
    path('<int:pk>/reviews/', ProfessorDetailView.as_view(), name='vizprof-detail'),
    # path('<int:professor_id>/reviews/', professor_reviews, name = 'vizprof-detail'),
]

app_name = "profs_to_pick"
