"""
RUT validation utilities for Chilean RUT (Rol Único Tributario)
Used across the SGICS platform for person identification
"""

import re
from typing import Optional

def validar_rut(rut: str) -> bool:
    """
    Valida un RUT chileno en formato '12345678-9'.
    Retorna True si el RUT es válido, False si no lo es.
    """
    rut = rut.upper().replace(".", "").replace("-", "")
    
    if not rut or len(rut) < 2:
        return False

    cuerpo = rut[:-1]
    dv = rut[-1]

    if not cuerpo.isdigit():
        return False

    suma = 0
    multiplo = 2

    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo = 9 if multiplo == 7 else multiplo + 1

    resto = suma % 11
    dv_calculado = '0' if resto == 0 else 'K' if resto == 1 else str(11 - resto)

    return dv == dv_calculado
