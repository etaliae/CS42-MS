from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView


from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import UserSchedule, UserTable, Subject, Department
from .forms import UserTableForm
from .tables import UScheduleHTMxTable, CoursesHTMxTable
# from .forms import UserTableForm, UserScheduleForm


def index(request):
    table = UserTable.objects.filter(user=request.user)
    return render(request, 'product_table_htmx.html', {'table': table})

def landing(request):
    return render(request, 'landing.html')

class UserTableDetailView(TemplateView):
    template_name = "Schedo/schedo_details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thisTable = get_object_or_404(UserTable, pk=self.kwargs['pk']) # Get current table instance
        
        context['thisTable'] = thisTable
          # Filter on userTable name column
        context['userSchedules'] = UserSchedule.objects.filter(table__name = thisTable.name)
        # context['form'] = UserScheduleForm
        # context['fields'] = '__all__'
        return context
    
class UserTableAdd(CreateView):
    model = UserTable
    form = UserTableForm
    fields = ['name',]
    template_name = 'Schedo/schedo_add.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.display_name = form.cleaned_data['name']
        form.save()
        return HttpResponseRedirect('../')
    
    # def post(self, request, *args, **kwargs):
    #     form = UserTableForm(request.POST)
    #     if form.is_valid():
    #         new_assignment = form.save()
    #         redirect_link = '../'
    #         return HttpResponseRedirect(redirect_link)
    #     else:
    #         return render(request, self.template_name, {'form': form})
    
class UserTableEdit(UpdateView):
    model = UserTable
    fields = ['name',]
    template_name = 'Schedo/schedo_edit.html'
    
    success_url = '../details/'

class UScheduleHTMxTableView(SingleTableMixin, FilterView):
    table_class = UScheduleHTMxTable
    queryset = UserTable.objects.filter()
    model = UserTable
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['table'] = UserTable.objects.filter(user=self.request.user)
        
        return context
        
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
