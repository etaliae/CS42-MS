from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget
from .models import Review
from schedo.models import Subject, Professor


class ProfessorForeignKeyWidget(widgets.ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value:
            last_name, given_name = value.split(",")
            try:
                return Professor.objects.get(
                    last_name=last_name.strip(),
                    # given_name=given_name.strip(),
                    # middle_initial=middle_initial.strip()
                )
            except Professor.DoesNotExist:
                return None
        return None


class ReviewAdminResource(resources.ModelResource):
    subject = fields.Field(column_name='subject', attribute='subject',
                           widget=ForeignKeyWidget(Subject, field='subject_code__iexact'))
    professor = fields.Field(column_name='professor', attribute='professor',
                             widget=ProfessorForeignKeyWidget(Professor, field='last_name__iexact'))

    class Meta:
        model = Review
        import_id_fields = ('subject', 'professor', 'review', 'sentiment')
        fields = ('subject', 'professor', 'review', 'sentiment')
