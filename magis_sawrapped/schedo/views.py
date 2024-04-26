from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView


from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import UserSchedule, UserTable, Subject, Department
from .tables import UScheduleHTMxTable, CoursesHTMxTable


def index(request):
    table = UserTable.objects.all()
    return render(request, 'index.html', {'table': table})

def landing(request):
    return render(request, 'landing.html')

class UScheduleHTMxTableView(SingleTableMixin, FilterView):
    table_class = UScheduleHTMxTable
    queryset = UserTable.objects.all()
    model = UserTable

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product_table_partial.html"
        else:
            template_name = "product_table_htmx.html"

        return template_name
    
class CourseHTMxTableView(SingleTableMixin, FilterView):
    table_class = CoursesHTMxTable
    queryset = Subject.objects.all()
    model = Subject

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product_table_partial.html"
        else:
            template_name = "view_courses.html"

        return template_name
        return template_name
