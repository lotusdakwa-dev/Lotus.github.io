# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion_view, name='login'),
    path('logout/', views.deconnexion_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('ajouter-tuteur/', views.ajouter_tuteur, name='ajouter_tuteur'),
    path('ajouter-eleve/', views.ajouter_eleve, name='ajouter_eleve'),
    path('ajouter-inscription/', views.ajouter_inscription, name='ajouter_inscription'),
]