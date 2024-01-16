from django.shortcuts import render
from .models import Movie, Rating
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

def index(request):
    data = {
       "message":"World"
    }
    return render(request, 'index.html', data)

@api_view(['GET'])
def getAllMovies(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(movies, many=True)
    return Response(serialized_movies.data)

@csrf_exempt
@api_view(['POST'])
def vote(request):
    movie_id = request.data['movieId'] # kiszedjük a POST-ból az adatokat
    rating = request.data['rating']

    movie = Movie.objects.get(id = movie_id) # film lekérése id szerint
    new_rating = Rating(value = rating, movie = movie) # új rating object létrehozása és feltöltés adatokkal
    new_rating.save() # rating object elmentése (háttérben abatbázisba helyezi)

    movie = Movie.objects.get(id = movie_id) # újra lekérjük a módosult filmet
    serialized_movie = MovieSerializer(movie, many=False)

    return Response(serialized_movie.data)
