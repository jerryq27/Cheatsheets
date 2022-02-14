# Blockchain

## Smart Contracts

Smart contracts are programs that live on the blockchian. They have their own
address and once created they **cannot** be changed. Since contracts are immutable,
there are various patterns that deal with handling updates:

1. Parameterize Pattern
1. Social YEET Pattern
1. Proxy Pattern

### Parameterize Pattern

With this pattern, there's no way to update the logic, or add new storage variables to
the smart contract. However, we can parameterize everything in the contract by adding
a bunch of setter functions to alter those values. This is a simple way to update values,
but it's not flexible since we're limited to just updating values.

This also brings into question the centralization of the smart contract. If one person
or group of developers are the admins and control those values, then it's not a decentralized
smart contract. To remedy this, the developer can define some governance protocol to how these
values are updates. If that governance contract is the admin, then it's decentralized.

### Social YEET Pattern

This pattern just deploys the upgraded contract to a new address and informs users to migrate
to the new contract. This respects the immutability nature and philosophy of decentralized
applications since users can still interact with the old contract and the contract wasn't
designed with upgradability in mind.

The downside of this pattern is that the developer has to take care of all the social tasks
that involves migrating users to the new contracts. If, for example, the upgrade was an ERC-20
token, the developer is in charge of making sure some logic is defined so that the users new
token balance matches that of the old token. Alongside that, any storage and state variables
of the old contract would have to migrate over as well.

### Proxy Pattern

The truest form of upgrades amongst these patterns. This pattern is also prone to making
mistakes since it uses low level functions, like `delegateCall()`. Contract 1 delegate
calls the logic in Contract 2 to handle modifications or updating of variables in Contract 1.

In this scenario, Contract 2 which has the implementation logic would be known as the _Implementation Contract_.
Evertime the developer upgrades, they launch a new version of the implementation contract. Contract 1 which
points the implentation contract and calls its logic is known as the _Proxy Contract_. This proxy contract
is what the users will interact with and will hold the implementation contract that it derives its logic from.

There are a couple of big potential problems that comes with using the proxy pattern:

1. Storage Clashes
1. Function Selector Clashes

#### Storage Clash

With storage classes, we need to understand how Solidity stores variables. When variables are defined they
are given a storage location, the first value is at location 0, the next at location 1, and so on.

Functions in the implementation contract point to storage locations, **not** the value names. So defined
storage variables' storage location cannot be altered or changed. We can only **append** new storage
variables in future implementation contracts.

So if an implentation contract had the following code:

```sol
uint256 value; // storage location 0
uint256 otherValue; // storage location 1

function setValue(uint256) {
    value = 2; 
}
```

`setValue()` will always update the value at storage location 0, and never the value at storage location 1.

#### Function Selector Clash

When using delegate calls to call the implentation contract's functions, Solidity uses the 4 byte hash
of the function known as the _Function Selector_. It's possible for a function in the implementation
contract to have the same function selector as a function in the proxy contract.
**EVEN IF THEY DON'T HAVE THE SAME NAME!**

```sol
contract Example {
    // This won't compile, both of these functions have the same function selector.
    function propogate_storage(bytes16) external {}
    function burn(uint256) external {}
}
```

To address these clashes, there are a couple of implementation patterns:

1. Transparent Proxy Implemenation
1. Universal Upgradable Proxies Implementation
1. Diamond Implementation

#### Transparent Proxy Implemenation

This implementation makes sure that Admins can't call implementation contract
functions and users can't call admin proxy contract functions.

#### Universal Upgradable Proxies Implementation

This implementation, also known as UUPS, puts the admin only upgrade functions in
the implementation contract **instead** of the proxy contract! By doing this, Solidity
will actually catch the duplicate function selector and throw a compiler error.
This also saves on gas since we don't have to check if the user is an admin or not and
results in a smaller proxy contract.

**BUT** if you create an implementation contract without any upgradable functionality,
then your fallback option is the YEET pattern.

#### Diamond Implementation

This allows for multiple implementation contracts. The benefit with this is you can
break up the logic in different contracts which makes smaller upgrades much easier
to implement.

The disadvantage is that with bigger projects, the code can get more complicated.
