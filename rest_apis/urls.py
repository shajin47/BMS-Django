from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="add_new_user"),
    path('register/admin/', views.admin_register, name="add_new_admin"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('getuser/<pk>/', views.get_user, name="getuser"),
    path("password_reset/", views.passwordReset, name= 'reset_pass'),
    path("password-reset/<str:encoded_pk>/<str:token>/",views.ResetPasswordAPI,name="reset-password",
    )
]