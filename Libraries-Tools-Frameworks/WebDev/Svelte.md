# Svelte

## Basics

Svelte components have a basic structure:

```html
<!-- Logic -->
<script>
</script>

<!-- Markup -->
<main>
</main>

<!-- Style -->
<style>
</style>
```

If a property shares the same name as a variable, the following shorthand can be used:

```html
<script>
    let src = "img/profile.jpg";
</script>

<img src={src} alt="Profile picture.">
<!-- Shorthand -->
<img {src} alt="Profile picture.">
```

Reactive values are pieces of code that re-run whenever the referenced values are changed:

```html
<script>
    let count = 0;
    // Reactive value with 'count' referenced.
    $: doubled = count * 2;

    function handleClick() {
        count += 1;
    }
</script>

<button on:click={handleClick}>Click</button>
<p>{count} doubled is {doubled}.</p>
```

This can also be used to run code reactively:

```html
<script>
    let count = 0;
    // Reactive code with 'count' referenced.
    $: {
        console.log("The count is " + count);
        if(count > 100) {
            consolg.log("The count is high!");
        }
    }

    function handleClick() {
        count += 1;
    }
</script>

<button on:click={handleClick}>Click</button>
<p>{count} doubled is {doubled}.</p>
```

### Objects & Arrays

Reactivity is triggered by assignment, however methods that mutate objects and arrays
**won't** trigger updates by themselves. There are a coulple ways around this:

```html
<script>
    let numbers = [1, 2, 3, 4];
    // No reactivity.
    numbers.push(5);
    // Reactive!
    numbers = numbers;
    // Using ES6 syntax:
    numbers = [...numbers, 6];
</script>

<p>{numbers.join(', ')}</p>
```

Objects are a bit more complicated, direct property assignements trigger reactivity, however,
_indirect_ property assignments won't and require a reassignment:

```html
<script>
    let pirate = {
        name: "Luffy",
        role: "Captain",
        hasPowers: true,
        crew: {
            crewmate1: {
                name: "Sanji",
                role: "Cook",
                hasPowers: false,
            }
        }
    };

    // Reactive!
    pirate.name = "Zoro";

    let roleProp = pirate.role;
    // Not reactive.
    roleProp = "First Mate";
    // Reactive.
    pirate.role = roleProp;
</script>
```

> A good rule of thumb is to have the updated variable directly on the left hand side of the assignment.

## Workflow

### Binds

Binding values avoids boilerplate code:

```html
<script>
    let goal = "King of the Pirates!";
</script>

<!-- Boilerplatey -->
<input on:input="{(event) => goal = event.target.value}" value={goal}>

<!-- Binding -->
<input bind:value={goal}>

<p>I'm going to be {goal}</p>
```

When working with arguments, since DOM values are all strings, binding takes
care of the type conversion if the argument is a number:

```html
<script>
    let x = 1;
</script>

<label>
    <input type=number bind:value={x} min=0 max=10>
    <input type=range bind:value={x} min=0 max=10>
</label>
<p>{x}^2 = {x * x}</p>
```

Common binds:

Bind|Effect
---|---
`bind:value`|links values and provides updates
`bind:checked`|links checkboxes and provides updates

### Conditionals

Conditional logic in markup is done through a Svelte `if` block:

```html
<script>
    let user = {
        loggedIn: false,
        membershipCode: 0,
    };

    function toggle() {
        user.loggedIn = !user.loggedIn;
    }
</script>

{#if user.loggedIn}
    <button on:click={toggle}>Log out</button>
{:else}
    <button on:click={toggle}>Log in</button>
{/if}

{#if code === 1}
    <p>Welcome admin!</p>
{:else if code === 0}
    <p>Welcome user!</p>
{:else}
    <p>Welcome un-registered user!</p>
{/if}
```

Symbol|Meaning
---|---
**#**|A block opening tag
**:**|A block continuation tag
**/**|A block closing tag

### Loops

Looping logic is done through the Svelte `each` block:

```html
<script>
    let slayers = [
        { id: 1, name: "Tanjiro", style: "water" },
        { id: 2, name: "Inosuke", style: "beast" }.
        { id: 3, name: "Zenitsu", style: "lighting" },
    ];
</script>

<ul>
    <!-- Basic usage -->
    {#each slayers as slayer}
        <li>{slayer.name} uses the {slayer.style} style.</li>
    {/each}

    <!-- Optional index -->
    {#each slayers as slayer, i}
        <li>{i}: {slayer.name} uses the {slayer.style} style.</li>
    {/each}

    <!-- Specifying a key -->
    {#each slayers as slayer (slayer.id)}
        <li>{slayer.name} uses the {slayer.style} style.</li>
    {/each}

    <!-- Destructuring -->
    {#each slayers as { name, style }}
        <li>{name} uses the {style} style.</li>
    {/each}

    <!-- Generic iterables -->
    {#each [...slayers] as slayer}
        <li>{slayer.name} uses the {slayer.style} style.</li>
    {/each}
</ul>
```

The `each` block can be used with any iterable, a good rule of thumb is that if it has a `.length` property
it can be processed by the `each` block.

### Async Calls

Svelte provides an `await` block for dealing with asynchronous data:

```html
<script>
    async function getNumber() {
        const res = await fetch("/api/get_number/");
        const data = await res.text();

        if(res.ok) {
            return data;
        }
        else {
            throw new Error(data);
        }
    }

    let promise = getNumber();

    function handleClick() {
        promise = getNumber();
    }
</script>

<button on:click={handleClick}>
    Get Number
</button>
{#await promise}
    <p>Getting number...</p>
{:then number}
    <p>The number is {number}.</p>
{:catch error}
    <p>{error.message}</p>
{/await}

<!-- Short hand -->
{#await promise then number}
    <p>The number is {number}.</p>
{/await}
```

## Events

Svelte listens to events using the `on:` directive:

```html
<script>
    let point = {
        x: 0,
        y: 0
    };

    function handleMouseMove(event) {
        point.x = event.clientX;
        point.y = event.ClientY;
    }
</script>

<div on:mousemove={handleMouseMove}>
    The mouse's position is [{point.x}, {point.y}].
</div>

<!-- Inline event. (Quotes are optional) -->
<div on:mousemove="{e => point = { x: e.clientX, y: e.clientY }}">
    The mouse's position is [{point.x}, {point.y}].
</div>

<style>
    div {
        width: 100%;
        height: 100%;
    }
</style>
```

Common directives:

Event|Action Captured
---|---
`on:click`|mouse click.
`on:mousemove`|mouse movement.
`on:message`|watches for dispatched events.

### Component Events

Components can dispatch events which are hadled using the `on:message` directive:

```html
<!-- ChildComponent -->
<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    function sendComponentEvent() {
        dispatch("message", { text: "Hello, world!" });
    }
</script>

<button on:click={sendComponentEvent}>Click me</button>


<!-- App -->
<script>
    import ChildComponent from "./ChildComponent.svelte";

    function handleMessage(event) {
        console.log(event.detail.text);
    }
</script>

<ChildComponent on:message={handleMessage}/>
```

Component events don't _bubble_ like DOM events do. In order to get messages from deeply nested child
components, use _event forwarding_ with the `on:message` directive by omitting the argument:

```html
<!-- ChildComponent -->
<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    function sendComponentEvent() {
        dispatch("message", { text: "Hello, world!" });
    }
</script>

<button on:click={sendComponentEvent}>Click me</button>


<!-- OuterChildComponent -->
<script>
    import ChildComponent from "./ChildComponent.svelte";
</script>

<ChildComponent on:message/>


<!-- App -->
<script>
    import OuterChildComponent from "./OuterChildComponent.svelte";

    function handleMessage(event) {
        console.log(event.detail.text);
    }
</script>

<OuterChildComponent on:message={handleMessage}/>
```

> Event forwarding also works for DOM events like on:click.

### Modifiers

Directives can also have modifiers to alter the DOM event (These modifiers can also be chained):

```html
<script>
    function handleClick() {
        console.log("Only occurs once.");
    }
</script>

<button on:click|once={handleClick}>
    Click me
</button>
```

Modifiers:

Modifier|Effect
---|---
`\|once`|removes handler after it runs once
`\|preventDefault`|calls `event.preventDefault()` before running the handler. Useful for client-side form handling.
`\|stopPropagation`|calls `event.stopProppagation()` before running the handler. Prevents event from reaching the next element.
`\|passive`|improves scrolling performance on touch/wheel events (Added automatically by Svelte where it's safe to do so).
`\|nonpassive`|explicitly set `passive: false`.
`\|capture`|runs handler during the _capture_ phase instead of the _bubbling_ phase. [MDN Docs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling_and_capture)
`\|self`|run handler if the `event.target` is the element itself.
`\|trusted`|run handler only if `event.isTrusted` is `true`, which means the event is triggered by a user action.

> Some frameworks recommend to avoid inline event handles for performance reasons. This doesn't apply to Svelte since
the compiler will optimize it.

## State

To handle passing state to children, child component _properties_ need to be decalared, and this
is done using the `export` keyword:

```html
<!-- ChildComponent -->
<script>
    export let value;
    export let defaultString = "This is a default value.";
</script>

<p>The value is {value}</p>
<p>Default value string is {defaultString}</p>


<!-- App -->
<script>
    import ChildComponent from "./ChildComponent.svelte";
</script>

<ChildComponent value={200}/>
```

Objects with the spread operator makes it easier to work with many props:

```html
<!-- ChildComponent -->
<script>
    export let name;
    export let rank;
    export let age;
    export let hasSpecialAbility;
</script>

<p>The ninja {name} is a {age} old {rank} and {hasSpecialAbility? "has a" : "doesn't have a"} special ability.</p>


<!-- App -->
<script>
    import ChildComponent from "./ChildComponent.svelte";
    const ninja = {
        name: "Neji",
        rank: "Jonin",
        age: 16,
        hasSpecialAbility: true,
    }
</script>

<ChildComponent name={ninja.name} rank={ninja.rank} age={ninja.age} hasSpecialAbility={ninja.hasSpecialAbility}/>
<!-- Or -->
<ChildComponent {...ninja}/>
```

> All the props (and props not defined with `export`) can be accessed directly using the `$$props` variable. Though this is not
recommended since it's difficult for Svelte to optimise.

## Styling

Styles and logic are scoped to the component, so they won't affect other components.

## Lifecycle

## Advance Use

Rendering strings with HTML:

```html
<script>
    let htmlstr = "This string has <strong>strong text</strong>!."
</script>

<p>{@html htmlstr}</p>
```

## Other
