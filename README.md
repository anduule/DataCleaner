# DataCleaner – Automatización y organización de datos

DataCleaner es una herramienta desarrollada en Python para automatizar tareas básicas de limpieza, validación y organización de datos provenientes de archivos CSV y Excel.

El proyecto busca facilitar el procesamiento de datos para pequeños negocios y tareas administrativas, reduciendo errores manuales y generando reportes claros sobre los problemas encontrados.

## Funcionalidades

- Lectura de archivos CSV y Excel.
- Limpieza de espacios innecesarios en campos de texto.
- Detección de registros duplicados.
- Identificación de campos vacíos.
- Generación de archivos procesados sin modificar los originales.
- Creación automática de reportes de limpieza.
- Manejo de errores para archivos inexistentes o formatos no compatibles.
- Pruebas automatizadas con pytest.

## Tecnologías utilizadas

- Python 3.10+
- Pandas
- OpenPyXL
- Pytest

## Estructura del proyecto

```text
DataCleaner/
├── data/
│   ├── entrada/
│   └── salida/
├── src/
│   ├── main.py
│   ├── lector_archivos.py
│   ├── limpiador.py
│   └── generador_reporte.py
├── tests/
│   ├── test_limpiador.py
│   ├── test_lector_archivos.py
│   └── test_generador_reporte.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd DataCleaner
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Colocar un archivo CSV de entrada en:

```text
data/entrada/
```

Ejecutar:

```bash
python -m src.main
```

Los archivos procesados y el reporte se guardarán en:

```text
data/salida/
```

El programa utiliza actualmente `clientes_ejemplo.csv` como archivo de entrada configurado en `main.py`.

## Pruebas

Ejecutar todas las pruebas automatizadas:

```bash
python -m pytest -v
```

Las pruebas verifican la limpieza de datos, la lectura de archivos CSV y Excel, el manejo de errores y la generación de reportes.

## Criterios de procesamiento

- Los archivos originales no se modifican.
- Los registros duplicados se detectan, pero no se eliminan automáticamente.
- Los campos vacíos se identifican, pero no se completan mediante suposiciones.
- Los resultados se guardan en una carpeta independiente.

## Estado del proyecto

Versión inicial funcional. Se prevén futuras mejoras para permitir seleccionar distintos archivos de entrada y ampliar las opciones de limpieza.

## Autora

Proyecto personal desarrollado como parte de mi formación en Ciencia de Datos e Inteligencia Artificial - Veronica Leiva
