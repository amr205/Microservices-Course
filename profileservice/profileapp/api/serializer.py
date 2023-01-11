from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    favorite_genres = serializers.ListField()