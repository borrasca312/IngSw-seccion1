
#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""
import os
import sys


def main():
    """Ejecuta tareas administrativas."""
    # Establece la variable de entorno DJANGO_SETTINGS_MODULE
    # Esto le dice a Django dónde encontrar la configuración del proyecto.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_scout.settings')
    try:
        # Intenta importar la función execute_from_command_line de Django.
        # Esta función es la que realmente ejecuta los comandos de Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no se puede importar, se lanza un error con un mensaje útil.
        # Esto ayuda a diagnosticar problemas comunes como Django no instalado
        # o un entorno virtual no activado.
        raise ImportError(
            "No se pudo importar Django. ¿Está seguro de que está instalado y "
            "disponible en su variable de entorno PYTHONPATH? ¿Olvidó "
            "activar un entorno virtual?"
        ) from exc
    # Ejecuta el comando de Django usando los argumentos de la línea de comandos.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Este es el punto de entrada principal cuando el script se ejecuta directamente.
    main()
