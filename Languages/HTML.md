# HTML

Hypertext Markup Language

## Basics

```html
<html>
    <head></head>

    <body></body>

    <footer></footer>
</html>
```

## I/O

### Data Attributes

Custom data attributes can be added to HTML tags by prefixing the attribute with `data-`.

```html
<div id="container" data-customValue="Container #1"></div>

<script>
    container.getAttribute('data-customValue'); // "Container #1"
</script>

```

### Forms

HTML forms define a section of _Input_ elements and submits them to a location specified by the form.

Things to note about forms:

* By default, forms submit to the current page.
* To specify a different location to submit to, the **action** and **method** attributes are used.
  * GET will submit the info into the URL, POST will submit it with the body to some server.
  * POST will throw errors cause browsers can only render GET requests and not POST requests.

```html

<!-- This form will be submitted to the results.html page. -->
<body>
<form action="results.html" method="GET">
    <label>User Input</label>
    <input name="userInput">
    <button>Submit</button>
</form>
</body>

<!-- results.html -->
<!-- URL looks like: localhost:3000/results.html?userInput=something -->
<body>
<div id="results"></div>

<script>
    const results = document.getElementById('results');
    
    new URLSearchParams(window.location.search).forEach((val, name) => {
        results.append(`${name}: ${val}`);
        results.append(document.createElement('br'));
    })
</script>
</body>
```

Things to know about _Input_ elements:

* `input` elements are the "text" type by default.
* Do not need to be closed, and they do not contain text.
*  `label` elements are used to display text for `inputs`.
  * Adding a **for** attribute to a `label` and setting the argument to an `input`'s id will highlight the `input` if the label is clicked.
  * Alternatively, an `input` can be nested in a `label` and the same effect will be acheived without the **for** attribute.
* `button` elements are automatically associated with parent `form` elements if one exists.
  * Buttons default `type` is "submit" so they will trigger the `form`'s `onSubmit()` handler by default even with a defined `onClick` on the button.
  * This behavior can be removed by changing the `type` to "button".
* `input`s have many different types.

element|attribute|effect
---|---|---
form|method|specifies how to submit the form GET or POST
form|action|specifies where to submit the form to
form|enctype|specifies how files on the form are handled and sent via POST
input|value|sets a default value for the input
input|placeholder|sets a hint for the input
input|required|required inputs prevent form submission if blank
input|min/max|sets min and max values for number/date inputs
input|step|sets increment/decrement amount for number/date inputs
label|for|links label to input by input id


element|type|result
---|---|---
input|text (default)|single line text
input|number|number only text field
input|date|date field with picker
input|password|formatted field to hide text
input|email|field with email validation
input|tel|field for entering phone numbers
input|url|field for entering urls
input|color|field for selecting a color
input|checkbox|selectable checkbox (multiple selection)
input|radio|selectable radio button (only one selection)
input|hidden|hidden field that users cannot interact with
input|file|field used to select a file
button|submit|form is submittable by input (or enter key)
button|reset|resets all form inputs to defaults

> Radio button inputs must share the same "name" value for the singular select functionality to work.

```html
<!-- Basic form -->
<form>
    <label>Username</label>
    <input>
    <!-- Nested input -->
    <label>
        Password
        <input>
    </label>
    <button>Submit</button>
</form>
```

### Other Inputs

There is also `select`s for drop downs with multiple options:

```html
<form>
    <label for="colors">RGB Colors</label>
    <select id="colors" name="rgb-colors">
        <option value="Red">Red</option>
        <option value="Green">Green</option>
        <option value="Blue">Blue</option>
    </select>
</form>
```

And TextAreas for multiple lines of text:

```html
<label for="description">Description</label>
<textarea id="description" name="description">
    <!-- Any spaces and new lines will be included!-->
    This is a default value for the text area.
</textarea>
```

> If you want to use the submit() method in JavaScript, make sure none of the Input 
elements are set to submit (name="submit", type="submit")
