from django import forms
from django.http import request

from .models import Imguploads


class ImgupForm(forms.ModelForm):

    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Imguploads
        fields = (
            'title',
            'file',
                  )

