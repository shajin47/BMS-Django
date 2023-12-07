from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import userSerializer
# Create your views here.


@api_view(['POST'])
def register(request):
    try:
        user = models.CustomUser.objects.create(username = request.data.get("username"), email = request.data.get("email"),password = request.data.get("password"))
        user.set_password(request.data.get('password'))
        user.save()
        return Response("success")

    except Exception as e:
        return Response(f"error{e}")
    
@api_view(['POST'])
def user_login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            
            login(request, user)

            # # Generate or get the authentication token
            token, created = Token.objects.get_or_create(user=user)

            res_user = userSerializer(user)

            res_map = {
                'token': token.key,
                'user': res_user.data,
                'message': "Login successful!"
            }
            return Response(res_map)
        else:
            return Response({"error": "invalid credentials!"})

    except Exception as e:
        return Response({"error": e})

    

