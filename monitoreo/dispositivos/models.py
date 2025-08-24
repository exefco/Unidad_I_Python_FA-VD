from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nombre

class Zona(models.Model):
    nombre = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo_Maximo = models.IntegerField()
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)
    zona = models.ForeignKey(Zona,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre
    
class Medicion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    consumo_registrado = models.IntergerField()
    dispositivo = models.ForeignKey(Dispositivo,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Medición con fecha: {self.fecha} del dispositivo: {self.dispositivo.nombre}, consumo: {self.consumo_registrado}"
    
class Alerta(models.Model):
    mensaje = models.CharField(max_length=250)
    nivel_alerta = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    dispositivo = models.ForeignKey(Dispositivo,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Alerta: {self.mensaje} - Nivel: {self.nivel_alerta} - Dispositivo: {self.dispositivo.nombre}"

