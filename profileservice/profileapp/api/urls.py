from profileapp.api.router import user_view, user_items_view
from django.urls import path

urlpatterns = [
    path('', user_view, name='profileapp.root'),
    path('<str:pk>', user_items_view, name='profileapp.items')
]