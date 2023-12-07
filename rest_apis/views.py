from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from . import models
from django.contrib.auth import authenticate, login,logout
from rest_framework.authtoken.models import Token
from .serializers import userSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Register
@api_view(['POST'])
def register(request):
    try:
        user = models.CustomUser.objects.create(username = request.data.get("username"), email = request.data.get("email"),password = request.data.get("password"))
        user.set_password(request.data.get('password'))
        user.save()
        return Response("success")

    except Exception as e:
        return Response(f"error{e}")


#Login
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

#Logout
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        logout(request)
        request.auth.delete()
        return Response({'message':'Logout Successfully'})


    except Exception as e:
        return Response({'error':f'There is an error:{str(e)}'})




