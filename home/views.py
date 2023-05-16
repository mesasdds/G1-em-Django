from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos, ArtigosRecommends
from django.http import JsonResponse
import requests

# Create your views here.


def minha_view(request):
    response = requests.get('http://127.0.0.1:8000/api/ArtigoSecundario/')
    data = response.json()
    return render(request, 'home/index.html', {'data': data})


def HomeView(request):
    #artigoP = ArtigoPrincipal.objects.latest('create_at')
    response = requests.get('http://127.0.0.1:8000/api/')
    data = response.json()

    dataPrincipal = data['ArtigoPrincipal']
    resposta = requests.get(dataPrincipal)
    artigoP = resposta.json()

    dataSecundaria = data['ArtigoSecundario']
    resposta2 = requests.get(dataSecundaria)
    artigoS = resposta2.json()

    dataTerceiro = data['ArtigoTerceiro']
    resposta3 = requests.get(dataTerceiro)
    artigoT = resposta3.json()

    dataGenerico = data['ArtigosGenericos']
    resposta4 = requests.get(dataGenerico)
    artigoGe = resposta4.json()

    dataRecommend = data['ArtigosRecommends']
    resposta5 = requests.get(dataRecommend)
    artigoRec = resposta5.json()

    print(artigoS)

    return render(request, 'home/homeview.html', {'artigoS':artigoS, 'artigoP':artigoP, 'artigoT':artigoT, 'artigoGe':artigoGe, 'artigoRec':artigoRec})


def detalhe_artigo(request):
    response = requests.get('http://127.0.0.1:8000/api/')
    data = response.json()

    dataPrincipal = data['ArtigoPrincipal']
    resposta = requests.get(dataPrincipal)
    artigoP = resposta.json()

    return render(request, 'home/detalhe_artigo1.html', {'artigoP':artigoP})


def detalhe_artigo2(request):
    response = requests.get('http://127.0.0.1:8000/api/ArtigoSecundario/')
    artigoS = response.json()

    return render(request, 'home/detalhe_artigo2.html', {'artigoS':artigoS})


def detalhe_artigo3(request):
    response = requests.get('http://127.0.0.1:8000/api/ArtigoTerceiro/')
    artigoT = response.json()

    return render(request, 'home/detalhe_artigo3.html', {'artigoT':artigoT})

def detalhe_artigogenerico(request):
    response = requests.get('http://127.0.0.1:8000/api/ArtigosGenericos/')
    artigoGe = response.json()

    return render(request, 'home/detalhe_artigogenerico.html', {'artigoGe':artigoGe})

def detalhe_recommends(request):
    response = requests.get('http://127.0.0.1:8000/api/ArtigosRecommends/')
    artigoRec = response.json()

    return render(request, 'home/detalhe_recommends.html', {'artigoRec':artigoRec})


'''
def add_content_primal(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        article = ArtigoPrincipal(titulo=titulo, texto=texto)
        article.save()
        return redirect('/home/')
    return render(request, 'home/add_content_primal.html')

'''