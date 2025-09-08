"""
Configuración ASGI (Asynchronous Server Gateway Interface) para el proyecto backend_scout.

Este archivo es crucial para el despliegue de aplicaciones Django que necesitan manejar
operaciones asíncronas. Define cómo su aplicación Django se comunica con un servidor web
que soporta el protocolo ASGI.

**¿Qué es ASGI y por qué es importante?**
ASGI es una especificación que permite a las aplicaciones Python comunicarse con servidores web
de manera asíncrona. Es la evolución de WSGI (Web Server Gateway Interface), que solo soporta
operaciones síncronas. La principal ventaja de ASGI es su capacidad para manejar:
- **WebSockets:** Conexiones persistentes y bidireccionales, ideales para chat en tiempo real, notificaciones, juegos multijugador.
- **HTTP/2 y HTTP/3:** Protocolos web modernos que permiten multiplexación y otras características avanzadas.
- **Largas encuestas (Long Polling):** Mantener una conexión abierta para recibir actualizaciones en tiempo real.
- **Tareas en segundo plano:** Ejecutar operaciones que no bloquean el hilo principal de la aplicación.

En términos sencillos, si su aplicación Django necesita funcionalidades como WebSockets,
chat en tiempo real, o cualquier otra operación que requiera una conexión persistente
o de larga duración, un servidor ASGI (como Uvicorn, Daphne o Hypercorn) utilizará
este archivo `asgi.py` para interactuar con su aplicación. El servidor ASGI actúa
como un intermediario entre el cliente (navegador) y su aplicación Django,
permitiendo que las solicitudes asíncronas sean gestionadas eficientemente.

Este archivo expone el invocable ASGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo y el despliegue con ASGI, consulta la documentación oficial de Django:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establece la variable de entorno DJANGO_SETTINGS_MODULE.
# Esto le indica a Django qué archivo de configuración (settings.py) debe usar para cargar
# la configuración de su proyecto. Es un paso fundamental para que Django funcione correctamente.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_scout.settings')

# Obtiene la aplicación ASGI de Django.
# Esta función devuelve el objeto de aplicación ASGI que el servidor web (por ejemplo, Uvicorn)
# utilizará para enrutar las solicitudes entrantes a su proyecto Django.
# Es el punto de entrada principal para que el servidor se comunique con su aplicación
# en un contexto asíncrono, permitiendo el manejo de WebSockets y otras operaciones asíncronas.
application = get_asgi_application()
