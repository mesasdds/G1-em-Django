from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.


def homeEsports (request):
    return render(request, 'esports/home.html')