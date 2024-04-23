from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Grade
from .grades import get_grades, Grades

import json

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

    return render(request, 'dashboard/dashboard.html', context)


class GradeListView(ListView):
    model = Grade
    template_name = 'dashboard/view_grades.html'


class GradeUpdateView(UpdateView):
    model = Grade
    fields = '__all__'
    template_name = 'dashboard/edit_grade.html'


class GradeDeleteView(DeleteView):
    model = Grade
    success_url = "/grades/"
    template_name = 'dashboard/delete_grade.html'


class GradeCreateView(CreateView):
    model = Grade
    fields = '__all__'
    template_name = 'dashboard/add_grade.html'
