import django_tables2 as tables
from .models import UserSchedule, UserTable

class UScheduleHTMxTable(tables.Table):
    class Meta:
        model = UserSchedule
        template_name = 'tables/bootstrap_htmx.html'
