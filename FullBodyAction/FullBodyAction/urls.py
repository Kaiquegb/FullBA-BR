from django.urls import path
from app_FullBA import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'treino'),
    path('cadastro/', views.cadastro, name='usuarios'),
    path('login/', views.login, name='login'),
    path('musculo/', views.smash, name='smash'),
    path('consumo_agua/', views.registro, name='registro_agua'),
    path('medidas/', views.exercicios, name= 'medidas')
    
]
