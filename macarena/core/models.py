from django.db import models
from django.forms import URLField
from .fields import UniqueBooleanField
# Create your models here.
class Home(models.Model):
    nombre_tema = models.CharField(max_length=200)
    selecionado = UniqueBooleanField()
    mostrar_dolar = models.BooleanField(default=True)
    titulo_principal = models.CharField(max_length=200)
    imagen_1 = models.ImageField(upload_to='images-home')
    imagen_2 = models.ImageField(upload_to='images-home')
    imagen_Servicios = models.ImageField(upload_to='images-home')
    titulo1 = models.CharField(max_length=200)
    texto1 = models.TextField()    
    titulo2 = models.CharField(max_length=200)
    texto2 = models.TextField()
    servicio_1=models.CharField(max_length=50)
    servicio_2=models.CharField(max_length=50)
    servicio_3=models.CharField(max_length=50)
    servicio_4=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tema
    
    class Meta:
        verbose_name = "Tema Home"
        verbose_name_plural = "Temas Home"

    def __unicode__(self):
        return str(self.selecionado)

class footer(models.Model):
    nombre_footer = models.CharField(max_length=200)
    selecionado = UniqueBooleanField()
    titulo =  models.CharField(max_length=200)
    texto = models.TextField()
    servicio_1= models.CharField(max_length=50)
    servicio_2= models.CharField(max_length=50)
    servicio_3= models.CharField(max_length=50)
    servicio_4= models.CharField(max_length=50)
    link_1_nombre= models.CharField(max_length=50)
    link_2_nombre= models.CharField(max_length=50)
    link_3_nombre= models.CharField(max_length=50)
    link_4_nombre= models.CharField(max_length=50)
    link_1_url= models.URLField(max_length=200)
    link_2_url= models.URLField(max_length=200)
    link_3_url= models.URLField(max_length=200)
    link_4_url= models.URLField(max_length=200)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='images-services')
    caption = models.CharField(max_length=200)  
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

