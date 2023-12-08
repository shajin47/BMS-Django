from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Movies
from datetime import timedelta
@api_view(["POST"])
def create_movie(request):
    try:
        movie = Movies.objects.create( movie_name= request.data.get("movie_name"),
            release_date = request.data.get("release_date"),
            duration= timedelta(days=request.data.get("duration").get('days'),
                                hours=request.data.get("duration").get('hours'),
                                minutes=request.data.get("duration").get('minutes')),
            rating= request.data.get("rating"),
            language = request.data.get("language"),
            genre = request.data.get("genre"),
            cbc = request.data.get("cbc"),
            movie_description= request.data.get("movie_description"))

        movie.save()
        return Response("Success")
    except Exception as e:
        return Response(f"There is the error :{e}")