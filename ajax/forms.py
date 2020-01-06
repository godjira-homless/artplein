from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from .models import Ajax
from artists.models import Artist


class AjaxForm(forms.ModelForm):
    artist = forms.CharField()

    class Meta:
        model = Ajax
        fields = ('code',
                  'title',
                  'tech',
                  'description',
                  )

#       widgets = {
#        'artist': TextInput(attrs={'id': 'artist'}),
#       }
