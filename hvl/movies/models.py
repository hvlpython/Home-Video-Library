from django.db import models
from django.db.models import Avg


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True, default=None, max_length=128)
    director = models.CharField(max_length=128)
    trailer = models.CharField(max_length=128)
    year = models.IntegerField()
    movie_image = models.ImageField(blank=True, null=True, upload_to="images/mowies-image")

    #zmiany
    @property
    def average_rating(self):
        data = self.movie.all().aggregate(Avg('rating')).get('rating__avg', 0.00)
        print(data)
        return data
        # Change 0.00 to whatever default value you want when there
        # are no reviews.

    # def get_avg_rating(self):
    #     reviews = Rating.objects.filter(product=self)
    #     count = len(reviews)
    #     sum = 0
    #     for rvw in reviews:
    #         sum += rvw.rating
    #     return (sum / count)
    #///
    def __str__(self):
        return f"{self.title}"

