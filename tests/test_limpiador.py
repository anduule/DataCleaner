
import pandas as pd

from src.limpiador import limpiar_datos


def test_elimina_espacios_sobrantes():
    datos = pd.DataFrame({
        "nombre": [" Ana Pérez ", " Juan López "],
        "ciudad": [" Buenos Aires ", " Córdoba "],
    })

    resultado, reporte = limpiar_datos(datos)

    assert resultado["nombre"].tolist() == ["Ana Pérez", "Juan López"]
    assert resultado["ciudad"].tolist() == ["Buenos Aires", "Córdoba"]


def test_detecta_duplicados_sin_eliminarlos():
    datos = pd.DataFrame({
        "nombre": ["Ana", "Ana"],
        "email": ["ana@gmail.com", "ana@gmail.com"],
    })

    resultado, reporte = limpiar_datos(datos)

    assert len(resultado) == 2
    assert reporte["duplicados_detectados"] == 1


def test_detecta_campos_vacios():
    datos = pd.DataFrame({
        "nombre": ["Ana", "María"],
        "email": ["ana@gmail.com", ""],
    })

    resultado, reporte = limpiar_datos(datos)

    assert reporte["campos_vacios"] == 1


def test_no_modifica_datos_originales():
    datos = pd.DataFrame({
        "nombre": [" Ana Pérez "],
    })

    original = datos.copy()

    limpiar_datos(datos)

    pd.testing.assert_frame_equal(datos, original)
