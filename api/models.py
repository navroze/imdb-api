from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    director = models.CharField(max_length = 50)
    movie_name = models.TextField()
    imdb_score = models.FloatField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.movie_name