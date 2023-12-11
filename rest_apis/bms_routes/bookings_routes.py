from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..serializers import BookingSerializer,userSerializer,ShowTimeSerializer,TheaterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..sendEmail import sendMail
from ..models import CustomUser,Showtime,Theater
from django_ratelimit.decorators import ratelimit

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@ratelimit(key='user', rate='5/m', block=True)
def booking_create(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(id = request.data.get("user"))
        user = userSerializer(user) 
        show = Showtime.objects.get(id = request.data.get("showtime"))
        show.avaliable_seates = show.avaliable_seates - request.data.get("number_of_seats") 
        show.save()
        show = ShowTimeSerializer(show) 
        theater = Theater.objects.get(pk = show.data.get('theater'))
        theater = TheaterSerializer(theater)
        
        message = f"Dear {user.data.get('username')},\nI hope you are doing well. Here are your Booking Confirmation Details:\nBooking ID: {serializer.data.get('id')}\nShow Timing: {show.data.get('start_time')}\nYour Theater is: {theater.data.get('theater_name')}\nNumber of Seats Booked: {serializer.data.get('number_of_seats')}\n\nThank you for choosing our service. We look forward to providing you with an enjoyable experience!\n"
        # print(user.data.get("email"))
        sendMail(user.data.get("email"),"Booking Confirmation",message) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
