from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



# Esta es la respuesta http mas simple que podemos crear 
# se gestiona desde la carpeta premios/urls.py
def index(request):
    return HttpResponse("Hello Word")