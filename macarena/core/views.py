from multiprocessing import context
from django.shortcuts import render
from .scripts import dolar_scraping
from .models import Home, Servicio
from .forms import ContactoForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic import TemplateView

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
            contactoMail(request)  # mail consulta
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
            contactoMail(request)  # mail consulta
            context['mensaje'] = "Mensaje guardado"
        else:
            context['form'] = formulario
    return render(request,'contacto.html',context=context)


def contactoMail(request):
    nombre = request.POST.get('nombre')
    emailUser = request.POST.get('email')
    asunto = 'Consulta ammfucilieri: '+request.POST.get('asunto')
    consulta = request.POST.get('consulta') 
    emailTemplate = render_to_string('email_template.html',
    {'nombre':nombre,'email':emailUser,'consulta':consulta})
    email = EmailMessage(
        asunto,
        emailTemplate,
        settings.EMAIL_HOST_USER,
        ['carrenogf@gmail.com']
    )
    email.fail_silently = False # para que no marque error en gmail
    email.send()

class Error404View(TemplateView):
    template_name = 'error_404.html'