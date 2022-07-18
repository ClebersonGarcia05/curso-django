from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('Contato')
