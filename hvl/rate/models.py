from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from movies.models import Movie


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    # # unique, it's probably bad
    # class Meta:
    #     unique_together = ('rating', 'movie')

    def __str__(self):
        return f"{self.rating}"
