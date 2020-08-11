# Web Development

Web development uses 3 languages for designing websites:

1. HTML - structures the website
1. CSS - stylizes the website
1. JavaScript -  handles the functionality of the website

## HTML

Using tags to structure content on a website.

Best practices:

* Link the stylesheet within the `head` tags.
* Link the JavaScript at the bottom of the `body` tags.

### Emmet

[Cheatsheet](https://docs.emmet.io/cheat-sheet/)

Emmet is a plugin that makes typing HTML much easier.
Common Emmet shorthands:

* element*n - creates element n times
* element.CLASS - creates an element with the class.
* element>child>child - creates element with the nested children

---

## CSS

Used to style HTML elements using selectors to target them.

Selectors can be:

* attribute - select elements of that attribute
* `#id` - select an element with the id attribute
* `.class` - select elements with the class attribute

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

More detailed CSS notes [here](CSS.md)

## JavaScript

Allows for sites to have functionality.
