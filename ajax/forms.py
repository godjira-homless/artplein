from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from .models import Ajax
from artists.models import Artist


class AjaxForm(forms.ModelForm):
    artist = forms.CharField(widget=forms.TextInput(attrs={'id': 'contact_name_search_input', 'name': "contact_name_search"}))

    class Meta:
        model = Ajax
        fields = ('code',
                  'title',
                  'tech',
                  'description',
                  'size',
                  )

