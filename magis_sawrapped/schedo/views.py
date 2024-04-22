from django.shortcuts import render

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import UserSchedule, UserTable
from .tables import UScheduleHTMxTable


def index(request):
    table = UserTable.objects.all()
    return render(request, 'index.html', {'table': table})

class UScheduleHTMxTableView(SingleTableMixin, FilterView):
    table_class = UScheduleHTMxTable
    queryset = UserSchedule.objects.all()
    model = UserSchedule

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product_table_partial.html"
        else:
            template_name = "product_table_htmx.html"

        return template_name
