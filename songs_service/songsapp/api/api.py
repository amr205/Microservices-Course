from rest_framework import viewsets
from songsapp.models import Song, Artist, Genre
from songsapp.api.serializers import SongSerializer, ArtistSerializer, GenreSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(detail=True, methods=['patch'])
    def like(self, request, pk=None):
        return Response(f'Liked Song: {pk}')

    @action(detail=True, methods=['patch'])
    def unlike(self, request, pk=None):
        return Response(f'Unliked Song: {pk}')


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer