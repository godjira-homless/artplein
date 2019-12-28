from django import forms
from .models import Person

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name')

