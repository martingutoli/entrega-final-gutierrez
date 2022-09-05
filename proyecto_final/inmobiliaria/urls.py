from django.urls import path
from inmobiliaria.views import *

urlpatterns =[
    path("", inicio, name = "inicio"),
    path("alquileres/", alquileres, name = "alquileres"),
    path("ventas/", ventas, name = "ventas"),
    path("about/", about, name = "about"),
    path("busqueda", form_busqueda, name = "busqueda"),
    path("resultados/", buscar, name = "resultado_busqueda"),
    path("login/", iniciar_sesion, name = "login"),
    path("registro/", registrar, name = "registro")

]
