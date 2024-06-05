from datetime import datetime

from django.shortcuts import render


# def _home(request):
#     now = datetime.datetime.now()
#     html = f'<html><body> It is now {now}</body></html>'
#     return HttpResponse(html)
def home(request):
    now = datetime.now()
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Jeferson Guimarães',
        'date': f'{now}'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html')
