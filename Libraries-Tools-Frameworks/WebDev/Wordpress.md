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

### Posts

Wordpress has two different types of posts:

1. Posts
1. Pages

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
archive.php|Layout for posts by archives (in Wordpress, archives are groups like author, date, and category)
front-page.php|Layout for an alternate home page (Page must be set in Wordpress "Reading" settings)
index.php|Fallback layout for all pages

Other files:

functions.php|File used to talk to the WordPress system and add hooks to certain events

#### Info Functions

Wordpress provides built-in functions to get information about the site:

```php
// Getting the site's name
<h1><?php bloginfo('name'); ?></h1>

// Getting the tagline/description.
<h2><?php bloginfo('description'); ?></h2>

// Get the current page's id.
<p><?php echo get_the_ID(); ?></p>
<p><?php the_ID(); ?></p>

// Get the specified page's title.
<p><?php echo get_the_title($someId); ?></p>
<p><?php the_title($someId); ?></p>

// Get the home page's url.
<p><?php echo site_url(); ?></p>

// Get the home page's url with "/blog" appended.
<p><?php echo site_url('/blog'); ?></p>

// Get the specified page's permalink.
<p><?php echo get_permalink($someId); ?></p>

// Get the specified page's parent's id, if not parent returns 0.
<p><?php wp_get_post_parent_id($someId); ?></p>

// Get the category title.
<p><?php echo single_cat_title(); ?></p>

// Returns $ARCHIVE: $TITLE
<p><?php the_archive_title(); ?></p>
```

Rule of thumb for these functions, if a function begins with _get_, the value is returned and would need to be `echo`'d
out. If the function begins with _the_, WordPress will `echo` it out.

The most famous of these functions is used with a while loop, known as "the loop" in the WordPress community:

```php
<?php
// Loop through posts or pages depending on which location.
while(have_posts()) {
    // Sets up values for the current post.
    the_post();
?>

<h1><?php the_title();?></h1>
<p><?php the_content();?></p>
// Shorter version of the_content(); with "..." included.
<p><?php the_excerpt();?></p>
<p><?php the_permalink();?></p>

<?php
}
?>
```

> This loop works with posts, pages, etc. depending on where it's used.

#### Queries

Wordpress has two query types:

1. Wordpress queries - ran automatically by Wordpress based on the URL.
1. Custom queries - developer defined queries that run on the page in which they are created.

##### Main Queries

These queries are ran on page load, the results can be altered by adding an action to `functions.php`:

```php
<?php
function adjust_queries($query) {
    // Conditionals
    is_admin(); // If we are in the admin dashboard.
    $query->is_main_query(); // If the query is a Wordpress query instead of a developer defined custom query.

    // Modifications
    $query->set($KEY, $VALUE);
}

add_action('pre_get_posts', 'adjust_queries')
?>
```

Wordpress will pass the query being ran into this function.

> The query runs on all pages that grab posts with a Wordpress query, including those in the admin dashboard.

##### Custom Queries

Custom queries allows us to query Wordpress for data in any location.
Query parameters are determined with associative arrays:

```php
<?php
$qPosts = new WP_Query(array(
    'posts_per_page' => 5,
    'category_name' => 'Programming',
    'post_type' => 'post' // Or page
));

while($qPosts->have_posts()) {
    $qPosts->the_post();

    the_title();
    the_permalink();
    echo get_the_content();
}

// Good cleanup practice after running a custom query.
wp_reset_postdata();
?>
```

Custom queries won't product pagination links with `echo paginate_links()` since this
function works with Wordpress queries. In order to get pagination working, both the
custom query and `paginate_links()` need to be modified:

```php
<?php
$qPosts = new WP_Query(array(
    'posts_per_page' => 5,
    'category_name' => 'Programming',
    'post_type' => 'post', // Or page
    // Grabs the value from the url, if it doesn't exists, use "1".
    'paged' => get_query_var('paged', 1)
));


echo paginate_links(array(
    'total' => $qPosts->max_num_pages
));
?>
```

#### Posts

##### Custom Posts

By default, Wordpress comes only with two default post types:

1. Posts
1. Pages

To create a custom post type, update `functions.php`:

```php
<?php
function custom_post_types() {
    $CUSTOM_POST_TYPE_NAME = 'event';
    $CUSTOM_POST_TYPE_PROPS = array(
        'public' => true,
        'menu_icon' => 'dashicons-calendar',
        'labels' => array(
            'name' => 'Events',
            'add_new_item' => 'Add New Event',
            'edit_item' => 'Edit Event',
            'all_items', => 'All Events',
            'singular_name' => 'Event'
        ),
        // Required to use the new Wordpress post editor instead of the old one.
        'show_in_rest' => true
    );

    register_post_type($CUSTOM_POST_TYPE_NAME, $CUSTOM_POST_TYPE_PROPS);
}

add_action('init', 'custom_post_types');
?>
```

> The menu icon IDs can be found by searching 'Wordpress Dashicons'.

This will create a custom post type and make it visible in the admin dashboard.
However, `functions.php` isn't the best place to put custom post types. If the 
user switches themes, all posts under a custom type won't be accessible.

To avoid this, it's better to have custom post types as plugins. A better location
would be `wp-content/mu-plugins/$FILE.php`:

```php
// wp-content/mu-plugins/custom_post_types.php
<?php
function custom_post_types() {
    $CUSTOM_POST_TYPE_NAME = 'event';
    $CUSTOM_POST_TYPE_PROPS = array(
        'public' => true,
        'menu_icon' => 'dashicons-calendar',
        'labels' => array(
            'name' => 'Events',
            'add_new_item' => 'Add New Event',
            'edit_item' => 'Edit Event',
            'all_items', => 'All Events',
            'singular_name' => 'Event'
        ),
        // Required to use the new Wordpress post editor instead of the old one.
        'show_in_rest' => true
    );

    register_post_type($CUSTOM_POST_TYPE_NAME, $CUSTOM_POST_TYPE_PROPS);
}

add_action('init', 'custom_post_types');
?>
```

The folder 'mu-plugins' stands for 'Must Use Plugins'.

Other things to keep in mind with custom post types:

* A layout file for the custom post type would be `single-$TYPE_NAME.php`.
* Archive support would have to be enabled to see all custom post types by adding the `has_archive => true` parameter to `register_post_type()`.
* 

> When creating custom post types, the permalinks for the new type must be created.
To do this, go to Admin Dash -> Settings -> Permalinks and hit 'Save Changes' to re-create
all the permalinks, including the new post type links.

Custom posts can also have custom fields:

```php
<?php
function custom_post_types() {
    $CUSTOM_POST_TYPE_NAME = 'event';
    $CUSTOM_POST_TYPE_PROPS = array(
        'public' => true,
        // Required to use the new Wordpress post editor instead of the old one.
        'show_in_rest' => true,
        'supports' => array(
            'title',
            'editor',
            'custom-fields'
        )
    );

    register_post_type($CUSTOM_POST_TYPE_NAME, $CUSTOM_POST_TYPE_PROPS);
}

add_action('init', 'custom_post_types');
?>
```

This will add a couple of fields in the admin dashboard when you edit the custom type posts
which include:

1. A name - the key used to refer to this value in PHP.
1. A value - the actual value.

This is a very basic way to implement custom fields. For more intuitive features, a plug-in is
required and **Advance Custom Fields** is a commong one to use.

#### WordPress Actions

The `functions.php` file is used to communicate with the WordPress system and add hooks:

```php
<?php
// Load in styles.css file.
function css_files() {
    // label, and the file name.
    wp_enqueue_style('css_main_styles', get_stylesheet_uri());
    // Other styles
    wp_enqueue_style('css_extre_styles', get_theme_file_uri('/css/extra-styles.css'));
    // External files ("https:" is omitted when using these urls).
    wp_enqueue_style('font-awesome', '//msxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
    // JavaScript: - Additional args: array of dependencies, version number, load at the bottom of the document?
    wp_enqueue_script('js_main', get_theme_file_uri('/js/index.js'), NULL, '1.0', true);
}

// Event to hook into, function name that will be injected.
add_action('wp_enqueue_scripts', 'css_files');
?>
```

Action to add a title to the site:

```php
<?php
function site_features() {
    add_theme_support('title-tag');
}

add_action('after_setup_theme', 'site_features');
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

#### Menus

Menus can be created manually in HTML, but to set the theme to create and modify menus in the Admin portal
the functionality would have to be specified in **functions.php**:

```php
<?php
// functions.php

function site_features() {
    register_nav_menu('my_nav_menu_location', 'My Navigation Menu');
}

add_action('after_setup_theme', 'site_features');
?>

// Using menu on page.php
<ul>
    <?php
        wp_nav_menu(array(
            'theme_location' => 'my_nav_menu_location',
        ));
    ?>
</ul>
```

Now the WPAdmin > Appearance > Menus page should be available and menus can be customized through there.

### Plugin Development

## Other