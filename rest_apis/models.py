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



class Theater(models.Model):
    theater_name = models.CharField(max_length=256,blank=False)
    city = models.CharField(max_length=100, blank=False)
    capacity = models.IntegerField(blank = False, default=0)
    cancellation = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

class Showtime(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)

    def __str__(self):
        return f"{self.movie.movie_name} at {self.theater.theater_name} - {self.start_time}"

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=256, blank=False)
    number_of_seats = models.IntegerField(blank=False, default=1)
    total_price = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}'s booking for {self.showtime}"