# Django

[Django](https://www.djangoproject.com/) is a web development framework
written in Python.

TODO:

* [Checkpoint](https://www.youtube.com/watch?v=q4jPR-M0TAQ)

## Basics

Django has a concept of Projects and Apps. Projects is the entire website, and apps are sections
of the website (store, blog, etc). Apps are designed to be pluggable and can be transferred from
one Django project to another.

### Projects

Projects can contain multiple apps, and apps can be in multiple projects.
In order for Django to look in an app directory for templates, models, etc.
The app must be included in the `INSTALLED_APPS` list in `settings.py`.

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

### Apps

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

Apps can contain subfolders and files not included in the default generated files.

> It is important that these subfolders created within the app that are processed by
Django should contain a folder with that app's name. The reason for this is with how
Django processes these files. Since the full path isn't processed, it could cause
issues is two apps contained a `base.html` file. With the subfolder structure, despite
looking redundant, Django would process `app1/base.html` and `app2/base.html` rather
than two `base.html` files.

### Common Commands

* `python manage.py runserver` - Calls starts the development server.
* `python manage.py startproject $PROJECT` - Creates a new Django project.
* `python manage.py startapp $APP` - Creates a new app.
* `python manage.py shell` - Calls the Django version of the Python shell.
* `python manage.py test $APP` - Calls the tests for a Django web app.

## Admin

The admin user is created with the `python manage.py createsuperuser` command.

> Make sure the database has been created by running [migrations](#Migrations)!

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
    # Giving these paths a name allows them to be referenced with the {% url '' %}
    # template tag
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]

# project/blog/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

> Django first tried to match a pattern in the project's `urls.py`, when it finds
one, (with the use of `include()`) it sends only the remaining string to the app's
`urls.py` for further pattern matching.

### Templates

Templates are HTML pages that can be used within `views.py`. They are defined
within an app's `app/templates/app/` directory.

Django also uses a templating engine which allows code to be written within the HTML.
Template tags allow for the use of logic such as loops and conditionals.
There are a number of ways to display a template, the easiest way to do so is with the
`render(request, template, optional_template_data_dict)` method:

```python
def home(request):
    context = {
        'posts': {...}
    }
    return render(request, 'blog/home.html', data)
```

```html
<body>
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
         <p>By {{ post.author }} on {{ post.date_posted }}</p>
         <p>{{ post.content }}</p>
    {% endfor %}
</body>
```

> In order for Django to search the app for templates, it must be included as an
installed app in `project/settings.py`.

#### Template Inheritance

Using inheritance with templates helps prevent duplicate code. Usually common code
is defined within a base and then extended by templates using that code. To use
inheritance in Django, the parent template defines a block that can be overridden
by a child template:

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <div class="container">
        <!-- Define a block for child templates to override. -->
        {% block content %}
        {% endblock content %}
    </div>

</body>
</html>

<!-- home.html -->
<!-- Specify the parent template to inherit from. -->
{% extends "blog/base.html" %}

<!-- Override the block defined in the parent. -->
{% block content %}

    {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>By {{ post.author }} on {{ post.date_posted }}</p>
        <p>{{ post.content }}</p>
    {% endfor %}

{% endblock content %}

```

### Static Files

Static files are located within the `static/$APPNAME` directory. To use
them in templates, you must include the `{% load static %}` line
at the start of the template file.

```html
<link rel="stylesheet" type="text/css" href="{% static '%APPNAME/main.css' %}">
```

## Database

Database specifics can be specified in `settings.py`. You can specify a database for
testing and production.

### Models

Models, also known as Object Relational Mappers (ORM), are an object representation of the database tables.
They define the layout for your database tables, and contain the essential fields and behaviors of the data
each table is storing. Models are created in `$APPNAME/models.py`.

```python
# Example model.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)

    # Changes how each object is represented when querying the database.
    def __str__(self):
        return self.title
```

In order to modify a model objects in the admin page, you must register the model in
`$APPNAME/admin.py`:

```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```

### Migrations

Models are used to create migrations. Migrations are what will
be used to create the database tables.

```bash
# Creates the migrations from the models.
python manage.py makemigrations

# Execute the migrations.
python manage.py migrate
```

A file is created in `$APPNAME/migrations/` that shows the Python code that will be used to generate SQL.
The reason for this is so that any tweaks the developer wants to make before the database creation can be made.
Django also automatically adds primary keys, and foreign keys are appended with `_id` by default.
Both of these settings can be overriden.

To view the SQL generated from the migrations:

```bash
python manage.py sqlmigrate $APPNAME 0001
```

Migrations are very powerful, and can keep track of which ones have already been ran, which ones need updating.
When the Models are changed, migrations can be updated, and the changes can be applied to your database without the loss of data.

### Queries

You can perform queries to the database using the `python manage.py shell` Django command.
This will open up the Python interactive shell, but we can make calls to the project's code:

```py
>>> from blog.models import Post
>>> from django.contrib.auth.models import user
>>>
>>> user = User.objects.get(id=1)
>>> # Queries for all items in a table
>>> Post.objects.all()
>>>
>>> # Insert items into a table
>>> post_1 = Post(title='Blog 1', content='First post content!', author=user)
>>> post_1.save()
>>>
>>> # Searching for items
>>> user = User.object.filter(username='jerry').first()
>>>
>>> # Getting item from a foreign keys
>>> post = Post.objects.first()
>>> post.author.email
>>>
>>> # Getting all values in a one to many relationship
>>> # $ONE.$MANY_set is the generated queryset.
>>> user.post_set.all()
>>> user.post_set.create(title='Blog 2', content='Second post content!')
```

## Advance Use

### Shell

Allows the use of the Python interpreter with the project.

```bash
python manage.py shell
>>> from blog.models import Post
>>> Post.objects.all()  # Will display all the posts saved in the database.
```