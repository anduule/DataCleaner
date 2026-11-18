
from src.generador_reporte import generar_reporte


def test_genera_reporte_correctamente(tmp_path):
    reporte = {
        "filas_totales": 5,
        "duplicados_detectados": 1,
        "campos_vacios": 1,
    }

    archivo = tmp_path / "salida" / "reporte.txt"

    resultado = generar_reporte(reporte, archivo)

    assert resultado.exists()

    contenido = resultado.read_text(encoding="utf-8")

    assert "Registros procesados: 5" in contenido
    assert "Duplicados detectados: 1" in contenido
    assert "Campos vacíos encontrados: 1" in contenido


def test_crea_carpeta_de_salida_si_no_existe(tmp_path):
    reporte = {
        "filas_totales": 3,
        "duplicados_detectados": 0,
        "campos_vacios": 0,
    }

    carpeta = tmp_path / "nueva_carpeta"
    archivo = carpeta / "reporte.txt"

    generar_reporte(reporte, archivo)

    assert carpeta.exists()
    assert archivo.exists()
