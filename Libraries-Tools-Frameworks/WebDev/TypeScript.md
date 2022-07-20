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

---
# TypeScript

Superset of the JavaScript language that was created by Microsoft.
It enchances JavaScript with extra features and a type system to make
development safer and easier:

* Enforces the use of types which helps reduce errors.
* Supports modern JavaScript features (Arrow functions, let, const).
* Includes other included features (generics, interfaces, tuples).

## Basics

All the JavaScript [primitive types] are recognized by TypeScript:

Type|Example
---|---
`number`|3, 4.2
`string`|"hello, world"
`boolean`|true, false
`null`|nothing value
`undefined`|uninitialized value
`any`|anything (not recommended)

## Workflow

TypeScript's system uses [type inference](../../Languages/Languages.md#type-inference) to determine a variable's type based on the value it's assigned.
The type system also supports type annotations to set a variables type without initializing it. If a value
isn't assigned to a variable, nor is it annotated with a type, it is assigned the `any` type:

```ts
let x = 12; // Type inferred to 'number'.
let name: string; // Type annotation sets name's type to 'string'.
let noType; // Set to the 'any' type.

// TypeScript errors.
x = "some string";
name = 3.14;
```

### Collections

JavaScript offers a lot of flexibility when it comes to storign value sin an array.
This is prone to errors since it can be difficult to determine what kind of values are
being processed. TypeScript allows typing for arrays and still provides ways to keep
the flexibility vanilla JavaScript offers in a safer typed system.

Simple array typing:

```ts
// Type can be annotated for arrays like this:
let animes: string[] = ['Naruto', 'One Piece', 'Demon Slayer', 'Attack On Titan'];
// or like this:
let episodes: Array<number> = [300, 1000, 30, 50];

// Setting to an empty array is ok.
let anyFiller: boolean[] = [];
```

Multi-dimensional array typing:

```ts
let narutoCharacter: string[] = ['Naruto', 'Sasuke', 'Sakura'];
let onePieceCharacters : string[] = ['Luffy', 'Zoro', 'Nami'];

// An additional '[]' is added for every dimension. This case, a string array of string arrays.
let animeCharacters: string[][] = [narutoCharacters, onePieceCharacters];

// Setting to an empty array is ok.
let episodeCounts: number[][] = [];
```

#### Tuples

TypeScript introduces [tuples](../../Languages/Languages.md#tuple) to JavaScript. Through tuples,
TypeScript can defined arrays that are as flexible and type safe:

```ts
// Tuple definition.
let character: [string, number, boolean, string] = ['Kakashi', 30, true, 'Jonin'];

// Array
let twoNums: number[] = [1, 2];
// Tuple
let twoOtherNums: [number, number] = [11, 12];

// Error, incompatable types: number[] and [number, number]
// Arrays can increase in size, tuples cannot.
twoNums = twoOtherNums;

// Tuples can use .concat(), the return will be an Array.
let allNums = twoOtherNums.concat(twoNums);
// Returns an array, so this is ok.
allNums[4] = 21;

// Inferred to be an array and NOT a tuple.
let randomVals = [1, 'two', 3.14, false];
// This is ok.
randomVals[4] = null;
```

> Tuples are strict in ordering and size. The order of types is enforced by TypeScript and a tuple
cannot be assigned to another tuple if the ordering and size are not the same.


### Functions

Type annotating function parameters ensures that those parameters will be of the correct type:

```ts
function logValues(num: number, name: string, isTypeSafe: boolean) {
    console.log(`number=${num} string${name} boolean${isTypeSafe}`);
}

logValues(5, "Luffy", true);

// Error
logValues("5", false, 1234);
```

TypeScript also supports both default and optional parameters:

```ts
// Default parameters
function addTwoNums(x = 1, y = 2) {
    console.log(x + y);
}

// Optional parameters.
function(name?: string, age?: number) {
    let greeting = `Hello, my name is ${name || 'John'}`;

    if(number) {
        greeting += ` and I'm ${age} years old`;
    }
    console.log(greeting);
}
```

The [rest parameter](../../Languages/JavaScript.md#rest-parameter) is inferred to be of type `any` unless
it is annoted:

```ts
// names is of type 'any[]'
function printNames(...names) {
    console.log(names);
}

// nams is of type 'string[]'
function safePrintNames(...names: string[]) {
    console.log(names);
}
```

The [spreader](../../Languages/JavaScript.md#spreader) syntax can also be used with [tuples](#tuples) as long as the number of parameters and their types
matches that of the tuple:

```ts
function printPirate(name: string, age: number, crew: string, fruitUser: boolean): void {
    console.log(`The pirate ${name} of the ${crew} is ${age} years old and ${hasPowers? 'has' : 'doesn\'t have'} powers.`);
}

let pirate1: [string, number, string, boolean] = ['Luffy', 'Straw Hat crew', 17, true];
let pirate2: [string, number, string, boolean] = ['Sanji', 'Straw Hat crew', 20, false];
let pirate3: [string, string, boolean] = ['Buggy', 'Buggy pirates', true];

// Ok, tuple matches parameter listing in arguments and argument types.
printPirate(...pirate1);
printPirate(...pirate2);

// Error, tuple doesn't match parameter listing, missing a value.
printPirate(...pirate3);
```

Return types can also be inferred by the value being returned, or by annotating the function. A function
can also specify that it returns nothing by annotating it with `void`:

```ts
// return type inferred to 'string'.
function isValid(val: any) {
    return val? 'true' : 'false';
}

// return type annotated to 'number'.
function square(num: number): number {
    return num * num;
}

// No return type with the function annotated with 'void'.
function sayHello(): void {
    console.log('Hello!');
}
```

### Enums

TypeScript introduces [enums](../../Languages/Languages.md#enum) to JavaScript. TypeScript enums
have a number associated with them by default, starting at 0 and incrementing the rest. Enums
can be either numeric, or string based enums.

```ts
// Ax = 0, Bow = 1, Sword = 2
enum Weapon {
    Ax,
    Bow,
    Sword
}

let warrior1: [string, number, Weapon] = ['Legolas', 5000, Weapon.Bow];

// Customizing the number associated with the enum value.
enum Grade {
    A = 90,
    B = 80,
    C = 70,
    D = 60,
    F = 0
}
let myGrade = Grade.F;
// This is ok
myGrade = 90;

// Taking advantage of the TypeScript auto increment feature by setting a starting value.
enum Numbers {
    One = 1,
    Two,
    Three,
    Four
}

// String based enum
enum DogBreed {
    Beagle = 'BEAGLE',
    Corgi = 'CORGI',
    Husky = 'HUSKY',
    Shiba = 'SHIBA',
    Aussie = 'AUSSIE'
}

let myDog = DogBreed.BEAGLE;
// Error!
myDog = 'HUSKY';
```

> String enums offer more safety and restrictions since string enums can only be changed using the enum value and not another string.
Numeric enums can be changed by using regular numbers. 

### Objects

#### Object Shape

Object shape refers to what member properties and object does or doesn't have. TypeScript knows
what an object's shape is, and will throw errors if the code attempst to access members that don't
exist within the object:

```ts
let sample = "Hello, world!";

// Throws an error, touppercase doesn't exist on type string. 
// TypeScript will even suggest to use toUpperCase() with this error.
sample.touppercase();
```

#### Typing Objects

Object literals consist of key-value pairs, TypeScript's typing system enforces these
properties and their associated types by creating _object types_:

```ts
// Custom object type.
let ninja: { name: string, rank: string, isOverPowered: boolean };

// Ok
ninja = { name: 'Rock Lee', rank: 'Chunin', isOverPowered: false };

// Error: isOverPowered can't be a string, and age isn't a propert in the object type!
ninja = { name: 'Sasuke', rank 'Genin', isOverPowered: 'YES', age: 16 };
```

Creating these object types can be very reppitive, so TypeScript provides a way to
reuse an object type by creating an alias with `type`:

```ts
// Bad and repititive.
let ninja1: { name: string, rank: string, isOverPowered: boolean };
let ninja2: { name: string, rank: string, isOverPowered: boolean };
let ninja3: { name: string, rank: string, isOverPowered: boolean };

// Alias the object type.
type Ninja = {
    name: string,
    rank: string,
    isOverPowered: boolean,
};
let ninja4: Ninja;
```

If two defined object types share the same properties, variables can be assigned to a variable of the another:

```ts
type ShounenCharacter = {
    name: string,
    isLoud: boolean,
};

type NarutoCharacter = {
    name: string,
    isLoud: boolean,
};

let naruto: NarutoCharacter = { name: 'Naruto', isLoud: true };
// This is ok
let animeCharacter: ShounenCharacter = naruto;

console.log(naruto === animeCharacter); // true
```

Since functions are [first class citizens](../../Languages/Languages.md#first-class-citizen), they can also
have their parameters and return type specified as in an object type:

```ts
type Accumulator = (arr: number[]) => number;

// Parameter names don't have to be the name, only the type needs to match!
const addAll: Accumulator = function(numbers: number[]) {
    let sum = 0;
    for(let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }

    return sum;
}
```

## Advance Use

### Generics

When creating object types, TypeScript allows the use of [generics](../../Languages/Languages.md#generics) type aliases.

```ts
type Collection<T> = {
    name: string,
    quantitiy: number,
    content: T[],
}

let books: Collection<string> = {
    name: 'The Stormlight Archives',
    quantity: 3,
    content: [
        'The Way of Kings',
        'Words of Radiance',
        'Oathbringer',
    ],
};
let funNumbers: Collection<number> = {
    name: "Fun numbers",
    quantity: 2,
    content: [
        3.14,
        55318008,
    ]
};
```

A function can also use generic typing:

```ts
function getLastItem<T>(arr: T[]): T {
    return arr[arr.length - 1];
}

console.log(getLastItem<number>([1, 2, 3, 4, 5])); // 5
```

## Other