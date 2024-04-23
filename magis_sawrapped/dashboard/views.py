from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

from .models import Grade
from .grades import get_grades, Grades

import json

@login_required
def dashboard(request):
    grades = Grades()
    
    df = get_grades()
    cumulative_qpi = grades.cumulative_qpi()
    latest_qpi = grades.latest_qpi()
    dean_list = grades.dean_list()

    qpi_by_semester = grades.qpi_by_semester()
    semester = json.dumps(qpi_by_semester['Semester'].tolist())
    qpi = json.dumps(qpi_by_semester['QPI'].tolist())

    letter_frequency = grades.letter_frequency()
    final_grade = json.dumps(letter_frequency['Final Grade'].tolist())
    subject_code = json.dumps(letter_frequency['Subject Code'].tolist())

    context = {'df': df,
               'cumulative_qpi': cumulative_qpi,
               'latest_qpi': latest_qpi,
               'dean_list': dean_list,
               'semester': semester,
               'qpi': qpi,
               'final_grade': final_grade,
               'subject_code': subject_code}

    # Pass user grades to the template
    context = {'user_grades': grades}
    return render(request, 'dashboard/dashboard.html', context)

    

class GradeListView(ListView):
    model = Grade
    template_name = 'dashboard/view_grades.html'
    def get_queryset(self):
        # Get the default queryset
        queryset = super().get_queryset()
        # Filter the queryset based on the currently logged-in user's username
        filtered_queryset = queryset.filter(username=self.request.user)
        return filtered_queryset


class GradeUpdateView(UpdateView):
    model = Grade
    fields = '__all__'
    template_name = 'dashboard/edit_grade.html'


class GradeDeleteView(DeleteView):
    model = Grade
    success_url = "/grades/"
    template_name = 'dashboard/delete_grade.html'


class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    fields = ['semester', 'subject', 'grade']
    template_name = 'dashboard/add_grade.html'
    success_url = reverse_lazy('dashboard:grades-list')

    def form_valid(self, form):
        current_user = self.request.user
        user_instance = User.objects.get(username=current_user.username)
        form.instance.username = user_instance
        try:
            return super().form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'Grade entry already exists for this semester and subject.')
            return self.render_to_response(self.get_context_data(form=form))
