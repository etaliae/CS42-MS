from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import UserSchedule, UserTable, Subject, Department
from .forms import UserTableForm, UserScheduleForm
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
    success_url = '../'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.display_name = form.cleaned_data['name']
        form.save()
        return super().form_valid(form)
    
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
    
class UserTableDelete(DeleteView):
    model = UserTable
    success_url = '/schedo/'
    
    # def form_valid(self, form):
    #     pk = self.request.user
    #     # form.instance.display_name = form.cleaned_data['name']
    #     UserTable.objects.get(pk).delete()
    #     return super().form_valid(form)
    template_name = 'schedo/schedo_delete.html'

class UserScheduleAdd(CreateView):
    model = UserSchedule
    form = UserScheduleForm
    fields = '__all__'
    template_name = 'Schedo/schedule_add.html'
    success_url = '../'

   
class UserScheduleEditView(UpdateView):
    
    model = UserSchedule
    fields = ['schedule',]
    template_name = 'Schedo/schedule_edit.html'
    
    success_url = "../../"
    
class UserScheduleDelete(DeleteView):
    model = UserSchedule
    success_url = '../../details/'
    
    template_name = 'schedo/schedule_delete.html'
    
    # model = UserSchedule
    # template_name = "Schedo/schedule_details.html"
    
    # def get_sucess_url(self, **kwargs):
    #     thisTable = self.request.META.get("HTTP_REFERER")
        
    #     sucess_url = '../../' + thisTable + '/details/'
    #     return sucess_url

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
