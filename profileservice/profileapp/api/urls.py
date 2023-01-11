from profileapp.api.router import user_view
from django.urls import path

urlpatterns = [
    path('', user_view, name='profileapp.root')
]