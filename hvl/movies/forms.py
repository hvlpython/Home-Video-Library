from django.forms import ModelForm, CharField, IntegerField, TextInput, ModelChoiceField, Select, IntegerField
from movies.models import Genre, Movie
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class FutureDateField(IntegerField):

    def validate(self, value):
        if value > datetime.datetime.today().year:
            raise ValidationError("Year cannot be in the future")


class MovieForm(ModelForm):
    title = CharField(max_length=128,
                      widget=TextInput(attrs={"class": "form-control"}))

    genre = ModelChoiceField(queryset=Genre.objects.all(),
                             widget=Select(attrs={"class": "form-control"}))
    director = CharField(max_length=128,
                         widget=TextInput(attrs={"class": "form-control"}))

    trailer = CharField(max_length=128,
                        widget=TextInput(attrs={"class": "form-control"}))

    year = FutureDateField(widget=TextInput(attrs={"class": "custom-select"}))

    class Meta:
        model = Movie
        fields = ("title", "genre", "director",
                  "trailer", "year", "movie_image")


class UpdateMovieForm(MovieForm):
    borrowed_by = ModelChoiceField(queryset=User.objects.all(),
                                   empty_label="If You not borrow, choose None!",
                                   widget=Select(attrs={"class": "form-control"}))

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
