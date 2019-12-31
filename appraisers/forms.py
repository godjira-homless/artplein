from django import forms
from .models import Appraisers

class AppraiserForm(forms.ModelForm):

    class Meta:
        model = Appraisers
        fields = ('name',)