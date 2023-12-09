from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from . import models
from django.contrib.auth import authenticate, login,logout
from rest_framework.authtoken.models import Token
from .serializers import userSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import utils
from django_ratelimit.decorators import ratelimit
from .sendEmail import sendMail
from .passwordOperations.resetPass import passwordReset, ResetPasswordAPI
from .bms_routes.movies_routes import create_movie,get_all_movies 
# Create your views here.
utils.create_groups_and_permissions()


# Register
@api_view(['POST'])
@ratelimit(key='user', rate='5/m', block=True)
def register(request):
    try:
        user = models.CustomUser.objects.create(username = request.data.get("username"), email = request.data.get("email"),password = request.data.get("password"), phone_number = request.data.get('phone_number'))
        user.set_password(request.data.get('password'))

        #Assign the user to 'User Group' by default
        user_group = utils.Group.objects.get(name = 'User Group')

        user.groups.add(user_group)
        user.save()
        return Response("success")

    except Exception as e:
        return Response(f"error{e}")
    


@api_view(['POST'])
@ratelimit(key='user', rate='5/m', block=True)
def admin_register(request):
    try:
        user = models.CustomUser.objects.create(username = request.data.get("username"), email = request.data.get("email"),password = request.data.get("password"), phone_number = request.data.get('phone_number'))
        user.set_password(request.data.get('password'))

        #Assign the user to 'User Group' by default
        user_group = utils.Group.objects.get(name = 'Admin Group')

        user.groups.add(user_group)
        user.save()
        return Response("success")

    except Exception as e:
        return Response(f"error{e}")


#Login
@api_view(['POST'])
@ratelimit(key='user', rate='5/m', block=True)
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
            mail_body = "We hope this message finds you well. We are writing to inform you that our system has detected a new login to your account."
            sendMail(res_user.data.get("email"), "New Login Detected!", mail_body)
            return Response(res_map)
        else:
            return Response({"error": "invalid credentials!"})

    except Exception as e:
        return Response({"error": e})

#Logout
@api_view(["POST"])
@ratelimit(key='user', rate='5/m', block=True)
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        logout(request)
        request.auth.delete()
        return Response({'message':'Logout Successfully'})


    except Exception as e:
        return Response({'error':f'There is an error:{str(e)}'})
    

#get User
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@ratelimit(key='user', rate='5/m', block=True)
def get_user(request,pk):
    try:
        res = request.user
        user = models.CustomUser.objects.get(id = pk)
        if  res == user:
            res_user = userSerializer(user,many = False)
            return Response(res_user.data)
        else:
            return Response("You do not have permission")

    except Exception as e: 
        return Response(f"There is an error:{str(e)}") 







