
from pathlib import Path

from src.lector_archivos import leer_archivo
from src.limpiador import limpiar_datos
from src.generador_reporte import generar_reporte


def main():
    carpeta_proyecto = Path(__file__).resolve().parent.parent

    archivo_entrada = (
        carpeta_proyecto / "data" / "entrada" / "clientes_ejemplo.csv"
    )

    carpeta_salida = carpeta_proyecto / "data" / "salida"

    archivo_limpio = carpeta_salida / "clientes_limpios.csv"
    archivo_reporte = carpeta_salida / "reporte_limpieza.txt"

    try:
        # 1. Leer el archivo original.
        datos = leer_archivo(archivo_entrada)

        # 2. Limpiar los datos y generar el resumen.
        datos_limpios, reporte = limpiar_datos(datos)

        # 3. Crear la carpeta de salida.
        carpeta_salida.mkdir(parents=True, exist_ok=True)

        # 4. Guardar el archivo limpio sin modificar el original.
        datos_limpios.to_csv(
            archivo_limpio,
            index=False,
            encoding="utf-8-sig",
        )

        # 5. Generar el reporte.
        generar_reporte(reporte, archivo_reporte)

        print("DATACLEANER FINALIZADO")
        print("----------------------")
        print(f"Archivo limpio: {archivo_limpio}")
        print(f"Reporte generado: {archivo_reporte}")
        print(f"Registros procesados: {reporte['filas_totales']}")
        print(f"Duplicados detectados: {reporte['duplicados_detectados']}")
        print(f"Campos vacíos: {reporte['campos_vacios']}")

    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error durante el procesamiento: {error}")


if __name__ == "__main__":
    main()
