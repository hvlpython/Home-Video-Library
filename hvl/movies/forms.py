from django.db.models.fields.files import ImageField
from django.forms import ModelForm, CharField, IntegerField, TextInput, ModelChoiceField, Select
from movies.models import Genre, Movie
from django.contrib.auth.models import User


class MovieForm(ModelForm):
    title = CharField(max_length=128, widget=TextInput(
        attrs={"class": "form-control"}))
    genre = ModelChoiceField(queryset=Genre.objects.all(), widget=Select(
        attrs={"class": "form-control"}))
    director = CharField(max_length=128, widget=TextInput(
        attrs={"class": "form-control"}))
    trailer = CharField(max_length=128, widget=TextInput(
        attrs={"class": "form-control"}))
    year = IntegerField(widget=TextInput(attrs={"class": "custom-select"}))
    borrowed_by = ModelChoiceField(queryset=User.objects.all(), widget=Select(
        attrs={"class": "form-control"}))


    class Meta:
        model = Movie
        fields = ("title", "genre", "director",
                  "trailer", "year", "movie_image", "borrowed_by")


class GenreForm(ModelForm):
    name = CharField(max_length=128, widget=TextInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Genre
        fields = ('name',)
