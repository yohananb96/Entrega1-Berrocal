from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto

# Create your views here.

def busquedaProductos(request):

    return render(request, "busqueda_productos.html")


def buscar(request):

    if request.GET["prd"]:

        mensaje = "Articulo Encontrado: %r" %request.GET["prd"]

        producto = request.GET["prd"]

        if len(producto) > 20:

             mensaje = "Texto de busqueda demasiado largo"

        else:
            
            articulos = Articulos.objects.filter(nombre__icontains = producto)

            return render (request, "resultados_busqueda.html", {"articulos":articulos, "query": producto})
    
    else:

        mensaje = "No has introducido ningun termino de busqueda"

    return HttpResponse(mensaje)


def contacto(request):

    if request.method == "POST":

        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():

            inForm = miFormulario.cleaned_data

            send_mail(inForm['asunto'],inForm['mensaje'],

            inForm.get('email',''),['sergio_portal@hotmail.com'],)

            return render(request, "gracias.html")
    
    else:

        miFormulario = FormularioContacto()
    
    return render(request,"formulario_contacto.html", {"form":miFormulario})