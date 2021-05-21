from django import forms
from .models import mymodel


class user_form(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = ['name', 'age', 'email']
