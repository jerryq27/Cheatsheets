// function name() public view returns (string) {}

// function symbol() public view returns (string) {}

// function decimals() public view returns (uint8) {}

// function totalSupply() public view returns (uint256) {}

// function balanceOf(address _owner) public view returns (uint256 balance) {}

// function transfer(address _to, uint256 _value) public returns (bool success) {}

// function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {}

// function approve(address _spender, uint256 _value) public returns (bool success) {}

// function allowance(address _owner, address _spender) public view returns (uint256 remaining) {}

// event Transfer(address indexed _from, address indexed _to, uint256 _value) {}

// event Approval(address indexed _owner, address indexed _spender, uint256 _value) {}

/* Taken from OpenZeppelin */
// contracts/MyToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }
}
