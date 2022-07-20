# CSS

CSS (Cascading Style Sheets) are used to add styling to websites.

## Basics

Styles can be loaded into an HTML page in 3 different ways:

1. **Inline style** - CSS written into the element (not recommended)
1. **Style element** - CSS written into the HTML document (not recommended)
1. **External CSS** - CSS writted in an external file (recommended)

```html
<html>
<head>
<!-- Style element -->
<style>
h1 {
    color: red;
}
</style>

<!-- External CSS -->
<link rel="stylesheet" href="styles.css"/>
</head>

    <body>
        <!-- Inline Style -->
        <h1 style="color: red;">Title</h1>
    </body>

</html>
```

> CSS should be linked in the bottom of the 'head' tag.

### Selectors

Elements on a page can be selected using their:

* `*` - selects all elements on the page
* $ATTRIBUTE - select all elements of that attribute (low-level)
* `.class` - select all elements with the class attribute (mid-level)
* `#id` - select the element with a unique id attribute (top-level)

The level determines the priority of the defined styles. Since elements
are the lowest level of selectors, their styles are overriden by classes
defined for the same target (likewise `id` styles override `class` styles):

```css
/* h1's with the .title class will be green even though the element selector is defined after the class. */
.title {
    color: green;
}

h1 {
    color: red;
}
```

> The `class` attribute is more commonly used than the `id` attribute since
elements can have multiple classes, but only one id.

```css

selector {
    attribute: value;
}

/* Circle model */
element {
    attr1: 5px; /* all sides 5px */
    attr2: 5px 10px; /* top/bottom 5px, right/left 10px */
    attr3: 5px 10px 1px; /* top 5px right/left 10px bottom 1px */
    attr4: 5px 4px 3px 2px; /* top 5px right 4px bottom 3px left 2px */
}
```

Selectors can be more specific:

```css
/* Select all h1 elements with the class '.blue' */
h1.blue {
    color: lightblue;
}

/* Select the element with the 'id' title and both the '.big' and '.green' classes. */
#title.big.green {
    font-size: 150%;
    color: green;
}

/* Select all 'p' tags with a 'div' ancestor (doesn't have to be the direct parent!) */
div p {
    font-size: 50%;
}
```

Combining classes with mutual attributes:

```css
.big, .large, .huge {
    font-size: 300%;
}
```

### Colors

Colors can be applied in various ways:

```css
h1 {
    /* Pre-defined colors */
    color: red;

    /* Using Hexadecimal: #RRGGBBAA (00-FF) */
    color: #FF0000;
    color: #FF000001;

    /* Using RGB/RGBA (0-255) */
    color: rgb(255, 0, 0);
    color: rgba(255, 0, 0, 0.5);

    /* Using HueSaturationLightness (0-360/0-100%/0-100%)*/
    color: hsl(0, 100%, 50%);
    color: hsla(0, 100%, 50%, 0.5);
}
```

### Units

* `px` - fixed unit
* `%` - percentage of the parent container (excluding the scrollbar)
* `vh/vw` - percentage of the entire screen size (including the scrollbar)
* `rem` - font-size based unit, 1rem = root font-size
* `em` - font-size based unit, 1em = parent font-size

## display property

How the elements are displayed on the page:

1. `block` - takes up the entire width of the page (div, p, h1)
    * other elements **cannot** be displayed next to block elements
    * height/width **can** be changed
1. `inline` - takes up only the space needed for the content (span, img, a)
    * other elements **can** be displayed next to inline elements
    * height/width **cannot** be changed
1. `inline-block` - best of both block and inline
    * other elements **can** be displayed next to inline-block elements
    * height/width **can** be changed
1. `none` - removes element completely from the document (`visibility: hidden` makes element invisible, while still respecting its width and height)

## position property

1. `static` - default position value for how HTML elements are positioned, follow the DOM flow.
1. `relative` - exact same flow as `static`, but allows the use of some additional attributes 
    * can use the (top, right, bottom, left) position attributes to modify its position relative to its defualt `static` position
    * overlaps other elements without affecting them, this is **rarely used** since it is difficult to style this behavior
1. `absolute` - removes element from the DOM flow, but allows the use of some additional attributes
    * can use the (top, right, bottom, left) position attributes to position itself inside a non-static parent (usually one that's positioned`relative`)
    * position can be affected by other relative elements
    * parent can be the body or any relative positioned element
1. `fixed` - element stays in its position on the DOM page even while scrolling
1. `sticky` - combination of `relative` and `fixed`
    * Starts off in it's default position, but then becomes `fixed` while scrolling

## float & clear properties

The float property is mainly used for wrapping text around an image, and clear is the inverse of float. It is recommended to only use float for wrapping text,
other use cases are prone to problems.

---

## Font

Using pixels doesn't allow for font to be scaled when users change their browser's font size. Using percentages/em allow for scalability, but these values can inherit
the parent's size (parent = 3em child 4em, child will display 7em)

Size values:

1. px = static pixels
    * No dynamic resizing on zoom
    * Doesn't inherit font size from parent
1. % = percentage value (100% = 16px)
    * Dynamic resizing on zoom
    * Does inherit font size from parent
1. em = 'M' value (1em = 16px)
    * Dynamic resizing on zoom
    * Does inherit font size from parent
1. rem = root em value (1rem = 16px)
    * Dynamic resizing on zoom
    * Doesn't inherit font size from parent, inherits from root
    * Most least error prone value

Example: 90px (90/16) = 5.625em or  ((90/16) * 100) = 562.5%

## Other

Making a nice looking dotted horizontal rule:

```css
hr {
    border: dotted 15px #EAF6F6;
    border-bottom: none;
    width: 5%;
    margin: 100px auto;
}
```

### CSS Tricks

#### Centering

1. `text-align: center` - works as long as it's inline-block/block elements with full widths (doesn't work if the width is changed to less than full width)
1. `margin: 0 auto` - centers vertically
1. `margin: auto 0 auto` - centers horizontally

#### Verticle Line

[background properties](https://css-tricks.com/almanac/properties/b/background/)

```css
#one-liner {
    background: linear-gradient(#000, #000) no-repeat center/2px 100%;
}

#extended {
    background-image: linear-gradient(#000, #000);
    background-size: 2px 100%;
    background-repeat: no-repeat;
    background-position: center center;
}
```
