from .models import UserTable
from django import forms

class UserTableForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = "__all__"