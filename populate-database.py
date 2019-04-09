import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb.settings')

import django
django.setup()


def save_movies_to_db(movies):
    from api.models import Genre, Movie
    for movie in movies:
        genre_arr = movie['genre']
        movie_data = Movie.objects.create(
                director = movie['director'], 
                movie_name = movie['name'],
                imdb_score = movie['imdb_score']
        )
        for g in genre_arr:
            genre = g.strip()
            genre_data = Genre.objects.get(genre_name = genre)            
            movie_data.genres.add(genre_data)
        movie_data.save()



def save_genres_to_db(movies):
    from api.models import Genre
    genre_arr = set()
    for movie in movies:
        genre = movie['genre']
        for g in genre:
            genre_arr.add(g.strip())
    for genre in genre_arr:
        genre = Genre.objects.create(genre_name = genre)
        genre.save()

def get_json_data():
    with open('imdb.json', 'r') as f:
        movies = json.load(f)
        return movies

if __name__ == '__main__':
    movies = get_json_data()
    print("Creating genres table")
    save_genres_to_db(movies)
    print("Genre table created")
    print("Creating movie table")
    save_movies_to_db(movies)
    print("Movie table created")
