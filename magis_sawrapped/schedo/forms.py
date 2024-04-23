    
from django import forms
from .models import UserTable, UserSchedule

class UserTableForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = "__all__"
        
class UserScheduleForm(forms.ModelForm):
    class Meta:
        model = UserSchedule
        fields = "__all__"