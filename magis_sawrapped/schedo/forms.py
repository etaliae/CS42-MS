from .models import UserTable, UserSchedule
from django import forms

class UserTableForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = "__all__"
        
class UserScheduleForm(forms.ModelForm):
    class Meta:
        model = UserSchedule
        fields = "__all__"