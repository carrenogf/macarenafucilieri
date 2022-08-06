from multiprocessing import context
from django.shortcuts import render
from .scripts import dolar_scraping
from .models import Home, footer, Servicio
# Create your views here.
def homeView(request):
    context = {}
    context["dolar"] = dolar_scraping()
    context['tema'] = Home.objects.get(selecionado=True)
    return render(request, 'index.html',context=context)

def serviciosView(request):
    context = {}
    servicios = Servicio.objects.all()
    context["servicios"] = servicios
    context["range_servicios"] = range(len(servicios))
    return render(request,'Servicio_detail.html',context=context)