# Brownie

[Checkpoint](https://youtu.be/M576WGiDBdQ?t=30479)

Brownie is a smart contract development framework built on top of Web3.py. There's
alot to manage with vanilla Web3.py from compiling the Solidity code into JSON
with `solcx`, keeping track of addresses, and deployment.

## Basics

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

### Console

The Brownie console opens the Python interpreter and allows us to run code normally ran in script.
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

### Tests

Tests are defined in the `test/` folder. To run those tests, you would use
the `brownie test` command:

```console
> brownie test
Brownie v1.17.2 - Python development framework for Ethereum

======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.9.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\KikoBrothers\Jerry\Documents\Dev\GitHub\Cheatsheets\Tutorials\Python\BlockchainDev\BrownieFundMe\src
plugins: eth-brownie-1.17.2, hypothesis-6.27.3, forked-1.3.0, xdist-1.34.0, web3-5.25.0
collected 1 item

Launching 'ganache-cli.cmd --accounts 10 --hardfork istanbul --gasLimit 12000000 --mnemonic brownie --port 8545'...

tests\test_fund_me.py
.
[100%]

=================================== 1 passed in 8.03s ===================================
Terminating local RPC client...
```

Since Brownie tests are built upon Pytest, you can use commands like `Pytest.skip()` to skip
certain tests. For example, we wouldn't want to run all the tests on a non-local network since
it would be really slow. Skipping tests is one way to handle this issue.

> By default, `brownie test` uses the network `development` to run the tests,
so `brownie test` is the same as running `brownie test --network development`.
You can changed the default network by defining a `default:` key in the networks
section of the `brownie-config.yaml` file.

### Testing Environment

There's a recommended environment setup for running tests.

You should use these setups for the most time while developing:

1. Brownie Ganache Chain with Mocks
1. Testnet

These are optional:

1. Brownie mainnet fork
1. Custom mainnet fork

And these aren't necessary and usually used for tinkering:

1. Local Ganache

## Workflow

### Local Network Deployment

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

Also notice that if we don't provide a network or testnet, Brownie launches a **Ganache** instance by default.
If we are running the Ganache GUI, Brownie will use that instance of Ganache if they are running on the same port.

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

This is much more manageable way to create and deploy contracts with Brownie than
with Web3.

### Test Network Deployment

To work with a testnet, you would first add an address from Metamask, for example,
Using `brownie accounts new $ACCOUNT_NAME`, this will prompt you for a private key
Of the account (**make sure to prepend `0x` to it!**):

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

* `brownie accounts new $ACCOUNT_NAME` - adds an account to Brownie's accounts
* `brownie accounts delete $ACCOUNT_NAME` - deletes an account from Brownie's accounts
* `brownie accounts list` - list the created accounts in Brownie

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

> Any network listed under _development_ delete any blockchain changes after the
script terminates. Other testnets will persist with those changes.

### Verification

Deploying a contract on a testnet will show up as a blob of bytecode in a site like Etherscan and
you won't be able to interact with it yet. To allow for interaction with the contract, it will have to
be verified. This can be done manually on Etherscan or programatically with an API token from Etherscan.

Place the API token in the `.env` file then change the deploy code to:

```py
from brownie import ExampleContract, accounts

example_contract = ExampleContract.deploy({"from": accounts[0]}, publish_source=True)
print("Contract has been deployed and verified!")
```

### Tests

Tests are created in the **tests/** directory. Usually files in the directory are prepended
with tests by convention, it also help Brownie locate the files with tests.

Common testing commands:

* `brownie test` - runs all the tests in the **tests/** folder
* `brownie test -k $TEST_FUNCTION_NAME` - runs a specific test function
* `brownie test -pdb` - opens the Python interpreter after a failed test (useful for debugging)
* `brownie test -s` - more output information on test and it will show print lines if they exist in a test

> Brownie test uses everything in the Pytest library, anything supported there is supported with Brownie testing as well.

## Advance Use

### Brownie Config

The config file is a YAML file located in the root directory of the Brownie project.
We can use this file (`brownie-config.yaml`) to tell Brownie about:

* Whether to use a `.env` file
* Wallet definitions
* Where to get external libraries (Brownie can download from GitHub, but **not** from NPM)
* Compiler options
* Networks

### Networks

Brownie has some built in network definitions that it can deploy contracts to. To see them
use the command `brownie networks list`:

```console
> brownie networks list

Brownie v1.17.2 - Python development framework for Ethereum

The following networks are declared:

Ethereum
  ├─Mainnet (Infura): mainnet
  ├─Ropsten (Infura): ropsten
  ├─Rinkeby (Infura): rinkeby
  ├─Goerli (Infura): goerli
  └─Kovan (Infura): kovan

Ethereum Classic
  ├─Mainnet: etc
  └─Kotti: kotti

Arbitrum
  └─Mainnet: arbitrum-main

Binance Smart Chain
  ├─Testnet: bsc-test
  └─Mainnet: bsc-main

Fantom Opera
  ├─Testnet: ftm-test

Polygon
  ├─Mainnet (Infura): polygon-main
  └─Mumbai Testnet (Infura): polygon-test

XDai
  ├─Mainnet: xdai-main
  └─Testnet: xdai-test

Development
  ├─Ganache-CLI: development
  ├─Geth Dev: geth-dev
  ├─Hardhat: hardhat
  ├─Hardhat (Mainnet Fork): hardhat-fork
  ├─Ganache-CLI (Mainnet Fork): mainnet-fork
  ├─Ganache-CLI (BSC-Mainnet Fork): bsc-main-fork
  ├─Ganache-CLI (FTM-Mainnet Fork): ftm-main-fork
  ├─Ganache-CLI (Polygon-Mainnet Fork): polygon-main-fork
  └─Ganache-CLI (XDai-Mainnet Fork): xdai-main-fork
```

Changes won't persist on networks in the Development category, all other categories will save network changes.
To add a network to the list, for example, a local Ganache instance, use the following command
`brownie networks add $NETWORK_CATEGORY $NETWORK_NAME host=$NETWORK_HOST chainid=$NETWORK_ID`:

```console
> brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=5777
INFO: Could not find files for the given pattern(s).
Brownie v1.17.2 - Python development framework for Ethereum

SUCCESS: A new network 'ganache-local' has been added
  └─ganache-local
    ├─id: ganache-local
    ├─chainid: 5777
    └─host: http://127.0.0.1:8545

> brownie networks list
Brownie v1.17.2 - Python development framework for Ethereum

The following networks are declared:

Ethereum
  ├─Mainnet (Infura): mainnet
  ├─Ropsten (Infura): ropsten
  ├─Rinkeby (Infura): rinkeby
  ├─Goerli (Infura): goerli
  ├─Kovan (Infura): kovan
  └─ganache-local: ganache-local <------------ new

Ethereum Classic
  ├─Mainnet: etc
  └─Kotti: kotti
```

Brownie can also fork a mainnet blockchian to a local blockchain. This allows us to work
with a simulated version of a mainnet without affecting the actual meinnet. You can fork
a mainnet from services like Infura or Alchemy.

### Brownie Mixes

Brownie mixes are location on [GitHub](https://github.com/brownie-mix). These mixes are
essentially templates that contain boiler plate code for various types of Brownie projects.

Some example mixes are:

* react-mix - Brownie project with React
* token-mix - ERC20 token project
* chainlink-mix - Brownie project with Chainlink
* nft-mix - NFT project

To use one of these mixes, you would use the `brownie bake $MIX` command:

```console
> brownie bake react-mix
```

## Other

### Tools

There are a variety of tools you can use for smart contract development:

* Ganache - simulates a local blockchain in which your computer is the only node (very fast).
* Infura - Gives access to testnet and mainnet by providing blockchain URLs.
* OpenZeppelin - Provides smart contracts to make developing other contracts easier and secure.
