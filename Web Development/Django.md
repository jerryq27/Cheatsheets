# Django

[Django](https://www.djangoproject.com/) is a web development framework
written in Python.

## Basics

Django has a concept of Website/Project and Apps. In Django every website
is built from a combination apps.

Apps are designed to be pluggable i.e.
apps can be transferred from one Django project to another.

* **Project** - a collection of configuration and apps for a website.
* **Apps** - An app is a web application that does something. (blog, store, database)

Projects can contain multiple apps, and apps can be in multiple projects.

### Folder Structure

```code
mysite/
    manage.py       -> is the file that processes our Django commands.
    mysite/         -> contains the site files.
        __init__.py -> not used, just required by Python to be treated as a package.
        settings.py -> important file, contains all the settings of the site.
        urls.py     -> contains all the routes for the site.
        wsgi.py
```

### Common Commands

* `python3 manage.py runserver` - Calls starts the development server.
* `python3 manage.py shell` - Calls the Django version of the Python shell.
* `python3 manage.py test $APPNAME` - Calls the tests for a Django web app.

## Apps

* `python manage.py startapp $APPNAME` - Creates a new app.

### App Folder Structure

```code
app/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py        -> All the views of the app.
```

Everytime you add an app, you have to include it in **settings.py**.

```python
INSTALLED_APPS = [
    ...,
    'app.apps.AppsConfig', # app/apps/AppConfig
]
```

## Models

The layout for your database. Models are the single definition of truth about the app's data. They contain the essential fields and behaviors of the data the app is storing. Models are created in **$APPNAME/models.py**.

```python
# Example model.
from django.db import models

class Example(models.Model):
    text_field = models.CharField(max_length=200)
    date_field = models.DateTimeField('date published')
```

In Django, models are used to create migrations. Migrations are what will
be used to create the database schema.

```bash
python manage.py makemigrations $APPNAME # Creates the migrations from the models.
```

A file is created in **$APPNAME/migrations/** that shows the Python code that will be used to generate SQL. The reason for this is so that any tweaks the developer wants to make before the database creation can be made.

```bash
python manage.py sqlmigrate $APPNAME 0001 # To view the SQL generated from the migrations.
```

Django automatically adds primary keys, and foreign keys are appended with `_id` by default. Both of these settings can be overriden.

```bash
python manage.py migrate # This runs the migrations to create the tables in the app's database.
```

Migrations are very powerful, and can keep track of which ones have already been ran, which ones need updating.

When the Models are changed, migrations can be updated, and the changes can be applied to your database without the loss of data.
