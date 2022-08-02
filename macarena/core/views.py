from django.shortcuts import render
from .scripts import dolar_scraping

# Create your views here.
def homeView(request):
    context = {}
    context["dolar"] = dolar_scraping()
    return render(request, 'index.html',context=context)