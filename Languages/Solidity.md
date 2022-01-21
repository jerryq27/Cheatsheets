# Solidity

[Zombie Course](https://cryptozombies.io/en/course)

[Stopping Point: Chapter 3 Lesson 1](https://cryptozombies.io/en/lesson/3/chapter/1)

[Free Code Camp Course: Lesson 6 - Brownie Fund Me](https://youtu.be/M576WGiDBdQ?t=18941)
[Issues Link](https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/chronological-issues-from-video.md)

```code
pragma solidity >=0.6.0 <0.9.0;

/*
    Contracts can be thought of like a class.
*/
contract SimpleStorage {
    
    uint256 myNum; // In solidity, this will get initialized to a null value, in this case: 0.
    
    struct People {
        uint256 favoriteNumber;
        string name;
    }
    
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNum;

    function store(uint256 _myNum) public {
        myNum = _myNum;
    }
    
    /*
        Two keywords that define functions:
        view - view functions read some state off of the blockchain. In Remix, functions that don't alter state create a blue buttons (public variables are also view functions!)
        pure - pure functions do some type of calculation, but pure functions also  don't alter the state.
    */
    function retreive() public view returns(uint256) {
        return myNum;
    }
    
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        // Order matters when creating an object like this.
        // people.push(People(_favoriteNumber, _name));
        
        // Order doesn't matter when specifying the names.
        people.push(People({name: _name, favoriteNumber: _favoriteNumber}));
        
        nameToFavoriteNum[_name] = _favoriteNumber;
        
    }
}
```

```sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {
    // This 'using A for B;' can be used to attach library functions(A) to any type(B) within a contract.
    using SafeMathChainlink for uint256;
    
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    
    /*
        Constructor - this function runs when a contract is deployed.
    */
    constructor() public {
        // in this case, the owner is the person who deployed the contract.
        owner = msg.sender;
    }
    
    
    function fund() public payable {
        uint256 minUSD = 50 * (10**18); // Minimum of $50 in wei.
        // if(msg.value < minUSD) {
        //     revert?
        // }
        
        // Solidity style would use 'require' which is a check before a function executes.
        require(getConversionRate(msg.value) >= minUSD, "You need to spend more ETH!");
        // 'revert' unspent gas and funds are returned to the user.
        
        /*
            msg.sender & msg.value are predefined values in every contract.
            1. msg.sender - the sender of funds
            2. msg.value - the amount of funds
        */
        addressToAmountFunded[msg.sender] += msg.value;
        
        // Oracles are used to connect contracts to "outside world data".
        // Find ETH -> USD conversion.
        
        
        funders.push(msg.sender);
    }
    
    function getVersion() public view returns(uint256) {
        
        // Addresss from https://docs.chain.link/docs/ethereum-addresses/ Rinkeby: ETH->USD
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }
    
    function getPrice() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        // This returns a Tuple of 5 values.
        // priceFeed.latestRoundData()
        
        // (
        //     uint80 roundId,
        //     int256 answer,
        //     uint256 startedAt,
        //     uint256 updatedAt,
        //     uint80 answeredInRound
        // ) = priceFeed.latestRoundData();
        
        // To fix unused variables warning, use blanks.
        (,int256 answer,,,) = priceFeed.latestRoundData();
        
        /* 
            returns 320120819731 which is 3201.20819731
            
            Reason being that Solidity doesn't work with decimals,
            and these values should be seen as having 8 decimals places
        */
        // return uint256(answer);
        
        // Returns the answer in wei (18 decimal places).
        return uint256(answer * 10000000000);
    }
    
    // 100000000 = 1 gwei
    function getConversionRate(uint256 ethAmount) public view returns(uint256) {
        uint256 ethPrice = getPrice();
        
        // 320801998386.000000000000000000
        // uint256 ethAmountInUSD = (ethPrice * ethAmount);
        
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        // 3208019983860 
        // add 0s to get 18 decimal places
        // 0.000003208019983860
        
        // 0.000003208019983860 * 1 Gwei = USD price.
        return ethAmountInUSD;
    }
    
    // Modifiers are used to change the behavior of a function in a declaritive way.
    modifier onlyOwner {
        require(msg.sender == owner);
        // this underscore means 'rest of the function code.'
        _;
    }
    
    // function withdraw() payable public {
    //     // Add a require to make sure only the contract owner/admin can withdraw funds.
    //     require(msg.sender == owner);
        
        
    //     // tansfer is a function that can be called on any address to send ETH from one address to another.
    //     // 'this' refers to the current contract.
    //     // 'balance' is the current value of funds at that address.
    //     msg.sender.transfer(address(this).balance);
    // }
    
    // withdraw function using a modifier.
    function withdraw() payable onlyOwner public {
        msg.sender.transfer(address(this).balance);
        
        // Reset all the funder's fund value to 0.
        for(uint256 i = 0; i < funders.length; i++) {
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }
        // reset the funders array to a blank array.
        funders = new address[](0);
    }

    
}
```

Solidity is a language used to build DApps on the Ethereum network.

## Basics

Solidity programs are compiled to the Ethereum Virtual Machine (EVM).
Blockchains that are EVM compatable are able to deploy Solidity contract on their network.

Solidity programs always start with the `pragma solidity $VERSION` to specify
which version the project's code runs on.

```code
pragma solidity 0.7.0  // Valid only for version 0.7.0.
pragma solidity ^0.6.0; // Valid for any 0.6 versions, only in the 0.6.* range.
pragma solidity >=0.6.0 <0.9.0; // Valid for the the version range 0.6.0 (inclusive) - 0.9.0 (exclusive).
```

Above the pragma, there should also be a SPDX License Identifier, otherwise the compiler will throw a warning:

```code
// SPDX-License-Identifier: MIT
pragma >=0.6.0 <0.9.0;
```

The language is [statically (strongly) typed](#) and uses the basic arithmetic
operators with the addition of `**` "Power of" operator.

Transactions made on the network are measured using _ether_, _wei_, and _gwei_.

* Ether - Base unit used in Ethereum.
* Gwei - Unit of Ether with 9 decimal places.
* Wei - The smallest unit of measure of Ether with 18 decimal places.

## Variables

Variables can contain numerous data types:

```code
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

### Casting

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

State variables are permanently stored in the contract's storage i.e. they're
written on the Ethereum blockchain (like writing to a database).

### Visibility

There are 4 types of visibility modifiers:

1. `external` - Can't be used by the same contract, has to be an external contract.
1. `public` - Any contract can use.
1. `internal` - Can't be used by an external contract, has to be used by internally.
1. `private` - Can only be used by the contract they are defined in.

By default, a variable (or function) is internal:

```sol
uint256 myNumber; // internal
uint256 public myPublicNumber; // public
```

### Global Variables

Solidity has predefined global variables that are available to all functions:

* `msg.sender` - refers to the address of the person/smart contract that called
the function

## Arrays

Soildity can define two types of arrays:

* Fixed arrays - array with a fixed size.
* Dynamic arrays - array with no fixed size and can grow dynamically

```code
// Fixed
Animal[5] animals2;

// Dynamic
Animal[] animals;

// Adding data to arrays.
animals.push(Animal('dog'));
animals.push(Animal({name: 'cat"}));
```

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

Mappings are another way to store data as key-value pairs:

```code
// mapping(key type => value type)
mapping(uint => string) public userIdToName;

// Adding data to a map.
userIdToName[key] = value;
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

There are a few keyword function modifiers:

1. `view` - view functions read some state off of the blockchain.
1. `pure` - pure functions do some type of calculation, without altering the state of the blockchain.
1. `payable` - payable functions gives us access to wallet and payment information in the form of the pre-defined `msg.sender` and `msg.value` variables.

```code
function sayHello() public view returns (string memory) {

}

// Pure functions are functions that don't access any data in the contract
function twoPlusTwo public pure returns (uint) {
    return 2 + 2;
}
```

> A data type's function call is technically a view function!

### Parameter Modifiers

There are a few keyword modifiers to handle how parameter values (objects only?) are stored during the execution of a function:

1. `memory` - the parameter value will only exist in memory during the execution of the function.
1. `storage` - the parameter value will persist even after the function has finished executing.

```code

function sayHello(string memory _name) {
  say("Hello " + _name);
}

function sayhello2(string storage _name) {
  say("Hello " + _name);
}
```

### Global Functions

Solidity has predefined global functions that are available to all functions:

* `require(condition)` - when used as the first line in a function, the function
will only run if the condition is true.

## Contracts

Contracts are the fundamental building block for Ethereum applications.
They can be thought of as classes and are the starting point to a project.

```code
pragma solidity >=0.5.0 <0.6.0;

contract Example {
    
}
```

### Structs

Like classes, structs are used to create new data types with properties and objects.

```code
contract Example {

  struct Person {
    string name;
    string blockchain;
  }

  Person person1 = Person({name: "Jerry", blockchain: "Ethereum"});
}
```

> Structs organize data the same way arrays do, as in 'name' would be at index 0, and 'blockchain' at index 1.

### Importing Contracts

You can import a contract to use with another contract:

```sol
import "/path/to/other/contract.sol"

// Assuming the file has a contract called 'Example'.

// Creating a contract object like this techinically deploys the contract to the blockchain.
Example ex = new Example();
address(ex); // Returns the address of the contract.
```

There are two things required to interact with the members/functions of an imported contract:

1. Contract address
1. ABI (Application Binary Interface) - ABIs is JSON that describes the contents of a Solidity file (contracts, functions, inputs, outputs, type of function, variables, variable types, etc.) this tells Solidity and other languages how they can interact with that contract. An ABI is always needed to interact with a contract.

### Inheritance

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

## Python & Solidity

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

1. call - simulates the function call and generates a value, but doesn't make a state change on the network.
1. transaction - actually makes a state change to the network.

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

Brownie is a smart contract development framework built on top of Web3.py. There's alot to manage
with vanilla Web3.py from compiling the Solidity code into JSON with `solcx`, keeping track of addresses,
and deployment.

To create a Brownie project, first install the `eth-brownie` package then run `brownie init` inside
and empty directory. This will generate the following folder structure:

* build/ - holds the low level files generated with `brownie compile`
  * contracts/ - where the compiled JSON for Solidity code is.
  * deployments/ - tracks deployments across all networks.
  * interfaces/
* contracts/ - holds the Solidity contract source files.
* interfaces/ - holds interfaces (interfaces makes it easy to interact with blockchain applications)
* reports/ - holds any type of report you want to save
* scripts/ - holds scripts to automates tasks
* tests/ - holds tests for the contracts
* .gitattributes
* .gitignore

Some common Brownie commands:

* `brownie init` - creates a Brownie project in the current folder (must be an empty directory)
* `brownie compile` - compiles Solidity code from projects folders into **build/**
* `brownie run $SCRIPT` - runs the script located in **scripts/**

#### Brownie Local Network Deployment

The following steps are how to deploy to a local network with Brownie:

1. Compile the contract's Solidity code
1. Create a transaction for the contract's creation
1. Connect to the network

To compile the contracts in **contracts/**, the `brownie compile` command is used.
Doing this will also place the contract object definition in Brownie so we can
use it:

```py
from brownie import ExampleContract
```

To deploy this, it's as simple as writing a script and running it with `brownie run scripts/deploy_example.py`:

```py
from brownie import ExampleContract, accounts

example_contract = ExampleContract.deploy({"from": accounts[0]})
print("Contract has been deployed!")
```

The contract has been deployed to a local network!
Notice that when running a script, Brownie displays the following output:

```console
> brownie run .\scripts\example_deploy.py
Brownie v1.16.4 - Python development framework for Ethereum

SrcProject is the active project.

Launching 'ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

Running 'scripts\example_deploy.py::main'...
Contract has been deployed!
Terminating local RPC client...
```

Also notice that if we don't provide a network or testnet, Brownie launches a Ganache instance by default.
Using the following code, we can access the addresses generated by Ganache:

```py
from brownie import accounts

# This only works for a local network
def deploy():
    account = accounts[0]
    print(account)


def main():
    deploy()
```

This is much more manageable to create and deploy contracts with Brownie than Web3.

#### Brownie Test Network Deployment

To work with a testnet, you would first add an account from Metamask, for example,
Using `brownie accounts new $ACCOUNT_NAME`, this will prompt you for a private key
Of the account (make sure to prepend `0x` to it!):

```console
> brownie accounts new jerry-test-account
Brownie v1.16.4 - Python development framework for Ethereum

Enter the private key you wish to add: 0x**********
Enter the password to encrypt this account with:
SUCCESS: A new account '0x3B67C3700632B63086FD2CCA2Ce918cBC19a4900' has been generated with the id 'jerry-test-account'

> brownie accounts list
Brownie v1.16.4 - Python development framework for Ethereum

Found 1 account:
 └─jerry-test-account: 0x3B67C3700632B63086FD2CCA2Ce918cBC19a4900
```

Once the account has been added (you will need the password you used when adding the account):

```py
from brownie import accounts


def deploy():
    account = accounts.load("jerry-test-account")
    print(account)


def main():
    deploy()
```

This is a great way to store account keys, it's not hard coded, won't be pushed up with git, and it's password protected.
Using Environment variables would be a bit less secure, but more developer friendly since you won't be inputting a password
everytime you run the script.

To load a private key with Environment variables, you would first need to tell Brownie to load in the variables in the `.env` file.
This is accomplished by creating a `brownie-config.yaml` file and adding the followin line:

```yaml
dotenv: .env
```

Then you update the script:

```py
import os
from brownie import accounts


def deploy():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)


def main():
    deploy()
```

> Rule of thumb: Use the password protected method for accounts with real money and the environment variable method for test
accounts.

Useful commands with accounts:

* brownie accounts new $ACCOUNT_NAME - adds an account to Brownie's accounts
* brownie accounts delete $ACCOUNT_NAME - deletes an account from Brownie's accounts
* brownie accounts list - list the created accounts in Brownie

Deploying to a testnet, Brownie comes with predefined testnets already. To view them, use `brownie networks list`:

```console
> brownie networks list

Brownie v1.16.4 - Python development framework for Ethereum

The following networks are declared:

Ethereum
  ├─Mainnet (Infura): mainnet       
  ├─Ropsten (Infura): ropsten
  ...
```

> Anything listed under development, those networks delete any blockchain changes after the script terminates. Other testnets,
those values will persist.

#### Tests

Tests are created in the **tests/** directory. Usually files in the directory are prepended
with tests by convention, it also help Brownie locate the files with tests.

Common testing commands:

* `brownie test` - runs all the tests in the **tests/** folder
* `brownie test -k $TEST_FUNCTION_NAME` - runs a specific test function
* `brownie test -pdb` - opens the Python interpreter after a failed test (useful for debugging)
* `brownie test -s` - more output information on test and it will show print lines if they exist in a test

> Brownie test uses everything in the Pytest library, anything supported there is supported with Brownie testing as well.

#### Console

The Brownie console opens the  Python interpreter and allows us to run code normally ran in script.
This is useful for code that doesn't necessarily need a file for reuseability, `brownie console`:

```console
> brownie console

Brownie v1.16.4 - Python development framework for Ethereum

SrcProject is the active project.

Launching 'ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...
Brownie environment is ready.
>>> SimpleStorage
[]
>>> account = accounts[0]
>>> account
<Account '0x66aB6D9362d4F35596279692F0251Db635165871'>
>>> simple_storage = SimpleStorage.deploy({"from": account})
Transaction sent: 0x1ff45e0f954f8736dcf6ce6287a1fa12b4e8ab3395b729cc8975c52f92cdf5cf
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  SimpleStorage.constructor confirmed   Block: 1   Gas used: 335476 (2.80%)
  SimpleStorage deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87    

>>> simple_storage
<SimpleStorage Contract '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'>
```

#### Brownie Config

The config file is a YAML file located in the root directory of the Brownie project.
We can use this file (`brownie-config.yaml`) to tell Brownie about:

* Where to get external libraries

### Tools

There are a variety of tools you can use for smart contract development:

* Ganache - simulates a local blockchain in which your computer is the only node (very fast).
* Infura - Gives access to testnet and mainnet by providing blockchain URLs.
