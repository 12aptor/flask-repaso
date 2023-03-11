## Crear un entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
venv\Scripts\activate
source venv/Scripts/activate
source venv/bin/activate
deactivate
```

## Instalar Flask

```
pip install Flask
```

## Instalar Flask-SQLAlchemy

```
pip install Flask-SQLAlchemy
```

## Instalar Flask-migrate

```
pip install Flask-Migrate
```

## Migrar la base de datos

```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Registrar las librerias usadas

```
pip freeze > requirements.txt
```