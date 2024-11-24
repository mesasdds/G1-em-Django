from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.HomeView, name='homeview'),  # Página inicial
    path('add_content/<str:article_type>/', views.add_content, name='add_content'),  # Adicionar conteúdo
    path('artigo/<str:article_type>/<int:id>/', views.detalhe_artigo, name='detalhe_artigo'),  # Detalhe do artigo
    path('edit_content/<int:id>/<str:article_type>/', views.edit_content, name='edit_content'),  # Editar conteúdo
    path('admin-view', views.lista_artigos, name='lista_artigos'),  # Lista de artigos (admin)
    path('search/', views.search_results, name='search_results'),  # Busca
    path('home/', views.HomeView, name='homeview'),  # Página inicial alternativa
    path('index/', views.Index, name='index'),  # Página índice
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
