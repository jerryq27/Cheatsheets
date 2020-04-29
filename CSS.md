# CSS

## display property

How the elements are displayed on the page:

1. `block` - takes up the entire width of the page (div, p, h1)
    * other elements cannot be displayed next to block elements
    * height/width can be changed
1. `inline` - takes up only the space needed for the content (span, img, a)
    * other elements can be displayed next to inline elements
    * height/width cannot be changed
1. `inline-block` - best of both block and inline
    * other elements can be displayed next to inline-block elements
    * height/width can be changed
1. `none` - removes element completely from the document (visibility: hidden makes element invisible, while still respecting its width and height)

## position property

1. `static` - default position value for how HTML elements are positioned
1. `relative` - position element relative to its default position (adding a margin away from its default position)
    * can use (top, right, bottom, left) attributes
    * doesn't affect other elements on the page, it overlaps other elements
1. `absolute` - position element relative to its _relative_ parent (adding a margin to the element away from its parent)
    * can use (top, right, bottom, left) attributes
    * removes element from the flow of the page, position can be affected by other relative elements
    * parent can be the body or any relative positioned element
1. `fixed` - element stays in its position relative to the website while scrolling

---

## Centering with CSS

1. `text-align: center` - works as long as it's inline-block/block elements with full widths (doesn't work if the width is changed to less than full width)
1. `margin: 0 auto` - centers vertically
1. `margin: auto 0 auto` - centers horizontally

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
    * Doesn't inherit font size from parent
    * Most least error prone value

Example: 90px (90/16) = 5.625em or  ((90/16) * 100) = 562.5%
