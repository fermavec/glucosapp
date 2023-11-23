# Django
## Primer Paso
1. Instalamos django2.2.3
```
pip install django==2.2.3
```
2. Creamos proyecto
```
django-admin startproject <glucosapp>
```
3. Creamos archivo views.py dentro de carpeta ./glucosapp y agregamos lo siguiente:
```
from django.http import HttpResponse

def index(response):
    return HttpResponse('This is Glucosapp')
```
4. Ajustamos el archivo urls con esta view
5. Iniciamos servidor
```
py manage.py runserver
```

## Templates
1. A la misma altura de la carpeta ./glucosapp creamos la carpeta templates. Debemos generarla para tener y presentar información de mejor forma a través de las vistas. Adicionalmente, se debe integrar a la lista TEMPLATES del settings.py dentro del atributo DIRS
2. Creamos el template dentro de la carpeta templates (un html).
3. Se ajusta el views para importar render y se adecua el return de la función con su archivo template correcto.
4. Integramos los CDN's de Bootstrap para darle estilos al index.html (o template que creaste)
5. Ajustamos el contexto que queremos imprimir en el template mediante el uso del tercer argumento en el return de la vista. 
6. Pasamos la variable del contexto al index con el uso de 
```
{{ <variable> }}
```
7. Recuerda que también puedes recorrer listados o usar condicionales con 
```
{% for %}{% endfor %}
```

## Static Files
1. Creamos la carpeta "./static" con las subcarpetas correspondientes a cada tipo de archivo (css, js o img).
2. Creamos la siguiente constante en nuestro archivo "settings.py" para conectar la carpeta de estáticos:
```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
3. Recuerda que debes colocar el "{% load static %}" al inicio de tus template.
4. También, al vincular los estáticos, debes incluir el siguiente: 
```
src="{% static 'js/main.js' %}"
```
dentro de tu script o link en el template.

## Super User
1. Primero ejecuta las migraciones para cargar las tablas de la base de datos; por default, django usa sqlite.
```
python manage.py migrate
```
2. Creamos el super usuario
```
python manage.py createsuperuser
```
y llenamos la información solicitada

## Manejo de sistema de login
1. Creamos la vista correspondiente en el "urls.py"
2. Creamos la función del "views.py"
```
def login(request):
    return render(request, 'users/login.html', {
        # Context
    })
```

3. Creamos nuestro archivo template de usuarios en el directorio correspondiente
4. Integramos el formulario en el html del template sin olvidar que TODO formulario debe contener su CSRF "{% csrf_token %}" después de la etiqueta form
5. Para obtener la información del formulario es importante conocer el método de envío de información usando "request.method" dentro de la función definida en el "views.py"
6. Una vez identificado el método (en este caso post), es hora de crear el siguiente condicional:
```
if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
```

La explicación es simple: El método POST de request devuelve un diccionario cuyo nombre de las claves son los nombres de los inputs del formulario. Es por eso que se integran en el POST.get(clave_del_diccionario_definida_en_input_de_formulario)
7. Ahora debemos proceder con el proceso de autenticación. Para ello, usaremos en el "views.py" la función authenticate de la librería auth que django nos provee.
```
from django.contrib.auth import authenticate, login
```
8. Creamos el objeto usuario dentro de la vista login_view
```
user = authenticate(username=username, password=password)
```
9. Ajustamos el condicional que dará login a nuestro usuario
```
if user:
    login(request, user)
    print('Excelente!')
else:
    print('error de usuario')
```
10. Una vez logeado, el usuario debe ser redirigido a la página de inicio por lo que debemos importar redirect y agregarlo al if user de la vista login_view con la redireccion a la página que especifiquemos del "urls.py" (en este caso 'home').
```
from django.shortcuts import redirect
```
11. Hay que avisarle al usuario que está logeado por lo que usaremos el modulo message
```
from django.contrib import messages
```
y se agrega al login_view
12. Nuestra función login_view se ve de la siguiente forma:
```
def login_view(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}!')
            return redirect('home')
        else:
            messages.error(request,'Error de usuario o contraseña')

    return render(request, 'users/login.html', {
        # Context
    })
```
13. Creamos la url para logout en "urls.py" y la función para la vista en el "views.py"
14. Para poder ejecutar un logout importamos el método.
```
from django.contrib.auth import logout
```
15. Así queda nuestro logout_view
```
def logout_view(request):
    logout(request)
    return redirect('http://fermavec.com')
```

## New Users Form
Nota: A partir de aquí, dejaremos de usar formularios de HTML para usar formularios de Django.
1. Creamos la url en el "urls.py" y creamos nuestra función view en el "views.py". También crearemos el template correspondiente.
2. En Django, los formularios pueden ser implementados como Clases de Django sin necesidad de usar formularios de HTML. Dentro de la carpeta "./glucosapp" crearemos un archivo llamado "forms.py" e importaremos la clase:
```
from django import forms
```
3. Creamos nuestro formulario como una clase:
```
class RegisterForm(forms.Form)
    username = forms.CharField(required=True,
                               min_length=4, max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    private_key = forms.CharField(required=True)
```
4. En el "views.py" importamos nuestra nueva clase para poder instanciarla dentro de la función de la vista (en este caso register_view)
```
from .forms import RegisterForm
```
5. Ya instanciada se agrega al contexto del return render.
6. Ajustamos nuestro register.html para presentar la información de nuestro formulario. También puedes usar ciclos para presentar los campos del formulario en html
7. Para estilos extra tendremos que trabajar con nuestro parámetro widget en la clase del formulario. 
8. Ajustar el register_view en "views.py" para obtener la información agregada al formulario de registro.
9. Importamos el modelo de usuarios que django nos ofrece para registrar usuarios en base de datos.
```
from django.contrib.auth.models import User
```
y ajustamos el código en la función register_view
10. Agregamos una validación en la clase del formulario en el archivo "forms.py" recordando que el prefijo "clea_" se refiere a este concepto de validación.
11. Ya terminadas las validaciones que queremos crear en nuestro formulario; generamos el método save para delegar el registro en base de datos a nuestro formulario. Se agrega el método a la clase creada en el "forms.py" y se ajusta la función register_view en el "views.py" que pasará de:
```
def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        private_key = form.cleaned_data.get('private_key')
                       
        user = User.objects.create_user(username, email, password, private_key)

        if user:
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('home')

    return render(request, 'users/register.html', {
        #Context
        'form': form
    })
```
A:
```
def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('home')

    return render(request, 'users/register.html', {
        #Context
        'form': form
    })
```

## Herencia de Templates
1. Creamos un archivo base.html en la carpeta "/templates" y ponemos todas las etiquetas que se repetiran a lo largo de nuestro sitio web, las cuales son las que heredaremos a nuestras demás páginas.
2. Definimos los bloques que siguen la siguiente sintaxis:
```
{% block <nombre del bloque> %}
{% endblock %}
```
3. Para que una página herede de otra tendrás que agregar el siguiente código al inicio de cada archivo html:
```
{% extends '<nombre del archivo del que se hereda.html>' %}
```
4. Una vez hecho eso, utilizas los bloques que creaste en el archivo base para integrarlos en el archivo hijo, en la sección que requieres.
5. Refactorizamos nuestros html con {% includes '<nombre.html>' %}.
6. Creamos nuestro navbar.html para la barra de navegación tomando en cuenta que, en vez de usar "#" para los enlaces, usaremos "{% url '<nombre de url>' %}".
7. Hacemos uso del objeto user.is_authenticated para ajustar lo que queremos y no mostrar en la barra de navegación dependiendo del estado del usuario.

## App readings
1. Creamos la aplicación
```
py manage.py startapp <nombre en plural>
```
2. Registramos la app en INSTALLED_APPS que se encuentra dentro del settings.py en la carpeta general del proyecto.
```
INSTALLED_APPS = [
    'readings',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
3. Creamos nuestro primer modelo en el archivo "models.py" de nuestra aplicación. Ejemplo:
```
class Reading(models.Model):
    reading_value = models.DecimalField(max_digits=8, decimal_places=2)
    # 1. Glucose, 2. Carbs, 3. Medication Insulin, 4. Excersise, 5. Other Meds
    category = models.IntegerField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```
4. Ejecutamos migraciones.
```
py manage.py makemigrations
```
5. Aplicamos la migración.
```
py manage.py migrate
```
6. Registramos nuestro modelo en el archivo 'admin.py' que se encuentra dentro de la carpeta de la aplicación.
```
from .models import Reading

admin.site.register(Reading)
```
7. Sobre escribimos el objeto str en nuestro model para retornar un valor y no un objeto del tipo Reading.
```
 def __str__(self):
        return f"{self.reading_value} on {self.created_at}"
```
8. Ajustaremos nuestra view index para que reciba la información de este modelo.
```
def index(request):
    readings = Reading.objects.all().order_by('-id')

    return render(request, 'index.html', {
        #context
        'title': 'Registros | Glucosapp',
        'message': 'Agrega un registro',
        'readings': readings
    })
```
9. Haremos un refactor para crear una view basada en clases en nuestro archivo 'views.py' dentro de la carpeta de la aplicación.
```
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *

class ReadingListView(ListView):
    template_name = 'index.html'
    queryset = Reading.objects.all().order_by('-id')
```
10. En el "urls.py" de la carpeta principal agregamos la clase como vista.
```
path('', ReadingListView.as_view(), name='home'),
```
11. Agregamos el contexto al 'views.py' de la app readings:
```
def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
```
12. Ajustamos el bucle for del 'index.html' para que recorra en object_list:
```
{% for reading in object_list %}
```
13. Creamos la carpeta reading dentro de los templates para generar un archivo 'reading.html' que servirá para una visión detallada de nuestras lecturas.
14. En nuestra carpeta readings, creamos un archivo para las 'urls.py' del proyecto.
```
from django.urls import path

from . import views

urlpatterns = [
    path('<pk>', views.ReadingDetailView.as_view(), name='Reading'),
]
```
15. En el 'urls.py' del proyecto, habilitamos el 'urls.py' de la aplicación readings.
```
from django.urls import path, include
```
y en el urlpatterns va:
```
path('readings/', include('readings.urls')),
```
16. Para tener un orden adecuado, cada aplicación debe llevar sus propios templates por lo que moveremos la carpeta "templates/readings" a una nueva carpeta "templates" dentro del directorio de la aplicación "readings/" junto con el archivo "readings.html".

## Slugs
1. Ya obtenemos nuestros registros mediante el id, sin embargo esto no es la mejor opción por lo que debemos ajustar nuestro model readings para trabajar con slugs.
2. Agregamos el siguente atributo a nuestro modelo:
```
slug = models.SlugField(null=False, blank=False, unique=True)
```
3. Corremos las migraciones.
4. Aprobamos las migraciones.
5. Ajustamos el urlpattern en las urls.py de la aplicación
```
path('<slug:slug>', views.ReadingDetailView.as_view(), name='Reading'),
```
6. Configuramos nuestro modelo, el método save para que el slug se registre y genere de forma automática.
```
def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.id}in{self.category}from{self.created_at}')
        super(Reading, self).save(*args, **kwargs)
```
7. Configuramos nuestro 'admin.py' de la aplicación para no mostrar el atributo slug al dar alta.
```
class ReadingAdmin(admin.ModelAdmin):
    fields = ('reading_value', 'category', 'notes')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Reading, ReadingAdmin)
```

## Imágenes
1. Para trabajar con imágenes dentro de Django necesitamos instalar la librería Pillow
```
pip install Pillow
```
2. En caso de requerirlo, en tu modelo tendrías que agregar el atributo con su correspondiente models.ImageField()
3. También sería necesario actualizar el 'settings.py' para agregar las constantes MEDIA_URL y MEDIA_ROOT que apunten a un nuevo directorio llamado media.
4. Otra cosa a ajustar sería el 'urls.py' principal para que conecte las rutas estáticas y de media.