from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from ..models import Movies
from datetime import timedelta
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_movie(request):
    try:
        user = request.user
        if user.groups.filter(name = 'Admin Group').exists():
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
            return Response({"Success": True,
                             "message":"New Movie has been added"})
        return Response({"Success": False,
                             "message":"You do not have Permission"})
    except Exception as e:
        return Response(f"There is the error :{e}")

