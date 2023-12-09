from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True, null=True)



class Movies(models.Model):
    movie_name = models.CharField(max_length=256,blank=False)
    movie_poster = models.FileField(upload_to ="..media/", blank=False )
    release_date = models.DateField()
    duration = models.DurationField()
    rating = models.DecimalField(decimal_places=2,max_digits=4,default=0.0,validators=[MaxValueValidator(limit_value=10)])
    language = models.CharField(max_length=256)
    genre=models.CharField(max_length=256)
    cbc = models.CharField(max_length=256)
    movie_description  = models.TextField(max_length=2000)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)
