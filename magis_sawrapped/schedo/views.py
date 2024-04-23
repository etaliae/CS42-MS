from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView


from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import UserSchedule, UserTable
from .tables import UScheduleHTMxTable
from .forms import UserTableForm


def index(request):
    context = {}
    context['UserTables'] = UserTable.objects.all()
    return render(request, 'product_table_htmx.html', context)

class UserTableDetailView(TemplateView):
    template_name = "Schedo/schedo_details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thisTable = get_object_or_404(UserTable, pk=self.kwargs['pk']) # Get current table instance
        
        context['thisTable'] = thisTable
          # Filter on userTable name column
        context['userSchedules'] = UserSchedule.objects.filter(table__name = thisTable.name)
        return context

class UserTableCreateView(CreateView):
    
    model = UserTable
    
    template_name = "schedo.html"
    
class UserTableUpdateView(UpdateView):
    model = UserTable
    fields = '__all__'
    template_name = 'schedo.html'


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

# class UserTableListView(ListView):
#     model = UserTable
#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)
#         context['form'] = UserTableForm()
#         return context
#     def post(self, request, *args, **kwargs):

#         form = UserTableForm(request.POST) # Create a Form object from the POST values
#         if form.is_valid():
#             return self.get(request, *args, **kwargs)

#         else:
#             return render(request, self.template_name, {'form': form})