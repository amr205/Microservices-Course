from rest_framework import serializers
from songsapp.models import Song, Artist, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    class Meta:
        model = Song
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'