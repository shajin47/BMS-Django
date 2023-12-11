from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from ..models import Movies
from datetime import timedelta
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..utils import get_file_path
import os
import json
from ..serializers import MoviesSerializer
from rest_framework.pagination import PageNumberPagination
from django_ratelimit.decorators import ratelimit
# from ..media


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@ratelimit(key='user', rate='5/m', block=True)
def create_movie(request):
    try:
        user = request.user
        if user.groups.filter(name = 'Admin Group').exists():
            uploaded_file = request.FILES['photo']
            payload = json.loads(request.POST['payload'])
            path = get_file_path(uploaded_file)
            movie = Movies.objects.create( movie_name= payload.get("movie_name"),
                movie_poster = path,
                release_date = payload.get("release_date"),
                duration= timedelta(days=payload.get("duration").get('days'),
                                    hours=payload.get("duration").get('hours'),
                                    minutes=payload.get("duration").get('minutes')),
                rating= payload.get("rating"),
                language = payload.get("language"),
                genre = payload.get("genre"),
                cbc = payload.get("cbc"),
                movie_description= payload.get("movie_description"))

            movie.save()
            return Response({"Success": True,
                             "message":"New Movie has been added"})
        return Response({"Success": False,
                             "message":"You do not have Permission"})
    except Exception as e:
        return Response(f"There is the error :{e}")



#Get all Movies

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@ratelimit(key='user', rate='5/m', block=True)
def get_all_movies(request):
    try:
        # Configure pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Set the number of items per page as needed

        movies = Movies.objects.all()
        result_page = paginator.paginate_queryset(movies, request)

        serializer = MoviesSerializer(result_page, many=True)
        return paginator.get_paginated_response({"Success": True, "movies": serializer.data})
    except Exception as e:
        return Response({"error": f"There is an error: {e}"})