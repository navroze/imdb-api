# imdb-api
A sample django rest api that will get data for movies using sample data.

# Local Setup for imdb application

1. Activate your virtual environment with python 3.5 and pip installed in it
2. Install dependencies mentioned in requirements.txt
  `pip install -r requirements.txt`
3. Add the .env file to the root project
4. Perform migration
 `python manage.py migrate`
5. Populate the any database using imdb.json.
  `python populate-database.py`
6. Since DEBUG is set to False we need to run the development in insecure mentioned
  `python manage.py runserver --insecure`
7. Create admin user with command
   `python manage.py createsuperuser`

# APIS

http://127.0.0.1:8000/movies/ -> list movies

http://127.0.0.1:8000/movies/:id -> list movie by id

http://127.0.0.1:8000/search_movie/?movie=The wizra -> Text Search on movie name
