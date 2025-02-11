<a href="https://www.breatheco.de"><img height="250" align="right" margin-top="90" src="https://github.com/4GeeksAcademy/fastapi-rest-hello/blob/main/docs/assets/fastapi.jpg?raw=true"></a>

# Plantilla FastAPI para Desarrolladores Junior

Crea API's con FastAPI en minutos, [📹 mira el tutorial en video](https://youtu.be/ORxQ-K3BzQA).

- [Documentación extensa aquí](https://fastapi.tiangolo.com/).
- Integrado con Pipenv para la gestión de paquetes.
- Despliegue rápido a Render.com con `$ pipenv run deploy`.
- Uso del archivo `.env` para configuración.
- Integración de SQLAlchemy para la abstracción de bases de datos.

## 1) Instalación

> Importante: La plantilla está hecha para Python 3.10, pero puedes cambiar la versión en el archivo `Pipfile`.

Los siguientes pasos se ejecutan automáticamente si usas Codespaces. Si estás haciendo una instalación local, debes ejecutarlos manualmente:

```sh
pipenv install
psql -U root -c 'CREATE DATABASE example;'
pipenv run init
pipenv run migrate
pipenv run upgrade
```

## 2) Cómo empezar a codificar

Hay una API de ejemplo funcionando con una base de datos de ejemplo. Todo tu código de aplicación debe escribirse dentro de la carpeta `./src/`.

- `src/main.py` (aquí es donde debes codificar tus endpoints con FastAPI)  
- `src/models.py` (tus tablas de base de datos y lógica de serialización usando SQLAlchemy)  
- `src/utils.py` (algunas clases y funciones reutilizables)  
- `src/admin.py` (configuración de FastAPI Admin para gestionar datos fácilmente)  

Para una explicación más detallada, busca el tutorial dentro de la carpeta `docs`.

## Recuerda migrar cada vez que cambies tus modelos

Debes migrar y actualizar las migraciones por cada actualización que hagas a tus modelos:

```bash
$ pipenv run migrate # (para hacer las migraciones)
$ pipenv run upgrade  # (para actualizar tu base de datos con las migraciones)
```

## Verifica tu API en vivo

Una vez que ejecutes el comando `pipenv run start`, tu API comenzará a ejecutarse en vivo y podrás abrirla en tu navegador.  
FastAPI genera automáticamente documentación interactiva en `/docs` y `/redoc`.

## ¡Publica/Despliega tu API!

Esta plantilla está 100% lista para desplegarse con Render.com en cuestión de minutos.  
Por favor, lee la [documentación oficial al respecto](https://fastapi.tiangolo.com/deployment/).

## Contribuidores

Esta plantilla fue construida como parte del [Bootcamp de Codificación](https://4geeksacademy.com/us/coding-bootcamp) de 4Geeks Academy por [Alejandro Sanchez](https://twitter.com/alesanchezr) y muchos otros contribuidores. Descubre más sobre nuestro [Curso de Desarrollador Full Stack](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer) y [Bootcamp de Ciencia de Datos](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning). Puedes encontrar otras plantillas y recursos como este en la [página de GitHub de la escuela](https://github.com/4geeksacademy/).

