from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ArtigoPrincipal, ArtigoSecundario

# Create your views here.


def initial(request):
    return render(request, 'home/init.html')

def HomeView(request):
    return render(request, 'home/homeview.html')

def Index(request):
    return render(request, 'home/index.html')

def lista_artigos(request):
    artigos_principais = ArtigoPrincipal.objects.all()
    artigos_secundarios = ArtigoSecundario.objects.all()
    return render(request, 'home/lista_artigos.html', {'artigos_principais':artigos_principais, 'artigos_secundarios':artigos_secundarios} )

def detalhe_artigo(request, id):
    artigo_principal = ArtigoPrincipal.objects.get(id=id)
    return render(request, 'home/detalhe_artigo.html', {'artigo_principal':artigo_principal})

def detalhe_artigo2(request, id):
    artigo_secundario = ArtigoSecundario.objects.get(id=id)
    return render(request, 'home/detalhe_artigo2.html', {'artigo_secundario':artigo_secundario})

def detalhe_artigo3(request, id):
    artigo_terceario = ArtigoTerceiro.objects.get(id=id)
    return render(request, 'home/detalhe_artigo3.html', {'artigo_terceiro':artigo_terceario})


def add_content_primal(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        article = ArtigoPrincipal(titulo=titulo, texto=texto)
        article.save()
        return redirect('home/init')
    return render(request, 'home/add_content_primal.html')


def add_content_sec(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        article2 = ArtigoSecundario(titulo=titulo, texto=texto)
        article2.save()
        return redirect('home/init')
    return render(request, 'home/add_content_sec.html')


def add_content_terc(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        article3 = ArtigoTerceiro(titulo=titulo, texto=texto)
        article3.save()
        return redirect('home/init')
    return render(request, 'home/add_content_terc.html')