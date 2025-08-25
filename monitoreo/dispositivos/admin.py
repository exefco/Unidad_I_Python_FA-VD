from django.contrib import admin
from .models import Dispositivo, Zona, Categoria, Medicion, Alerta

admin.site.register([Zona,Categoria,Medicion,Alerta])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ("nombre","categoria","zona","consumo_Maximo")
