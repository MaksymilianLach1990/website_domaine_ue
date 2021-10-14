
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vineyards/', views.vineyards, name='vineyards'),
    path('domains_list/', views.domains_list, name='domains list'),
    path('<int:id>/', views.domaine_detals, name='domaine detals'),
    path('work/', views.work, name='work'),
    path('spring_season', views.spring_season, name='spring season'),
    path('winter_season/', views.winter_season, name='winter season'),
    path('vintage/', views.vintage, name='vintage'),
    path('contact/', views.contact, name='contact')
]
