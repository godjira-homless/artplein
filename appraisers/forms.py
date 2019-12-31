from django import forms
from django.core.exceptions import ValidationError

from .models import Appraisers


class AppraiserForm(forms.ModelForm):
    class Meta:
        model = Appraisers
        fields = ('name',)
        exclude = ('response_returned',)

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name
        if len(name_l) < 3:
            raise ValidationError("at least 3 character!")


        return name_l
