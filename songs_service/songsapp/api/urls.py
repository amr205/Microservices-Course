from songsapp.api.api import SongViewSet, GenreViewSet, ArtistViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'songs', SongViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'artists', ArtistViewSet)

urlpatterns = router.urls