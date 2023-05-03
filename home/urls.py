from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos, name="lista_artigos"),
    path('add_content_primal/', views.add_content_primal, name = 'add_content_primal' ),
    path('add_content_sec/', views.add_content_sec, name= 'add_content_sec'),
    path('add_content_terc/', views.add_content_terc, name='add_content_terc'),
    path('<int:id>', views.detalhe_artigo3, name='detalhe_artigo3'),
    path('<int:id>/', views.detalhe_artigo2, name='detalhe_artigo2'),
    path('<int:id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('home/', views.HomeView, name="homeview"),
    path('index/', views.Index, name="index"),
]