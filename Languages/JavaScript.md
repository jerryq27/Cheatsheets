# JavaScript

JavaScript is a language developed by Brendan Eich and is mainly used to
add functionality to websites.

## Basics

JavaScript can be loaded into an HTML page in different ways:

1. **Script element**
    1. **Script Tag - default** - Loads the JavaScript, runs the code, then finishes loading the HTML afterwards
    1. **Script Tag - async** - Loads the JavaScript and HTML synchronously, but puases to run the code after the JavaScript finishes loading.
    1. **Script Tag - defer** - Loads the JavaScript and HTML synchronously, waits until everything is loaded before running the JavaScript code.
1. **External JavaScript**

> JavaScript should be linked in the bottom of the 'body' tag, unless the `defer` attribute is specified or the script type is set to [module](#Modules).

### DOM

The DOM (Document Object Model) is a tree structure of objects/HTML elements
that can be manipulated and selected.

```js
// Selecting objects.
document.getElementById("title"); // Returns the element with that #title id.
document.querySelector("#list li.item a"); // Returns an element using a CSS style selector.
document.getElementsByTagName("p"); // Returns an array of <p> elements.
document.getElementsByClassName("btn"); // Returns an array of elements with the .btn class.

// Manipulating properties.
```

## Variables

Variables can be decalared using `var`, `let`, and `const`.

Variables are loosely typed (no need to include a data type)
`var someVar = 12;`

Using the `typeof()` function returns a variable's data type.

### Scope

`var` - function scoped (if not in a function, globally scoped)
`let/const` - block scoped (if/for/functions/etc.)

`let` and `const` were introduced to fix some of the problems with `var`:

```js
var x = 1;
// No error..
var x = 10;

let y = true;
// SyntaxError, y has already been delcared.
let y = false;

const z = 'a';
// TypeError, invalid assignment to const 'z'
z = 'b';

const person = {
    name: 'Frodo'
};
// Object properties can be changed for const variables.
person.name = 'Bilbo';
```

### Strings

* Strings can be defined with both single and double quotes
* Multline strings are defined between backticks.
* Strings can be concatenated using the `+` operator.

Common String functions:

```js
var example = "Hello";

// Grabbing the length.
console.log(example.length);

// Getting a substring(inclusive, exclusive).
console.log(example.slice(0, 1));
```

### Numbers

### Scope

## Conditionals
## Collections

### Array Methods

#### filter

Filter returns an array of items based on a condition:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

const filteredItems = items.filter(item => item.price <= 100);
// Only items with a price of 100 or below.
console.log(filteredItems);
```

#### map

Map returns an new array constructed from the old array:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

const itemNames = items.map(item => item.name);
// Array of the item names.
console.log(itemNames);
```

#### find

Find will return a single item in the array based on a condition:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

const foundItem = items.find(item => item.name === 'Book');
// { name: 'Book', price: 5 }
console.log(foundItem);
```

#### foreach

Foreach applies a function to every single item in the array:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

// Less clunky than the for loop.
items.foreach(item => console.log(item));
```

#### some

Some returns a boolean of whether an item in the array meets the condition:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

// Less clunky than the for loop.
const hasExpensiveItems = items.some(item => item.price >= 100);
```

#### every

Every returns a boolean of whether all items in teh array meet the condition:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

// Less clunky than the for loop.
const hasOnlyExpensiveItems = items.every(item => item.price >= 100);
```

#### reduce

Reduce takes every item in the array and reduces it into some accumulator:

```js
const items = [
    { name: 'Bike',     price: 100  },
    { name: 'TV',       price: 200  },
    { name: 'Album',    price: 10   },
    { name: 'Book',     price: 5    },
    { name: 'Phone',    price: 500  },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25   },
];

// Less code than a for loop accumulation.
let accumulatorStartPoint = 0;
const total = items.reduce((accumulator, item) => {
    return item.price + accumulator;
}, accumulatorStartPoint);
```

#### includes

includes() returns a boolean of whether the item exists in the array or not:

```js
const nums = [1, 2, 3, 4, 5];

const hasBook = items.includes(5);
console.log(hasBook); // true
```

> `includes()` uses the `===` comparison, so it doesn't work well with objects (unless they are pointing to the same instance).

## Loops
## I/O

### Standard Input & Output

Standard input and output in JavaScript is handled through the console or
the website:

```js
// Message is displayed through the console.
console.log('Hello, world!');

// Message displayed through the browser.
alert('Hello, world!');

// Prompt message with an input field is displayed through the browser.
prompt('Enter your name: ');
```

## Functions

### Closures

A closure is a function defined inside another function and the inner function maintains
the state of the outer function even though the outer function has finished its execution.

```js
function outer() {
    let num = 7;

    function inner() {
        console.log(num);
    }
    return inner;
}

let closure = outer();
// Outer function's state is maintained.
closure(); // 7
closure(); // 7
```


### Arrow Functions

Arrow functions were introduced in ES6 to simplify function definitions:

```js
// No Argument Function
function sayHello() {
    console.log('Hello!');
}
let sayHello = () => console.log('Hello!');

// Single Argument Function
function printVal(val) {
    console.log(val);
}
let printVal = val => console.log(val);

// Multiple Argument Function
function sum(x, y) {
    return x + y;
}
let sum = (x, y) => x + y;

//Anonymous Function
document.addEventListener('click', function() {
    alert('Click!');
});
document.addEventListener('click', () => alert('Click!'));
```

It is important to note that inside arrow functions, the `this` keyword references a
different value than that of normal functions.

* Normal Functions - `this` gets defined in the scope of where the function is **called**, usually the global scope.
* Arrow Functions - `this` gets defined in the scope of where the function is **defined** (like other languages!).

Example:

```js
class Person {
    constructor(name) {
        this.name = name;
    }

    printNameFunction() {
        setTimeout(function() {
            console.log(`Function 'this': ${this.name}`);
        }, 100);
    }

    printNameArrow() {
        setTimeout(()=>console.log(`Arrow 'this': ${this.name}`), 100);
    }
}

let person = new Person('John');
person.printNameFunction(); // undefined, using global 'this', equivalent to doing console.log(this.name); here.
person.printNameArrow(); // 'John'
```

## Exceptions
## Classes & Objects
## Language Specifics

### ES6

#### Modules

Modules allow for the importing and exporting of JavaScript code, which
removes dependencies defined in HTML and allows us to only need one `<script>`
tag. Exporting is done using the `export` keyword. A JavaScript module can
contain many `export` statements, but only one `export default` statement.

```js
// hobbit.js

// Can be exported inline
export default class Hobbit {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

export function printName(character) {
    console.log(`Character's name is ${character.name}`);
}

export function printAge(character) {
    console.log(`Character's age is ${character.age}`);
}

// or can be exported at the end of the file.
// export default Hobbit;
// export { printName, printAge }
```

The `import` can be used in code that is trying to grab exported
code. In order for JavaScript to use the `import` keyword, the
`type` attribute needs to be set for the `script` tag.

```html
<!-- The defer attribute is set by default for modules! -->
<script type="module" src="main.js"></script>
```

```js
// main.js
import Hobbit, { printName, printAge } from './hobbit.js';
// You can alias imports as well
// import Hobbit, { printName as printHobbitName, printAge } from './hobbit.js';

const hobbit = new Hobbit('Bilbo', 111);
```

#### Promises

Promises are used to handle tasks that can take some time in the background
without putting everything else on hold. Promises were also mean to solve the
issue with the continuous nested callbacks (callback hell).

```js
let p = new Promise((resolve, reject) => {
    // Task code..
    let a = 1 + 1;
    let success = a === 2;
    if(success) {
        resolve('Success');
    }
    else {
        reject('Failed');
    }
});

p.then((message) => {
    console.log(`Resolve message: ${message}`);
}).catch((message) => {
    console.log(`Reject message: ${message}`);
});

// Multiple Promises
const p1 = new Promise((resolve, reject => resolve('Success 1')))
const p2 = new Promise((resolve, reject => resolve('Success 2')))
const p3 = new Promise((resolve, reject => resolve('Success 3')))

// Used to run all the promises at the same time (if one task takes more time, the others will wait for it to finish).
Promise.all([p1, p2, p3]).then((messages) => {
    // Array of resolve() messages.
    console.log(messages);
});

// Same except the task that finishes first returns instead of waiting.
Promise.race([p1, p2, p3]).then((message) => {
    // First returned resolve() message.
    console.log(message);
});
```

##### async & await

The keywords `async` and `await` are syntactic sugar for working with Promises:

```js
// Using Promises
function makeRequest(location) {
    return new Promise((resolve, reject) => {
        console.log(`Making a request to ${location}`);
        if(location === 'Google') {
            resolve('Google says hi');
        }
        else {
            reject('We can only talk to Google');
        }
    });
}
function processRequest(response) {
    return new Promise((resolve, reject) => {
        console.log('Processing response');
        resolve(`Extra information + ${response}`);
    });
}

makeRequest('Google').then(response => {
    console.log('Response has been received');
    // Returned promise gets handled in the next then().
    return processRequest(response);
}).then(processedResponse => {
    // Extra information + Google says hi
    console.log(processedResponse);
}).catch(err => {
    console.log(err);
});

// Using async & await

// A function must be marked with 'async' to tell JavaScript that this function is working with Promises.
async function doWork() {
    try {
        // Mark function calls that return a promise with 'await' to get the resolved response instead of a Promise.
        const response = await makeRequest('Google');
        console.log('Response has been received');

        const processedResponse = await processRequest(response);
        console.log(processedResponse);
    } catch(err) {
        console.log(err);
    }
}
doWork();
```

## Libraries & Frameworks

* jQuery
* CoffeeScript
* TypeScript
* Vue.js
* React.js
* NativeScript