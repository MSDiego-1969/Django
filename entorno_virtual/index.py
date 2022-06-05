# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
# conda install pytohn
# conda install django
# conda create --name entornoDjango en consola
# conda activate entornoDjango 
# Ingresar a la carpeta de nuestro proyecto "NO OLVIDAR"
# conda install django
# django-admin startproject "nombre del proyecto"
# cd e ingresar el directorio creado con django. En nuestro caso "servidor"
# python manage.py runserver para que arranque el servidor creado, en nuestro caso localhost
# copiar URL despues del arranque para ver en explorador http://127.0.0.1:8000/
# python manage.py startapp "nombre de la aplicacion" en nuestro caso 
# En la Aplicación creada (Host_proj) buscar el archivo "views.py" y generar una vista de la siguiente manera:
# from django.http import HttpResponse
# Crear una vista en el HTML
# def vista(request):
#     return HttpResponse("Hola")

# En el proyecto(Hosting), en el archivo url.py, importamos de la aplicacion Host_proj la vista creada en views.py de la siguiente manera:
# from Host_proj import views
# Y añadimos la ruta del servidor, si dejamos vacio el path toma la ruta que genero el servidor en el entorno virtual que creamos, pero se puede modificar
# path("",views.vista, name="vista"),

#Ahora en el fichero settings.py del Proyecto, en el item INSTALLED_APPS agregamos  el nombre de nuestra Aplicación (Host_proj):
# "Host_proj",

# Vamos a la terminal para arrancar el servidor con python manage.py runserver, copiamos la dirección que nos da y la pegamos en el navegador


# ******************************************************************************************************************

# Para crear otra ruta o path, creamos un archivo con la ruta incluida. Abrimos el archivos urls.py y en "urlpatterns" agregamos la línea : path("miruta/", include("Host_proj.miruta")),

# En el nuevo archivo escribimos: 
# from django.conf.urls import url
# from Host_proj import views
# urlpatterns= [
#     url("", views.vista1, name="vista1")
# Osea, creamos una nueva vista o página a la que podemos acceder desde el navegador con /miruta

# En el archivo views.py escribimos la funcion de la nueva vista: 
# def vista1(request):
# return HttpResponse("Hola Diego")

# Vamos a la terminal para arrancar el servidor con python manage.py runserver, copiamos la dirección que nos da y la pegamos en el navegador

# ****************************************************************************************************
# Crear plantilla o template (pagina html):
# En la carpeta del proyecto crear una carpeta llamada "templates" y allí un archivo "página1.html".Donde y con doble llave, en el body, creamos una etiqueta que sera una variable dinamica
# En settings.py le decimos donde se ecuentra el directorio template, en la linea BASE_DIR creamos un print(BASE_DIR) para ver que phat tiene. Importamos el "os" para juntar BASE_DIR con TEMPLATE_DIR. Copiamos esta dirección mas abajo en la línea TEMPLATE en la siguiente manera 'DIRS': [TEMPLATE_DIR,],
# En urls.py creamos la nueva ruta path("miruta1",views.vista1, name="vista1"),
# y en el archivo views.py creamos la funcion de la segunda vista: def vista1(request):
    # diccionario = {"etiqueta":"Este es el valor de la etiqueta"}
    # return render(request,"pagina1.html",context= diccionario)
 
# ****************************************************************************************************** 
# Crear carpeta de imagenes 
# Creamos la direccion STATIC_DIR para unir base con nuestra carpeta de imagenes
# STATIC_DIR = os.path.join(BASE_DIR,"static")

# conda deactivate 
# conda env list muestra todos los entornos, primero desactivar el que tenemos
# conda remove --name entornoDjango para borrar el entorno