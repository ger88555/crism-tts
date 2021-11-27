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