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
// Declaring a variable with/without a value to infer the type.
let age = 20;
let name: string;
// Using a 'Union Type' to infer two possible types.
let age2: number|string;
// Using the 'Any Type' to infer any type.
let age3: any;
// Ok.
age = 25;
age = true;
age = 'hello';
age = {}

age = '20'; // Type Error.

/**** Arrays ****/

let names = ['luigi', 'mario'];
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

/**** Objects ****/

let ninja = {
    name: 'naruto',
    age: 14,
    rank: 'genin',
};
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
```

> Types are inferred based on the value upon initialization.

#### Functions

Functions can be defined with parameters specifying a type.

```ts
const circle = (diameter) => {
    return diameter * Math.PI;
};

console.log(circle('hello')); // Runtime NaN error.

const tsCircle = (diameter: number) => {
    return diameter * Math.PI;
};

console.log(tsCircle('hello')); // Compiler Error.
```

## Advance Use

### Config file

The TypeScript config file allows us to configure the behavior of the `tsc`
program.

```console
tsc --init # Generates a tsconfig.json file in a project.
```

Changing the properties here alters `tsc` defaults.
You can specify a root directory for TypeScript files and an output
directory for the compiled JavaScript files by using the `rootDir` and `outDir`
properties.

## Other
