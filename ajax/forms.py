from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from .models import Ajax


class AjaxForm(forms.ModelForm):
    class Meta:
        model = Ajax
        fields = ('code',
                  'title',
                  'artist',
                  'tech',
                  'description',
                  )

        widgets = {
            'title': TextInput(attrs={'id': 'post-text'}),
         }

