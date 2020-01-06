from django import forms
from django.core.exceptions import ValidationError

from .models import Ajax


class AjaxForm(forms.ModelForm):
    class Meta:
        model = Ajax
        fields = ('code',
                  'title',
                  'artist',
                  'tech',
                  )

