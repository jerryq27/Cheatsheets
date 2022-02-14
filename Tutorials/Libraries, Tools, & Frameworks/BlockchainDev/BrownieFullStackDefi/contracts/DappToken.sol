// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/* Reward ERC-20 token for users of this Dapp */
contract DappToken is ERC20 {
    constructor() public ERC20("Dapp Token", "DAPP") {
        // Create initial supply of 1,000,000 tokens.
        _mint(msg.sender, 1_000_000 * 10**18);
    }
}
