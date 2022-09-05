from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from inmobiliaria.models import Alquileres, Ventas
from django.contrib.auth.forms import AuthenticationForm
from inmobiliaria.forms import UserCustomCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


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


def form_busqueda(request):
    return render(request, "inmobiliaria/form_busqueda.html")

def buscar (request):
    inmueble_tipo = request.GET.get('descripcion', None)

    if not inmueble_tipo:
        return HttpResponse ("No indicaste nada")
    inmuebles_lista = Alquileres.objects.filter(descripcion__icontains=inmueble_tipo)
    return render(request, "inmobiliaria/resultado_busqueda.html", {"inmuebles": inmuebles_lista})

def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        context ={

            "form" : formulario
        }

        return render(request, "inmobiliaria/login.html", context)
    else:
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login  (request, usuario)
                return redirect("inicio")
            else:
                context = {
                    "error" : "Credenciales no validas",
                    "form" : formulario
                }
                
                return render(request, "inmobiliaria/login.html", context)
        else:

            context = {
                    "error" : "Formulario no valido",
                    "form" : formulario
            }
                
            return render(request, "inmobiliaria/login.html", context)

    return HttpResponse()

def registrar(request):

    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "inmobiliaria/registro.html", {"form": formulario})
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "inmobiliaria/registro.html", {"form": formulario, "error": "Formulario no valido"})