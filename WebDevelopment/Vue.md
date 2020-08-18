# Vue

Vue.js is a JavaScript framework for reactive frontend applications.

TODO:

* [Docs Checkpoint](https://vuejs.org/v2/guide/components-registration.html)
* [Checkpoint](https://youtu.be/BPyniDJ5QOQ?t=1161)

## Basics

Vue can be used in a simple `index.html` file, provided the script is included.

Simplest HelloWorld Vue application:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My first Vue app</title>
  <script src="https://unpkg.com/vue"></script>
</head>
<body>

  <div id="app">
    {{ message }}
  </div>

  <script>
    var app = new Vue({
      el: '#app',
      data: {
        message: 'Hello Vue!',
      }
    });
  </script>
</body>
</html>
```

A div is given the id `#app` which is used as the entry point for the Vue
application. The script attaches the div to Vue by including it in the
object argument's `el` (element) key.

> All Vue code can only be used within the `#app` div.

### Vue Instance

When a Vue instance is created, all the properties found in the `data` object
are added to Vue's _reactivity system_. When the data is changed, the changes
are updated reactively. However, this does **not** work if additional properties
are added after intiialization. It is common practice to set blank values for
propterties that will be used initially and later in code.

Vue provided [properties and methods](https://vuejs.org/v2/api/#Instance-Properties)
are prefixed with `$` to differentiate them from user defined properties:

```js
var data = { a: 1 }
var vm = new Vue({
  el: '#example',
  data: data
})

vm.$data === data // => true
vm.$el === document.getElementById('example') // => true

// $watch is an instance method
vm.$watch('a', function (newValue, oldValue) {
  // This callback will be called when `vm.a` changes
})
```

Common predefined properties:

* `data` - defined values that can be used by the current instance
* `methods` - defined methods that can be used as expressions for directives
* `computed` - defined methods that compute values from the data's propertied which are then cached
* `watch` - defined methods that watch for data changes requiring asynchronous or expensive operations

```js
var app = new Vue({
  el: "#app",
  data: {},
  methods: {},
  computed: {},
  watch: {},
});
```

#### Reactivity

The Vue instance does not allow for properties to be added dynamically.
However, new properties for an already defined object can be added.

#### The data Property

Values defined in the data property are reactive when updated. 

##### Arrays

Arrays are reactive when using mutating methods the modify the array such as:

* `push()`
* `pop()`
* `shift()`
* `unshift()`
* `splice()`
* `sort()`
* `reverse()`

However, with non-muating methods:

* `filter()`
* `concat()`
* `slice()`

That always return a new array, make sure to replace the original array and
Vue will handle the update with the DOM efficiently.

```js
this.items = this.items.filter(function(items){
  ...
});
```

> Displaying the result of a non-mutating method without altering the original
`data` array property is best handled using a `computed` property.

## Lifecyle

Each Vue instance goes through a series of steps throughout it's
[lifecycle](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram).
These steps offer _lifecycle hooks_ for user defined code at each of
these steps.

Common lifecycle hooks:

* [created](https://vuejs.org/v2/api/#created)
* [mounted](https://vuejs.org/v2/api/#mounted)
* [updated](https://vuejs.org/v2/api/#updated)
* [destroyed](https://vuejs.org/v2/api/#destroyed)

```js
new Vue({
    data:{},
    created: function() {}, // Runs after an instance is created.
    mounted: function() {}, // Runs when mounted to the page.
    updated: function() {}, // Runs when data gets updated.
    destroyed: function() {}, // Runs when the instance is destroyed.
});
```

> Do **not** use arrow functions with these lifecycle methods! Arrow
functions don't have a `this`, so `this` gets treated as any other
variabel resulting in `TypeError` being thrown.

## Templates

Vue's templating uses custom HTML elements and attributes. Vue HTML
attributes are known as _directives_ and makes it easier to perform
common logic and connect methods defined in the Vue instance.

### Directives

**Directives** are special Vue attributes pre-fixed with a `v-`.
The values for these attributes are expected to be a value from the Vue
instance or a **single** JavaScript expression. Directives are in charge of
reactively applying changes to the DOM when the value of its expression changes.

> A notable exception for the single expression rule is the `v-for` directive.

Directives can take an _argument_ denoted by a `:`. Directives can also
take _dynamic_ arguments, but their are some notable
[limitations](https://vuejs.org/v2/guide/syntax.html#Dynamic-Arguments).

Common directives used with values defined in the Vue instance:

* `v-bind:ATTR="EXPR"` - one-way binding of an attribute to a an expression (listens to changes in `data`)
  * Shorthand: `:ATTR="EXPR"`
* `v-on:EVENT="METHOD"` - attaches a method to an event
  * Shorthand: `@EVENT="METHOD"`
* `v-show="EXPR"` - displays or hides elements (instead of adding or removing them)
* `v-model="DATA"` - two-way binding of an attribute to an expression (listens to changes in `data` and the HTML elements like forms)

#### Conditional Rendering

Conditional rendering is done using the `v-if/v-else-if/v-else` directives.
Rendering of an element (and their children) is determined by the _truthyness_
of the arguments passed into these directives:

```html
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
```

#### List Rendering

List rendering is done using the `v-for` directive. When rendering lists with a `v-for`
a unique key (string or integer) **should** be provided to each element rendered to help
ensure that Vue consistently renders items in order.

```html
<!-- 'item of items' works as well (JavaScript iterator syntax) -->
<ul>
  <li v-for="item in items">
    {{ item.message }}
  </li>
</ul>

<!-- Optional second parameter for the index. -->
<ul>
  <li v-for="(item, index) in items">
    {{ index }} - {{ item.message }}
  </li>
</ul>

<!-- Rendering with a range. -->
<ul>
  <li v-for="i in 10">
    {{ i }}
  </li>
</ul>
```

List rendering can also iterate over objects:

```html
<ul>
  <li v-for="value in object">
    {{ value }}
  </li>
</ul>

<!-- Optional second parameter for the object key. -->
<ul>
  <li v-for="(value, key) in object">
    {{ key }}: {{ value }}
  </li>
</ul>

<!-- Optional third parameter for the index. -->
<ul>
  <li v-for="(value, key, index) in object">
    {{ index }} - {{ key }}: {{ value }}
  </li>
</ul>
```

> It is usually not recommended to use `v-for` and `v-if` together. However, it can be useful to have both
directives used on the same element in [some cases](https://vuejs.org/v2/guide/list.html#v-for-with-v-if).
Also, `v-for` can be used inside of `v-if` directives, however the inverse is not a good practice.

#### Events

Events are handled using the `v-on:$EVENT` directive. Since this is a commonly used directive, it has the
`@$EVENT=""` shorthand.

Example:

```html
<div>
  <button v-on:click="counter += 1">Add One</button>
  <p>Button has been clicked {{ counter }} time(s).</p>
</div>
```

Methods defined in the Vue instance are passed into this directive for more complex logic:

```html
<div>
  <button v-on:click="greet">Greet</button>
</div>

<script>
var app = new Vue({
  data: {
    name: 'Vue.js'
  },
  methods: {
    greet: function(event) {
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      // `event` is the native DOM event
      if(event) {
        alert(event.target.tagName);
      }
    }
  }
});
</script>
```

Parenthesis aren't required unless arguments other than the event are passed into a
defined method. To pass additional arguments and the event, the variable `$event` is
used:

```html
<button v-on:click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>

<script>
methods: {
  warn: function (message, event) {
    // now we have access to the native event
    if(event) {
      event.preventDefault()
    }
    alert(message)
  }
}
</script>
```

##### Event Modifiers

Event modifierd are used on the `v-on` directive to deal with DOM event.
Some common modifiers for `v-on` are:

* `.stop`
* `.prevent` - prevents the default behavior for an event (like the page reloade when submitting a form)
* `.capture`
* `.self` - handle the event only when the element is clicked and not the child.
* `.once` - event will only be triggered once.
* `.passive` - default behavior isn't prevented.

Vue also includes modifiers for handling key events:

```html
<input v-on:keyup.enter="submit">
<!-- Keycodes also work, but are depracated and may not work on newer browsers. -->
<input v-on:keyup.13="submit">
```

All [KeyboardEvents](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values) are
supported using kebab-case.

And mouse events as well:

* `.left`
* `.right`
* `.middle`

More [details](https://vuejs.org/v2/guide/events.html#Key-Modifiers) on key and mouse events in Vue.

#### Input Bindings

Two-way data binding on forms, text areas, and select elements are created using the `v-model` directive.
It automatically picks the best way to update the element based on the input type.

Example:

```html
<input v-model="message" placeholder="edit me">
<p>Message is: {{ message }}</p>
```

The following modifiers can be used with `v-model`:

* `.lazy` - syncs changes after the input event
* `.number` - type casts the input into a number
* `.trim` - trims whitespace from the input

## Styling

Styling in Vue can is handled with directives. Styles can be defined inline or
within the Vue instance using style objects. In both approaches the CSS properties
can be defined in either CamelCase or kebab-case.

### Inline style

We use objects to define inline styles in Vue. The expression passed into `v-bind:style`
is an object with user-defined styles:

```html
<div v-bind:style="{ background: blue, fontSize: 14 }"></div>
<!-- Translates to -->
<div style="background: blue; font-size: 14px"></div>
```

However, it is much cleaner to use a defined style object as the expression:

```html
<div v-bind:style="divStyle"></div>

<script>
data: {
    divStyle: {
        background: 'blue',
        fontSize: 14,
    }
}
</script>
```

Using the Array Syntax with `v-bind:style` allows multiple style objects to
be applied.

```html
<div v-bind:style="[ styleObj1, styleObj2 ]"></div>
```

> CSS properties with [vendor prefixes](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)
are automatically detected and applied by Vue.

### Class Bindings

Adding styles and classes dynamically is done with `v-bind`.
When `v-bind` is used with the `style` and `class` attributes,
Vue provides special enhancements to the expression argument.

Objects are passed into `v-bind:class` to toggle a class using
the following syntax: `v-bind:class="{ className: isActive }"`
Where the class `className` will toggle if `isActive` is truthy.

The `v-bind:class` directive can co-exist with the normal `class`
attribute:

```html
<div
  class="square"
  v-bind:class="{ active: isActive, error: errors.length }">
</div>

<!-- The object expression doesn't have to be inline. -->
<div
  class="square"
  v-bind:class="classObject">
</div>
<script>
data: {
  classObject: {
    active: true,
    errors: false,
  }
}
</script>

<!-- Using a computed property is a common pattern. -->
<div
  class="square"
  v-bind:class="classObject">
</div>
<script>
data: {
  isActive: true,
  hasErrors: false,
},
computed: {
  classObject: function() {
    return {
      active: this.isActive && !this.hasErrors,
      error: this.error && this.error.type === 'fatal',
    }
  }
}
</script>
```

Using the Array Syntax, multiple classes can be applied:

```html
<div v-bind:class="[active, error]"></div>

<script>
data: {
  active: {...},
  error: {...},
}
</script>

<!-- Ternary operators and the object expression are allowed in the array syntax. -->
<div v-bind:class="[ isActive? active : '', error]"></div>
<div v-bind:class="[{ active: isActive }, error]"></div>

<script>
data: {
  isActive: true,
  active: {...},
  error: {...},
}
</script>
```

> Using class bindings on a component apply the classes to the component's root element.

## Components

Components are named Vue instances that are reusable. Since they are Vue instances as well,
they accept the same properties like `data`, `methods`, `computed`, etc. properties.
However, there are some root-only properties such as `el`. Components are used to divide
an application in manageble pieces. An ideal Vue template using components should look like:

```html
<div id="app">

  <app-nav></app-nav>
  <app-view>
    <app-sidebar></app-sidebar>
    <app-content></app-content>
  </app-view>

</div>
```

A simple Vue component is created using two arguments:

1. The component name
1. An options object with the component's properties.

Simple Vue Component:

```js
Vue.component(
    'vue-component',
    {
        template: '<p>Simple Vue Component Layout</p>',
        data() {
          return {}
        }
    }
);
// Can now be included in other templates with the <vue-component> tags!
```

> The reason for using a data function to return a data object instead of just
defining a data object is that the former allows each instance of the component
to have it's own data object. The latter would have each component sharing the
same data object.

### Props

Values from a parent can be passed into a component using the component's
props option. The component must explicitly declare the props it's
expecting to receive:

```html
<test-component message="Hello"></test-component>

<script>
Vue.component('test-component', {
  props: [message],
  template: '<div>{{ message }}</div>',
  data() {
    return {}
  }
});
</script>
```

Values passed in through a `v-for` are handled differently using the `v-bind` directive.
[requires more study](https://vuejs.org/v2/guide/list.html#v-for-with-a-Component)

```html
<test-component
  v-for="(item, index) in items"
  v-bind:item="item"
  v-bind:index="index"
  v-bind:key="item.id">
</test-component>

<script>
Vue.component('test-component', {
  props: [item],
  template: '<div>{{ item }}</div>',
  data() {
    return {}
  }
});
</script>
```

#### Prop Validation

It is usually recommended to define requirements for props using built-in prop validation:

```html
<test-component message="Hello"></test-component>

<script>
Vue.component('test-component', {
  props: {
    message: {
      type: String,
      required: true,
      default: "Hi",
    },
  },
  template: '<div>{{ message }}</div>',
  data() {
    return {}
  }
});
</script>
```

#### Emit

The `emit` method is used by a component to signal an event to the parent.
The  first argument for `emit` is the custom event attribute specified in the parent,
arguments following after are arguments that will be passed into the parent's
method:

```html
<test-component
  message="message"
  v-on:update-message="updateMessage"
  v-on:display-event-value="displayValue($event)"
  v-on:print-number>
</test-component>;

<script>
Vue.component('test-component', {
  props: {
    message: {
      type: String,
      required: true,
      default: "Hi",
    },
  },
  template: `
  <div>
    <button v-on:click="$emit('update-message')">Change Message</button>
    <button v-on:click="$emit('display-event-val', 5)">Event Value</button>
    <button v-on:click="informParentToPrint">Print Number</button>
    {{ message }}
  </div>
  `,
  data() {
    return {}
  },
  methods: {
    displayValue(e) {
      console.log(e);
    },
    informParentToPrint() {
      this.$emit('print-number', 7);
    }
  }
});

var app = new Vue({
  el: "#app",
  data: {
    message: 'Hello',
  },
  methods: {
    updateMessage() {
      this.message = 'Hello, World!';
    },
    printNumber(n) {
      console.log(n);
    }
  },
  computed: {},
});
</script>
```

### Template Property

The HTML defined in a component's template property **must** have only one root element.
Templates can access values from the data object using the _Mustache syntax_ `{{ }}`.
Data processed by the mustache syntax is treated as plain text.

> To process something like HTML, use the `v-html` directive.

Mustaches cannot be used inside of HTML attributes. In these cases, use
the `v-bind` directive to access values from the data property.

JavaScript expressions are supported inside of Mustaches. However, they
are limited to a single expression:

```html
<!-- This works fine. -->
<p>{{ message.split('').reverse().join('') }}</p>

<!-- These don't work. -->
<p>{{ var a = 1 }}</p> <!-- Statement, not an expression -->
<p>{{ if(true) { return message } }}</p> <!-- Use ternary instead. -->
```

Using the `v-bind` directive, data can be passed into a component's `props`:

```html
<div id="app">
    <!-- Using a for loop to pass in the p value to the component's props binding it to 'person'. -->
    <vue-component
        v-for="p in people"
        v-bind:person="p"
        v-bind:key="id">
    </vue-component>
</div>

<script>
Vue.component(
    'vue-component',
    {
        template: '<p>Key: {{ person.key }} Name: {{ person.name }}</p>',
        props: ['person'], // This component is grabbing the `person` value passed in from the parent.
    }
)

var app = new Vue({
  el: '#app',
  data: {
    people: [
      { id: 0, name: 'Jim' },
      { id: 1, name: 'Michael' },
      { id: 2, name: 'Dwight' }
    ]
  }
})
</script>
```

### Computed Properties

A `computed` object can be defined in a Vue instance's options. Methods
defined here compute a value based on the values in the `data` object.
The difference between methods defined in `computed` and `methods` is that
`computed` methods are cached. This means that the resulting value is saved
once calculated, and subsequent calls to the method won't run again unless
their reactive properties change. Functions in `methods` are ran everytime
they're called.

> Using non-reactive properties (not defined in `data`) in computed methods
won't cause a recalculation on update.

```js
computed: {
  willUpdateOnChange: function() {
    // Will update when message changes.
    this.message.split('').reverse().join('');
  }

  willNotUpdateOnChange: function() {
    // Not a reactive property!
    return Date.now();
  }
}
```

Computed properties are by default a getter only. However, you can provide setters
when needed:

```js
computed: {
  fullName: {
    get: function() {
      return this.firstName + ' ' + this.lastName;
    },
    set: function(newVal) {
      var names = newValue.split(' ');
      this.firstName = names[0];
      this.lastName = names[names.length - 1];
    }
  }
}

this.fullName = "John Smith"; // Will invoke the setter method.
```

### Global & Local Components

Vue components so far have been created using:

```js
Vue.component('example-component', {
  ...
});
```

This creates a component and registers it globally. Which means
that these components can be used in any root Vue instance created
afterwards. This also applies to sub-components, which means all
components defined this way will also be available inside each other.

Global registration isn't always ideal since unused components will be
included in your final build with Webpack which increases the amount of
JavaScript users will have to download.

#### Local Registration

Using the `components` property in the root Vue Instance registers a
component locally:

```js
var exampleComponent = {...};

new Vue({
  el: '#app',
  components: {
    // The key will be the component name, and the object will contain the component's options.
    'example-component': exampleComponent,
  }
})
```

Defining components locally will also make them unavailable to sub-components. To make
them available, they would need to be included in a sub-component's `components` property.

The more common approach is using the ES15 modules:

```js
import ExampleComponent from './ExampleComponent.vue';

export default {
  components: {
    // ES15+, this is a shorthand for 'ExampleComponent: ExampleComponent'.
    ExampleComponent
  }
}
```

Vue components are composed of a template, script, and style.

Basic Vue component:

```vue
<template>
    <div>Basic Component</div>
</template>

<script>
export default {
    name: 'BasicComponent'
}
</script>

<style scoped>

</style>
```

> Templates can only have one child element. `scoped` means the styling is only for this component.

## Workflow

## Advance Use

### Vue CLI

Vue offers a command-line interface to automate the creation of a project.
The CLI configures things like Webpack, Babel, and npm and creates this
files and folders:

* public/ - where files you don't want processed by webpack are stored
* src/ - app specific code goes here
  * assets/ - where images, fonts, etc. are stored
  * components/ - where Vue components (building blocks) are stored
  * router/index.js - (Vue router plugin)
  * store/index.js - (Vuex plugin)
  * views/ - where the different views (pages) are stored
  * App.vue - root Vue component where all others are nested in
  * main.js - file that renders the app and mounts it to the DOM

## Other
