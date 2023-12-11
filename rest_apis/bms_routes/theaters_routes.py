from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Theater
from ..serializers import TheaterSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_ratelimit.decorators import ratelimit
 
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@ratelimit(key='user', rate='5/m', block=True)
def theater_list_create(request):
    if request.method == 'GET':
         # Configure pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Set the number of items per page as needed
        theaters = Theater.objects.all()
        result_page = paginator.paginate_queryset(theaters, request)

        
        serializer = TheaterSerializer(result_page, many=True)
        return paginator.get_paginated_response({"Success": True, "movies": serializer.data})

    elif request.method == 'POST':
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
