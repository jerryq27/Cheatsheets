# Vue

Vue.js is a JavaScript framework for reactive frontend applications.

TODO:

* [Checkpoint](https://youtu.be/Wy9q22isx3U?t=1607)

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
    })
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

* `data` - defined values that can be used by the current instance.
* `methods` - defined methods that can be used as expressions for directives.
* `computed` - defined methods that compute values from the data's propertied which are then cached.

```js
var app = new Vue({
  el: "#app",
  data: {},
  methods: {},
  computed: {},
});
```

### Directives

**Directives** are special Vue attributes pre-fixed with a `v-`.
The values for these attributes are expected to be a **single**
JavaScript expression. Directives are in charge of reactively applying
changes to the DOM when the value of its expression changes.

A notable exception for the single expression rule is the `v-for` directive.

Directives can take an _argument_ denoted by a `:`. Directives can also
take _dynamic_ arguments, but their are some notable
[limitations](https://vuejs.org/v2/guide/syntax.html#Dynamic-Arguments).

Common directives:

* `v-bind:ATTR="EXPR"` - one-way binding of an attribute to a an expression (listens to changes in `data`)
  * Shorthand: `:ATTR="EXPR"`
* `v-on:EVENT="METHOD"` - attaches a method to an event
  * Shorthand: `@EVENT="METHOD"`
* `v-if="EXPR"`/`v-else-if="EXPR"`/`v-else` - removes or adds elements based on a condition
(elements are not added by default unless their condition is true)
* `v-show="EXPR"` - displays or hides elements (instead of adding or removing them)
* `v-for="VAR in LIST"` - allows for reading through a list
* `v-model="DATA"` - two-way binding of an attribute to an expression (listens to changes in `data` and the HTML elements like forms)

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
})
```

> Do **not** use arrow functions with these lifecycle methods! Arrow
functions don't have a `this`, so `this` gets treated as any other
variabel resulting in `TypeError` being thrown.

## Components & Styling

### Components

Components are used to divide an application in manageble pieces.
An ideal Vue template using components should look like:

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

#### Props

Values from a parent can be passed into a component using the component's
props option. The component must explicitly declare the props it's
expecting to receive:

```html
<example message="Hello"></example>

<script>
Vue.component('example', {
  props: [message],
  template: '<div>{{ message }}</div>',
  data() {
    return {}
  }
});
</script>
```

It is usually recommended to define requirements for props using built-in prop validation:

```html
<example message="Hello"></example>

<script>
Vue.component('example', {
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

The `emit` method is used by a component to signal an event to the parent.
The  first argument for `emit` is the event attribute specified in the parent,
arguments following after are arguments that will be passed into the parent's
method:

```html
<example message="message" v-on:update-message="updateMessage" v-on:print-number></example>;

<script>
Vue.component('example', {
  props: {
    message: {
      type: String,
      required: true,
      default: "Hi",
    },
  },
  template: `
  <div>
    <button v-on:click="informParentToUpdate">Change Message</button>
    <button v-on:click="informParentToPrint">Print Number</button>
    {{ message }}
  </div>
  `,
  data() {
    return {}
  },
  methods: {
    informParentToUpdate() {
      this.$emit('update-message');
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

#### Templates

Templates are renderable HTML code. Templates **must** have only one root element.
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

#### Computed Properties

A `computed` object can be defined in a Vue instance's options. Methods
defined here compute a value based on the values in the `data` object.
The difference between methods defined in `computed` and `methods` is that
`computed` methods are cached. This means that the resulting value is saved
once calculated, and the method won't run again unless the arguments change.
Functions in `methods` are ran everytime they're called.

#### Exportable Components

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

### Styling

We use objects to modify styles in Vue. The expression we pass into `v-bind:style`
is an object with user-defined styles.

Inline style:

```html
<div v-bind:style="{ background: blue, fontSize: 14 }"></div>
<!-- Translates to -->
<div style="background: blue; font-size: 14px"></div>
```

It is much cleaner to use a defined object as the expression.

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

#### Class Bindings

Adding styles and classes dynamically is done with `v-bind`.
When `v-bind` is used with the `style` and `class` attributes,
Vue provides special enhancements to the expression argument.

Objects are passed into `v-bind:class` to toggle a class using
the following syntax: `v-bind:class="{ className: isActive }"`
Where the class `className` will toggle if `isActive` is true.

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

Multiple classes can also be applied using array syntax:

```html
<div v-bind:class="[active, error]"></div>

<script>
data: {
  active: {...},
  error: {...},
}
</script>

<!-- Ternary operators are allowed in the array syntax. -->
<div v-bind:class="[ isActive? active : '', error]"></div>

<script>
data: {
  isActive: true,
  active: {...},
  error: {...},
}
</script>
```

## Workflow

## Advance Use

## Other
