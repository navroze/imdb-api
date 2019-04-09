from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'director', 'movie_name', 'imdb_score', 'genres')