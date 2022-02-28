# Jekyll

[Jekyll] is a static site generator written in Ruby.

## Basics

* `jekyll new $PROJECT_NAME` - generates a new Jekyll project.
* `bundle exec jekyll build` - compiles and builds the Jekyll project.
* `jekyll serve` - runs the Jekyll development server.
* `bundle install` - installs the dependencies in **Gemfile**.
* `bundle update` - updates the dependencies.

### Project structure

```code
_posts          -> Where you place your blog posts.
_site           -> The generated Jekyll site (Shouldn't be modified).
.sass-cache     -> ???
_config.yml     -> Configuration file for the Jekyll site.
.gitignore      -> gitignore file.
404.html        -> Default 404 page being used.
about.md        -> About Me page Markdown file.
Gemfile         -> File with all the Ruby dependencies.
Gemfile.lock    -> Lock file. ('Locks' down the current version of packages to keep them consistent)
index.md        -> Default page Markdown file.
```

> Editing **_config.yml** requires Jekyll to be restarted for the changes
to be implemented.

## Liquid

Jekyll uses the [Liquid] templating language
to generate HTML.

There are 3 main parts to Liquid:

### 1. Objects

Objects tell Liquid where to put out content:

```html
{{ page.title }}
```

### 2. Tags

[Tags] create logic and control flow for templates:

```html
{% if page.showH1 %}
    <h1>Show Me</h1>
{% endif %}
```

### 3. Filters

[Filters] change the output of an Object:

```html
<h1>{{ "hi" | capitalize }}</h1>
{% comment %} Outputs 'Hi'. {% endcomment %}
```

## Front Matter

Front matter gives files a special meaning in Jekyll.  
It is a [YAML] snippet that
defines variables for the page.

Front matter is denoted on top of the page by:

```yaml
---
    title: Home,
    var: Some Value
---
```

> You only need quotes when escaping special characters.

You can use it with Liquid:

```html
<title>{{ page.title }}</title>

```

## Layouts

Layouts are HTML documents defined in `_layouts/` that can be referenced in a
page's front matter to reference a layout for the page.

_layouts/default.html

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{{ page.title }}</title>
    </head>
    <body>
        {{ content }}
    </body>
</html>
```

`content` is a special variable that renders the content of the page using
this layout. The layout can also use the page's front matter, in this case
`page.title` is the title variable of the page that uses this layout.

To use the **default.html** layout:

index.html

```html
---
layout: default
title: Home
---
<h1>{{ "Hello World!" | downcase }}</h1>
```

Markdown files may also be used (Supported and recommended by Jekyll for simple pages):

about.md

```markdown
---
    layout: default
    title: About
---
# About page

This page tells you a little bit about me.
```

## Includes

Includes are HTML snippets defined in **_includes/**.  They aren't defined in front
matter like layouts are. Jekyll recommends using includes for navigation:

_includes/navigation.html

```html
<nav>
    <a href="/">Home</a>
    <a href="/about.html">About</a>
</nav>
```

To add an include to a layout:

_layouts/default.html

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{{ page.title }}</title>
    </head>
    <body>
        {% include navigation.html %}
        {{ content }}
    </body>
</html>
```

> To get the current url use one of Jekyll's [special variables]: `page.url`.

## Data

Data files are files defined in YAML, JSON, or CSV defined in  **_data/**.  
Great way to separate content from source code and allows for easier
site maintenance.

YAML is the recommended approach, since it is common in the Ruby ecosystem.

Creating a data file for navigation:

_data/navigation.yml

```yaml
- name: Home
  link: /
- name: About
  link: /about.html
```

To access this data, Jekyll makes it available with the
special variable:
`site.data.navigation`.

(Jekyll defined front matter?)

_includes/navigation.html

```html
<nav>
  {% for item in site.data.navigation %}
    <a href="{{ item.link }}" 
        {% if page.url == item.link %}
            style="color: red;"
        {% endif %}>
        {{ item.name }}
    </a>
  {% endfor %}
</nav>
```

## Assets

Assets (static files) in Jekyll are JavaScript, CSS, and image files.

### Folder structure

```code
assets/
    css/
    images/
    js/
```

### CSS

For CSS Jekyll uses [Sass], and extension to CSS

assets/css/styles.scss

```scss
---
---
@import "main";

```

Few things happening here:

* The `---` is telling Jekyll to process the file.
* `@import "main"` is telling Sass to look for a file called **main.scss** in the Sass directory (**_sass/** by default).

_sass/main.scss

```scss
.current {
  color: green
}
```

Link the style sheet to the default layout:

_layouts/default.html

```html
<html>
    <head>
        <meta charset="utf-8">
        <title>{{ page.title }}</title>
        <link rel="stylesheet" href="/assets/css/styles.css">
    </head>
    <body>
        {% include navigation.html %}
        {{ content }}
    </body>
</html>
```

Replace the inline styling (not good practice) from the include file:

_includes/navigation.html

```html
<nav>
    {% for item in site.data.navigation %}
        <a href="{{ item.link }}" 
            {% if page.url == item.link %}
                class="current"
            {% endif %}>
            {{ item.name }}
        </a>
    {% endfor %}
</nav>
```

## Blogging

Jekyll is a [static site] generator, which is perfect for building blogs.
Blogs are usually built with databases, however, the Jekyll approach is to
only use text files.

Blog posts are defines in `_posts`. Blog post filenames have to follow a special
format: `YYYY-MM-DD-post-tile.md`.

Posts usually have their own layout and author in the front matter:

```yaml
---
layout: post
author: tom
---
```

* `author` is custom, it can be named something else.
* HTML can be used for posts, however, Markdown is easier to use and gives
a consistent look to blog posts.

### Drafts

Drafts are created in **_drafts/**.

Naming convention isn't required for drafts like it is for posts. They use the
current day by default.

* `jekyll serve --draft` to view drafts on the development server.

<!-- STILL UNSURE HOW TO IMPLEMENT.
https://jekyllrb.com/docs/step-by-step/09-collections/
### Collections
Collections are a great way to group posts. To implement this, modify the
`_config.yml` configuration file:

##### _config.yml
```yaml
...
collections:
  authors:
```

Items in a collection are defined in a folder of the collection name, in
this case the folder is `_authors/`

##### _authors/tom.md
```yaml
---
short_name: tom
name: Tom the Cat
position: Writer
---
Tom has been chasing Jerry for a long time.
``` -->

[Jekyll]:               https://jekyllrb.com/
[Liquid]:               https://shopify.github.io/liquid/
[Tags]:                 https://jekyllrb.com/docs/liquid/tags/
[Filters]:              https://jekyllrb.com/docs/liquid/filters/
[YAML]:                 http://yaml.org/
[special variables]:    https://jekyllrb.com/docs/variables/
[Sass]:                 https://sass-lang.com/
[static site]:          https://en.wikipedia.org/wiki/Static_web_page