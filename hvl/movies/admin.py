from django.contrib import admin
from movies.models import Genre, Movie

admin.site.register(Movie)
admin.site.register(Genre)
