from multiprocessing import context
from django.shortcuts import render
from .scripts import dolar_scraping
from .models import Home, footer, Servicio
from .forms import ContactoForm
# Create your views here.
def homeView(request):
    context = {
        'form':ContactoForm(),
        "dolar":dolar_scraping(),
        'tema':Home.objects.get(selecionado=True)
        }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Mensaje guardado"
        else:
            context['form'] = formulario

    return render(request, 'index.html',context=context)

def serviciosView(request):
    context = {}
    servicios = Servicio.objects.all()
    context["servicios"] = servicios
    context["range_servicios"] = range(len(servicios))
    context['tema'] = Home.objects.get(selecionado=True)
    return render(request,'Servicio_detail.html',context=context)

def aboutView(request):
    context = {}
    context['tema'] = Home.objects.get(selecionado=True)
    return render(request,'about.html',context=context)

def contactoView(request):
    context = {
    'form':ContactoForm(),
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Mensaje guardado"
        else:
            context['form'] = formulario
    return render(request,'contacto.html',context=context)