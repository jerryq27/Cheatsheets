# NativeScript-Vue

[Playground Checkpoint](https://play.nativescript.org/?template=play-vue&id=mvX1v9)

NativeScript-Vue is used to build crossplatform mobile applications
with the Vue framework.

## Basics

Basic NativeScript-Vue app structure:

```js
<Page>
    <ActionBar title="Example"/>
    <Label text="Hello, world!"/>
</Page>
```

* The top level element for a NativeScript-Vue app is the `<Page>` element
* Pages can only contain one ActionBar

## Workflow

### Styling

Styling in NativeScript-Vue can be done in four ways:

1. Platform-specific CSS - proccessed for Android or IOS
1. Application-wide CSS - processed first
1. Scoped CSS - processed and applied to the current component only
1. Inline CSS - processed in the individual element

CSS Variables are also supported:

```css
.ns-root {
    --theme-color: blue;
}

.login-button {
    /* defined color, fallback color */
    bolor: var(--theme-color, cyan);
}
```

As well as simple calculations:

```css
element {
    width: calc(100% * 1.25); /* 125% */ 
}
```

CSS files can also be imported:

```css
@import url('~/path/to/style.css');
```

### Alerts

Alerts display dialogs with specified actions:

```js
alert("body text", "", [])
    .then(result => {
        // Handle the result.
    });
```

## Advance Use

## Other
