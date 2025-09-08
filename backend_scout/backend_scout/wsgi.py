"""
Configuración WSGI para el proyecto backend_scout.

Este archivo define cómo su aplicación Django se comunica con el servidor web.
WSGI (Web Server Gateway Interface) es un estándar de Python que describe
cómo un servidor web debe interactuar con las aplicaciones web escritas en Python.

En términos sencillos, cuando alguien visita su sitio web, el servidor web
(como Gunicorn, Apache con mod_wsgi, etc.) utiliza este archivo `wsgi.py`
para "hablar" con su aplicación Django y obtener la respuesta que debe enviar al navegador.

Expone el invocable WSGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os# Módulo para interactuar con el sistema operativo, incluyendo variables de entorno.

from django.core.wsgi import get_wsgi_application# Función para obtener la aplicación WSGI de Django.

# Establece la variable de entorno DJANGO_SETTINGS_MODULE.
# Esto le dice a Django qué archivo de configuración (settings.py) debe usar para su proyecto.
# Es crucial para que Django sepa dónde encontrar sus configuraciones.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_scout.settings')

# Obtiene la aplicación WSGI de Django.
# Esta es la "aplicación" principal que el servidor web utilizará para manejar las solicitudes.
# Es el punto de entrada para que el servidor web se comunique con su proyecto Django.
application = get_wsgi_application()
