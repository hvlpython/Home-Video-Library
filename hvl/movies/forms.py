from django.db.models.fields.files import ImageField
from django.forms import ModelForm, CharField, IntegerField, TextInput, ModelChoiceField
from movies.models import Genre, Movie


class MovieForm(ModelForm):
    title = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    genre = ModelChoiceField(queryset=Genre.objects.all())
    director = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    trailer = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    year = IntegerField(widget=TextInput(attrs={"class": "custom-select"}))

    class Meta:
        model = Movie
        fields = ("title", "genre", "director", "trailer", "year", "movie_image")


class GenreForm(ModelForm):
    name = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Genre
        fields = ('name',)
