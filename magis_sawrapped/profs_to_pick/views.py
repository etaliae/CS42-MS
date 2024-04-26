from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Count

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
        sentiment_counts = Review.objects.filter(professor=self.get_object().pk).values(
            'sentiment').annotate(count=Count('sentiment'))

        sentiment = []
        count = []
        for sentiment_count in sentiment_counts:
            sentiment.append(sentiment_count['sentiment'])
            count.append(sentiment_count['count'])

            context['sentiment_data'] = {
                'sentiment': sentiment,
                'count': count,
            }
            return context
