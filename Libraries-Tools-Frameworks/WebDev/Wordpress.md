# Wordpress

Wordpress is an open source content management system written in [PHP](../../Languages/PHP.md).

## Basics

Creating a local Wordpress site requires 3 things:

1. PHP
1. Nginx
1. MySQL

Using a tool like [Local](https://localwp.com) automates the creation of these environments.

Directory structure:

* app/public/
* conf/
* logs/

### Admin

Accessing the admin panel is done by going to `$SITE/wp-admin` and entering the login created during setup.

## Workflow
## Advance Use

### Theme Development

For Wordpress to recognize a custom theme, the following files are required
inside a new theme folder in `app/public/wp-content/themes/`:

File|Purpose
---|---
index.php|Used as the entry point for a theme (home page).
style.css|Provides metadata for the theme along with the styles.

Defining the theme's metadata inside of styles.css:

```css
/*
    Theme Name: Sample Theme
    Author: Jerry
    Version: 1.0
*/

...styles
```

Optional metadata files are:

File|Purpose
---|---
screenshot.png|Image cover file used for the Wordpress theme. (1200X900)

Template files:

File|Purpose
---|---
single.php|Layout for posts
page.php|Layout for pages
header.php|Header layout
footer.php|Footer layout

Other files:

functions.php|File used to talk to the WordPress system and add hooks to certain events


#### Info Functions

Wordpress provides built-in functions to get information about the site:

```php
// Getting the site's name
<h1><?php bloginfo('name'); ?></h1>

// Getting the tagline/description.
<h2><?php bloginfo('description'); ?></h2>
```

The most famous of these functions is used with a while loop, known as "the loop" in the WordPress community:

```php
<?php
// Loop through posts or pages depending on which file.
while(have_posts()) {
    the_post();
?>

<h1><?php the_title();?></h1>
<p><?php the_content();?></p>
<p><?php the_permalink();?></p>

<?php
}
?>
```

#### WordPress Actions

The `functions.php` file is used to communicate with the WordPress system and add hooks:

```php
<?php
// Load in styles.css file.
function css_files() {
    // label, and the file name.
    wp_enqueue_style('css_main_styles', get_stylesheet_uri());
}

// Event to hook into, function name that will be injected.
add_action('wp_enqueue_scripts', 'css_files');
?>
```

#### Header & Footer

Headers and footers are defined in the `header.php` and `footer.php` files
and are included using built-in WordPress functions:

```php
<?php
// Get header.php content.
get_header();

// Includes footer.php content.
get_footer();
?>
```

Function to include actions from `functions.php` and other WordPress defined header values into the header template:

```php
<!DOCTYPE html>
<html lang="en">
<head><?php wp_head(); ?></head>

</html>
```

Function to include defined WordPress JavaScript in the footer template:

```php
    <?php wp_footer();?>
</body>
</html>
```

### Plugin Development

## Other