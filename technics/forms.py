from django import forms
from .models import Technic

class TechnicMofelForm(forms.ModelForm):

    class Meta:
        model = Technic
        fields = ('name',)

