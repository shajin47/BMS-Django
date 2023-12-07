from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="add_new_user"),
    path('login/', views.user_login, name="login")
]