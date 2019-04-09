from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Movie
from .serializer import MovieSerializer
# Create your views here.

class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class SearchMovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        movie = self.request.GET.get('movie')
        return Movie.objects.filter(movie_name__contains=movie)

