from django.shortcuts import render

# Create your views here.
def inicio(requests):
    contexto = {"Nombre": "Panel de Dispositivos EcoEnergy"}
    productos = [{"nombre" : "Sensor de la puerta", "valor": 20},
                 {"nombre": "Sensor de la ventana", "valor": 120},
                 {"nombre": "Sensor del piso", "valor": 10},
                 {"nombre": "Sensor del Ventilador", "valor": 100}]
    
    consumo_max = 100

    return render(requests, "dispositivos/panel.html",{
        "contexto": contexto,
        "productos": productos,
        "Consumo_Maximo": consumo_max

    })
