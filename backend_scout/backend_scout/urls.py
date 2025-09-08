"""
Configuración de URL para el proyecto backend_scout.

Este archivo es donde se definen las "rutas" o "direcciones" de su aplicación web.
Cuando un usuario ingresa una URL en su navegador (por ejemplo, www.misitio.com/admin/),
Django busca en este archivo `urls.py` para ver qué función o clase debe ejecutar
para responder a esa solicitud.

La lista `urlpatterns` dirige las URLs a las vistas. Para más información, consulta:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Ejemplos de cómo definir URLs:

Vistas basadas en funciones:
    Son funciones de Python que reciben una solicitud web y devuelven una respuesta.
    1. Añadir una importación:  from my_app import views
    2. Añadir una URL a urlpatterns:  path('', views.home, name='home')
       - `path('', ...)`: Define la URL. En este caso, la raíz del sitio.
       - `views.home`: La función de vista que se ejecutará cuando se acceda a esta URL.
       - `name='home'`: Un nombre para esta URL, útil para referenciarla en plantillas o código Python.



Incluyendo otra configuración de URL:
    Para proyectos grandes, es común dividir las URLs en archivos separados para cada aplicación.
    1. Importar la función include(): from django.urls import include, path
    2. Añadir una URL a urlpatterns:  path('blog/', include('blog.urls'))
       - `path('blog/', ...)`: Todas las URLs que comiencen con 'blog/' serán manejadas por 'blog.urls'.
       - `include('blog.urls')`: Le dice a Django que busque las URLs adicionales en el archivo `urls.py` de la aplicación 'blog'.
"""
from django.contrib import admin
from django.urls import path, include # Importamos 'include' para poder incluir URLs de otras aplicaciones.

# urlpatterns es la lista principal donde se definen todas las rutas de URL de su proyecto.
# Cada elemento en esta lista es una función `path()` que mapea una URL a una vista.
urlpatterns = [
    # Esta línea define la URL para la interfaz de administración de Django.
    # Cuando accedes a '/admin/', Django te mostrará el panel de administración.
    path('admin/', admin.site.urls),
    # Si tuvieras otras aplicaciones, las incluirías aquí, por ejemplo:
    # path('mi_app/', include('mi_app.urls')),
]
