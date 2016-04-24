from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from models import Pages
# Create your views here.

def processCMS(request,recurso):
    if request.method == "GET":
        try:
            fila = Pages.objects.get(name = recurso)
            plantilla = get_template('plantilla.html')
            Context = ({'contenido':fila.page})
            return HttpResponse(plantilla.render(Context))
        except Pages.DoesNotExist:
            return HttpResponse('Page Not Found')

    elif request.method == "PUT":
        try:
            pagina = request.body
            fila = Pages.objects.get(name=recurso,page=pagina)
            fila.save()
            return HttpResponse('Nueva pagina')
        except:
            return HttpResponse("Error, try again")
def addCSS(request,recurso):
    if request.method=="GET":
        try:
            fila = Pages.objects.get(name='css/'+recurso)
            return HttpResponse(fila.page,content_type='text/css')
        except Pages.DoesNotExist:
            return HttpResponse('Page not found')
    elif request.method == "PUT":
        try:
            pagina = request.body
            fila = Pages.objects.create(name='css/'+recurso,page = pagina)
            fila.save()
            return HttpResponse("CSS incluido")
        except :
            return HttpResponse("Error, try again. ")
