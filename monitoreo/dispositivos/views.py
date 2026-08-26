from django.shortcuts import render,redirect,get_object_or_404
from .models import Dispositivo
from .forms import DispositivoForm

# Create your views here.
def inicio(requests):
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(requests, "dispositivos/panel.html",{"dispositivos":dispositivos})

def dispositivo(request,dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)

    return render(request,"dispositivos/dispositivo.html",{"dispositivo":dispositivo})

def crear_dispositivos(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm()
    
    return render(request,'dispositivos/crear.html',{'form':form})

def editar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo,id=dispositivo_id)
    if request.method == 'POST':
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm(instance=dispositivo)
    return render(request, 'dispositivos/editar.html',{'form':form})

def eliminar_dispositivo(request,dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo,id=dispositivo_id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('listar_dispositivos')
    return render(request,'dispositivos/eliminar.html',{'dispositivo':dispositivo})

