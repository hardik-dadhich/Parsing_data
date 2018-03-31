from django import forms
from Userdata.models import UserInput

CHOICES_IN_INPUTS = (('c', 'Cats'), ('d', 'Dogs'), ('cn', 'Chuck Norris'))
category = (('m', 'movie'), ('f', 'food'), ('a', 'animal'), ('s', 'sports'))


class InputFormData(forms.Form):
    number = forms.IntegerField(required=True)
    name = forms.CharField(max_length=50, blank=False, choices=CHOICES_IN_INPUTS, default='Cats')
    jcat = forms.CharField(max_length=50, blank=False, choices=category, default='no')
