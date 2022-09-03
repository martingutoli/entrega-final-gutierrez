from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from inmobiliaria.models import Alquileres, Ventas


# Create your views here.

def inicio(request):

    listado_inmuebles = Alquileres.objects.all()

    return render (request, "inmobiliaria/index.html", {"inmuebles": listado_inmuebles})

def alquileres(request):
   
    listado_inmuebles = Alquileres.objects.filter(tipo_de_operacion = 'Alquiler')

    return render (request, "inmobiliaria/alquileres.html", {"inmuebles": listado_inmuebles})

def ventas(request):

    listado_inmuebles = Ventas.objects.filter(tipo_de_operacion = 'Venta')

    return render(request, "inmobiliaria/ventas.html", {"inmuebles": listado_inmuebles})

def about(request):
    return render(request, "inmobiliaria/about.html")
