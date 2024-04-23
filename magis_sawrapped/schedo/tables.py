import django_tables2 as tables
from .models import UserSchedule, UserTable, Subject

class UScheduleHTMxTable(tables.Table):
    class Meta:
        model = UserSchedule
        template_name = 'tables/bootstrap_htmx.html'

class CoursesHTMxTable(tables.Table):
    class Meta:
        model = Subject
        template_name = 'tables/bootstrap_htmx.html'