from django import forms
from django.forms import HiddenInput

from rate.models import Rating


class RatingForm(forms.Form):
    rating = forms.IntegerField()
    movie = forms.IntegerField(widget=HiddenInput())

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        print(instance)
