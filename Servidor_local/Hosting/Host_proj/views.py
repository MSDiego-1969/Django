from django.shortcuts import render
from django.http import HttpResponse
# Crear una vista en el HTML
def vista(request):
    return HttpResponse("Hola")
def vista1(request):
    return HttpResponse("Hola Diego")
# Ahora creamos una funcion que sera una nueva vista, en el HTML cambiamos el valor de la etiqueta por el diccionario que creamos igualando la etiqueta a el valor del string
def vista2(request):
    diccionario = {"etiqueta":"Ahora si????"}
    return render(request,"HTML/pagina1.html", context= diccionario)
    # return render(request,"pagina1.html",)
