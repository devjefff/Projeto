import datetime

from django.http import HttpResponse
from django.shortcuts import render


# def _home(request):
#     now = datetime.datetime.now()
#     html = f'<html><body> It is now {now}</body></html>'
#     return HttpResponse(html)
def home(request):
    return render(request, 'home.html')


def contact(request):
    return HttpResponse('contato')


def about(request):
    return HttpResponse('Sobre')
