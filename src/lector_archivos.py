
from pathlib import Path

import pandas as pd


def leer_archivo(ruta: str | Path) -> pd.DataFrame:
    """
    Lee un archivo CSV o Excel y devuelve sus datos como DataFrame.
    """

    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    extension = ruta.suffix.lower()

    if extension == ".csv":
        return pd.read_csv(ruta)

    if extension in [".xlsx", ".xls"]:
        return pd.read_excel(ruta)

    raise ValueError(
        f"Formato no compatible: {extension}. "
        "Utilizá archivos CSV o Excel."
    )
