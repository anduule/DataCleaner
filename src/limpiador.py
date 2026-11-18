
import pandas as pd


def limpiar_datos(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Limpia espacios innecesarios y genera un resumen de los datos.

    No elimina filas ni modifica el DataFrame original.
    """

    resultado = df.copy()

    # Limpiar espacios al principio y al final de los textos.
    for columna in resultado.select_dtypes(include=["object", "string"]).columns:
        resultado[columna] = resultado[columna].map(
            lambda valor: valor.strip() if isinstance(valor, str) else valor
        )

    # Detectar filas duplicadas sin eliminarlas.
    duplicados = int(resultado.duplicated().sum())

    # Detectar celdas vacías.
    campos_vacios = int(resultado.isna().sum().sum())

    # También considerar como vacíos los textos sin contenido.
    for columna in resultado.select_dtypes(include=["object", "string"]).columns:
        campos_vacios += int(resultado[columna].eq("").sum())

    reporte = {
        "filas_totales": len(resultado),
        "duplicados_detectados": duplicados,
        "campos_vacios": campos_vacios,
    }

    return resultado, reporte
