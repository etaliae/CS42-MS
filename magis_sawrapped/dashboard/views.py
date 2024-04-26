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
from .grades import get_grades, Grades, honors_dict

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

    remaining_units = 0
    honor = 'Honorable Mention'
    if request.method == 'POST':
        remaining_units = int(request.POST.get('remaining_units', 0))
        honor = request.POST.get('honor', 'Honorable Mention')
        print(f"Remaining units from request: {remaining_units}")
        print(f"User Choice: {honor}")

    completed_units = grades.completed_units()
    total = completed_units + remaining_units
    ips_progress = round(grades.completed_units() * 100 / total, 2).tolist()

    honor_min = honors_dict[honor][0]
    honor_max = honors_dict[honor][-1]
    highest_possible = grades.check_highest_possible(
        remaining_units, {'A': 100}, by_percent=True)
    minimum_required = grades.check_minimum_required(remaining_units, honor)
    eligibility_text = 'Possible!' if highest_possible >= honors_dict[
        honor][0] else 'Impossible'
    print(f"Highest Possible Grade: {highest_possible}")
    print(f"Minimum Grade Required: {minimum_required}")
    print(eligibility_text)
    print(honor_min)
    print(honor_max)

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
    fields = ['semester', 'subject', 'grade']
    template_name = 'dashboard/edit_grade.html'
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
