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
object argument's `el` key.

> All Vue code can only be used within the `#app` div.

### Directives

**Directives** are special Vue attributes pre-fixed with a `v-`which provide
functionality and the reactive behavior. The argument passed into the attribute
is the key from script code.

Common directives:

* `v-if="BOOLEAN"` - displays element based on a condition
* `v-for="VAR in LIST"` - allows for reading through a list
* `v-on:EVENT="METHOD"` - attaches a method to an event
* `v-model="DATA"` - connects data to a form and allows dynamic updating
* `v-bind:KEY="DATA"` - passes data to the component's `props`

## Components

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
1. An object with the component's properties.

Simple Vue Component:

```js
Vue.component(
    'vue-component',
    {
        template: '<p>Simple Vue Component Layout</p>',
    }
)
// Can now be included in other templates with the <vue-component> tags!
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

### Exportable Components

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

## Other
