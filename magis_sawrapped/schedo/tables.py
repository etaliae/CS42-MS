import django_tables2 as tables
from .models import UserSchedule, UserTable, Subject

class UScheduleHTMxTable(tables.Table):
    # name = tables.LinkColumn('<a href="">Edit</a>')
    class Meta:
        model = UserTable
        
        row_attrs = {
            'data-id': lambda key: key.pk
        }
        
        template_name = 'tables/bootstrap_htmx.html'
        
        
    # def render_link(self, UserTable):
    #     return mark_safe(f'<a href="/">{UserTable.name}</a>')

class CoursesHTMxTable(tables.Table):
    class Meta:
        model = Subject
        template_name = 'tables/bootstrap_htmx.html'