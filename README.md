# FastAPI User API

Este repositorio contiene una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD sobre un modelo de "Usuario". La API interactúa con una base de datos MongoDB para almacenar y gestionar los datos.

## Instrucciones de Uso

1. Clona este repositorio:

```bash
git clone https://github.com/TheClockwork9438/pruebatecnica.git
```

2. Navega al directorio del proyecto:

```bash
cd <ruta_donde_clono_el_repo>/pruebatecnica
```

3. Levanta la aplicación y la base de datos usando Docker Compose:

```bash
docker-compose up -d --build
```

La API estará disponible en http://localhost:8000.

## Endpoints

POST /users/: Crea un nuevo usuario.
GET /users/{user_id}: Obtiene un usuario por su ID.
PUT /users/{user_id}: Actualiza un usuario existente.
DELETE /users/{user_id}: Elimina un usuario existente.

## Documentacion de la API

Una vez levantado el servicio con docker-compose, quedaran disponible las siguientes urls para acceder a la documentacion detallada de la API y facilitar las pruebas de los endpoints. 

* [FastAPI](http://localhost:8000/docs) (Swagger)
* [ReDocs](http://localhost:8000/redoc)

## Supuestos

> Se asume que la aplicación FastAPI y MongoDB estarán disponibles en sus puertos predeterminados (8000 y 27017 respectivamente).

> Para el id del User se utiliza el _id autogenerado por MongoDB y PyMongo
