"""
Configuración de Django para el proyecto backend_scout.

Generado por 'django-admin startproject' usando Django 5.2.5.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.2/topics/settings/

Para la lista completa de configuraciones y sus valores, consulta
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os # Módulo para interactuar con el sistema operativo, incluyendo variables de entorno.
from pathlib import Path # Módulo para manejar rutas de archivos de manera más intuitiva y segura. 
from dotenv import load_dotenv # Importa la función para cargar variables de entorno desde un archivo .env.
import dj_database_url # Importa la librería para parsear URLs de bases de datos.

load_dotenv() # Carga las variables de entorno desde el archivo .env en la raíz del proyecto.
              # Esto permite que la aplicación acceda a configuraciones sensibles o específicas del entorno.

# Construye rutas dentro del proyecto como esta: BASE_DIR / 'subdir'.
# BASE_DIR es la ruta base del proyecto. Se usa para construir rutas a otros archivos y directorios.
# Es fundamental para que Django encuentre tus archivos y directorios, sin importar dónde esté instalado el proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de desarrollo rápido - no apto para producción
# Consulta https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡mantén en secreto la clave secreta usada en producción!
# SECRET_KEY es una cadena de caracteres larga y aleatoria utilizada para la seguridad de Django.
# Se usa para firmar cookies de sesión, tokens CSRF y otras operaciones criptográficas.
# ¡Nunca la compartas ni la expongas en un repositorio público en producción!
# Ahora se obtiene de las variables de entorno para mayor seguridad y flexibilidad.
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fsg2z)8t4k4vwza6(!r8&+xshg#66%*i-g@3xtz-z$mkg#6+t_')

# ADVERTENCIA DE SEGURIDAD: ¡no ejecutes con el modo depuración activado en producción!
# DEBUG = True activa el modo de depuración de Django.
# En este modo, Django muestra errores detallados en el navegador, lo cual es útil para el desarrollo.
# Sin embargo, en producción, esto puede exponer información sensible a los usuarios malintencionados.
# Siempre debe ser `False` en un entorno de producción.
# Ahora se obtiene de las variables de entorno. 'True' o 'False' se convierte a booleano.
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS es una lista de cadenas que representan los nombres de host/dominios que su sitio Django puede servir.
# En modo DEBUG=True, puede estar vacío. En producción, debe contener los dominios de su sitio (ej. ['www.example.com']).
# Se obtiene de las variables de entorno, permitiendo múltiples hosts separados por comas.
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else []


# Definición de aplicaciones
# INSTALLED_APPS lista todas las aplicaciones Django activas en este proyecto.
# Cada cadena en esta lista es una aplicación que Django carga y utiliza.
# Incluye aplicaciones integradas de Django (django.contrib.*) y cualquier aplicación personalizada que crees.
INSTALLED_APPS = [
    'django.contrib.admin', # Interfaz de administración de Django. Permite gestionar datos del modelo a través de una interfaz web.
    'django.contrib.auth', # Sistema de autenticación. Maneja usuarios, permisos y grupos.
    'django.contrib.contenttypes', # Framework para tipos de contenido. Permite asociar permisos a modelos.
    'django.contrib.sessions', # Framework de sesiones. Permite almacenar datos específicos del usuario entre solicitudes.
    'django.contrib.messages', # Framework de mensajes. Permite mostrar mensajes de una sola vez a los usuarios.
    'django.contrib.staticfiles', # Gestión de archivos estáticos. Ayuda a servir CSS, JavaScript e imágenes.
]

# MIDDLEWARE es una lista de clases middleware que procesan las peticiones antes de que lleguen a la vista
# y las respuestas antes de que se envíen al cliente.
# Cada middleware realiza una función específica, como seguridad, manejo de sesiones o autenticación.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Mejora la seguridad de su sitio.
    'django.contrib.sessions.middleware.SessionMiddleware', # Habilita el manejo de sesiones para los usuarios.
    'django.middleware.common.CommonMiddleware', # Realiza operaciones comunes como reescritura de URL.
    'django.middleware.csrf.CsrfViewMiddleware', # Protección contra ataques de falsificación de solicitudes entre sitios (CSRF).
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Asocia usuarios autenticados a las peticiones.
    'django.contrib.messages.middleware.MessageMiddleware', # Habilita el sistema de mensajes de Django.
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Protección contra ataques de clickjacking.
]

# ROOT_URLCONF especifica el módulo Python donde Django buscará las configuraciones de URL raíz.
# Este es el punto de partida para el enrutamiento de URL de su proyecto.
ROOT_URLCONF = 'backend_scout.urls'

# TEMPLATES configura los motores de plantillas que Django usará para renderizar HTML.
# Aquí se define cómo Django encontrará y procesará sus archivos HTML (plantillas).
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Motor de plantillas de Django.
        'DIRS': [], # Directorios adicionales donde buscar plantillas. Puedes añadir rutas a tus plantillas aquí.
        'APP_DIRS': True, # Permite que las aplicaciones busquen sus propias plantillas en sus directorios 'templates'.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request', # Añade el objeto `request` al contexto de la plantilla.
                'django.contrib.auth.context_processors.auth', # Añade variables de autenticación (usuario, etc.) al contexto.
                'django.contrib.messages.context_processors.messages', # Añade mensajes del framework de mensajes al contexto.
            ],
        },
    },
]

# WSGI_APPLICATION especifica el objeto WSGI que Django usará para servir la aplicación.
# Apunta al archivo `wsgi.py` que configuramos anteriormente.
WSGI_APPLICATION = 'backend_scout.wsgi.application'

# ASGI_APPLICATION especifica el objeto ASGI que Django usará para servir la aplicación
# en un entorno asíncrono (por ejemplo, para WebSockets).
# Apunta al archivo `asgi.py` que configuramos anteriormente.
ASGI_APPLICATION = 'backend_scout.asgi.application'


# Base de datos
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES configura las bases de datos que usará el proyecto.
# Por defecto, Django configura una base de datos SQLite, que es ideal para el desarrollo.
# En producción, es común usar bases de datos más robustas como PostgreSQL o MySQL.
# La configuración de la base de datos se obtiene de la variable de entorno DATABASE_URL.
# Esto permite cambiar fácilmente entre diferentes bases de datos (SQLite, PostgreSQL, MySQL)
# sin modificar el código, ideal para entornos de desarrollo y producción.
# Si DATABASE_URL no está definida, por defecto usa SQLite.
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3'))
}


# Validación de contraseñas
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS define las reglas para la validación de contraseñas de usuario.
# Estas reglas ayudan a asegurar que los usuarios elijan contraseñas seguras.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Valida la similitud con atributos del usuario (nombre, email).
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Valida la longitud mínima de la contraseña.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Valida contra una lista de contraseñas comunes y fáciles de adivinar.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Valida la presencia de números en la contraseña.
    },
]


# Internacionalización
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# LANGUAGE_CODE define el idioma por defecto para su proyecto Django.
LANGUAGE_CODE = 'es-cl' # Código de idioma por defecto (español de Chile en este caso).

# TIME_ZONE define la zona horaria por defecto para su proyecto.
# Es importante para el manejo correcto de fechas y horas en su aplicación.
TIME_ZONE = 'UTC' # Zona horaria por defecto (Coordinated Universal Time).

# USE_I18N habilita el sistema de internacionalización de Django, permitiendo traducir su aplicación.
USE_I18N = True # Habilita el sistema de internacionalización de Django.

# USE_TZ habilita el soporte para zonas horarias en Django, lo que es crucial para aplicaciones globales.
USE_TZ = True # Habilita el soporte para zonas horarias.


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL es la URL base para referenciar archivos estáticos (CSS, JS, imágenes) en sus plantillas.
# Por ejemplo, si STATIC_URL es '/static/', un archivo 'style.css' se accedería en '/static/style.css'.
STATIC_URL = 'static/'

# Tipo de campo de clave primaria por defecto
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD define el tipo de campo automático para las claves primarias de los modelos.
# BigAutoField es un entero de 64 bits, adecuado para la mayoría de los proyectos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
