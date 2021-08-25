from django import forms
from movies.models import Movie


class MovieForm(forms.ModelForm):
    form_class = Movie
    title = forms.CharField(max_length=128)
    genre = forms.CharField(max_length=128)
    director = forms.CharField(max_length=128)
    trailer = forms.CharField(max_length=128)
    year = forms.IntegerField()

    class Meta:
        model = Movie
        fields = "__all__"