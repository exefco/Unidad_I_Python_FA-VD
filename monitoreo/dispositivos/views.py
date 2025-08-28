from django.shortcuts import render
from .models import Dispositivo

# Create your views here.
def inicio(requests):
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(requests, "dispositivos/panel.html",{"dispositivos":dispositivos})

def dispositivo(request,dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)

    return render(request,"dispositivos/dispositivo.html",{"dispositivo":dispositivo})