from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.HomeView, name='homeview'),
    path('add_content_primal/', views.add_content_primal, name = 'add_content_primal' ),
    path('add_content_sec/', views.add_content_sec, name= 'add_content_sec'),
    path('add_content_terc/', views.add_content_terc, name='add_content_terc'),
    path('artigo/<int:id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('artigo2/<int:id>/', views.detalhe_artigo2, name='detalhe_artigo2'),
    path('artigo3/<int:id>/', views.detalhe_artigo3, name='detalhe_artigo3'),
    path('admin-view', views.lista_artigos, name="lista_artigos"),
    path('home/', views.HomeView, name="homeview"),
    path('index/', views.Index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)