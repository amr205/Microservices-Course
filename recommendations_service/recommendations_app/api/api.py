from rest_framework.response import Response
from recommendations_app.models import User, Song
from rest_framework.decorators import api_view

@api_view(["GET"])
def generate_recommendation(request):
    user = User.objects.get(id=request.data['user_id'])
    genres = user.genres.all()
    genres_id = [x.id for x in genres]

    songs = Song.objects.filter(genres__in=genres_id).order_by("-number_of_likes")[:5]
    songs_name = [x.name for x in songs]

    return Response(songs_name)