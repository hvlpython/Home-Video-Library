from django.forms import ModelForm, CharField, IntegerField, TextInput
from movies.models import Movie


class MovieForm(ModelForm):
    title = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    genre = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    director = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    trailer = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    year = IntegerField(widget=TextInput(attrs={"class": "custom-select"}))

    class Meta:
        model = Movie
        fields = "__all__"
