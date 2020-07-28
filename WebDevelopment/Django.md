# Django

[Django](https://www.djangoproject.com/) is a web development framework
written in Python.

TODO:

* [Checkpoint](https://www.youtube.com/watch?v=qDwdMDQ8oX4)

## Basics

Django has a concept of Projects and Apps. Projects is the entire website, and apps are sections
of the website (store, blog, etc). Apps are designed to be pluggable and can be transferred from 
one Django project to another.

* **Project** - the website
* **Apps** - parts of the website (blog, store, etc)

Projects can contain multiple apps, and apps can be in multiple projects.

Project structure:

```code
mysite/
    manage.py       -> is the file that processes our Django commands.
    mysite/         -> contains the site files.
        __init__.py -> not used, just required by Python to be treated as a package.
        settings.py -> important file, contains all the settings of the site.
        urls.py     -> root router of the sites urls.
        wsgi.py
```

App structure:

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

### Common Commands

* `python manage.py runserver` - Calls starts the development server.
* `python manage.py startproject $PROJECT` - Creates a new Django project.
* `python manage.py startapp $APP` - Creates a new app.
* `python manage.py shell` - Calls the Django version of the Python shell.
* `python manage.py test $APP` - Calls the tests for a Django web app.

## Routing

Both the project and apps can contain a `urls.py` file to handle routing.
The project's `urls.py` file is the root router, defining the main routes
and the routes leading to each app. 

Example:

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]

# project/blog/urls.py

from django.urls import path
from . import views

# Since blog/ already got matched, only the string after blog/ is processed here.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
```

> Django first tried to match a pattern in the project's `urls.py`, when it finds
one, (with the use of `include()`) it sends only the remaining string to the app's
`urls.py` for further pattern matching.

## Database

### Models

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
