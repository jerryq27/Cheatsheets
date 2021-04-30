# Solidity

[Zombie Course](https://cryptozombies.io/en/course)

[Stopping Point: Chapter 3 Lesson 1](https://cryptozombies.io/en/lesson/3/chapter/1)

Solidity is a language used to build DApps on the Ethereum network.

## Basics

Solidity programs always start with the `pragma solidity $VERSION` to specify
which version the project's code runs on.

The language is [statically (strongly) typed](#) and uses the basic arithmetic
operators with the addition of `**` "Power of" operator.

### Contracts

Contracts are the fundamental building block for Ethereum applications.
They are the starting point to a project.

```code
// From 0.5.0 (inclusive) to 0.6.0 (exclusive).
pragma solidity >=0.5.0 <0.6.0;

contract Example {
    
}
```

### Variables

State variables are permanently stored in the contract's storage i.e. they're
written on the Ethereum blockchain (like writing to a database).

### Global Variables

Solidity has predefined global variables that are available to all functions:

* `msg.sender` - refers to the address of the person/smart contract that called
the function

## Arrays

Soildity has two types of arrays:

* Fixed arrays - array with a fixed size
* Dynamic arrays - array with no fixed size and can grow dynamically

Arrays can be declared public and Solidity automatically creates a getter method
for it.

```code
// Other contracts can now read data from this, useful for storing public data
// in a contract.
string[] public names;
names.push("Tom");
names.push("Jerry"); // Tom, Jerry
```

### Mappings

Mappings are another way to store organized data as key-value pairs:

```code
// key => value types
mapping(uint => string) public userIdToName;
```

## I/O

### Storage

Solidity offers two locations to store variables:

1. `storage` - variables stored permanently on the blockchain
1. `memory` - temporary variables which are erased between external function
calls in a contract.

These keywords aren't commonly used, variables defined outside of a function
(state variables) are `storage` variables by default. Variables defined within
functions are `memory` variables and will dissapear when the function call ends.

Use cases for these keywords are when dealing with structs and arrays:

```code
contract SandwichFactory {
  struct Sandwich {
    string name;
    string status;
  }

  Sandwich[] sandwiches;

  function eatSandwich(uint _index) public {
    // Sandwich mySandwich = sandwiches[_index];

    // ^ Seems pretty straightforward, but solidity will give you a warning
    // telling you that you should explicitly declare `storage` or `memory` here.

    // So instead, you should declare with the `storage` keyword, like:
    Sandwich storage mySandwich = sandwiches[_index];
    // This will permanently change `sandwiches[_index]` on the blockchain.
    mySandwich.status = "Eaten!";

    // If you just want a copy, you can use `memory`:
    Sandwich memory anotherSandwich = sandwiches[_index + 1];
    // This will just modify the temporary variable and have no effect on what's
    // stored in the blockchain
    anotherSandwich.status = "Eaten!";

    // You can do this if you want to copy the changes back into blockchain
    // storage.
    sandwiches[_index + 1] = anotherSandwich;
  }
}
```

## Functions

You can pass values into a function by [value or by reference](#):

* To pass a value by value, add `memory` after the type (this is required by
all reference types like strings, structs, arrays, maps, etc.)
* To pass by reference, nothing else needs to be added.

By convention, function parameters are prepended with an `_` to differentiate
them from the global variables.

Functions are also `public` by default which means other contracts can call
those functions. If this behavior is undesired, mark the function as `private`.
By convention, private function names are prepended with an `_`.

Syntax:

```code
function sayHello(string memory _name, uint _age) public {

}

// Can't be executed by other contracts.
function _sayGoodbye(string _name, uint _age) private {

}
```

Along with `public` and `private`, Solidity also has the `internal` and
`external` access modifiers:

```code
// Similar to private, except child contacts can also execute this function (like 'protected'!)
function hello() internal {

}

// Similar to public, except this function can ONLY be called from outside the contract.
function bye() external {

}
```

Functions with a return must specify it in the function signature:

```code
function sayHello() public returns (string memory) {
    return "Hello";
}
```

Functions in Solidity can also have multiple returns:

```code
function getVals() public returns(uint numA, uint numB, uint numC) {
  return(1, 2, 3);
}

uint a;
uint b;
uint c;
// Grab all return values
(a, b, c) = getVals();
// Grab specific return values
(,,c) = getVals();
```

### Function Modifiers

View functions are functions that don't modify, only view the contract's state
(global variables):

```code
function sayHello() public view returns (string memory) {

}
```

Pure functions are functions that don't access any data in the contract:

```code
function twoPlusTwo public pure returns (uint) {
    return 2 + 2;
}
```

### Global Functions

Solidity has predefined global functions that are available to all functions:

* `require(condition)` - when used as the first line in a function, the function
will only run if the condition is true.

## Classes & Objects

### Structs

Like classes, structs are used to create data types with properties.

### Contracts & Inheritance

Contract inheritance allows the separation of code logic into multiple contracts
for more organized, clean code.

```code
// Dog.sol
contract Dog {

}
```

```code
// Husky.sol
import "./Dog.sol";

contract Husky is Dog {
    // Husky has access to all functions defined in dog.
}
```

## Events

Events are a way for the contract to notify your frontend that something happened
to the blockchain (state).

Example:

```code
event NameAdded(string name);

string[] public names;
addName("Tom");

function addName(string memory _name) public {
    names.push(_name);
    emit NameAdded(_name);
}
```

Frontend:

```js
ContractName.NameAdded(function(error, result) {
  // do something with result
})
```
