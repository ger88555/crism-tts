![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ger88555/crism-tts/CI)
[![codecov](https://codecov.io/gh/ger88555/crism-tts/branch/master/graph/badge.svg?token=O8QS2P0CGE)](https://codecov.io/gh/ger88555/crism-tts)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/ger88555/crism-tts)
![Python 3.9](https://img.shields.io/badge/python-%5E3.9-blue)

# CRIS-TTS \[Prototipo\]

Lector de TTS para documentos web.

## Guía de desarrollo

### 1. Opcional: con un entorno virtual.
Un entorno virtual permite utilizar las versiones de las librerías y de Python requeridos por el proyecto de forma aislada.

### 1.1 [Crear el entorno virtual](https://flask.palletsprojects.com/en/2.0.x/installation/#create-an-environment) con el comando:

- Windows: ```py -3 -m venv venv```
- MacOS/Linux: ```python3 -m venv venv```

### 1.2 [Entrar al entorno virtual](https://flask.palletsprojects.com/en/2.0.x/installation/#activate-the-environment) con el comando:

- Windows: ```venv\Scripts\activate```
- MacOS/Linux: ```. venv/bin/activate```

### 2. Instalar dependencias.

- ```python setup.py develop```

### 3. Arrancar el servidor.

- ```flask run```

## Estructura del proyecto

    .
    └── app/                        # Archivos del proyecto
        └── exceptions/             # Excepciones personalizadas
            ├── UnreadableWebsiteError.py
            └── WebsiteNotFoundError.py
        └── parsers/                # Analizadores sintácticos
            ├── AbstractParser.py   # Analizador sintáctico abstracto (clase base para los analizadores)
            ├── HTMLParser.py       # Analizador de HTML a texto en prosa
            └── TTSParser.py        # Analizador de texto a voz
        └── static/                 # Archivos estáticos para servir en la aplicación de Flask
            └── home.js
        ├── storage/                # Depósito para los archivos de voz generados
        ├── tests/                  # Pruebas automatizadas del proyecto
            └── data/               # Datos de prueba
        └── templates/              # Plantillas de Flask (con sintaxis de Jinja2 sobre HTML)
            └── home.html           # Vista única del prototipo
        ├── __init__.py             # Inicialización de la aplicación de Flask
        └── views.py                # Declaración de vistas de Flask
    ├── README.md
    └── setup.py                    # Script de instalación del proyecto

## Testing

Este proyecto utiliza [`pytest`](https://docs.pytest.org/en/6.2.x/) y [`tox`](https://tox.wiki/en/stable/example/pytest.html) para pruebas automatizadas. `pytest` es la librería de pruebas automatizadas mientras que `tox` permite utilizar un entorno virtual exclusivo para las pruebas e informar a servicios de integración continua.

Es posible utilizar cualquiera de las dos opciones para ejecutar las pruebas. Sin embargo, `pytest` es suficiente para los desarrolladores. Las instrucciones son las siguientes:

### 1 Instalar dependencias

- ```pip install pytest pytest-datafiles```

### 2 Correr pruebas

- ```pytest```

