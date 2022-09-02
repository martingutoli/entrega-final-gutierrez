from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from inmobiliaria.models import Alquileres, Ventas


# Create your views here.

def inicio(request):
    return render (request, "inmobiliaria/index.html")

def alquileres(request):
    alquileres = Alquileres.objects.all()
    context = {
        "alquileres": alquileres
    }
    return render (request, "inmobiliaria/alquileres.html", context)

def ventas(request):
    return render(request, "inmobiliaria/ventas.html")

def about(request):
    return render(request, "inmobiliaria/about.html")
