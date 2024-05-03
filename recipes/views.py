import datetime

from django.http import HttpResponse
from django.shortcuts import render


# def _home(request):
#     now = datetime.datetime.now()
#     html = f'<html><body> It is now {now}</body></html>'
#     return HttpResponse(html)
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Jeferson Guimarães',
    })


def contact(request):
    return render(request, 'recipes/contato.html')


def about(request):
    return HttpResponse('Sobre')
