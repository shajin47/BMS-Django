from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Showtime
from ..serializers import ShowTimeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import Theater

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def showtime_list_create(request):
    if request.method == 'GET':
        # Configure pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Set the number of items per page as needed
        showtimes = Showtime.objects.all()
        result_page = paginator.paginate_queryset(showtimes, request)

        serializer = ShowTimeSerializer(result_page, many=True)
        return paginator.get_paginated_response({"Success": True, "showtimes": serializer.data})

    elif request.method == 'POST':
        Capacity = Theater.objects.get(id = request.data.get('theater')).capacity
        request.data["avaliable_seates"] = Capacity
        serializer = ShowTimeSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
