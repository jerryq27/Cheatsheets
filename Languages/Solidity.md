# Solidity

[Issues Link](https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/chronological-issues-from-video.md)
[Checkpoint](https://youtu.be/coQ5dg8wM2o?t=2355)

Solidity is a language used to build decentralized applications (DApps) on the blockchain networks.

## Basics

Solidity programs are compiled by the Ethereum Virtual Machine (EVM). Other blockchains
that are EVM compatable are able to deploy Solidity contract on their network as well.

Solidity programs always start with the `pragma solidity $VERSION` to specify
which version the project's code runs on:

```cpp
pragma solidity 0.7.0  // Valid only for version 0.7.0.
pragma solidity ^0.6.0; // Valid for any 0.6 versions, only in the 0.6.* range.
pragma solidity >=0.6.0 <0.9.0; // Valid for the the version range 0.6.0 (inclusive) - 0.9.0 (exclusive).
```

Above the `pragma`, there should also be a _SPDX License Identifier_, otherwise the compiler will throw a warning:

```cpp
// SPDX-License-Identifier: MIT
pragma >=0.6.0 <0.9.0;
```

The language is [statically](Languages#statically-typed) and [strongly typed](Languages#strongly-typed) and uses the
[basic arithmetic operators](Languages#arithmetic) with the addition of `**` "Power of" operator.

Transactions made on the network are measured using _ether_, _wei_, and _gwei_.

* **Ether** - Base unit used in Ethereum.
* **Gwei** - Unit of Ether with 9 decimal places.
* **Wei** - The smallest unit of measure of Ether with 18 decimal places.

## Variables

Variables in Solidity are **not** typically stored in memory unless [specified](#storage). A contract's global
variables are permanently stored in the contract's storage i.e. they're written on the Ethereum blockchain (like writing to a database).
These global variables are more commonly referred to as _state variables_.

Variables can contain numerous data types:

```cpp
uint256 myNumber = 5; // unsigned integer of 256 bits (32 bytes).
bool myBool = false; // boolean
string myString = "String"; // Strings
int256 myint = -5; // Signed integer of 256 bits (32 bytes).
address myAddress = 0x3B67C3700632B63086FD2CCA2Ce918cBC19a4900; // Ethereum wallet address value.
bytes32 myBytes = "cat"; // byte value of 32 bytes.

// If a value isn't specified, it will automatically be initialized to the null value of that type, in this case '0'.
uint256 myNumber2; // 0
```

> These types are technically functions, when using something like `myNumber()` it just returns the value.

### Overflow

Solidity does have the issue of **overflow**, which means when an integer reaches it's max size, it wraps
around and goes back to its lowest value:

```sol
contract Overflow {

  funciton overflow() public view {
    uint8 max = 255;
    // returns '99'.
    return max + uint8(100);
  }

}
```

The **SafeMathChainlink** package was created to address this issue:

```sol
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract Overflow {
  // This 'using A for B;' can be used to attach library functions(A) to any type(B) within a contract.
  using SafeMathChainlink for uint8;

  funciton overflow() public view {
    uint8 max = 255;
    // returns '355'.
    return max + uint8(100);
  }
}

```

> As of 0.8.0, Solidity now checks for overflow. Code is more readable at the slight increase in gas cost.

### Global Variables

Solidity has predefined global variables that are available to all functions:

* `msg.sender` - refers to the address of the person/smart contract that called
the function

### Casting

### Enums

Solidity supports [enums](Languages/#variables).

Example:

```sol
// No Semicolon needed
// Each value has a numerical representation which it's its index, starting at 0.
enum Dogs {HUSKY, BEAGLE, CORGI, SHIBA INU, PITBULL}
```

### Visibility

There are 4 types of visibility modifiers:

1. **external** - Can't be used by the same contract, has to be an external contract.
1. **public** - Any contract can use and a getter is generated to access it.
1. **internal** - Can't be used by an external contract, has to be used by internally and child contracts.
1. **private** - Can only be used by the contract they are defined in.

By default, a variable and functions are _internal_:

```sol
uint256 myNumber; // internal
uint256 public myPublicNumber; // public
```

## Collections

### Arrays

Soildity arrays can either be _fixed_ (size pre-defined) or _dynamic_ (size not defined):

```cpp
// Fixed
Animal[5] animals2;

// Dynamic
Animal[] animals;

// Adding data to arrays.
animals.push(Animal('dog'));
animals.push(Animal({name: 'cat"}));
```

Arrays, like other variable types, can be declared public and Solidity automatically
creates a getter method for it.

```cpp
// Other contracts can now read data from this, useful for storing public data
// in a contract.
string[] public names;
names.push("Tom");
names.push("Jerry"); // Tom, Jerry
```

### Mappings

Mappings are key-value pairs:

```cpp
// mapping($KEY_TYPE => $VALUE_TYPE)
mapping(uint => string) public userIdToName;

// Adding data to a map.
userIdToName[key] = value;
```

> It's considered best practice to _emit_ an event whenever a mapping is updated.

## I/O

### Storage

Solidity offers two locations to store variables:

1. **storage** - variables stored permanently on the blockchain. Default setting for variables defined outside of functions.
1. **memory** - temporary variables. Default setting for variables defined inside functions and don't persist beyond the function scope.

Although these keywords aren't commonly used, there is some use cases when dealing with structs and arrays:

```cpp
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

### Events

Events are similar to what logging is, but they are for the blockchain to log what a contract is doing.
Events are stored and accessible on the blockchain as well. They are not accessible by any smart contract
and are much more gas efficient than using a storage variable.

Events are also a way for the contract to notify your frontend that something happened
to the blockchain/state.

Example:

```cpp
// A custom event needs to be defined.
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
});
```

## Functions

Functions are _public_ by default which means other contracts can call those functions.
If this behavior is undesired, mark the function as _private_.
Private function names are also prepended with an underscore by convention.

By convention, function parameters are also prepended with an underscore to differentiate
them from global variables.

Solidity also uses the _internal_ and _external_ access modifiers:

```cpp
// Similar to private, except child contacts can also execute this function (like 'protected'!)
function hello() internal {

}

// Similar to public, except this function can ONLY be called from outside the contract.
function bye() external {

}
```

Functions with a return must specify it in the function signature:

```cpp
function sayHello() public returns (string memory) {
    return "Hello";
}
```

Solidity functions can also have multiple returns:

```cpp
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

With functions, alongside access modifiers, there are also function modifiers:

1. **view** - view functions read some state off of the blockchain.
1. **pure** - pure functions do some type of calculation, without needing to alter or access the contract's state on the blockchain.
1. **payable** - payable functions gives us access to wallet and payment information in the form of the pre-defined `msg.sender` and `msg.value` variables.

```cpp
// View functions read the contract's state on the blockchain.
function sayHello() public view returns (string memory) {

}

// Pure functions are functions that don't access any data in the contract's state.
function twoPlusTwo public pure returns (uint) {
    return 2 + 2;
}
```

> A data type's default function call is technically a view function!

### Parameter Modifiers

The storage modifiers handle how parameter values (objects only?) are stored during the execution of a function:

1. **memory** - the parameter value will only exist in memory during the execution of the function.
1. **storage** - the parameter value will persist even after the function has finished executing.

```cpp

function sayHello(string memory _name) {
  say("Hello " + _name);
}

function sayhello2(string storage _name) {
  say("Hello " + _name);
}
```

You use also use these modifiers to pass values into a function by [value](Languages/#functions) or by [reference](Languages/#functions):

* To pass a value by value, add _memory_ after the type (required by all reference types like strings, structs, arrays, maps, etc.)
* To pass by reference, nothing else needs to be added.

Syntax:

```cpp
function sayHello(string memory _name, uint _age) public {

}

// Can't be executed by other contracts.
function _sayGoodbye(string _name, uint _age) private {

}
```

### Custom Modifiers

Custom modifiers are used to change the behavior of a function in a declaritive way:

```cpp
modifier onlyOwner {
    require(msg.sender == owner);
    // this underscore means 'rest of the function code.'
    _;
}

// Withdraw function using the onlyOwner modifier.
function withdraw() payable onlyOwner public {
    msg.sender.transfer(address(this).balance);
    ...
}
```

### Global Functions

Solidity provides some predefined functions that are available to all functions:

* `require(condition)` - when used as the first line in a function, the function
will only run if the condition is true.

## Contracts

Contracts are the fundamental building block for decentralized applications.
They can be thought of as [classes](Languages/#classes--objects) and are the starting point to a project.

```cpp
pragma solidity >=0.5.0 <0.6.0;

contract Example {
    // Constructor - this function runs when a contract is deployed.
    constructor() public {
        // in this case, the owner is the person who deployed the contract.
        owner = msg.sender;
    }
}
```

### Structs

Like classes, structs are used to create new data types with properties and objects.

```cpp
contract Example {

    struct Person {
        string name;
        string blockchain;
    }

    // Order matters when creating an object like this.
    Person person1 = Person("Jerry", "Ethereum")
    // Order doesn't matter when specifying the names.
    Person person2 = Person({blockchain: "Solana", name: "Tom"});
}
```

> Structs organize data the same way arrays do, as in 'name' would be at index 0, and 'blockchain' at index 1.

### Importing Contracts

You can import a contract to use with another contract:

```cpp
import "/path/to/other/contract.sol"

// Assuming the file has a contract called 'Example'.

// Creating a contract object like this techinically deploys the contract to the blockchain.
Example ex = new Example();
address(ex); // Returns the address of the contract.
```

There are two things required to interact with the members/functions of an imported contract:

1. **Contract address**
1. **ABI (Application Binary Interface)** - ABIs is JSON that describes the contents of a Solidity file (contracts, functions, inputs, outputs, type of function, variables, variable types, etc.) this tells Solidity and other languages how they can interact with that contract. An ABI is always needed to interact with a contract.

### Inheritance

Contract inheritance allows the separation of code logic into multiple contracts
for more organized, clean code.

```cpp
// Dog.sol
contract Dog {

}
```

```cpp
// Husky.sol
import "./Dog.sol";

contract Husky is Dog {
    // Husky has access to all functions defined in dog.
}
```

## Libraries & Frameworks

### Web3.py

The Web3.py framework allows us to create and deploy smart contracts to various networks like Ethereum.

#### Web3 Local Network Deployment

The following steps are how to deploy to a local network with Web3:

1. Connect to the network
1. Compile the contract's Solidity code
1. Create a transaction for the contract's creation

Connecting to a network:

```py
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
```

To compile the contract, we use the `solcx` library:

```py
from solcx import compile_standard, install_solc

# Compile the Solidity file.
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_sol}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as json_file:
    json.dump(compiled_sol, json_file)
```

The resulting JSON will give us all the information we need to deploy this contract to a network,
the ABI and the bytecode. To get this information, we traverse the JSON tree:

```py
# Get the bytecode by traversing the JSON tree.
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# Get the ABI.
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
```

Now we need to create the _transaction_ for the contract creation.
We will need the _nonce_ (the transaction counter), the address deploying the contract, and
the private key for that address to sign the transaction:

```py
# chain_id is obtained from the local network (Ganache)
chain_id = 1337
address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = "0x" + "24d5640bac3b8d9e55520e272058dac69590bd83f50c5f451c9962e1226b4145"


# Get latest transaction using the transaction counter AKA the Nonce
nonce = w3.eth.getTransactionCount(address)

# 1. Build the transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": address, "nonce": nonce}
)
# 2. Sign the transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 3. Send the transaction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=transaction_hash)
```

> When working with private keys, make sure to prepend the `0x` since Python needs
it to be in hexadecimal format.

#### Working With a Deployed Contract

Working with any contract requires two things:

1. The contract's address.
1. The contract's ABI.

Once we have those, we can invoke the members in a couple ways:

1. **call** - simulates the function call and generates a value, but doesn't make a state change on the network.
1. **transaction** - actually makes a state change to the network.

```py
simple_storage = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)

# print(simple_storage.functions.retrieve().call()) # 0
# print(simple_storage.functions.store(27).call()) # 15
# print(simple_storage.functions.retrieve().call()) # 0 Why? Cause call() is just a simulation.

# Increment Nonce since it is currently pointing to the contract creation transaction.
store_transaction = simple_storage.functions.store(27).buildTransaction(
    {"chainId": chain_id, "from": address, "nonce": nonce + 1}
)
signed_store_transaction = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)

send_store_transaction_hash = w3.eth.send_raw_transaction(signed_store_transaction.rawTransaction)

transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_transaction_hash)
print(simple_storage.functions.retrieve().call())  # 27
```

### Brownie

Brownie is a Python library built on top of the Web3.py library and simplifies working with and deploying
smart contracts.

#### Brownie Deployments

This section details how the above code for Web3 deployment can be done the Brownie way. The
[Brownie cheatsheet](../Libraries,%20Tools,%20&%20Frameworks/BlockchainDev/Brownie#brownie) has
more details with using the library.

Compiling contracts defined in **contracts/**:

```sh
> brownie compile
```

The compiled contract is now populating the **build/** folder.

To deploy compile contracts locally, create a deploy script in **scripts/**:

```py
from brownie import ExampleContract, accounts

example_contract = ExampleContract.deploy({"from": accounts[0]})
print("Contract has been deployed!")
```

Run with `brownie run scripts/deploy_example.py`:

```sh
> brownie run .\scripts\example_deploy.py
Brownie v1.16.4 - Python development framework for Ethereum

SrcProject is the active project.

Launching 'ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

Running 'scripts\example_deploy.py::main'...
Contract has been deployed!
Terminating local RPC client...
```

The contract has been deployed to a local network!
If a network isn't specified in the run command, Brownie launches a local Ganache instance by default.

Deploying to a testnet, use the `--network` flag with a Brownie predefined testnets.
To view them, use `brownie networks list`:

```console
> brownie networks list

Brownie v1.16.4 - Python development framework for Ethereum

The following networks are declared:

Ethereum
  ├─Mainnet (Infura): mainnet       
  ├─Ropsten (Infura): ropsten
  ...
```

You will also need an account's private key to use for the testnet deployment, then just
run `brownie run scripts\example_deploy.py --network ropsten` and the contract had been
deployed to a test network!
