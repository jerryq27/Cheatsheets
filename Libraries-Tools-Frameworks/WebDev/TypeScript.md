# TypeScript

[Checkpoint](https://www.youtube.com/watch?v=jXoSaX_yFh4&list=PL4cUxeGkcC9gUgr39Q_yD6v-bSyMwKPUI&index=8)

Superset of the JavaScript language with extra features meant to make
development easier:

* Allows for the use of _strict_ types which helps reduce errors.
* Supports modern JavaScript features (Arrow functions, let, const)
* Other included features (generics, interfaces, tuples)

## Basics

TypeScript code must be compiled down to JavaScript in order to be understood
by the browser.

```console
# Install TypeScript
npm install -g typescript

# Compile to JavaScript
tsc $INPUT.ts $OPT_OUTPUT.js

# Watch for changes and compile
tsc $INPUT.ts -w
```

## Workflow

### Types

#### Variables

Defining variables is done much the same way as JavaScript, however, unlike
JavaScript, the variable cannot be reassigned to a value of a different type.

```ts
// Declaring a variable implicitly AKA with/without a value to infer the type.
let age = 20;
// Declaring a variable explicitly by inferring a type.
let name: string;
// Using a 'Union Type' to infer two possible types.
let age2: number|string;
// Using the 'Any Type' to infer any type (not recommended).
let age3: any;

// Ok.
age = 25;
age = true;
age = 'hello';
age = {}

age = '20'; // Type Error.
```

> Types are inferred based on the value upon initialization.

#### Arrays

```ts
/**** Arrays ****/
// Implicit definition.
let names = ['luigi', 'mario'];
// Explicit definition
let nums: number[];
// To use array methods.
let nums2: number[] = [];

// Type Errors.
names = 'super mario characters';
names.push(4);
names[0] = 4;

// Ok
names.push('toad');

// Mixes are allowed as long as it's defined in initialization.
let mix = [1, 'link', 20, 305, 'zelda'];
// Use a 'Union Type' to infer a mix type.
let mix2: (string|number|boolean)[] = [];
// Use an 'Any Type' to infer a list that contains data of any type.
let mix3: any[] = [];

mix.push('ganon'); // Ok
mix[0] = 10; // Ok
```

#### Tuples

TypeScript allows for the definition of tuples, which isn't a data structure in JavaScript:

```ts
type MyTuple [number, string, boolean];
const tuple: MyTuple = [1, 'value', false];

// Make tuple values optional.
type OtherTuple [number?, string?, boolean];
const tuple2: OtherTuple = [true]; // Ok.
```

#### Objects

```ts
/**** Objects ****/

let ninja = {
    name: 'naruto',
    age: 14,
    rank: 'genin',
};
// Ok
ninja.age = 16;
ninja.name = 'sasuke';
ninja = {
    name: 'sakura',
    age: 14,
    rank: 'genin',
};

// Type Errors.
ninja = 'naruto';
ninja.age = '16';

// Reassignment doesn't match defined object structure.
ninja = {
    name: 'naruto',
    food: 'ramen',
};

// Can't add properties that weren't defined.
ninja.skills = ['fire', 'lightning'];

let ninja2: object;
ninja2 = {
    name: 'sasuke',
    age: 14,
    rank: 'genin',
};

let ninja3: {
    name: string,
    age: number,
    name: string,
};
// Type Error, doesn't match object structure.
ninja3 = { name: 'sakura' };
```

#### Functions

Functions can also restrict their parameters and return values to a type.

```ts
function pow(x: number, y: number) {
    return Math.pow(x, y);
}

pow('1', 2); // Type error.
pow(1, 2); // Ok

// Type checking the return value
function sqr(x: number): string {
    // return x*x; // Type error.
    return (x*x).toString(); // Ok.
}

// Function with an optional parameter and no return.
function sayHello(name: string?): void {
    if(name) {
        console.log(`Hello ${name}!`)!
    }
    else {
        console.log('Hello!');
    }
}
```

## Advance Use

### Custom Types

You can define your own types:

```ts
// Simple and redundant example.
type MyType = string;
let value: MyType; 

// Union Type with only two possible values.
type FontStyle = 'bold' | 'italic';
let font: FontStyle; // Can only be assigned to bold or italic.
font = 'neither'; // Type Error.
```

Custom typing is usually used on strong defining an object's 'shape'
with an _interface_:

```ts
interface Person {
    first: string,
    last: string,
    // You can add this to make it possible to add other object attributes with a key of the string type.
    // [key: string]: any,
}

// ok
const person: Person = {
    first: 'Frodo',
    last: 'Baggins',
};

const person2: Person = {
    first: 'Pippin',
    last: 'Took',
    race: 'Hobbit', // Type error.
}
```

### Generics

TypeScript also allows for [Generics](../../Languages/Languages.md):

```ts
class GenericValue<T> {
    constructor(public value: T) {}
}

let val: Generic<number>;
let obj: Generic<Person>;
let str = new GenericValue("String");
```

### Config file

The TypeScript config file allows us to configure the behavior of the TypeScript
compiler.

```console
tsc --init # Generates a tsconfig.json file in a project.
```

Changing the properties here alters `tsc` defaults.
You can specify a root directory for TypeScript files and an output
directory for the compiled JavaScript files by using the `rootDir` and `outDir`
properties.

```json
{
    "compilerOptions": {
        // Which version of JavaScript to compile to.
        "target": "esnext",
        // Recompile TypeScript on save.
        "watch": true,
        // Include typings for certain environments (we can use URL class which is part of DOM and get linting for this)
        "lib": ["dom", "es2017"]
    }
}

```

## Other
