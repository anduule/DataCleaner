
import pandas as pd
import pytest

from src.lector_archivos import leer_archivo


def test_lee_archivo_csv(tmp_path):
    archivo = tmp_path / "clientes.csv"
    archivo.write_text(
        "nombre,email\nAna,ana@gmail.com\nJuan,juan@gmail.com\n",
        encoding="utf-8",
    )

    resultado = leer_archivo(archivo)

    assert len(resultado) == 2
    assert resultado["nombre"].tolist() == ["Ana", "Juan"]


def test_lee_archivo_excel(tmp_path):
    archivo = tmp_path / "clientes.xlsx"

    datos = pd.DataFrame({
        "nombre": ["Ana", "Juan"],
        "email": ["ana@gmail.com", "juan@gmail.com"],
    })

    datos.to_excel(archivo, index=False)

    resultado = leer_archivo(archivo)

    assert len(resultado) == 2
    assert resultado["nombre"].tolist() == ["Ana", "Juan"]


def test_error_si_archivo_no_existe(tmp_path):
    archivo = tmp_path / "inexistente.csv"

    with pytest.raises(FileNotFoundError):
        leer_archivo(archivo)


def test_error_si_formato_no_es_compatible(tmp_path):
    archivo = tmp_path / "clientes.txt"
    archivo.write_text("datos de prueba", encoding="utf-8")

    with pytest.raises(ValueError):
        leer_archivo(archivo)
