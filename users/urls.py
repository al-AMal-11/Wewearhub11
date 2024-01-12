from django.urls import path
from . import views

urlpatterns = [
    # Other URLs
    path('', views.custom_login, name='login'),
    path('register/', views.custom_register, name='register'),
    path('home', views.home, name='home'),
]

