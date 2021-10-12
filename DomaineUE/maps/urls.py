from django.urls import path 
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('points/', views.points, name='points'),
    path('date_vintage/', views.date_vintage, name='date_vintage'),
    
]