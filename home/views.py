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
    response = requests.get('http://127.0.0.1:8000/api/')
    data = response.json()

    dataPrincipal = data['ArtigoPrincipal']
    resposta = requests.get(dataPrincipal)
    artigoP1 = resposta.json()
    artigoP = artigoP1[-1]

    dataSecundaria = data['ArtigoSecundario']
    resposta2 = requests.get(dataSecundaria)
    artigoS1 = resposta2.json()
    artigoS = artigoS1[-1]

    dataTerceiro = data['ArtigoTerceiro']
    resposta3 = requests.get(dataTerceiro)
    artigoT1 = resposta3.json()
    artigoT = artigoT1[-1]

    dataGenerico = data['ArtigosGenericos']
    resposta4 = requests.get(dataGenerico)
    artigoGe1 = resposta4.json()
    artigoGe = artigoGe1[-4:][::-1]

    dataRecommend = data['ArtigosRecommends']
    resposta5 = requests.get(dataRecommend)
    artigoRec = resposta5.json()

    print(artigoP)

    return render(request, 'home/homeview.html', {'artigoS':artigoS, 'artigoP':artigoP, 'artigoT':artigoT, 'artigoGe':artigoGe, 'artigoRec':artigoRec})


def detalhe_artigo(request, artigoP_id):
    response = requests.get('http://127.0.0.1:8000/api/')
    data = response.json()

    dataPrincipal = data['ArtigoPrincipal']
    resposta = requests.get(dataPrincipal)
    artigoP1 = resposta.json()

    artigoP = next((artigoP for artigoP in artigoP1 if artigoP['id'] == artigoP_id), None)


    return render(request, 'home/detalhe_artigo1.html', {'artigoP':artigoP})


def detalhe_artigo2(request, artigoS_id):
    response = requests.get('http://127.0.0.1:8000/api/ArtigoSecundario/')
    artigoS1 = response.json()

    artigoS = next((artigoS for artigoS in artigoS1 if artigoS['id'] == artigoS_id), None)

    return render(request, 'home/detalhe_artigo2.html', {'artigoS':artigoS})


def detalhe_artigo3(request, artigoT_id):
    response = requests.get('http://127.0.0.1:8000/api/ArtigoTerceiro/')
    artigoT1 = response.json()

    artigoT = next((artigoT for artigoT in artigoT1 if artigoT['id'] == artigoT_id), None)

    return render(request, 'home/detalhe_artigo3.html', {'artigoT':artigoT})

def detalhe_artigogenerico(request, artigoGe_id):
    response = requests.get('http://127.0.0.1:8000/api/ArtigosGenericos/')
    artigoGe1 = response.json()

    artigoGe = next((artigoGe for artigoGe in artigoGe1 if artigoGe['id'] == artigoGe_id), None)

    return render(request, 'home/detalhe_artigogenerico.html', {'artigoGe':artigoGe})

def detalhe_recommends(request, artigoRec_id):
    response = requests.get('http://127.0.0.1:8000/api/ArtigosRecommends/')
    artigoRec1 = response.json()

    artigoRec = next((artigoRec for artigoRec in artigoRec1 if artigoRec['id'] == artigoRec_id), None)

    return render(request, 'home/detalhe_recommends.html', {'artigoRec':artigoRec})


