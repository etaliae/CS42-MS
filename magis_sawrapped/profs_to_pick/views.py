from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Review
from schedo.models import Professor


class ProfessorListView(ListView):
    model = Professor
    template_name = 'profs_to_pick/search_page.html'

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = Professor.objects.all()
        if search != '':
            object_list = Professor.objects.filter(last_name__icontains=search)
        return object_list


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'profs_to_pick/prof_reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['positive'] = Review.objects.filter(
            sentiment__iexact='Positive').count()
        context['neutral'] = Review.objects.filter(
            sentiment__iexact='Neutral').count()
        context['negative'] = Review.objects.filter(
            sentiment__iexact='Negative').count()

        return context
