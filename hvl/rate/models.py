from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return f"{self.rating}"


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return f"{self.movie.title} {self.name}"
