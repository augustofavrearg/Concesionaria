from django.db import models
from django.forms import CharField, DateField, ImageField
import datetime
from django.db.models.fields.files import ImageField

# Create your models here.


class Auto(models.Model):

    nombre = models.CharField(max_length= 100, default="inserte nombre")
    suceso = models.CharField(max_length= 100, default="venta, alquiler o permutacion")
    marca = models.CharField(max_length= 100, default=" ")
    modelo = models.TextField(default=" ")
    imagen = models.ImageField(default = "adjunte imagen" , upload_to='autos/images/')
    imagen2 = models.ImageField(upload_to='autos/images/', default = "adjunte imagen" )
    imagen3 = models.ImageField(upload_to='autos/images/', default = "adjunte imagen" )
    imagen4 = models.ImageField(upload_to='autos/images/', default = "adjunte imagen" )
    imagen5 = models.ImageField(upload_to='autos/images/', default = "adjunte imagen" )
    imagen6 = models.ImageField(upload_to='autos/images/', default = "adjunte imagen" )
    fecha = models.DateField(datetime.date.today, default= None)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=1)
    año = models.IntegerField(default=0)
    km = models.TextField(default="inserte kilometros")
    motor = models.TextField(default="...")