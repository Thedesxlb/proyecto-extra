from django.db import models


class Cabañas(models.Model): 
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Cabaña")
    clave = models.CharField(max_length=50, verbose_name="Clave")
    descripcion = models.TextField(verbose_name="Descripcion")
    personas = models.CharField(max_length=50 ,verbose_name="Numero maximo de personas")
    camas = models.CharField(max_length=50, verbose_name="Numero de Camas")
    costo = models.CharField(max_length=50, verbose_name="Costo por día")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotos")
    created = models.DateTimeField(auto_now_add=True) 
    update = models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name = "Cabañas"
        verbose_name_plural = "Cabañas"
        ordering = ["created"]
        
    def __str__(self):
        return self.nombre


class Promociones(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombrePromo = models.CharField(max_length=100, verbose_name="Nombre de la Cabaña")
    descripcionPromo = models.TextField(verbose_name="Descripcion")
    costoPromo = models.CharField(max_length=50, verbose_name="Costo de promoción")
    imagenPromo = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Subido") 
    update = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado") 
    class Meta:
        verbose_name = "Promociones"
        verbose_name_plural = "Promociones"
        ordering = ["created"]
        
    def __str__(self):
        return self.nombrePromo

class Opinion(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombreClien = models.CharField(max_length=50, verbose_name="Nombre del Cliente")
    nombreCabaña = models.CharField(max_length=50, verbose_name="Nombre de la Cabaña")
    duda = models.TextField(verbose_name="Duda")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Subido") 
    update = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado") 
    imagenOp = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotos")
    
    class Meta:
        verbose_name = "Opiniones"
        verbose_name_plural = "Opiniones"
        ordering = ["created"]
    def __str__(self):
        return self.nombreClien


