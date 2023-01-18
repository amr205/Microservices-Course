from django.db import models


class User(models.Model):
    id = models.CharField(max_length=200, primary_key=True)


class Artist(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Song(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    year = models.IntegerField()
    
    artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="songs", null=True)
    liked_by_users = models.ManyToManyField(User, related_name="liked_songs", null=True)