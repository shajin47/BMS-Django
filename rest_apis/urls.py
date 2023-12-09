from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name="add_new_user"),
    path('register/admin/', views.admin_register, name="add_new_admin"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('getuser/<pk>/', views.get_user, name="getuser"),
    path("password_reset/", views.passwordReset, name= 'reset_pass'),
    path("password-reset/<str:encoded_pk>/<str:token>/",views.ResetPasswordAPI,name="reset-password"),
    path('create_movie/',views.create_movie,name='create_movie'),
    path('get_all_movies/', views.get_all_movies, name="get_all_movies"),
    path('movies/', views.get_all_movies, name='get_all_movies'),
    path('theaters/', views.theater_list_create, name='theater-list-create'),
    path('showtimes/', views.showtime_list_create, name='showtime-list-create'), 
]