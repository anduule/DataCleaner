
from pathlib import Path


def generar_reporte(reporte: dict, ruta_salida: str | Path) -> Path:
    """
    Genera un reporte de texto con los resultados de la limpieza.
    """

    ruta_salida = Path(ruta_salida)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    contenido = f"""REPORTE DE DATACLEANER
=====================

Resumen del procesamiento

Registros procesados: {reporte["filas_totales"]}
Duplicados detectados: {reporte["duplicados_detectados"]}
Campos vacíos encontrados: {reporte["campos_vacios"]}

Observaciones:
- Los espacios innecesarios fueron eliminados.
- Los registros duplicados fueron detectados, pero no eliminados.
- Los campos vacíos fueron identificados, pero no completados.
- El archivo original no fue modificado.
"""

    ruta_salida.write_text(contenido, encoding="utf-8")

    return ruta_salida
