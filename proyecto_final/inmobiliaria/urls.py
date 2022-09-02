from django.urls import path
from inmobiliaria.views import *

urlpatterns =[
    path("", inicio, name = "inicio"),
    path("alquileres/", alquileres, name = "alquileres"),
    path("ventas/", ventas, name = "ventas"),
    path("about/", about, name = "about"),

]
