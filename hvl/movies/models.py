from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    trailer = models.CharField(max_length=128)
    year = models.IntegerField()
    movie_image = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return f"{self.title}"


