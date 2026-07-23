from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    rating = models.FloatField()

    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='movies')
    genres = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name='movies')

    def __str__(self):
        return self.title