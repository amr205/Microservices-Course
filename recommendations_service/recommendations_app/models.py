from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)


class Song(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number_of_likes = models.IntegerField()
    genres = models.ManyToManyField(Genre)


class User(models.Model):
    id = models.CharField(max_length=512, primary_key=True)
    genres = models.ManyToManyField(Genre)