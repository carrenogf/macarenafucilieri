from django.contrib import admin
from .models import *
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ('nombre_tema','selecionado','titulo_principal')

class FooterAdmin(admin.ModelAdmin):
    list_display = ('nombre_footer','selecionado','titulo')

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')

admin.site.register(Home,HomeAdmin)
admin.site.register(footer,FooterAdmin)
admin.site.register(Servicio,ServicioAdmin)