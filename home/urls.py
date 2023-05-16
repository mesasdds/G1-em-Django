from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.HomeView, name='homeview'),
    path('home/', views.HomeView, name="homeview"),
    path('artigo_principal/<int:artigoP_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('artigo_secundario/<int:artigoS_id>/', views.detalhe_artigo2, name='detalhe_artigo2'),
    path('artigo_terceiro/<int:artigoT_id>/', views.detalhe_artigo3, name='detalhe_artigo3'),
    path('artigo_generico/<int:artigoGe_id>/', views.detalhe_artigogenerico, name='detalhe_artigo4'),
    path('artigo_recomendado/<int:artigoRec_id>/)', views.detalhe_recommends, name='detalhe_artigo5'),
    path('index/', views.minha_view, name='minha_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)