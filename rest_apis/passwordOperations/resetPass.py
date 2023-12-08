from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, response 
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.conf import settings
from ..serializers import EmailSerializer, ResetPasswordSerializer
from .. import models
# ========================================

#reset password
@api_view(['POST'])
def passwordReset(request):
    # # The data parameter in the serializer is used for deserialization, where the serializer will take the raw data from the request and convert it into a Python object, validating the data in the process.
    # serializer = EmailSerializer(data=request.data)
    # # is_valid() - will check the email format
    # serializer.is_valid(raise_exception=True)
    # email = serializer.data["email"]
    user = models.CustomUser.objects.filter(email = request.data.get('email')).first()
    print(user)
    if user:
        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
        reset_link = f"http://127.0.0.1:8000{reset_url}"
        # send the rest_link as mail to the user.

        return Response(
            {
                "message": 
                f"Your password rest link: {reset_link}"
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"message": "User doesn't exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )



@api_view(['PATCH'])
def ResetPasswordAPI(request, *args, **kwargs):
    """
    Verify and Reset Password Token View.
    """
    
    serializer = ResetPasswordSerializer(
        data=request.data, context={"kwargs": kwargs}
    )
    serializer.is_valid(raise_exception=True)
    return Response(
        {"message": "Password reset complete"},
        status=status.HTTP_200_OK,
    )
