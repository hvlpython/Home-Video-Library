from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

from movies.models import Movie


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    # # unique, it's probably bad
    # class Meta:
    #     unique_together = ('rating', 'movie')
    # @property
    # def aver(self):
    #     return Movie.objects.annotate(avg_rating=Avg('rating_set__rating')).order_by('-avg_rating')


    def __str__(self):
        return f"{self.rating}"
