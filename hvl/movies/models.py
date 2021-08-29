from django.db import models


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
    movie_image = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return f"{self.title}"

