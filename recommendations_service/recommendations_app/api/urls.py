from recommendations_app.api.api import generate_recommendation
from django.urls import path

urlpatterns = [
    path('get_recommendations', generate_recommendation)
]