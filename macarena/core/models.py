from django.db import models
from django.forms import URLField
from .fields import UniqueBooleanField
from ckeditor.fields import RichTextField
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
    articulo = RichTextField(blank=True,null=True)
    articulo_servicios = RichTextField(blank=True,null=True)
    articulo_sobre_mi = RichTextField(blank=True,null=True)
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
    mi_nombre =  models.CharField(max_length=200)
    texto = models.TextField()
    # redes
    facebook = models.URLField(max_length=200,blank=True,null=True)
    twitter = models.URLField(max_length=200,blank=True,null=True)
    google = models.URLField(max_length=200,blank=True,null=True)
    instagram = models.URLField(max_length=200,blank=True,null=True)
    linkedin = models.URLField(max_length=200,blank=True,null=True)
    github = models.URLField(max_length=200,blank=True,null=True)
    # servicios
    servicio_1= models.CharField(max_length=50,blank=True,null=True)
    servicio_2= models.CharField(max_length=50,blank=True,null=True)
    servicio_3= models.CharField(max_length=50,blank=True,null=True)
    servicio_4= models.CharField(max_length=50,blank=True,null=True)
    # links
    link_1_nombre= models.CharField(max_length=50,blank=True,null=True)
    link_2_nombre= models.CharField(max_length=50,blank=True,null=True)
    link_3_nombre= models.CharField(max_length=50,blank=True,null=True)
    link_4_nombre= models.CharField(max_length=50,blank=True,null=True)
    link_1_url= models.URLField(max_length=200,blank=True,null=True)
    link_2_url= models.URLField(max_length=200,blank=True,null=True)
    link_3_url= models.URLField(max_length=200,blank=True,null=True)
    link_4_url= models.URLField(max_length=200,blank=True,null=True)
    # datos
    direccion = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    telefono = models.CharField(max_length=200,blank=True,null=True)

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

