from rest_framework import viewsets
from songsapp.models import Song, Artist, Genre
from songsapp.api.serializers import SongSerializer, ArtistSerializer, GenreSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from sbus_utils import send_message
import json
from songs_service.viewsets import ChildModelViewset


class SongGenresViewSet(ChildModelViewset):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    parent_model = Song
    child_model = Genre
    parent_to_child_rel = "genres"


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(detail=True, methods=['patch'])
    def like(self, request, pk=None):
        song = Song.objects.get(id=pk)
        song_serializer = SongSerializer(song)
        data = {
            'action': 'liked',
            'song': song_serializer.data
        }
        send_message(json.dumps(data))
        return Response(data)

    @action(detail=True, methods=['patch'])
    def unlike(self, request, pk=None):
        song = Song.objects.get(id=pk)
        song_serializer = SongSerializer(song)
        data = {
            'action': 'unliked',
            'song': song_serializer.data
        }
        send_message(json.dumps(data))
        return Response(f'Unliked Song: {pk}')


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer