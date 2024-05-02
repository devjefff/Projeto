from django.http import HttpResponse
from django.shortcuts import render


def _home(request):
    return HttpResponse('HOME 1')


def contact(request):
    return HttpResponse('contato')


def about(request):
    return HttpResponse('Sobre')
