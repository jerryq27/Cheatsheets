# JavaScript

JavaScript is a language developed by Brendan Eich and is mainly used to
add functionality to websites.

## Basics

JavaScript can be loaded into an HTML page in different ways:

1. **Script element**
1. **External JavaScript**

> JavaScript should be linked in the bottom of the 'body' tag.

## Variables

Variables can be decalared using `var`, `let`, and `const`.

Variables are loosely typed (no need to include a data type)
`var someVar = 12;`

Using the `typeof()` function returns a variable's data type.

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

### map

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

### find

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

### foreach

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

### some

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

### every

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

### reduce

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

### includes

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
## Libraries & Frameworks

* jQuery
* CoffeeScript
* TypeScript
* Vue.js
* React.js
* NativeScript