from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
# Create your views here.


@api_view(['POST'])
def register(request):
    try:
        # checkUser = models.Customuser.objects.get(email = request.data.get('email'))

        # if checkUser:
        #     return Response("user already exist!")

        user = models.CustomUser.objects.create(username = request.data.get("username"), email = request.data.get("email"),password = request.data.get("password"))
        user.set_password(request.data.get('password'))
        user.save()
        return Response("success")

    except Exception as e:
        return Response(f"error{e}")