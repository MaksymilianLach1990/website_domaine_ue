from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('conditions/', views.conditions, name='conditions'),
    path('for_employers/', views.for_employers, name='for_employers'),
    path('for_workers/', views.for_workers, name='for_workers'),
    path('jobs/', views.jobs, name='jobs'),
]