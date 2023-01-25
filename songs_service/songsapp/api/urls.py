from songsapp.api.api import SongViewSet, GenreViewSet, ArtistViewSet, SongGenresViewSet
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register(r'songs', SongViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'artists', ArtistViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('songs/<int:parent_pk>/genres/',
    SongGenresViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'patch': 'modify'
    })),
    path('songs/<int:parent_pk>/genres/<uuid:pk>',
    SongGenresViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]